%global translation_domain org.fcitx.fcitx5.kcm

Name:           fcitx5-configtool
Version:        5.0.3
Release:        1%{?dist}
Summary:        Configuration tools used by fcitx5
License:        GPLv2+
URL:            https://github.com/fcitx/fcitx5-configtool
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gettext-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kirigami2-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Utils)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  /usr/bin/appstream-util


%description
Configuration tools used by fcitx5.

%package -n kcm-fcitx5
Summary:        Config tools to be used on KDE based environment.
Requires:       kf5-filesystem
Requires:       kf5-kcmutils
Suggests:       %{name}%{?_isa} = %{version}-%{release}

%description -n kcm-fcitx5
Config tools to be used on KDE based environment. Can be installed seperately.

%package -n fcitx5-migrator
Summary:        Migration tools for fcitx5
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n fcitx5-migrator
Migration tools for fcitx5, containing fcitx5-migrator

%package -n fcitx5-migrator-devel
Summary:        Devel files for fcitx5-migrator
Requires:       fcitx5-migrator%{?_isa} = %{version}-%{release}

%description -n fcitx5-migrator-devel
Development files for fcitx5-migrator

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

#fix typos
sed -i 's/Catogories/Categories/g' src/configtool/org.fcitx.fcitx5-config-qt.desktop.in
sed -i 's/Catogories/Categories/g' src/migrator/app/org.fcitx.fcitx5-migrator.desktop.in

%build
%cmake_kf5 -GNinja
%cmake_build 

%install
%cmake_install
# kservices5/*.desktop desktop file dont't need to use desktop-file-install
# only for applications/*.desktop
for desktop_file_name in kbd-layout-viewer5 org.fcitx.fcitx5-config-qt org.fcitx.fcitx5-migrator
do
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/${desktop_file_name}.desktop
done
sed "/icon/d" -i %{buildroot}%{_metainfodir}/%{translation_domain}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name}
%find_lang %{translation_domain}


%files -f %{name}.lang 
%license LICENSES/GPL-2.0-or-later.txt
%doc README
%{_bindir}/fcitx5-config-qt
%{_datadir}/applications/org.fcitx.fcitx5-config-qt.desktop
%{_bindir}/kbd-layout-viewer5
%{_datadir}/applications/kbd-layout-viewer5.desktop

%files -n kcm-fcitx5 -f %{translation_domain}.lang 
%license LICENSES/GPL-2.0-or-later.txt
%{_kf5_qtplugindir}/kcms/kcm_fcitx5.so
%{_datadir}/kpackage/kcms/%{translation_domain}
%{_datadir}/kservices5/kcm_fcitx5.desktop
%{_metainfodir}/%{translation_domain}.appdata.xml

%files -n fcitx5-migrator
%{_bindir}/fcitx5-migrator
%{_libdir}/libFcitx5Migrator.so.5*
%{_datadir}/applications/org.fcitx.fcitx5-migrator.desktop

%files -n fcitx5-migrator-devel
%{_libdir}/libFcitx5Migrator.so

%changelog
* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- update to 5.0.3 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 11:18:46 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- update to 5.0.2 upstream release

* Sat Dec  5 16:54:30 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release
- sobump libFcitx5Migrator.so.0 -> libFcitx5Migrator.so.5

* Tue Nov  3 19:34:44 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 upstream release

* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.6
- update to 8b2aec745af6da7a82b76a32a4b9196bb03db067 upstream commit

* Wed Sep 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.5
- Upstream commit e8c08930045bc00d49aebb9465445d9ab8d2a120
- new subpackage fcitx5-migrator containing migration tools

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- Rebuild for fcitx5
- Upstream commit 8f113a78e334ecc962d5aa92022887ca077df588

* Tue Sep  1 10:17:42 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Add subpackage kcm-fcitx5
- Improve macros

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitecd16e5
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitecd16e5
- initial package
