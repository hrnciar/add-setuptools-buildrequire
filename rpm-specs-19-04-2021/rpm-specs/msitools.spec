#define _version_suffix

# The mingw* RPMs are noarch, and the wxi data files are
# arch independant, so it is a waste of CPU cycles to run
# validation on all arches. Just run on x86_64 since that
# has the fastest Fedora builders.
%ifarch x86_64
%define with_validate 1
%else
%define with_validate 0
%endif

Name:           msitools
Version:        0.101
Release:        2%{?dist}
Summary:        Windows Installer tools

License:        GPLv2+
URL:            http://ftp.gnome.org/pub/GNOME/sources/%{name}
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}%{?_version_suffix}.tar.xz

Requires:       libgsf >= 1.14.24-2

BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libgcab1-devel >= 0.2
BuildRequires:  libgsf-devel
BuildRequires:  vala
BuildRequires:  bison

%if %{with_validate}
BuildRequires:  perl-base
BuildRequires:  perl-XML-XPath
BuildRequires:  mingw32-adwaita-icon-theme
BuildRequires:  mingw64-adwaita-icon-theme
BuildRequires:  mingw32-atk
BuildRequires:  mingw64-atk
BuildRequires:  mingw32-brotli
BuildRequires:  mingw64-brotli
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-curl
BuildRequires:  mingw64-curl
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw32-expat
BuildRequires:  mingw64-expat
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw64-freetype
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-glib-networking
BuildRequires:  mingw64-glib-networking
BuildRequires:  mingw32-gmp
BuildRequires:  mingw64-gmp
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw32-gsm
BuildRequires:  mingw64-gsm
BuildRequires:  mingw32-gstreamer1-plugins-bad-free
BuildRequires:  mingw64-gstreamer1-plugins-bad-free
BuildRequires:  mingw32-gstreamer1-plugins-base
BuildRequires:  mingw64-gstreamer1-plugins-base
BuildRequires:  mingw32-gstreamer1-plugins-good
BuildRequires:  mingw64-gstreamer1-plugins-good
BuildRequires:  mingw32-gstreamer1
BuildRequires:  mingw64-gstreamer1
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-gtk-vnc2
BuildRequires:  mingw64-gtk-vnc2
BuildRequires:  mingw32-gvnc
BuildRequires:  mingw64-gvnc
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw32-hicolor-icon-theme
BuildRequires:  mingw64-hicolor-icon-theme
BuildRequires:  mingw32-icu
BuildRequires:  mingw64-icu
BuildRequires:  mingw32-ilmbase
BuildRequires:  mingw64-ilmbase
BuildRequires:  mingw32-jasper
BuildRequires:  mingw64-jasper
BuildRequires:  mingw32-json-glib
BuildRequires:  mingw64-json-glib
BuildRequires:  mingw32-libepoxy
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw32-libffi
BuildRequires:  mingw64-libffi
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw32-libgovirt
BuildRequires:  mingw64-libgovirt
BuildRequires:  mingw32-libgpg-error
BuildRequires:  mingw64-libgpg-error
BuildRequires:  mingw32-libidn2
BuildRequires:  mingw64-libidn2
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw32-libogg
BuildRequires:  mingw64-libogg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libpsl
BuildRequires:  mingw64-libpsl
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw64-libsoup
BuildRequires:  mingw32-libssh2
BuildRequires:  mingw64-libssh2
BuildRequires:  mingw32-libtasn1
BuildRequires:  mingw64-libtasn1
BuildRequires:  mingw32-libtheora
BuildRequires:  mingw64-libtheora
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw32-libunistring
BuildRequires:  mingw64-libunistring
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw32-libvirt-glib
BuildRequires:  mingw64-libvirt-glib
BuildRequires:  mingw32-libvirt
BuildRequires:  mingw64-libvirt
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-nettle
BuildRequires:  mingw64-nettle
BuildRequires:  mingw32-OpenEXR
BuildRequires:  mingw64-OpenEXR
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-openssl
BuildRequires:  mingw32-opus
BuildRequires:  mingw64-opus
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  mingw32-p11-kit
BuildRequires:  mingw64-p11-kit
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-pango
BuildRequires:  mingw32-pcre
BuildRequires:  mingw64-pcre
BuildRequires:  mingw32-pixman
BuildRequires:  mingw64-pixman
BuildRequires:  mingw32-portablexdr
BuildRequires:  mingw64-portablexdr
BuildRequires:  mingw32-readline
BuildRequires:  mingw64-readline
BuildRequires:  mingw32-rest
BuildRequires:  mingw64-rest
BuildRequires:  mingw32-SDL
BuildRequires:  mingw64-SDL
BuildRequires:  mingw32-speex
BuildRequires:  mingw64-speex
BuildRequires:  mingw32-spice-glib
BuildRequires:  mingw64-spice-glib
BuildRequires:  mingw32-spice-gtk3
BuildRequires:  mingw64-spice-gtk3
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw32-termcap
BuildRequires:  mingw64-termcap
BuildRequires:  mingw32-usbredir
BuildRequires:  mingw64-usbredir
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-wavpack
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1924216
ExcludeArch: s390x

