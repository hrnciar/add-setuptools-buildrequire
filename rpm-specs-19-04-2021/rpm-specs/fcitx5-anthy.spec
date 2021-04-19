%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-anthy
Version:    5.0.5
Release:    1%{?dist}
Summary:    Anthy Wrapper for Fcitx5
License:    GPLv2+
URL:        https://github.com/fcitx/fcitx5-anthy
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  pkgconfig(anthy)
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Anthy Wrapper for Fcitx5
Ported from scim-anthy. Released under GPL2+.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4-*
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done 
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%doc README.md AUTHORS 
%{_libdir}/fcitx5/anthy.so
%{_datadir}/fcitx5/addon/anthy.conf
%{_datadir}/fcitx5/anthy
%{_datadir}/fcitx5/inputmethod/anthy.conf
%{_datadir}/icons/hicolor/*/status/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Anthy.metainfo.xml

%changelog
* Wed Apr 07 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5 upstream release

* Mon Mar 22 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4 upstream release

* Wed Feb 24 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- update to 5.0.3 upstream release

* Fri Feb 19 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- update to 5.0.2 upstream release

* Fri Dec 11 23:12:03 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release

