%{?mingw_package_header}

%global verdir %(echo ${version} | cut -d. -f1,2)

Name: mingw-gtk-vnc
Version: 1.2.0
Release: 1%{?dist}
Summary: MinGW Windows port of VNC client GTK widget

License: LGPLv2+
Source: https://download.gnome.org/sources/gtk-vnc/%{verdir}/gtk-vnc-%{version}.tar.xz
URL: https://gitlab.gnome.org/GNOME/gtk-vnc

BuildArch: noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: mingw32-cairo
BuildRequires: mingw64-cairo
BuildRequires: mingw32-gettext
BuildRequires: mingw64-gettext
BuildRequires: mingw32-libgcrypt
BuildRequires: mingw64-libgcrypt
BuildRequires: mingw32-gnutls
BuildRequires: mingw64-gnutls
BuildRequires: mingw32-gtk3
BuildRequires: mingw64-gtk3

BuildRequires: pkgconfig
BuildRequires: meson
BuildRequires: gcc
BuildRequires: gettext

BuildRequires: /usr/bin/pod2man

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

# Mingw32
%package -n mingw32-gvnc
Summary: MinGW Windows port of VNC GObject

%package -n mingw32-gvnc-tools
Summary: Command line VNC tools

%package -n mingw32-gtk-vnc2
Summary: A GTK3 widget for VNC clients
Requires: pkgconfig
Obsoletes: mingw32-gtk-vnc < 1.0.0

%description -n mingw32-gvnc
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

%description -n mingw32-gvnc-tools
Provides useful command line utilities for interacting with
VNC servers. Includes the gvnccapture program for capturing
screenshots of a VNC desktop

%description -n mingw32-gtk-vnc2
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

# Mingw64
%package -n mingw64-gvnc
Summary: MinGW Windows port of VNC GObject

%package -n mingw64-gvnc-tools
Summary: Command line VNC tools

%package -n mingw64-gtk-vnc2
Summary: A GTK3 widget for VNC clients
Requires: pkgconfig
Obsoletes: mingw64-gtk-vnc < 1.0.0

%description -n mingw64-gvnc
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

%description -n mingw64-gvnc-tools
Provides useful command line utilities for interacting with
VNC servers. Includes the gvnccapture program for capturing
screenshots of a VNC desktop

%description -n mingw64-gtk-vnc2
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%{?mingw_debug_package}


%prep
%autosetup -n gtk-vnc-%{version}


%build
%mingw_meson -Dintrospection=disabled
%mingw_ninja


%install
export DESTDIR=%{buildroot}
%mingw_ninja install

rm -f $RPM_BUILD_ROOT%{mingw32_mandir}/man1/gvnccapture.1*
rm -f $RPM_BUILD_ROOT%{mingw64_mandir}/man1/gvnccapture.1*

%mingw_find_lang gtk-vnc


# Mingw32
%files -n mingw32-gvnc -f gtk-vnc.lang
%doc AUTHORS
%doc ChangeLog
%doc ChangeLog-old
%doc NEWS
%doc README
%doc COPYING.LIB
%{mingw32_bindir}/libgvnc-1.0-0.dll
%{mingw32_libdir}/libgvnc-1.0.dll.a
%{mingw32_libdir}/pkgconfig/gvnc-1.0.pc
%{mingw32_includedir}/gvnc-1.0

%files -n mingw32-gtk-vnc2
%{mingw32_bindir}/libgtk-vnc-2.0-0.dll
%{mingw32_libdir}/libgtk-vnc-2.0.dll.a
%{mingw32_libdir}/pkgconfig/gtk-vnc-2.0.pc
%{mingw32_includedir}/gtk-vnc-2.0

%files -n mingw32-gvnc-tools
%{mingw32_bindir}/gvnccapture.exe

# Mingw64
%files -n mingw64-gvnc -f gtk-vnc.lang
%doc AUTHORS
%doc ChangeLog
%doc ChangeLog-old
%doc NEWS
%doc README
%doc COPYING.LIB
%{mingw64_bindir}/libgvnc-1.0-0.dll
%{mingw64_libdir}/libgvnc-1.0.dll.a
%{mingw64_libdir}/pkgconfig/gvnc-1.0.pc
%{mingw64_includedir}/gvnc-1.0

%files -n mingw64-gtk-vnc2
%{mingw64_bindir}/libgtk-vnc-2.0-0.dll
%{mingw64_libdir}/libgtk-vnc-2.0.dll.a
%{mingw64_libdir}/pkgconfig/gtk-vnc-2.0.pc
%{mingw64_includedir}/gtk-vnc-2.0

%files -n mingw64-gvnc-tools
%{mingw64_bindir}/gvnccapture.exe

%changelog
* Wed Apr 14 2021 Daniel P. Berrang?? <berrange@redhat.com> - 1.2.0-1
- Update to 1.2.0 release
- Update URLs better sites
- Use versioned obsoletes tags

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:40:41 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-5
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-3
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug  8 2019 Daniel P. Berrang?? <berrange@redhat.com> - 1.0.0-1
- Update to 1.0.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Daniel P. Berrang?? <berrange@redhat.com> - 0.9.0-1%{?extra_release}
- Update to 0.9.0 release

* Wed Aug  1 2018 Daniel P. Berrang?? <berrange@redhat.com> - 0.8.0-1
- Update to 0.8.0 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Daniel P. Berrang?? <berrange@redhat.com> - 0.7.2-1
- Update to 0.7.2 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb  9 2017 Daniel P. Berrange <berrange@redhat.com> - 0.7.0-1
- Update to 0.7.0 release
- CVE-2017-5884 - fix bounds checking for RRE, hextile and
  copyrect encodings
- CVE-2017-5885 - fix color map index bounds checking

* Thu Oct  6 2016 Daniel P. Berrange <berrange@redhat.com> - 0.6.0-1
- Update to 0.6.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
