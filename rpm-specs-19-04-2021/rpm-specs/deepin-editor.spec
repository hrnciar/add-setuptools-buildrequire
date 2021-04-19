Name:           deepin-editor
Version:        5.9.0.24
Release:        1%{?dist}
Summary:        Simple editor for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  freeimage-devel
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(DFrameworkdbus)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-notifications
Requires:       deepin-qt5integration
# bundled libraries
Provides:       bundled(libiconv) = 1.16
Provides:       bundled(enca) = 1.19
Provides:       bundled(uchardet) = 0.0.7

%description
%{summary}.

%prep
%autosetup -p1
# force bundled libaries install to 'third/lib/lib'
sed -i 's/lib$/lib -DCMAKE_INSTALL_LIBDIR=lib/' third/uchartdet_install.sh

%build
# force bundled libaries to build with -fPIE
export CFLAGS="%{optflags} -fPIE"
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Fri Mar 12 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.9.0.24-1
- fix: 更新桌面翻译 (ut000616)
- fix: 修复bug (ut001763)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.9.0.11-1
- new upstream release: 5.9.0.11

* Mon Nov 23 07:49:33 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.9.0.3-2
- rebuild (qt5)

* Thu Nov 12 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.9.0.3-1
- new upstream release: 5.9.0.3

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.2.9.1-8
- rebuild (qt5)

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.2.9.1-7
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.2.9.1-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.9.1-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.9.1-2
- rebuild (qt5)

* Sun Aug 11 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.9.1-1
- Release 1.2.9.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.6.3-5
- rebuild (qt5)

* Mon Jun 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.6.3-4
- Rebuild (Qt5)

* Wed Mar 13 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.6.3-3
- Requires private Qt symbols

* Thu Feb 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.6.3-2
- Fix translations

* Sat Feb  9 2019 mosquito <sensor.wen@gmail.com> - 1.2.6.3-1
- Update to 1.2.6.3

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 1.2.6.2-1
- Update to 1.2.6.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Jul 23 2018 mosquito <sensor.wen@gmail.com> - 0.0.5-1
- Initial package build
