%global build64 0
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 7
%{!?openblas_arches:%global openblas_arches x86_64 %{ix86} armv7hl %{power64} aarch64}
%ifnarch %{openblas_arches}
# matches openblas ExclusiveArch
%bcond_without atlas
%else
%if 0%{?__isa_bits} == 64
%global build64 1
%endif
%endif
%endif

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif

# We are linking FORTRAN symbols.  Thus we cannot link --as-needed.
%undefine _ld_as_needed

Name:		arpack
Version:	3.7.0
Release:	9%{dist}
Summary:	Fortran 77 subroutines for solving large scale eigenvalue problems

License:	BSD
URL:		https://github.com/opencollab/arpack-ng
Source0:	https://github.com/opencollab/arpack-ng/archive/%{version}/arpack-ng-%{version}.tar.gz
# Upstream fixes for 
Patch0:		https://patch-diff.githubusercontent.com/raw/opencollab/arpack-ng/pull/197.patch
# Fix for gcc 10
Patch1:         239.patch

BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
%if %{with flexiblas}
BuildRequires:  pkgconfig(flexiblas)
%else
%if %{with atlas}
BuildRequires:	atlas-devel
%else
BuildRequires:	openblas-devel
%endif
%endif
BuildRequires:	libtool >= 2.4.2
BuildRequires: make
Provides:	arpack-ng = %{version}-%{release}
Provides:	arpack-ng%{?_isa} = %{version}-%{release}

%description
ARPACK is a collection of Fortran 77 subroutines designed to solve large
scale eigenvalue problems.

The package is designed to compute a few eigenvalues and corresponding
eigenvectors of a general n by n matrix A. It is most appropriate for
large sparse or structured matrices A where structured means that a
matrix-vector product w <- Av requires order n rather than the usual
order n**2 floating point operations. This software is based upon an
algorithmic variant of the Arnoldi process called the Implicitly
Restarted Arnoldi Method (IRAM).


%package devel
Summary:	Files needed for developing arpack based applications
Requires:	arpack%{?_isa} = %{version}-%{release}
Provides:	arpack-ng-devel = %{version}-%{release}
Provides:	arpack-ng-devel%{?_isa} = %{version}-%{release}

%description devel
ARPACK is a collection of Fortran 77 subroutines designed to solve
large scale eigenvalue problems. This package contains the so
library links used for building arpack based applications.


%package doc
Summary:	Examples for the use of arpack
BuildArch:	noarch

%description doc
This package contains examples for the use of arpack.


%package static
Summary:	Static library for developing arpack based applications
Requires:	arpack-devel%{?_isa} = %{version}-%{release}
Provides:	arpack-ng-static = %{version}-%{release}
Provides:	arpack-ng-static%{?_isa} = %{version}-%{release}

%description static
ARPACK is a collection of Fortran 77 subroutines designed to solve
large scale eigenvalue problems. This package contains the static
library and so links used for building arpack based applications.


%prep
%setup -qc
mv arpack-ng-%{version} src
pushd src
%patch0 -p1
%patch1 -p1
autoreconf -vif
popd
%if %{build64}
cp -pr src src64
%endif


%build
%if %{with flexiblas}
%global blaslib -lflexiblas
%else
%if %{with atlas}
%if 0%{?fedora} || 0%{?rhel} >= 7
%global blaslib -L%{_libdir}/atlas -ltatlas
%else
%global blaslib -L%{_libdir}/atlas -lf77blas -latlas
%endif
%else
%global blaslib -lopenblasp
%endif
%endif
pushd src
%configure --enable-shared --enable-static \
    --with-blas="%{blaslib}" \
    --with-lapack="%{blaslib}" \
    --enable-icb
%make_build
popd
%if %{build64}
pushd src64
%configure --enable-shared --enable-static \
    LIBSUFFIX=64 \
    INTERFACE64=1 \
    --with-blas=%{blaslib}64 \
    --with-lapack=%{blaslib}64 \
    --enable-icb
%make_build
popd
%endif

