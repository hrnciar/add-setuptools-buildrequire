# The GMP package in Fedora does a full autoreconf; the purpose of doing so is
# not documented in the spec file or in the commit logs, but it is probably a
# reasonable choice for forward-compatibility given the upstream updates
# rarely and the library is very platform-dependent.
%bcond_without autoreconf

Name:           mpir
Version:        3.0.0
%global so_version_c 23
%global so_version_cxx 8
Release:        15%{?dist}
Summary:        Highly optimised library for bignum arithmetic


# The package claims an overall license of LGPLv3+; for a breakdown of the
# licensing of various source files, see PACKAGE-LICENSING.
License:        LGPLv3+ and LGPLv2+ and (LGPLv3+ or GPLv2+) and BSD
URL:            https://mpir.org/

Source0:        https://mpir.org/%{name}-%{version}.tar.bz2
Source1:        PACKAGE-LICENSING
# Fix broken configure test compromised by LTO
Patch0:         %{name}-config.patch
# Preserve debug information from assembly routines; see also
# gmp-6.0.0-debuginfo.patch in the GMP package
Patch1:         %{name}-3.0.0-debuginfo.patch
# Upstream non-ASCII source files are currently encoded in a mixture of UTF-8
# and ISO-8859-1. This patch standardizes on UTF-8, except files in the
# mpir.net directory. See https://github.com/wbhart/mpir/pull/291.
Patch2:         %{name}-3.0.0-utf8-encoding.patch

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# According to GMP spec file, autoreconf on arm needs:
BuildRequires:  perl-Carp
%endif
# For updated config.guess/config.sub with aarch64 support:
BuildRequires:  gnulib-devel

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  m4
%ifarch x86_64 %ix86
BuildRequires:  yasm
%endif

%global _hardened_build 1

%description
MPIR is a highly optimised library for bignum arithmetic forked from the GMP
bignum library. It is written in assembly language and C. It is community
maintained via the GitHub repositories of William Hart (Linux/OSX) and Brian
Gladman (Windows). There are currently no curators for other platforms.

MPIR is assembly optimised for various x86-64 CPUs. It is designed to be
threadsafe.


%package c++
Summary:        Bindings for using %{name} in C++ applications
Requires:       %{name}%{?_isa} = %{version}-%{release}

BuildRequires:  gcc-c++

%description c++
Bindings for using %{name} in C++ applications



%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

Provides:       %{name}-c++-devel%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package doc
Summary:        Documentation for %{name}
License:        LGPLv3+ and LGPLv2+ and GFDL

BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)

%description doc
Documentation for %{name}.


%prep
%autosetup -p1
# Update config.guess/config.sub for aarch64 support, bringing in other updated
# build-aux scripts while we are at it:
for script in compile config.guess config.sub install-sh
do
  cp -vp "%{_datadir}/gnulib/build-aux/${script}" ./
done
cp -vp %{_datadir}/gnulib/build-aux/texinfo.tex ./doc/

cp -vp '%{SOURCE1}' .


%build
%if %{with autoreconf}
autoreconf -ifv
%endif
# Keep the assembler from producing an executable stack; this is an important
# hardening step.
CCAS='gcc -c -Wa,--noexecstack'; export CCAS
# Do we still need to add this manually?
LIBS='-lrt'; export LIBS
%ifarch ppc64le
# MPIR mistakes ppc64le for big-endian PowerPC. Force it to use the generic
# implementation instead so we do not have to exclude the architecture. See
# https://trac.sagemath.org/ticket/19704.
ABI='mode64'; export ABI
MPN_PATH='generic'; export MPN_PATH
%endif
# YASM on EPEL7 explodes on some AVX code; the really coarse workaround is to
# disable fat binaries so these paths are just not compiled.
%configure \
    --disable-static \
%if 0%{?epel} > 7 || ! 0%{?epel}
    --enable-fat \
%endif
%ifnarch x86_64 %ix86
    --with-yasm=%{_bindir}/false \
%endif
    --enable-cxx

# Get rid of undesirable hardcoded rpaths; work around libtool reordering
# -Wl,--as-needed after all the libraries.
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_removing_rpath
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g.*\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Build PDF and HTML docs from the texinfo docs.
texi2pdf --output ./doc/%{name}.pdf ./doc/%{name}.texi
texi2any --output ./doc/html --html ./doc/%{name}.texi


%install
%make_install
rm -vf \
  %{buildroot}%{_infodir}/dir \
  %{buildroot}%{_libdir}/lib%{name}.la \
  %{buildroot}%{_libdir}/lib%{name}xx.la

