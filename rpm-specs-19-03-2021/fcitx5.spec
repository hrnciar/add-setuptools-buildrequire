%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx5.conf
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Name:           fcitx5
Version:        5.0.5
Release:        1%{?dist}
Summary:        Next generation of fcitx
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5
Source:         https://download.fcitx-im.org/fcitx5/fcitx5/fcitx5-%{version}_dict.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/fcitx5/fcitx5-%{version}_dict.tar.xz.sig
# Checked by chatting, this key is used to verify fcitx* tarballs
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9
Source3:        fcitx5-xinput
Source4:        fcitx5.sh

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gnupg2
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cldr-emoji-annotation)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-imdkit)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  /usr/bin/appstream-util
Requires:       dbus-x11
Requires:       %{name}-data = %{version}-%{release}
Requires:       setup
Requires(post):     %{_sbindir}/alternatives
Requires(postun):   %{_sbindir}/alternatives

Suggests:       (fcitx5-gtk if (gtk2 or gtk3 or gtk4))
Suggests:       (fcitx5-qt if qt5-qtbase)
Suggests:       (fcitx5-qt-module if qt5-qtbase)

%description
Fcitx 5 is a generic input method framework released under LGPL-2.1+.

%package data
Summary:        Data files of Fcitx5
BuildArch:      noarch
# require with isa will lead to problem on koji build
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       dbus

%description data
The %{name}-data package provides shared data for Fcitx5.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using Fcitx5 libraries.

%package autostart
Summary:        This package will make fcitx5 start with your GUI session
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description autostart
This package will setup autostart and environment needed for fcitx5 to work properly.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install
install -pm 644 -D %{S:3} %{buildroot}%{_xinputconf}
install -pm 644 -D %{S:4} %{buildroot}%{_sysconfdir}/profile.d/fcitx5.sh
install -d                %{buildroot}%{_datadir}/%{name}/inputmethod
install -d                %{buildroot}%{_datadir}/%{name}/table
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop
 
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/org.fcitx.Fcitx5.desktop
  
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

%post
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 55 || :

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%config %{_xinputconf}
%{_bindir}/%{name}
%{_bindir}/%{name}-configtool
%{_bindir}/%{name}-remote
%{_bindir}/%{name}-diagnose
%{_libdir}/%{name}/
%{_libdir}/libFcitx5*.so.*.*
%{_libdir}/libFcitx5Config.so.6
%{_libdir}/libFcitx5Core.so.7
%{_libdir}/libFcitx5Utils.so.2

%files devel
%{_includedir}/Fcitx5/
%{_libdir}/cmake/Fcitx5*
%{_libdir}/libFcitx5*.so
%{_libdir}/pkgconfig/Fcitx5*.pc


%files data
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.fcitx.Fcitx5.service
%{_datadir}/applications/org.fcitx.Fcitx5.desktop
%{_metainfodir}/org.fcitx.Fcitx5.metainfo.xml
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/icons/hicolor/*/apps/*

%files autostart
%config %{_sysconfdir}/xdg/autostart/org.fcitx.Fcitx5.desktop
%config %{_sysconfdir}/profile.d/fcitx5.sh

%changelog
* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.5-1
- update to 5.0.5 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 12:19:25 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-2
- use conditional suggests

* Tue Jan 12 21:48:18 CST 2021 yan - 5.0.4-1
- update to 5.0.4 upstream release

* Fri Dec 11 16:49:42 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-3
- fix conlict with fcitx4

* Wed Dec  9 00:25:45 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-2
- explicit Conflicts against fcitx-data

* Mon Dec  7 10:40:52 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.3-1
- Update to 5.0.3 upstream release

* Sat Dec  5 15:14:08 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-2
- add weak dep to im-modules

* Sat Dec  5 13:30:48 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2 upstream release

* Tue Nov  3 21:20:30 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-2
- add fcitx5-autostart package to auto setup env and autostart

* Tue Nov  3 18:00:49 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- update to 5.0.1 upstream release

* Sat Oct 31 22:01:00 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.10
- update to a5a0551a22971738283fc4812d2afe77efb626e3 upstream commit
- upstream added dbus service

* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.9.20201016gitdd9dc94
- update to dd9dc94c42ee98ea04782bdb4d4aa3f7822e56f0 upstream commit

* Wed Sep 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.8
- upstream commit 5415db391c1b84ea9964b0d508c053ae5c25e4aa

* Sat Sep 12 2020 Karuboniru <yanqiyu01@gmail.com> - 0-0.7
- Drop imsetting
- Update to commit d0383bc4a8e65e71189c18e31f7b832e543144c1
- sobump from libFcitx5Core.so.6 to libFcitx5Core.so.7

* Wed Sep  2 08:44:37 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.6
- Fix a typo

* Tue Sep  1 09:07:22 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.5.20200830git4706f37
- Own /usr/share/fcitx5/inputmethod

* Sun Aug 30 23:39:20 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4.20200830git4706f37
- rebuild to push to f32

* Sun Aug 30 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200830git4706f37
- update to commit 4706f37e60686d391a7f9a45ca1be6df6052ec4d
- fix a wrong xinputrc file

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200813git87fb655
- change according to review suggestions

* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200813git87fb655
- new version

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitc87ea48
- initial package
