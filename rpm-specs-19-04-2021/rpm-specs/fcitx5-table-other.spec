Name:       fcitx5-table-other
Version:    5.0.4
Release:    1%{?dist}
Summary:    Other tables for Fcitx5
License:    GPLv3
URL:        https://github.com/fcitx/fcitx5-table-other
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9
BuildArch:  noarch

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build
BuildRequires:  boost-devel
BuildRequires:  cmake(Fcitx5Utils)
BuildRequires:  cmake(LibIMETable)
BuildRequires:  gettext
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Fcitx-table-other provides some other tables 
for Fcitx, fork from ibus-table-others, scim-tables.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build 
%cmake -GNinja -DCMAKE_PREFIX_PATH="%{_libdir}/cmake;%{_libdir}64/cmake"
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

%files 
%license LICENSES/GPL-3.0-only.txt
%doc README NEWS 
%{_datadir}/fcitx5/inputmethod/*
%{_datadir}/fcitx5/table/*
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.TableOther.metainfo.xml

%changelog
* Mon Mar 22 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4 upstream release

* Fri Mar 12 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- Update to 5.0.3 upstream release

* Fri Feb 19 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- update to 5.0.2 upstream release

* Fri Dec 11 23:37:13 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release
