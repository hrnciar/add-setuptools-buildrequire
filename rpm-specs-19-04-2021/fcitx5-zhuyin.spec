%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-zhuyin
Version:    5.0.4
Release:    1%{?dist}
Summary:    Libzhuyin Wrapper for Fcitx
License:    GPLv2+
URL:        https://github.com/fcitx/fcitx5-zhuyin
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9
# upstream 5.0.3 provides a broken tarball, manually including data files
Source3:    https://download.fcitx-im.org/data/model.text.20161206.tar.gz

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  pkgconfig(libzhuyin) >= 2.3.0
BuildRequires:  libpinyin-tools
BuildRequires:  cmake(fmt)
BuildRequires:  gettext
BuildRequires:  libappstream-glib
Requires:       %{name}-data = %{version}-%{release}

%description
Libzhuyin Wrapper for Fcitx.

%package data
Summary:        Data files for fcitx5-zhuyin
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fcitx5-lua
Requires:       fcitx5-data
Requires:       hicolor-icon-theme

%description data
Provides data files and icon files need for fcitx5-zhuyin package.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp %{S:3} data/model.text.20161206.tar.gz

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
%doc README AUTHORS ChangeLog 
%{_libdir}/fcitx5/zhuyin.so
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Zhuyin.metainfo.xml

%files data
%{_datadir}/fcitx5/addon/zhuyin.conf
%{_datadir}/fcitx5/inputmethod/zhuyin.conf
%{_datadir}/icons/hicolor/48x48/apps/fcitx-zhuyin.png
%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx-zhuyin.png
%{_datadir}/fcitx5/zhuyin
%{_datadir}/fcitx5/lua/imeapi/extensions/zhuyin.lua

%changelog
* Mon Mar 22 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4 upstream release

* Fri Mar 12 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- Update to 5.0.3 upstream release

* Fri Feb 19 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- update to 5.0.2 upstream release

* Fri Dec 11 23:50:55 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release

* Fri Dec  4 21:13:39 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- Initial Release
