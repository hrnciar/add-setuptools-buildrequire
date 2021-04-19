%global commit 280aac5a0ee09c45b17ec4be0681397f7c34c12e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#global gitdate 20210201
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

Summary:   Xwayland
Name:      xorg-x11-server-Xwayland
Version:   21.1.1
Release:   1%{?gitdate:.%{gitdate}git%{shortcommit}}%{?dist}

URL:       http://www.x.org
%if 0%{?gitdate}
Source0:   https://gitlab.freedesktop.org/xorg/%{pkgname}/-/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
%else
Source0:   https://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.xz
%endif
License:   MIT

Requires: xorg-x11-server-common
Requires: libEGL

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

BuildRequires: wayland-devel
BuildRequires: pkgconfig(wayland-client) >= 1.3.0
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-eglstream-protocols)

BuildRequires: pkgconfig(dmx)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(fontenc)
BuildRequires: pkgconfig(libdrm) >= 2.4.0
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xfont2)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xorg-macros) >= 1.17
BuildRequires: pkgconfig(xpm)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xres)
BuildRequires: pkgconfig(xshmfence) >= 1.1
BuildRequires: pkgconfig(xtrans) >= 1.3.2
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xv)
BuildRequires: xorg-x11-proto-devel >= 7.7-10

BuildRequires: mesa-libGL-devel >= 9.2
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel

BuildRequires: audit-libs-devel
BuildRequires: libselinux-devel >= 2.0.86-1

# libunwind is Exclusive for the following arches
%ifarch aarch64 %{arm} hppa ia64 mips ppc ppc64 %{ix86} x86_64
%if !0%{?rhel}
BuildRequires: libunwind-devel
%endif
%endif

BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)

%description
Xwayland is an X server for running X clients under Wayland.

%package devel
Summary: Development package
Requires: pkgconfig

%description devel
The development package provides the developmental files which are
necessary for developing Wayland compositors using Xwayland.

%prep
%autosetup -S git_am -n %{pkgname}-%{?gitdate:%{commit}}%{!?gitdate:%{version}}

%build
%meson \
        -Dxwayland_eglstream=true \
        -Ddefault_font_path=%{default_font_path} \
        -Dbuilder_string="Build ID: %{name} %{version}-%{release}" \
        -Dxkb_output_dir=%{_localstatedir}/lib/xkb \
        -Dxcsecurity=true \
        -Dglamor=true \
        -Ddri3=true

%meson_build

%install
%meson_install

# Remove unwanted files/dirs
rm $RPM_BUILD_ROOT%{_mandir}/man1/Xserver.1*
rm -Rf $RPM_BUILD_ROOT%{_libdir}/xorg
rm -Rf $RPM_BUILD_ROOT%{_includedir}/xorg
rm -Rf $RPM_BUILD_ROOT%{_datadir}/aclocal
rm -Rf $RPM_BUILD_ROOT%{_localstatedir}/lib/xkb

%files
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1*

%files devel
%{_libdir}/pkgconfig/xwayland.pc

%changelog
* Wed Apr  14 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-1
- xwayland 21.1.1 (CVE-2021-3472 / ZDI-CAN-1259)

* Thu Mar  18 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.0-1
- xwayland 21.1.0

* Thu Mar  4 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.0.99.902-1
- xwayland 21.0.99.902
- Remove xdmcp, udev, udev_kms build options
- Stop overriding the vendor name, same as xorg-x11-server

* Thu Feb 18 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.0.99.901-1
- xwayland 21.0.99.901

* Mon Feb  1 2021 Olivier Fourdan <ofourdan@redhat.com> - 1.20.99.1-0.1.20210201git5429791
- Initial import (#1912335).