%install
pushd src
%make_install
popd
%if %{build64}
pushd src64
%make_install
popd
%endif
# Get rid of .la files
rm -r %{buildroot}%{_libdir}/*.la
# Get rid of generic file names (https://github.com/opencollab/arpack-ng/issues/130)

%check
pushd src
%make_build check
pushd EXAMPLES ; make clean ; popd
popd
%if %{build64}
pushd src64
%make_build check
pushd EXAMPLES ; make clean ; popd
popd
%endif

%ldconfig_scriptlets

%files
%doc src/CHANGES src/README.md
%license src/COPYING
%{_libdir}/libarpack.so.*
%if %{build64}
%{_libdir}/libarpack64.so.*
%endif

%files devel
%{_libdir}/pkgconfig/arpack.pc
%{_libdir}/libarpack.so
%if %{build64}
%{_libdir}/pkgconfig/arpack64.pc
%{_libdir}/libarpack64.so
%endif
%{_includedir}/arpack/

%files doc
%doc src/EXAMPLES/ src/DOCUMENTS/
%doc src/CHANGES src/README.md
%license src/COPYING


%files static
%{_libdir}/libarpack.a
%if %{build64}
%{_libdir}/libarpack64.a
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.7.0-8
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 29 2020 Orion Poplawski <orion@nwra.com> - 3.7.0-6
- Tests no longer failing on ppc64le 

* Wed Feb 19 2020 David Schwörer <davidsch@fedoraproject.org> - 3.7.0-5
- fix failure with gcc 10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Orion Poplawski <orion@nwra.com> - 3.7.0-3
- Ignore ppc64le test failure for now

* Thu Nov 28 2019 Orion Poplawski <orion@nwra.com> - 3.7.0-2
- Build ILP64 version properly against non-symbol suffixed openblas (FTBFS bz#1734942)
- Add upstream fix for icb_arpack_cpp test
- New include dir (/usr/include/arpack)

* Thu Aug 01 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1, adding C and C++ bindings.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Björn Esser <besser82@fedoraproject.org> - 3.5.0-5
- Rebuilt for GCC8

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Dominik Mierzejewski <rpm@greysector.net> - 3.5.0-2
- build against openblas on supported arches
- generating configure for 3.4.0+ requires new libtool
- build 64-bit ILP64 version (#1294201)

* Sat May 20 2017 Björn Esser <besser82@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0 (#1451525)
- Drop stuff needed for el5
- Update spec-file to recent guidelines

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-2
- Rebuilt for GCC-7

* Thu Sep 29 2016 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-1
- Update to 3.4.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2.b0f7a60git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Dominik Mierzejewski <rpm@greysector.net> - 3.3.0-1.b0f7a600git
- Update to 3.3.0
- BR: libtool and call autoreconf
- simplify some conditions

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.2.0-1.8fc8fbe3git
- Update source URL.
- Update to 3.2.0.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 Dominik Mierzejewski <rpm@greysector.net> - 3.1.5-1
- update to 3.1.5
- fix source URL
- example binary is no longer installed by default
- enable tests
- don't duplicate documentation and examples in -devel
- clean binaries in EXAMPLES after running testsuite

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 21 2013 Orion Poplawski <orion@cora.nwra.com> - 3.1.3-2
- Rebuild for atlas 3.10 using threaded library

* Thu Sep 05 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.0.1-1
- Change sources to arpack-ng, which provides an up-to-date version of ARPACK.
- Include examples and documentation in a new -doc package.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul  7 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1-12
- Bump spec to fix update path.

* Wed Apr  7 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.1-11
- Change license to BSD (see RH bugs #234191 and #578873).

* Wed Sep 24 2008 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2.1-10
- fix libarpack.so: undefined reference to `etime_' with recent gfortran

* Mon Aug 25 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.1-9
- Patch0 and %%patch make recent rpm silenty fail.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-8
- fix license tag

* Wed Oct 24 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2.1-7
- apply Frederic Hecht's patch for eigenvalue bug
- move static libs to separate package

* Mon Mar 26 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.1-6
- Add license and clarification note
- Add lapack support

* Thu Nov  9 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.1-4
- Freshen up for submitting to fedora extras.
- Fix permissions of so file.
- Add forgotten ldconfig
- Remove dot from summaries.

* Wed Jul 16 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.
