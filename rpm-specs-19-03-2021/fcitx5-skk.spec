%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-skk
Version:    5.0.4
Release:    1%{?dist}
Summary:    Japanese SKK (Simple Kana Kanji) Engine for Fcitx5
License:    GPLv3+
URL:        https://github.com/fcitx/fcitx5-skk
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-qt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(libskk)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  /usr/bin/appstream-util
Requires:       skkdic
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Fcitx5-skk is an SKK (Simple Kana Kanji) engine for Fcitx.  It provides
Japanese input method using libskk.

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
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/qt5/libfcitx5-skk-config.so
%{_libdir}/fcitx5/skk.so
%{_datadir}/fcitx5/addon/skk.conf
%{_datadir}/fcitx5/inputmethod/skk.conf
%dir %{_datadir}/fcitx5/skk
%{_datadir}/fcitx5/skk/dictionary_list
%{_datadir}/icons/hicolor/64x64/apps/fcitx-skk.png
%{_datadir}/icons/hicolor/64x64/apps/org.fcitx.Fcitx5.fcitx-skk.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Skk.metainfo.xml

%changelog
* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- update to 5.0.4 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 11:15:59 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- update to 5.0.3 upstream release

* Fri Dec 11 16:57:02 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-2
- fix conlict with fcitx4

* Sat Dec  5 17:30:36 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2 upstream release

* Sat Dec  5 16:43:52 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release

* Tue Nov  3 20:19:30 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 upstream release

* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- update to eff9bc32bcccdae65dcae05adfc9eb7a642a667e upstream commit

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5
- Upstream commit cc9261407b496a5708dca642deec5bcafe1cf58c

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200813git02fb41d
- rebuilt

* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200813git02fb41d
- Initial Package