# Manually install documentation (except info pages, already installed)
install -d %{buildroot}%{_pkgdocdir}
cp -vrp ./doc/devel ./doc/html %{buildroot}%{_pkgdocdir}/
install -m 0644 -t %{buildroot}%{_pkgdocdir} \
   AUTHORS ChangeLog NEWS README \
   doc/isa_abi_headache \
   doc/%{name}.pdf


%check
env LD_LIBRARY_PATH="${PWD}/.libs" %make_build check


# Needed for EPEL only:
%ldconfig_scriptlets


%files
%license COPYING
%license COPYING.LIB
%license PACKAGE-LICENSING
%{_libdir}/lib%{name}.so.%{so_version_c}
%{_libdir}/lib%{name}.so.%{so_version_c}.*


%files c++
%{_libdir}/lib%{name}xx.so.%{so_version_cxx}
%{_libdir}/lib%{name}xx.so.%{so_version_cxx}.*


%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}xx.h
%{_libdir}/lib%{name}xx.so


%files doc
%license COPYING
%license COPYING.LIB
%license PACKAGE-LICENSING

%{_infodir}/%{name}.info*

%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/NEWS
%{_pkgdocdir}/README
%{_pkgdocdir}/%{name}.pdf
%{_pkgdocdir}/devel
%{_pkgdocdir}/html
%{_pkgdocdir}/isa_abi_headache


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-14
- Do not BR yasm on platforms where it is not used in the build
  (https://github.com/wbhart/mpir/issues/270)

* Tue Dec  8 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-13
- Convert character encodings with a patch instead of a script; it turns out it
  takes manual inspection to get this right

* Mon Dec  7 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-12
- Split the C++ library into a subpackage; keep a combined -devel package, as
  the GMP package in Fedora does, to avoid breaking BR’s

* Sun Dec  6 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-11
- Stop excluding ppc64le architecture: build a generic version, without
  optimized assembly
- Enable fat binaries where supported (x86)
- Fix missing debuginfo for assembly routines
- Ensure hardened build is always enabled, including on EPEL
- Strict so-versions in files pattern for shared library (helps detect
  so-version changes)
- Create -doc subpackage; add HTML and PDF documentation built from texinfo
- Add virtual Provides for -c++ and -c++-devel subpackages, by analogy to GMP;
  note, however, that we cannot actually split out the subpackage without
  breaking most C++ packages that have this as a BuildRequires
- Add BR on make for
  https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot
- Use modern macros like autosetup, make_build, make_install
- Get an updated config.guess, etc. from gnulib-devel instead of patching it
- Convert HTTP URLs to HTTPS
- Updated summary and description from upstream
- Correct license field (not just LGPLv3+) and add PACKAGE-LICENSING file
- More conversion of ISO-8859-1-encoded files
- Reformat whitespace

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 3.0.0-9
- Fix broken configure test compromised by LTO

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 3.0.0-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Jerry James <loganjerry@gmail.com> - 2.7.2-1
- New upstream release (bz 1284140)

* Fri Nov 13 2015 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- New upstream release (bz 1281980)

* Wed Jul  1 2015 Jerry James <loganjerry@gmail.com> - 2.7.0-1
- New upstream release (bz 1236066)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 2.6.0-9
- Update URLs
- Use license macro
- Drop workaround for binutils bug, fixed in 2.24
- Combine libtool workarounds for -Wl,--as-needed

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Jerry James <loganjerry@gmail.com> - 2.6.0-5
- Add aarch64 support (bz 926173)

* Fri Feb 22 2013 Jerry James <loganjerry@gmail.com> - 2.6.0-4
- Add -test patch to fix a broken test

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec  5 2012 Jerry James <loganjerry@gmail.com> - 2.6.0-2
- Drop ExcludeArch; s390/s390x systems use the generic mpn support

* Fri Nov  9 2012 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- New upstream release
- Drop libtool typo fix; fixed upstream
- Fix libtool workaround for -Wl,--as-needed

* Thu Oct  4 2012 Jerry James <loganjerry@gmail.com> - 2.5.2-1
- New upstream release
- Link with -lrt to get the clock_* functions
- Convince libtool to use -Wl,--as-needed appropriately

* Wed Sep 12 2012 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- New upstream release
- License change to LPGLv3+
- Support for s390 / s390x has been dropped
- Minor spec file cleanups

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Dan Horák <dan[at]danny.cz> - 1.3.1-6
- add s390x support from GMP

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 16 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-4
- Fix the RHEL build

* Fri Mar 05 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-3
- Include HTML documentation
- Include demos

* Thu Mar 04 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-2
- Ensure consistent use of macros
- Avoid multilib conflict due to modified timestamp on AUTHORS doc
- Replace perl find and replace with sed

* Wed Feb 17 2010 M D Chappell <tremble@tremble.org.uk> - 1.3.1-1
- Initial build
