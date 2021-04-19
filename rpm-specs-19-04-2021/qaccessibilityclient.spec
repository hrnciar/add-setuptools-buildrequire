Name:    qaccessibilityclient
Summary: Accessibility client library for Qt5
Version: 0.4.1
Release: 1%{?dist}

# KDE e.V. may determine that future LGPL versions are accepted
License: LGPLv2 or LGPLv3
URL:     https://cgit.kde.org/libkdeaccessibilityclient.git/
Source0: http://download.kde.org/stable/libqaccessibilityclient/libqaccessibilityclient-%{version}.tar.xz

## upstream patches

BuildRequires: cmake
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: extra-cmake-modules

# upstream name
Provides: libqaccessibilityclient = %{version}-%{release}

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Provides: libqaccessibilityclient-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description  devel
%{summary}.


%prep
%autosetup -n libqaccessibilityclient-%{version} -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

## unpackaged files


%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog README*
%license COPYING
%{_libdir}/libqaccessibilityclient-qt5.so.0*

%files devel
%{_includedir}/qaccessibilityclient/
%{_libdir}/cmake/QAccessibilityClient/
%{_libdir}/libqaccessibilityclient-qt5.so


%changelog
* Thu Apr 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-1
- 0.4.1, Qt5 support

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-15
- cleanup, use %%make_build
- drop Provides: libqaccessibilityclient
- drop qt5 support (to be packaged separately)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 Than Ngo <than@redhat.com> - - 0.1.1-12
- fixed FTBS

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-8
- pull in upstream fixes
- initial support for Qt5 build (not enabled yet)
- .spec cosmetics: update URL, use %%license

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-1
- 1.1.1 release
- support QT4_BUILD option
- fix dso patch
- Provides: libqaccessibilityclient(-devel)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-0.3.20121113git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.2.20121113git
- fix changelog
- -devel: +Requires: cmake qt4-devel
- link QT_QTGUI_LIBRARY for undefined symbols
- s/Url/URL/
- don't package accessibleapps

* Sat Feb 02 2013 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.1.20121113git
- adapt for fedora
- fresh snapshot

* Sat Nov 10 2012 alinm.elena@gmail.com
- initial commit
