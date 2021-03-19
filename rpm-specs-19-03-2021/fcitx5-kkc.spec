%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-kkc
Version:        5.0.4
Release:        1%{?dist}
Summary:        Libkkc input method support for Fcitx5
License:        GPLv3+
Url:            https://github.com/fcitx/fcitx5-kkc
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Qt5WidgetsAddons)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(kkc-1.0)
BuildRequires:  pkgconfig(Qt5Core) >= 5.7
BuildRequires:  pkgconfig(Qt5Gui) >= 5.7
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.7
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data
Requires:       libkkc-data

%description
This provides libkkc input method support for fcitx5. Released under GPL3+.

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
%doc README.md
%license LICENSES/GPL-3.0-or-later.txt
%{_libdir}/fcitx5/kkc.so
%{_libdir}/fcitx5/qt5/libfcitx5-kkc-config.so

%{_datadir}/fcitx5/addon/kkc.conf
%{_datadir}/fcitx5/inputmethod/kkc.conf

%dir %{_datadir}/fcitx5/kkc
%{_datadir}/fcitx5/kkc/dictionary_list
%{_datadir}/fcitx5/kkc/rule

%{_datadir}/icons/hicolor/*/apps/fcitx-kkc.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-kkc.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Kkc.metainfo.xml
%changelog
* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- update to 5.0.4 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 11:10:03 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- update to 5.0.3 upstream release

* Fri Dec 11 18:58:34 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-2
- fix conlict with fcitx4

* Sat Dec  5 17:28:32 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2 upstream release

* Sat Dec  5 16:27:52 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release

* Tue Nov  3 19:54:55 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 upstream release

* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- update to 0ffde563576b3ac4f62c55f5508251de3f22fd0b upstream commit

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2
- Rebuild for fcitx5

* Mon Aug 31 09:58:21 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200831git7c6d0b5
- Initial Package

