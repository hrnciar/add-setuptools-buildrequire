Name:		libnxz
Version:	0.61
Release:	3%{?dist}
Summary:	Zlib implementation for POWER processors
License:	ASL 2.0
Url:		https://github.com/libnxz/power-gzip
BuildRequires:	zlib-devel
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Stop depending on a git repository when running make.
Patch0: rm-git.patch
# Upstream PR #42: Keep libraries' symlinks when installing.
Patch1: libnxz.so.patch

# Be explicit about the soname in order to avoid unintentional changes.
%global soname libnxz.so.0.61

ExclusiveArch:	ppc64le
BuildRequires:	gcc
BuildRequires: make

%description
libnxz is a zlib-compatible library that uses the NX GZIP Engine available on
POWER9 or newer processors in order to provide a faster zlib/gzip compression
without using the general-purpose cores.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains header files for developing application that
use %{name}.

%package	static
Summary:	Static library for %{name} development
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description	static
The %{name}-static package contains static libraries for developing
application that use %{name}.

%prep
%autosetup -p1 -n power-gzip-%{version}

%build
%make_build FLG="-std=gnu11 %{build_cflags} "

%check
# libnxz tests only work on P9 servers or newer, bare metal, with
# Linux >= 5.8.  This combination is not guaranteed to have at build time,
# forcing us to disable the tests.

%install
make install PREFIX="%{buildroot}%{_prefix}" LIBDIR="%{buildroot}%{_libdir}"

%files
%{_libdir}/%{soname}
%{_libdir}/libnxz.so.0
%license licenses/APACHE-2.0.txt
%doc README.md

%files devel
%{_includedir}/libnxz.h
%{_libdir}/libnxz.so

%files static
%{_libdir}/libnxz.a

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 0.61-2
- Fix release version and match with changelog.

* Tue Oct 27 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 0.61-0
- Initial packaging
