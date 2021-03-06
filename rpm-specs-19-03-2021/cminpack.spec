%undefine __cmake_in_source_build
%global soversion 1

Name:           cminpack
Version:        1.3.6
Release:        2%{?dist}
Summary:        Solver for nonlinear equations and nonlinear least squares problems

License:        BSD
URL:            http://devernay.free.fr/hacks/cminpack/cminpack.html
Source0:        http://devernay.free.fr/hacks/cminpack/%{name}-%{version}.tar.gz
# Install CMinpackConfig.cmake to libdir instead of datadir.
Patch0:         %{name}-1.3.6-fedora.patch
# Update path to cblas.h for flexiblas
Patch1:         %{name}-1.3.6-blas.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gcc-gfortran
BuildRequires:  flexiblas-devel

%description
cminpack is an ISO C99 implementation of the FORTRAN Minpack solver package.
It is fully re-entrant and thread-safe.

%package devel
Summary: Header files and libraries for cminpack
Requires: %{name} = %{version}-%{release}

%description devel
Contains the development headers and libraries needed to build a program with
cminpack.

%prep
%setup -q
%patch0 -p0 -b .fedora
%patch1 -p0 -b .blas

%build
%cmake \
  -DUSE_FPIC=ON \
  -DSHARED_LIBS=ON \
  -DBUILD_EXAMPLES=ON \
  -DBUILD_EXAMPLES_FORTRAN=ON \
  -DCMINPACK_LIB_INSTALL_DIR=%{_lib} \
  -DUSE_BLAS=ON \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%license CopyrightMINPACK.txt
%doc README.md
%{_libdir}/libcminpack.so.%{version}
%{_libdir}/libcminpack.so.%{soversion}

%files devel
%doc doc/*.html doc/*.txt
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/CMinpack
%{_libdir}/libcminpack.so
%{_includedir}/cminpack-1


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Rich Mattes <richmattes@gmail.com> - 1.3.6-1
- Update to 1.3.6
- Fix CMake macro FTBFS (rhbz#1863343)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Rich Mattes <richmattes@gmail.com> - 1.3.4-1
- Update to release 1.3.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 19 2013 Rich Mattes <richmattes@gmail.com> - 1.3.1-1
- Update to release 1.3.1 to remove non-free nvidia headers from srpm (rhbz#1019037) 

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Rich Mattes <richmattes@gmail.com> - 1.3.0-2
- Bump to maintain upgradepath

* Sat Oct 27 2012 Rich Mattes <richmattes@gmail.com> - 1.3.0-1
- Update to release 1.3.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Dan Hor??k <dan[at]danny.cz> - 1.2.2-2
- fix build on 64-bit secondary arches

* Fri May 25 2012 Rich Mattes <richmattes@gmail.com> - 1.2.2-1
- Upgrade to version 1.2.2

* Sat Feb 18 2012 Rich Mattes <richmattes@gmail.com> - 1.1.4-1
- Upgrade to version 1.1.4

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Dan Hor??k <dan[at]danny.cz> - 1.1.3-2
- fix build on non-x86 64-bit arches

* Wed Mar 23 2011 - Rich Mattes <richmattes@gmail.com> - 1.1.3-1
- Upgrade to vesion 1.1.3

* Sun Dec 05 2010 - Rich Mattes <richmattes@gmail.com> - 1.1.2-1
- Initial build
