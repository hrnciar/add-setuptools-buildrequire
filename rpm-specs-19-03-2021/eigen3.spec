# The (empty) main package is arch, to have the package built and tests run
# on all arches, but the actual result package is the noarch -devel subpackge.
# Debuginfo packages are disabled to prevent rpmbuild from generating an empty
# debuginfo package for the empty main package.
%global debug_package %{nil}

# FIXME ICE on ppc64le when buildings docs with optflags
%ifarch ppc64le
%global optflags %{nil}
%endif


%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%if 0%{?rhel} >= 8
%bcond_with qt
%else
%bcond_without qt
%endif

Name:           eigen3
Version:        3.3.9
Release:        4%{?dist}
Summary:        A lightweight C++ template library for vector and matrix math

License:        MPLv2.0 and LGPLv2+ and BSD
URL:            http://eigen.tuxfamily.org/index.php?title=Main_Page
Source0:        https://gitlab.com/libeigen/eigen/-/archive/%{version}/eigen-%{version}.tar.bz2

# Backport fix for conflicting declarations of log1p
# https://gitlab.com/libeigen/eigen/-/commit/d55d392e7b1136655b4223bea8e99cb2fe0a8afd.patch
Patch0:         eigen3_logp.patch

BuildRequires:  %{blaslib}-devel
BuildRequires:  fftw-devel
BuildRequires:  glew-devel
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  mpfr-devel
BuildRequires:  sparsehash-devel
BuildRequires:  suitesparse-devel
BuildRequires:  gcc-gfortran
BuildRequires:  SuperLU-devel
%if %{with qt}
BuildRequires:  qt-devel
%endif
BuildRequires:  scotch-devel
BuildRequires:  metis-devel

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  tex(latex)

%description
%{summary}.


%package devel
Summary:        A lightweight C++ template library for vector and matrix math
BuildArch:      noarch
# -devel subpkg only atm, compat with other distros
Provides:       %{name} = %{version}-%{release}
# not *strictly* a -static pkg, but the results are the same
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:        Developer documentation for Eigen
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description doc
Developer documentation for Eigen.


%prep
%autosetup -p1 -n eigen-%{version}


%build
%cmake \
    -DINCLUDE_INSTALL_DIR=include/%{name} \
    -DBLAS_LIBRARIES="-l%{blaslib}" \
    -DSUPERLU_INCLUDES=%{_includedir}/SuperLU \
    -DSCOTCH_INCLUDES=%{_includedir} -DSCOTCH_LIBRARIES="scotch" \
    -DMETIS_INCLUDES=%{_includedir} -DMETIS_LIBRARIES="metis" \
    -DCMAKEPACKAGE_INSTALL_DIR=share/cmake/%{name}

%cmake_build
%cmake_build --target doc

rm -f %{_vpath_builddir}/doc/html/installdox
rm -f %{_vpath_builddir}/doc/html/unsupported/installdox


%install
%cmake_install


%check
# Run tests but make failures non-fatal. Note that upstream doesn't expect the
# tests to pass consistently since they're seeded randomly.
#cmake_build --target buildtests
#cmake_build --target test -- test ARGS="-V" || :


%files devel
%license COPYING.README COPYING.BSD COPYING.MPL2 COPYING.LGPL
%{_includedir}/%{name}
%{_datadir}/cmake/%{name}
%{_datadir}/pkgconfig/%{name}.pc

%files doc
%doc %{_vpath_builddir}/doc/html


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Jan Grulich <jgrulich@redhat.com> - 3.3.9-3
- Drop qt dependency on RHEL 8 and higher

* Tue Jan 19 2021 Sandro Mani <manisandro@gmail.com> - 3.3.9-2
- Backport fix for conflicting declarations of log1p

* Sun Dec 06 2020 Sandro Mani <manisandro@gmail.com> - 3.3.9-1
- Update to 3.3.9

* Mon Oct 05 2020 Sandro Mani <manisandro@gmail.com> - 3.3.8-2
- Drop reference to undefined Eigen::eigen_assert_exception

* Mon Oct 05 2020 Sandro Mani <manisandro@gmail.com> - 3.3.8-1
- Update to 3.3.8

* Tue Sep 01 2020 I??aki ??car <iucar@fedoraproject.org> - 3.3.7-7
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 29 2020 Fabio Valentini <decathorpe@gmail.com> - 3.3.7-6
- Adapt to CMake macros changes in fedora 33+.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 25 2018 Sandro Mani <manisandro@gmail.com> - 3.3.7-1
- Update to 3.3.7
- Modernize spec
- Add doc

* Mon Dec 10 2018 Sandro Mani <manisandro@gmail.com> - 3.3.6-1
- Update to 3.3.6

