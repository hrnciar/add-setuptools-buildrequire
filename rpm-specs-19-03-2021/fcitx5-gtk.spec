Name:           fcitx5-gtk
Version:        5.0.4
Release:        1%{?dist}
Summary:        Gtk im module and glib based dbus client library
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5-gtk
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  cmake(fmt)

Requires:       (%{name}2 if gtk2)
Requires:       (%{name}3 if gtk3)
Requires:       (%{name}4 if gtk4)

# not requiring fcitx5 due to that I want to make 
# im_modules be able to install seperately
# this will be helpful to those who are looking 
# forward to use upstream flatpak version.

%description
Gtk im module and glib based dbus client library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel%{?_isa}

%description devel
Development files for fcitx5-gtk.

%package -n %{name}2
Summary:        fcitx5 gtk module for gtk2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}2
fcitx5 gtk module for gtk2.

%package -n %{name}3
Summary:        fcitx5 gtk module for gtk3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}3
fcitx5 gtk module for gtk3.

%package -n %{name}4
Summary:        fcitx5 gtk module for gtk4
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}4
fcitx5 gtk module for gtk4.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install

%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/libFcitx5GClient.so.5.*
%{_libdir}/libFcitx5GClient.so.2
%{_libdir}/girepository-1.0/FcitxG-1.0.typelib

%files devel
%{_includedir}/Fcitx5/GClient/
%{_libdir}/cmake/Fcitx5GClient
%{_libdir}/libFcitx5GClient.so
%{_libdir}/pkgconfig/Fcitx5GClient.pc
%{_datadir}/gir-1.0/

%files -n %{name}2
%{_libdir}/gtk-2.0/*/immodules/im-fcitx5.so

%files -n %{name}3
%{_libdir}/gtk-3.0/*/immodules/im-fcitx5.so

%files -n %{name}4
%{_libdir}/gtk-4.0/*/immodules/libim-fcitx5.so

%changelog
* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.4-1
- update to 5.0.4 upstream release
- a sobump from libFcitx5GClient.so.1 to libFcitx5GClient.so.2
- no external dependecies exist.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 12:14:40 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-2
- seperate gtk modules

* Wed Jan 13 10:55:56 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.2-1
- update to 5.0.2 upstream release
- build with gtk4 support

* Sat Dec  5 13:56:23 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 upstream release

* Tue Nov  3 19:43:10 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 upstream release

* Wed Sep 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- upstream commit 8835e96d9ce0620b930d3f4ef7db73ceae4f029c

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5
- Upstream commit 0e59f66318faafc3856465a80bf42376aa5b56dc

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitfc335f1
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitfc335f1
- initial package
