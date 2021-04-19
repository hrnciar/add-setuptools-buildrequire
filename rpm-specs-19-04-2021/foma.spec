# Upstream changed its licensing to ASL 2.0 after releasing 0.9.18.
# I have decided to use the newest upstream code from September 2020 because
# in addition to many other fixes it fixes the build on Fedora.
%global commit0 b44022c7d9d347dc7392aabbf72c82e558767675
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshotdate 20200928

%global libname libfoma

Name:           foma
Version:        0.9.18
Release:        0.10.%{snapshotdate}git%{shortcommit0}%{?dist}
Summary:        Xerox-compatible finite-state compiler

License:        ASL 2.0
URL:            https://github.com/mhulden/foma
Source0:        https://github.com/mhulden/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

# This patch is made after the OpenSUSE patch at
# https://build.opensuse.org/package/view_file/openSUSE:Factory/foma/foma-harden-build.patch?expand=1
#
# Foma does not use autotools, which complicates things a bit.
# CFLAGS, LDFLAGS and FLOOKUPLDFLAGS are edited with sed during the build so
# that the Fedora hardening switches are used. We can't, however, just
# add -pie to all of the linking phases with sed, because that would break
# the linker when building the shared library. For discussion on a similar
# issue, see https://lists.debian.org/debian-devel/2016/05/msg00302.html
Patch0:         foma-harden-build-fedora.patch

BuildRequires:  gcc zlib-devel readline-devel flex bison
BuildRequires: make
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description
Foma can be used for constructing finite-state automata and transducers.
It has support for many natural language processing applications such as
producing morphological analyzers. It is sufficiently generic to use for
a large number of purposes in addition to NLP. The foma interface is
similar to the Xerox xfst interface.

This package includes the foma command line tools.


%package -n     %{libname}
Summary:        The foma C library

%description -n %{libname}
Foma can be used for constructing finite-state automata and transducers.
It has support for many natural language processing applications such as
producing morphological analyzers. It is sufficiently generic to use for
a large number of purposes in addition to NLP. The foma interface is
similar to the Xerox xfst interface.

This package includes the foma C library.


%package -n     %{libname}-devel
Summary:        Development files for %{libname}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n %{libname}-devel
The libfoma-devel package contains libraries and header files for
developing applications that use libfoma.

%prep
%autosetup -n %{name}-%{commit0} -p1


%build
sed -i '/^CFLAGS/c\CFLAGS = %{optflags} -Wl,--as-needed -D_GNU_SOURCE -std=c99 -fvisibility=hidden -fPIC' foma/Makefile
sed -i '/^LDFLAGS/c\LDFLAGS = -lreadline -lz -ltermcap %{build_ldflags}' foma/Makefile
sed -i '/^FLOOKUPLDFLAGS/c\FLOOKUPLDFLAGS = libfoma.a -lz %{build_ldflags}' foma/Makefile
sed -i 's|echo "prefix=${prefix}"|echo "prefix=%{_prefix}"|' foma/Makefile

cd foma
%make_build


%install
sed -i '/^prefix/c\prefix = %{buildroot}%{_prefix}' foma/Makefile
sed -i '/^libdir/c\libdir = %{buildroot}%{_libdir}' foma/Makefile
cd foma
%make_install
# Remove static archive
find %{buildroot} -name '*.a' -exec rm -f {} ';'


%files
%{_bindir}/cgflookup
%{_bindir}/flookup
%{_bindir}/foma

%files -n %{libname}
%license foma/COPYING
%doc foma/README
%{_libdir}/%{libname}.so.0
%{_libdir}/%{libname}.so.0.9.18

%files -n %{libname}-devel
%{_includedir}/*.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-0.10.20200928gitb44022c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Ville-Pekka Vainio <vpvainio AT iki.fi> - 0.9.18-0.9.20200928gitb44022c
- Fix typo in spec
- Rewrite patch, name it foma-harden-build-fedora.patch and explain the need for it

* Sun Oct 04 2020 Ville-Pekka Vainio <vpvainio AT iki.fi> - 0.9.18-0.8.20200928gitb44022c
- Use latest upstream code with my own Makefile fix merged

* Mon Sep 28 2020 Ville-Pekka Vainio <vpvainio AT iki.fi> - 0.9.18-0.7.20200715git0cd2e4a
- Fix dependencies in Makefile to enable parallel build

* Sun Sep 27 2020 Ville-Pekka Vainio <vpvainio AT iki.fi> - 0.9.18-0.6.20200715git0cd2e4a
- Use newest code from upstream, fixes build
- Update foma-harden-build.patch
- Package the pkgconfig file

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-0.5.20150613git0fa48db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-0.4.20150613git0fa48db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.18-0.3.20150613git0fa48db
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-0.2.20150613git0fa48db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Ville-Pekka Vainio <vpvainio AT iki.fi> 0.9.18-0.1.20150613git0fa48db
- Initial package.
