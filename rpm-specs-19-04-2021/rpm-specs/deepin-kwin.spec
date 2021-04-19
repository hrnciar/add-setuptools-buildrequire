%global repo dde-kwin
%global __provides_exclude_from ^%{_qt5_plugindir}.*\.so$

Name:           deepin-kwin
Version:        5.2.0.13
Release:        2%{?dist}
Summary:        KWin configuration for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# revert added functions from their forked kwin
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0001: 0001-revert-added-functions-from-their-forked-kwin.patch

# tabbox chameleon rename
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0002: 0002-tabbox-chameleon-rename.patch

# unload blur
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0003: 0003-unload-blur.patch

# fix: blurmanager interface changed
# Author: justforlxz <justforlxz@gmail.com>
Patch0004: 0004-fix-blurmanager-interface-changed.patch

# fix: doesn't compile with Kwin 5.21 …
# Author: justforlxz <justforlxz@gmail.com>
Patch0005: 0005-fix-doesn-t-compile-with-Kwin-5.21.patch

# kwin 5.19
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0006: 0006-kwin-5.19.patch







BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= 5.54
BuildRequires:  kwin-devel
BuildRequires:  kwayland-server-devel
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  gsettings-qt-devel
BuildRequires:  libepoxy-devel
BuildRequires:  dtkgui-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  qt5-linguist
# for libQt5EdidSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-qt5integration%{?_isa}
Requires:       kwin-x11%{?_isa} >= 5.21
# since F31
Obsoletes:      deepin-wm <= 1.9.38
Obsoletes:      deepin-wm-switcher <= 1.1.9
Obsoletes:      deepin-metacity <= 3.22.24
Obsoletes:      deepin-metacity-devel <= 3.22.24
Obsoletes:      deepin-mutter <= 3.20.38
Obsoletes:      deepin-mutter-devel <= 3.20.38

%description
This package provides a kwin configuration that used as the new WM for Deepin
Desktop Environment.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kwin-devel%{?_isa}
Requires:       qt5-qtx11extras-devel%{?_isa}
Requires:       gsettings-qt-devel%{?_isa}
Requires:       dtkcore-devel%{?_isa}
Requires:       kf5-kglobalaccel-devel%{?_isa}


%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}

sed -i 's:/lib/:%{_libdir}/:' plugins/platforms/lib/CMakeLists.txt
sed -i 's:/lib/:/%{_lib}/:' plugins/platforms/plugin/main.cpp \
                            plugins/platforms/plugin/main_wayland.cpp
sed -i 's:/usr/lib:%{_libexecdir}:' deepin-wm-dbus/deepinwmfaker.cpp

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DKWIN_VERSION=$(rpm -q --qf '%%{version}' kwin-devel)
%cmake_build

%install
%cmake_install
chmod 755 %{buildroot}%{_bindir}/kwin_no_scale

%files
%doc CHANGELOG.md
%license LICENSE
%{_sysconfdir}/xdg/*
%{_bindir}/deepin-wm-dbus
%{_bindir}/kwin_no_scale
%{_qt5_plugindir}/org.kde.kdecoration2/libdeepin-chameleon.so
%{_qt5_plugindir}/platforms/lib%{repo}-xcb.so
%{_qt5_plugindir}/platforms/lib%{repo}-wayland.so
%{_qt5_plugindir}/kwin/effects/plugins/
%{_datadir}/dde-kwin-xcb/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/kwin/scripts/*
%{_datadir}/kwin/tabbox/*
%{_libdir}/libkwin-xcb.so.0
%{_libdir}/libkwin-xcb.so.0.*

%files devel
%{_libdir}/libkwin-xcb.so
%{_libdir}/pkgconfig/%{repo}.pc
%{_includedir}/%{repo}

%changelog
* Mon Mar 29 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.2.0.13-2
- Re-add missed patch

* Mon Mar 29 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.2.0.13-1
- new upstream release: 5.2.0.13

* Fri Mar 12 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.2.0.2-4
- Make it a symlink to kwin_x11 since it does not build with kwin 5.21

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:49:48 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.2.0.2-2
- rebuild (qt5)

* Thu Nov 12 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.2.0.2-1
- new upstream release: 5.2.0.2

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 0.1.0-10
- rebuild (qt5)

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.1.0-9
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-7
- rebuild (qt5)

* Thu Feb 27 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.1.0-6
- Fix path conflict with kdeplasma-addons (RHBZ#1807283)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.1.0-4
- Fix runtime issue with kwin 5.17

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.1.0-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.1.0-2
- rebuild (qt5)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.0.4-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 0.0.4-2
- rebuild (qt5)

* Mon Apr 22 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.4-1
- new version

* Mon Apr 15 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.3.2-1
- Update to 0.0.3.2

* Fri Apr 12 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.3.1-1
- Initial packaging
