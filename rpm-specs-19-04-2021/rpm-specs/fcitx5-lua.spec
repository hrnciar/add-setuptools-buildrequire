%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-lua
Version:        5.0.4
Release:        1%{?dist}
Summary:        Lua support for fcitx
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5-lua
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  /usr/bin/appstream-util
Requires:       fcitx5-data

%description
Lua support for fcitx.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description devel
Devel files for fcitx5-lua

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install
install -d  %{buildroot}%{_datadir}/lua/imeapi/extensions
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%check
%ctest

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/luaaddonloader.so
%{_datadir}/fcitx5/addon/imeapi.conf
%{_datadir}/fcitx5/addon/luaaddonloader.conf
%{_datadir}/fcitx5/lua
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Lua.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/luaaddonloader
%{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader


%changelog
* Mon Mar 22 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4 upstream release

* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- update to 5.0.3 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 11:10:56 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- update to 5.0.2 upstream release

* Sat Dec  5 16:24:45 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release

* Tue Nov  3 20:07:15 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 upstream release

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5
- Upstream commit ff218dd82db069d4a502a3eb212a80184c592ce0

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitd705404
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitd705404
- initial package
