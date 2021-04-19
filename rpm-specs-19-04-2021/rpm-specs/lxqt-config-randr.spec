# Sources use deprecated Qt4 code.
# https://bugreports.qt.io/browse/QTBUG-29333
# https://codereview.qt-project.org/#/c/107725/
# https://codereview.qt-project.org/#/c/105285/
%bcond_without  qt5

%global gitdate 20140202
%global commit0 6ada849baca7918078e53f7dece4d96b2a0e6210

Name:           lxqt-config-randr
Version:        0.1.2
%if 0%{?gitdate}
Release:        13.%{gitdate}git%(c=%{commit0}; echo ${c:0:7} )%{?dist}
%else
Release:        13%{?dist}
%endif
Summary:        GUI interface to RandR extension

License:        GPLv2+
URL:            https://github.com/zballina/%{name}
%if 0%{?gitdate}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
%else
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
# Initial qt5 support
Patch0:         http://bazaar.launchpad.net/~lubuntu-dev/lxde/%{name}/diff/29#/%{name}-qt5.patch

BuildRequires: make
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  desktop-file-utils

%if %with qt5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  qt5-linguist
%endif

# qmake-qt4, even needed to configure qt5
BuildRequires:  qt4-devel

%description
Qt-based tool to configure the X output using the RandR 1.3/1.2 extension,
based in KDE parts, intended to be a viable option for the LXQt desktop.


%prep
%if 0%{?gitdate}
%setup -qn%{name}-%{commit0}
# revert Virtual Modes: Fixing bug in Brightness setting (PR#6)
# commit/3aa7fa26fb61a7a521443ff3ef1d3abc574f609e
# prevents gcc error: 'sleep' was not declared in this scope
sed -i /sleep/d src/randrcrtc.cpp
%else
%setup -q
%endif
%if %with qt5
%patch0 -p0
# fixes for Fedora Qt5.6
sed -i -r -e 's,(find_package.lxqt)-qt5,\1,' -e /include/d CMakeLists.txt
# permessive gcc
sed -i s,None,0, src/randroutput.cpp
%endif

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake_lxqt -DCMAKE_BUILD_TYPE:STRING=Debug \
%if %with qt5
 -DUSE_QT5:BOOL=ON \
%endif
 ..
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}
# Exclude category as been Service 
desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt \
 --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING*
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12.20140202git6ada849
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Raphael Groner <projects.rg@smart.ms> - 0.1.2-2.20140202git6ada849
- add+improve qt5 patch from lubuntu
- enable full debug build

* Fri May 13 2016 Raphael Groner <projects.rg@smart.ms> - 0.1.2-1.20140202git6ada849
- initial