%description
msitools is a collection of utilities to inspect and create Windows
Installer files.  It is useful in a cross-compilation environment such
as fedora-mingw.

%package -n libmsi1
Summary:        A library to manipulate Windows .MSI files
License:        LGPLv2+

%description -n libmsi1
libmsi is a GObject library to work with Windows Installer files.  It is
a port from the MSI library of the Wine project.

%package -n libmsi1-devel
Summary:        A library to manipulate Windows .MSI files
License:        LGPLv2+
Requires:       libmsi1%{?_isa} = %{version}-%{release}

%description -n libmsi1-devel
The libmsi1-devel package includes the header files for libmsi.

%prep
%autosetup -S git_am -n msitools-%{version}%{?_version_suffix}

%build
%if %{with_validate}
%meson -Dvalidate-wxi=true
%else
%meson
%endif
%meson_build

%install
%meson_install

%find_lang %{name}

%check
%meson_test

%ldconfig_scriptlets -n libmsi1

%files
%doc copyright NEWS README.md TODO
%{_bindir}/msibuild
%{_bindir}/msidiff
%{_bindir}/msidump
%{_bindir}/msiextract
%{_bindir}/msiinfo
%{_bindir}/wixl
%{_bindir}/wixl-heat
%{_datadir}/bash-completion/completions/msitools
%{_datadir}/wixl-%{version}%{?_version_suffix}

%files -n libmsi1 -f %{name}.lang
%{_libdir}/girepository-1.0/Libmsi-1.0.typelib
%{_libdir}/libmsi.so.0*

%files -n libmsi1-devel
%{_datadir}/gir-1.0/Libmsi-1.0.gir
%{_datadir}/vala/vapi/libmsi-1.0.vapi
%{_datadir}/vala/vapi/libmsi-1.0.deps
%{_includedir}/libmsi-1.0/*
%{_libdir}/libmsi.so
%{_libdir}/pkgconfig/libmsi-1.0.pc


%changelog
* Wed Feb  3 2021 Daniel P. Berrangé <berrange@redhat.com> - 0.101-2
- Fix enablement of wxi tests
- Use perl-base and gettext for more minimal dep chain

* Tue Feb 02 2021 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.101-1
- new version v0.101
- Fix FTBFS. rhbz#1923683

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.100-7
- Fix FTBFS. rhbz#1864178
- Drop mingw-gstreamer* checks, it's outdated.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Daniel P. Berrangé <berrange@redhat.com> - 0.100-4
- Switch spice back to dsound instead of wasapi

* Thu Apr 23 2020 Daniel P. Berrangé <berrange@redhat.com> - 0.100-3
- Re-enable wix validation
- Fix bugs in multiple wxi manifests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
