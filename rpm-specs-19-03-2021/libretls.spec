Summary:        Port of libtls from LibreSSL to OpenSSL
Name:           libretls
Version:        3.3.1p1
Release:        1%{?dist}
# libretls itself is ISC but uses other source codes, breakdown:
# BSD: compat/strsep.c
# MIT: compat/timegm.c
# Public Domain: compat/{{explicit_bzero,ftruncate,pread,pwrite}.c,chacha_private.h}
License:        ISC and BSD and MIT and Public Domain
URL:            https://git.causal.agency/libretls/about/
Source0:        https://causal.agency/libretls/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  openssl-devel >= 1.1.1b
%else
BuildRequires:  openssl11-devel >= 1.1.1b
%endif
BuildRequires:  man

%description
LibreTLS is a port of libtls from LibreSSL to OpenSSL. OpenBSD's libtls is a
new TLS library, designed to make it easier to write foolproof applications.

%package devel
Summary:        Development files for libretls
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The libretls-devel package contains libraries and header files for developing
applications that use libtls.

%if 0%{!?_without_static:1}
%package static
Summary:        Static library for libretls
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The libretls-static package includes static libraries of libretls. Install it
if you need to link statically with libtls.
%endif

%prep
%setup -q

%build
%if 0%{?rhel} == 7
sed -e 's| openssl | openssl11 |g' -i configure
%endif

%configure %{?_without_static:--disable-static}
%make_build

%install
%make_install

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/libtls.la

# Convert README man page to text file
MANWIDTH=72 man ./README.7 | col -bx > README
touch -c -r README.7 README

# Install README man page as libtls.7
sed -e 's/README 7/libtls 7/g' -i README.7
touch -c -r README README.7
install -D -p -m 0644 README.7 $RPM_BUILD_ROOT%{_mandir}/man7/libtls.7

%ldconfig_scriptlets

%files
%doc README
%{_libdir}/libtls.so.20*
%{_mandir}/man7/libtls.7*

%files devel
%{_libdir}/libtls.so
%{_libdir}/pkgconfig/libtls.pc
%{_includedir}/tls.h
%{_mandir}/man3/tls_*.3*

%if 0%{!?_without_static:1}
%files static
%{_libdir}/libtls.a
%endif

%changelog
* Sat Mar 06 2021 Robert Scheck <robert@fedoraproject.org> 3.3.1p1-1
- Upgrade to 3.3.1p1

* Fri Mar 05 2021 Robert Scheck <robert@fedoraproject.org> 3.3.1-1
- Upgrade to 3.3.1 (#1935540)
- Initial spec file for Fedora and Red Hat Enterprise Linux
