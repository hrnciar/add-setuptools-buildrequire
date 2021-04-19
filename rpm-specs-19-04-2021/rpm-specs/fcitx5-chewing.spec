%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-chewing
Version:    5.0.5
Release:    1%{?dist}
Summary:    Chewing Wrapper for Fcitx
License:    GPLv2+
URL:        https://github.com/fcitx/fcitx5-chewing
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(chewing)
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
fcitx5-chewing is a Chewing Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese 
Phonetic IME.


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

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/chewing.so
%{_datadir}/fcitx5/addon/chewing.conf
%{_datadir}/fcitx5/inputmethod/chewing.conf
%{_datadir}/icons/hicolor/48x48/apps/fcitx-chewing.png
%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx-chewing.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Chewing.metainfo.xml

%changelog
* Mon Mar 22 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5 upstream release

* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- update to 5.0.4 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 11:05:36 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- update to 5.0.3 upstream release

* Fri Dec 11 16:51:27 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-2
- fix conlict with fcitx4

* Sat Dec  5 15:26:02 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2 upstream release

* Wed Nov  4 13:42:47 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- update to 5.0.1 upstream release

* Tue Nov  3 19:49:37 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 upstream release

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200813git7f7ea5e
- rebuilt

* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200813git7f7ea5e
- Initial Package
