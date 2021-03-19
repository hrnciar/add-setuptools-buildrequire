%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-rime
Version:        5.0.4
Release:        1%{?dist}
Summary:        RIME support for Fcitx
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5-rime
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  brise 
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  pkgconfig(rime)
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data
Requires:       brise

%description
RIME(中州韻輸入法引擎) is mainly a Traditional Chinese 
input method engine.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install

# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%check
%ctest

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/rime.so
%{_datadir}/fcitx5/*/rime.conf
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Rime.metainfo.xml

%changelog
* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- update to 5.0.4 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 11:12:05 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- update to 5.0.3 upstream release

* Fri Dec 11 16:56:26 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-2
- fix conlict with fcitx4

* Thu Dec 10 22:39:12 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2 upstream release

* Sat Dec  5 16:29:01 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release

* Tue Nov  3 20:13:39 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 upstream release

* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.5
- update to e20996d752e3b2882d35c15630fa4b75da177485 upstream commit

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- Rebuild for fcitx5
- Upstream commit 6da82ec569e3a83a94f7c1fff71fce885a6b2252

* Sat Aug 22 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200811gite4fc600
- add missing Requires

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gite4fc600
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gite4fc600
- initial package
