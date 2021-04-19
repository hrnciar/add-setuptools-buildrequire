# Smoldyn provides the SFMT-1.3.3 (SIMD-oriented Fast Mersenne Twister) source code;
# currently unavailable on Fedora.
# http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/SFMT/index.html

# VTK support?
# See https://github.com/ssandrews/Smoldyn-official/issues/3
%global with_vtk 0

Name:  smoldyn
Summary: A particle-based spatial stochastic simulator
Version: 2.63
Release: 2%{?dist}

# The rxnparam.c and SurfaceParam.c source code files are in the public domain.
#
# The Next Subvolume module is Copyright 2012 by Martin Robinson and is distributed
# under the Gnu LGPL license.
#
# The rest of the code is Copyright 2003-2018 by Steven Andrews and also
# distributed under the Gnu LGPL.
#
# source/libSteve/SFMT is licensed under the 'BSD 3-clause "New" or "Revised" License'
License: LGPLv3+ and Public Domain and BSD
URL:   http://www.smoldyn.org
Source0: %{url}/%{name}-%{version}.zip

# Fix library paths according to the Fedora Project guidelines
Patch0: %{name}-fix_libpaths.patch
Patch1: %{name}-freeglut.patch

BuildRequires: make
BuildRequires: cmake3
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: freeglut-devel
BuildRequires: libXmu-devel
BuildRequires: libXi-devel
BuildRequires: libtiff-devel
BuildRequires: libglvnd-devel
BuildRequires: perl-macros
BuildRequires: python3-devel
%if %{?with_vtk}
BuildRequires: vtk-devel
%endif
BuildRequires: zlib-devel

Requires: bionetgen-perl
Provides: bundled(SFMT) = 1.3.3 

%description
Smoldyn is a computer program for cell-scale biochemical simulations.
It simulates each molecule of interest individually to capture natural
stochasticity and to yield nanometer-scale spatial resolution.
It treats other molecules implicitly, enabling it to simulate hundreds
of thousands of molecules over several minutes of real time.

Simulated molecules diffuse, react, are confined by surfaces,
and bind to membranes much as they would in a real biological system.

It is more accurate and faster than other particle-based simulators.
Smoldyn unique features include: a "virtual experimenter" who can
manipulate or measure the simulated system, support for spatial compartments,
molecules with excluded volume, and simulations in 1, 2, or 3 dimensions. 

%package doc
Summary: %{name} PDF documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{name} PDF documentation.

%prep
%autosetup -n %{name}-%{version} -N
%patch0 -p0 -b .fix_libpaths
%patch1 -p0 -b .freeglut

# Remove bundled archives
rm -rf source/MSVClibs source/pybind11

# Remove bundled libraries
rm -rf source/BioNetGen source/MinGWlibs Toolchain-mingw32.cmake
rm -rf source/vcell/* source/NextSubVolume/Eigen
rm -rf source/NextSubVolume/boost_include
%if !%{?with_vtk}
rm -f source/vtk/*
%endif

#Fix permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.c" -exec chmod 0644 '{}' \;
find . -type f -name "*.pdf" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec sed -i 's/\r$//' '{}' \;

# Set system path to BNG2.pl
sed -e 's|../../../source/BioNetGen/BNG2.pl|%{perl_vendorlib}/BioNetGen/BNG2.pl|g' -i examples/S95_regression/lrmsim.txt \
 examples/S12_bionetgen/lrm/lrmsim.txt \
 examples/S12_bionetgen/abba/abbasim.txt \
 examples/S94_archive/Andrews_2016/BioNetGen/lrm/lrmsim.txt \
 examples/S94_archive/Andrews_2016/BioNetGen/abba/abbasim.txt
 
# Copy license file
cp -p source/libSteve/SFMT/LICENSE.txt source/libSteve/SFMT/SFMT-LICENSE.txt
cp -p source/libSteve/SFMT/README.txt source/libSteve/SFMT/SFMT-README.txt

%build
# Python binding needs shared libraries
%cmake3 -Wno-dev -B . -S . \
 -DCPACK_BINARY_STGZ:BOOL=OFF \
 -DCPACK_BINARY_TGZ:BOOL=OFF \
 -DCPACK_BINARY_TZ:BOOL=OFF \
 -DCPACK_SOURCE_TBZ2:BOOL=OFF \
 -DCPACK_SOURCE_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TXZ:BOOL=OFF \
 -DCPACK_SOURCE_TZ:BOOL=OFF \
 -DOPTION_VCELL:BOOL=OFF \
%if %{?with_vtk}
 -DOPTION_VTK:BOOL=ON \
%else
 -DOPTION_VTK:BOOL=OFF \
%endif
 -DBUILD_SHARED_LIBS:BOOL=OFF \
 -DSMOLDYN_VERSION:STRING=%{version} \
 -DOPTION_TARGET_LIBSMOLDYN:BOOL=OFF \
 -DOPTION_STATIC:BOOL=OFF \
 -DOPTION_PYTHON:BOOL=OFF -DPYBIND11_FINDPYTHON:BOOL=OFF \
 -DOPTION_USE_ZLIB:BOOL=ON \
 -DOPTION_PDE:BOOL=ON \
 -DPERL_VENDORLIB:PATH=%{perl_vendorlib} \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DHAVE_GL_FREEGLUT_H=TRUE
%make_build

%install
%make_install

%files
%license License.txt source/libSteve/SFMT/SFMT-LICENSE.txt
%{_bindir}/%{name}

%files doc
%doc documentation/*

%changelog
* Sat Jan 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.63-2
- Exclude example files (strange permissions)

* Fri Jan 29 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.63-1
- Release 2.63

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.61-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.61-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 2.61-4
- Use  __cmake_in_source_build

* Mon May 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.61-3
- Fix patch for EPEL7

* Mon May 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.61-2
- Patched for using Boost169 on EPEL7

* Sun May 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.61-1
- Release 2.61

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.58-3
- Rebuilt for new freeglut

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.58-1
- Release 2.58

* Sun Feb 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.56-1
- First package
- Unbundle zlib, boost and BioNetGen
- Remove unused header files
- Fix file permissions
- Add License file provided by upstream