* Thu Sep 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.3.5-2
- backport upstream fix for step FTBFS (#1619860)

* Thu Jul 26 2018 Sandro Mani <manisandro@gmail.com> - 3.3.5-1
- Update to 3.3.5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Bj??rn Esser <besser82@fedoraproject.org> - 3.3.4-6
- Fix compilation of Jacobi rotations with ARM NEON, some
  specializations of internal::conj_helper were missing

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 3.3.4-5
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Sandro Mani <manisandro@gmail.com> - 3.3.4-1
- Update to 3.3.4

* Wed Feb 22 2017 Sandro Mani <manisandro@gmail.com> - 3.3.3-1
- Update to 3.3.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Sandro Mani <manisandro@gmail.com> - 3.3.2-1
- Update to 3.3.2

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 3.3.1-1
- Update to 3.3.1 (rhbz#1408538)

* Wed Nov 23 2016 Rich Mattes <richmattes@gmail.com> - 3.3.0-1
- Update to 3.3.0
- Stop renaming tarball - just use upstream tarball

* Tue Oct 04 2016 Sandro Mani <manisandro@gmail.com> - 3.2.10-1
- Update to 3.2.10

* Tue Jul 19 2016 Sandro Mani <manisandro@gmail.com> - 3.2.9-1
- Update to 3.2.9

* Sat Feb 20 2016 Sandro Mani <manisandro@gmail.com> - 3.2.8-1
- Update to 3.2.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Sandro Mani <manisandro@gmail.com> - 3.2.7-3
- Again: Fix incorrect include path in pkgconfig file

* Fri Nov 06 2015 Sandro Mani <manisandro@gmail.com> - 3.2.7-2
- Fix incorrect include path in pkgconfig file

* Thu Nov 05 2015 Sandro Mani <manisandro@gmail.com> - 3.2.7-1
- Update to release 3.2.7

* Thu Oct 01 2015 Sandro Mani <manisandro@gmail.com> - 3.2.6-1
- Update to release 3.2.6

* Fri Aug 21 2015 Rich Mattes <richmattes@gmail.com> - 3.2.5-2
- Apply patch to install FindEigen3.cmake

* Tue Jun 16 2015 Sandro Mani <manisandro@gmail.com> - 3.2.5-1
- Update to release 3.2.5

* Thu Jan 22 2015 Sandro Mani <manisandro@gmail.com> - 3.2.4-1
- Update to release 3.2.4

* Mon Jan 05 2015 Rich Mattes <richmattes@gmail.com> - 3.2.3-2
- Backport upstream Rotation2D fix

* Thu Dec 18 2014 Sandro Mani <manisandro@gmail.com> - 3.2.3-1
- Update to release 3.2.3
- Drop upstreamed eigen3-ppc64.patch

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Sandro Mani <manisandro@gmail.com> - 3.2.2-1
- Update to release 3.2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-4
- Add ppc64 support

* Thu Feb 27 2014 Sandro Mani <manisandro@gmail.com> - 3.2.1-3
- Make doc package noarch

* Thu Feb 27 2014 Sandro Mani <manisandro@gmail.com> - 3.2.1-2
- Split off doc to a separate package

* Wed Feb 26 2014 Sandro Mani <manisandro@gmail.com> - 3.2.1-1
- Udpate to release 3.2.1

* Sun Aug 11 2013 Sandro Mani <manisandro@gmail.com> - 3.2-3
- Build and run tests
- Drop -DBLAS_LIBRARIES_DIR, not used
- Add some BR to enable tests of corresponding backends
- spec cleanup

* Wed Jul 24 2013 Sandro Mani <manisandro@gmail.com> - 3.2-1
- Update to release 3.2

* Sat Jun 29 2013 Rich Mattes <richmattes@gmail.com> - 3.1.3-2
- Add upstream patch to fix malloc/free bugs (rhbz#978971)

* Fri Apr 19 2013 Sandro Mani <manisandro@gmail.com> - 3.1.3-1
- Update to release 3.1.3
- Add patch for unused typedefs warning with gcc4.8

* Tue Mar 05 2013 Rich Mattes <richmattes@gmail.com> - 3.1.2-1
- Update to release 3.1.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 28 2012 Tim Niemueller <tim@niemueller.de> - 3.0.6-1
- Update to release 3.0.6 (fixes GCC 4.7 warnings)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 11 2012 Rich Mattes <richmattes@gmail.com> - 3.0.5-1
- Update to release 3.0.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Rich Mattes <richmattes@gmail.com> - 3.0.4-1
- Update to release 3.0.4

* Tue Nov 15 2011 Rich Mattes <richmattes@gmail.com> - 3.0.3-1
- Update to release 3.0.3

* Sun Apr 17 2011 Rich Mattes <richmattes@gmail.com> - 3.0.0-2
- Patched sources to fix build failure
- Removed fixes made upstream
- Added project name to source tarball filename

* Sat Mar 26 2011 Rich Mattes <richmattes@gmail.com> - 3.0.0-1
- Update to release 3.0.0

* Tue Jan 25 2011 Rich Mattes <richmattes@gmail.com> - 3.0-0.2.beta2
- Change blas-devel buildrequirement to atlas-devel
- Don't make the built-in experimental blas library

* Mon Jan 24 2011 Rich Mattes <richmattes@gmail.com> - 3.0-0.1.beta2
- Initial package
