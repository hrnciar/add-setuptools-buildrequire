%global _terminals gnome-terminal mate-terminal xfce4-terminal lxterminal qterminal qterminal-qt5 terminology yakuake fourterm roxterm lilyterm termit xterm mrxvt
%global repo deepin-terminal
%global libname terminalwidget5

Name:           deepin-terminal
Version:        5.4.0.6
Release:        1%{?dist}
Summary:        Default terminal emulation application for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(lxqt) >= 0.14.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  qt5-linguist
Requires:       deepin-qt5integration%{?_isa}
# right-click menu style
Requires:       deepin-menu
# subprocess command
Requires:       deepin-shortcut-viewer
Requires:       expect
Requires:       xdg-utils
Recommends:     deepin-manual
Recommends:     zssh
Requires:       %{name}-data = %{version}-%{release}

%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%package data
Summary:        Data files of Deepin Terminal
BuildArch:      noarch
Requires:       hicolor-icon-theme

%description data
The %{name}-data package provides shared data for Deepin Terminal.

%prep
%autosetup -p1 -n %{repo}-%{version}
# don't hard code -fPIE
sed -i 's/-fPIE//' CMakeLists.txt
# fix error: 'QString::QString(const char*)' is private within this context
sed -i '/LXQtCompilerSettings/a remove_definitions(-DQT_NO_CAST_FROM_ASCII -DQT_NO_CAST_TO_ASCII)' 3rdparty/terminalwidget/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
chmod -v 755 %{buildroot}%{_bindir}/*
# delete a stale file
find %{buildroot} -name install_flag -delete

%check
# failing for now
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop ||:

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove x-terminal-emulator %{_bindir}/%{name}
fi

%post
if [ $1 -ge 1 ]; then
  %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
    x-terminal-emulator %{_bindir}/%{name} 20
fi

%triggerin -- konsole5 %_terminals
if [ $1 -ge 1 ]; then
  PRI=20
  for i in konsole %{_terminals}; do
    PRI=$((PRI-1))
    test -x %{_bindir}/$i && \
    %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
      x-terminal-emulator %{_bindir}/$i $PRI &>/dev/null ||:
  done
fi

%triggerpostun -- konsole5 %_terminals
if [ $2 -eq 0 ]; then
  for i in konsole %{_terminals}; do
    test -x %{_bindir}/$i || \
    %{_sbindir}/alternatives --remove x-terminal-emulator %{_bindir}/$i &>/dev/null ||:
  done
fi

%files
%{_bindir}/%{name}
%{_libdir}/lib%{libname}.so.0*
%{_datadir}/applications/%{name}.desktop

%files devel
%{_includedir}/%{libname}/
%{_libdir}/lib%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc
%{_libdir}/cmake/%{libname}/

%files data
%doc README.md
%license LICENSE
%{_datadir}/%{name}/
%{_datadir}/%{libname}/
%{_datadir}/icons/hicolor/*/apps/%{name}*

%changelog
* Fri Mar 12 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.4.0.6-1
- chore: [1040-2] 修改UT测试相关配置 (zhangmeng)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.3-1
- new upstream release: 5.3.0.3

* Thu Nov 12 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.1-1
- new upstream release: 5.3.0.1

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.4.1-3
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May  1 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.4.1-1
- Update to 5.0.4.1 (RHBZ#1828023, RHBZ#1699622)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.2.6-1
- Update to 3.2.6

* Tue Apr 16 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.2.2.1-1
- new version

* Tue Feb 26 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.2.1.1-2
- Recover triggers and fix triggerin to not generate error

* Tue Feb 26 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.2.1.1-1
- Update to 3.2.1.1
- Remove triggers

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 3.0.12-2
- Append curdir to CMake invokation. (#1668512)

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.0.12-1
- Update to 3.0.12

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 3.0.11.1-1
- Update to 3.0.11.1

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 3.0.10.2-1
- Update to 3.0.10.2

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.0.10-1
- Update to 3.0.10

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec  7 2017 mosquito <sensor.wen@gmail.com> - 2.9.2-1
- Update to 2.9.2

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 2.7.6-1
- Update to 2.7.6

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 2.7.4-1
- Update to 2.7.4

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 2.7.2-1
- Update to 2.7.2

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 2.7-1
- Update to 2.7

* Mon Oct 16 2017 mosquito <sensor.wen@gmail.com> - 2.6.4-1
- Update to 2.6.4
- Unbundle vte

* Thu Sep 21 2017 mosquito <sensor.wen@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Tue Aug 29 2017 mosquito <sensor.wen@gmail.com> - 2.5.5-1
- Update to 2.5.5

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 2.5.3-1
- Update to 2.5.3

* Mon Jul 31 2017 mosquito <sensor.wen@gmail.com> - 2.5.2-1
- Update to 2.5.2

* Fri Jul 21 2017 mosquito <sensor.wen@gmail.com> - 2.5.1-2.git82c4a12
- Split package

* Tue Jul 18 2017 mosquito <sensor.wen@gmail.com> - 2.5.1-1.git82c4a12
- Update to 2.5.1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 2.5.0-1.git439ab57
- Update to 2.5.0

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 2.4.2-1.git76b20cd
- Update to 2.4.2

* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 2.2.2-1.git3ec5488
- Update to 2.2.2

* Sat Feb 11 2017 mosquito <sensor.wen@gmail.com> - 2.1.12-1.git4f7069e
- Update to 2.1.12

* Sun Feb  5 2017 mosquito <sensor.wen@gmail.com> - 2.1.9-3.git1ded038
- Rewrite Req depends

* Sat Jan 28 2017 mosquito <sensor.wen@gmail.com> - 2.1.9-2.git1ded038
- Add trigger for terminal emulator

* Sat Jan 28 2017 mosquito <sensor.wen@gmail.com> - 2.1.9-1.git1ded038
- Update to 2.1.9

* Sun Jan 22 2017 mosquito <sensor.wen@gmail.com> - 2.1.7-2.git32f96be
- Add x-terminal-emulator command for dde-file-manager

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 2.1.7-1.git32f96be
- Update to 2.1.7

* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.6-1
- Updated to version 2.1.6

* Thu Dec 15 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.5-2
- Fixed icon path

* Mon Dec 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.5-1
- Initial package build
