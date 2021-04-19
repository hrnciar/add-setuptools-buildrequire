%global __provides_exclude_from ^%{_libdir}/(fcitx5|qt5)/.*\\.so$

Name:           fcitx5-qt
Version:        5.0.5
Release:        1%{?dist}
Summary:        Qt library and IM module for fcitx5
# Fcitx5Qt{4,5}DBusAddons Library and Input context plugin are released under BSD.
License:        LGPLv2+ and BSD
URL:            https://github.com/fcitx/fcitx5-qt
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(Fcitx5Utils)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui) 
BuildRequires:  gettext
BuildRequires:  qt5-qtbase-private-devel
# This needs to be rebuilt on every minor Qt5 version bump
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

Requires:       %{name}-module%{?_isa} = %{version}-%{release}
Requires:       %{name}-libfcitx5qtdbus%{?_isa} = %{version}-%{release}
Requires:       %{name}-libfcitx5qt5widgets%{?_isa} = %{version}-%{release}

%description
Qt library and IM module for fcitx5.

%package module
Summary:        Provides seperately modules for fcitx5-qt

%description module
This package provides im-modules that can be installed seperately
from fcitx5-qt.

%package libfcitx5qtdbus
Summary:        Provides libFcitx5Qt5DBusAddons for fcitx5

%description libfcitx5qtdbus
This package provides libFcitx5Qt5DBusAddons for fcitx5.

%package libfcitx5qt5widgets
Summary:        Provide libFcitx5Qt5WidgetsAddons for fcitx5

%description libfcitx5qt5widgets
This package provides libFcitx5Qt5WidgetsAddons for fcitx5.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel
Requires:       cmake-filesystem%{?_isa}

%description devel
Development files for %{name}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake -GNinja -DENABLE_QT4=False
%cmake_build 

%install
%cmake_install

%find_lang %{name}


%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libexecdir}/fcitx5-qt5-gui-wrapper
%{_libdir}/fcitx5/qt5/

%files devel
%{_includedir}/Fcitx5Qt5/
%{_libdir}/cmake/Fcitx5Qt5*
%{_libdir}/libFcitx5Qt5DBusAddons.so
%{_libdir}/libFcitx5Qt5WidgetsAddons.so

%files module 
%{_qt5_plugindir}/platforminputcontexts/libfcitx5platforminputcontextplugin.so

%files libfcitx5qt5widgets
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.2
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.*.*

%files libfcitx5qtdbus
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libFcitx5Qt5DBusAddons.so.1
%{_libdir}/libFcitx5Qt5DBusAddons.so.*.*

%changelog
* Tue Mar 23 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5 upstream release

* Mon Mar 22 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4 upstream release

* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- update to 5.0.3 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 10:50:52 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- update to 5.0.2 upstream release

* Sun Dec  6 00:42:46 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-2
- split package
- libfcitx5qtdbus and libfcitx5qt5widgets

* Sat Dec  5 14:12:52 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release

* Tue Nov 24 18:00:57 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-2
- rebuild for qt 5.15.2

* Tue Nov  3 19:39:01 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 upstream release

* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.5
- update to 932e25f361f588a1e87f57e8a994bba80bf8798d upstream commit

* Wed Sep 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- Upstream commit f5adc1bd85a89a1d3888052fa9403c8e9b454bfa
- make provides sane

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200912git02bbbf6
- Rebuild for fcitx5, QT5
- Upstream commit 02bbbf671dc44e83ef8eb9352483e67ad43381e3

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811git3ddd34a
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811git3ddd34a
- initial package
