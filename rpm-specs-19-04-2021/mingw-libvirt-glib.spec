%{?mingw_package_header}

Name:           mingw-libvirt-glib
Version:        4.0.0
Release:        1%{?dist}
Summary:        MinGW Windows libvirt-glib virtualization library

License:        LGPLv2+
URL:            https://libvirt.org/
Source0:        https://libvirt.org/sources/glib/libvirt-glib-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libvirt
BuildRequires:  mingw64-libvirt
BuildRequires:  gettext
BuildRequires:  pkgconfig
# Native pkg needed for glib-mkenums
BuildRequires:  glib2-devel

BuildArch:      noarch

%package -n mingw32-libvirt-glib
Summary: MingwGW Windows libvirt-gconfig virtualization library

Requires: pkgconfig

%package -n mingw32-libvirt-gconfig
Summary: MingwGW Windows libvirt-gconfig virtualization library

Requires: pkgconfig

%package -n mingw32-libvirt-gobject
Summary: MingwGW Windows libvirt-gobject virtualization library

Requires: pkgconfig

%package -n mingw64-libvirt-glib
Summary: MingwGW Windows libvirt-gconfig virtualization library

Requires: pkgconfig

%package -n mingw64-libvirt-gconfig
Summary: MingwGW Windows libvirt-gconfig virtualization library

Requires: pkgconfig

%package -n mingw64-libvirt-gobject
Summary: MingwGW Windows libvirt-gobject virtualization library

Requires: pkgconfig

%description
MinGW Windows libvirt-glib virtualization library.

%description -n mingw32-libvirt-glib
MinGW Windows libvirt-glib virtualization library.

%description -n mingw32-libvirt-gconfig
MinGW Windows libvirt-gconfig virtualization library.

%description -n mingw32-libvirt-gobject
MinGW Windows libvirt-gobject virtualization library.


%description -n mingw64-libvirt-glib
MinGW Windows libvirt-glib virtualization library.

%description -n mingw64-libvirt-gconfig
MinGW Windows libvirt-gconfig virtualization library.

%description -n mingw64-libvirt-gobject
MinGW Windows libvirt-gobject virtualization library.

%{?mingw_debug_package}

%prep
%setup -q -n libvirt-glib-%{version}


%build
%mingw_meson -Drpath=disabled -Ddocs=disabled -Dintrospection=disabled -Dvapi=disabled
%mingw_ninja

%install
%mingw_ninja_install

%mingw_find_lang libvirt-glib

%files -n mingw32-libvirt-glib -f mingw32-libvirt-glib.lang
%doc README COPYING AUTHORS NEWS
%{mingw32_bindir}/libvirt-glib-1.0-0.dll

%{mingw32_libdir}/libvirt-glib-1.0.dll.a

%{mingw32_libdir}/pkgconfig/libvirt-glib-1.0.pc

%dir %{mingw32_includedir}/libvirt-glib-1.0
%dir %{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib
%{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib.h
%{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib-*.h

%files -n mingw64-libvirt-glib -f mingw64-libvirt-glib.lang
%doc README COPYING AUTHORS NEWS
%{mingw64_bindir}/libvirt-glib-1.0-0.dll

%{mingw64_libdir}/libvirt-glib-1.0.dll.a

%{mingw64_libdir}/pkgconfig/libvirt-glib-1.0.pc

%dir %{mingw64_includedir}/libvirt-glib-1.0
%dir %{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib
%{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib.h
%{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib-*.h



%files -n mingw32-libvirt-gconfig
%{mingw32_bindir}/libvirt-gconfig-1.0-0.dll

%{mingw32_libdir}/libvirt-gconfig-1.0.dll.a

%{mingw32_libdir}/pkgconfig/libvirt-gconfig-1.0.pc

%dir %{mingw32_includedir}/libvirt-gconfig-1.0
%dir %{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig
%{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig.h
%{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig-*.h

%files -n mingw64-libvirt-gconfig
%{mingw64_bindir}/libvirt-gconfig-1.0-0.dll

%{mingw64_libdir}/libvirt-gconfig-1.0.dll.a

%{mingw64_libdir}/pkgconfig/libvirt-gconfig-1.0.pc

%dir %{mingw64_includedir}/libvirt-gconfig-1.0
%dir %{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig
%{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig.h
%{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig-*.h



%files -n mingw32-libvirt-gobject
%{mingw32_bindir}/libvirt-gobject-1.0-0.dll

%{mingw32_libdir}/libvirt-gobject-1.0.dll.a

%{mingw32_libdir}/pkgconfig/libvirt-gobject-1.0.pc

%dir %{mingw32_includedir}/libvirt-gobject-1.0
%dir %{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject
%{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject.h
%{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject-*.h

%files -n mingw64-libvirt-gobject
%{mingw64_bindir}/libvirt-gobject-1.0-0.dll

%{mingw64_libdir}/libvirt-gobject-1.0.dll.a

%{mingw64_libdir}/pkgconfig/libvirt-gobject-1.0.pc

%dir %{mingw64_includedir}/libvirt-gobject-1.0
%dir %{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject
%{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject.h
%{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject-*.h


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:43:50 GMT 2020 Sandro Mani <manisandro@gmail.com> - 3.0.0-5
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 3.0.0-3
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
