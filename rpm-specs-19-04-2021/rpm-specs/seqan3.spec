%global debug_package %{nil}
%global middle_release 0

# Redefine vpath builddir
# Default in Fedora 33+ is %%{_target_platform}
%global _vpath_builddir .

# test/unit/alignment/matrix/detail/two_dimensional_matrix_test.cpp:420:1:
# internal compiler error: tree code 'typename_type' is not supported in LTO streams
# https://github.com/seqan/seqan3/issues/2013
%define _lto_cflags %{nil}

%bcond_with check
%bcond_with test_api
%bcond_with test_header
%bcond_with benchmark
%bcond_without doc

# SeqAn3 aims to support any 64-bit architecture running Linux/POSIX;
# currently big-endian CPU architectures like s390x are less supported.
ExclusiveArch: %{power64} x86_64 aarch64

%if 0%{?middle_release}
%global  commit      bf04354bab903dc7f8c12f3bb478c02cd5f2c553
%global  date        20200806git
%global  shortcommit %(c=%{commit}; echo ${c:0:7})
%else
%global  commit      %{nil}
%global  date        %{nil}
%global  shortcommit %{nil}
%endif

Name:      seqan3
Summary:   The modern C++ library for sequence analysis
Version:   3.0.2
Release:   7%{date}%{shortcommit}%{?dist}
License:   BSD
URL:       http://www.seqan.de/
Source0:   https://github.com/seqan/seqan3/releases/download/%{version}/seqan3-%{version}-Source.tar.xz

BuildRequires: make
BuildRequires: gcc, gcc-c++
BuildRequires: cmake >= 3.4
BuildRequires: cereal-devel >= 1.2.3
BuildRequires: zlib-devel >= 1.2
BuildRequires: bzip2-devel >= 1.0
BuildRequires: range-v3-devel >= 0.11.0
BuildRequires: coin-or-lemon-devel
%if %{with check}
BuildRequires: google-benchmark-devel
BuildRequires: gtest-devel >= 1.10.0
%endif
%if %{with doc}
BuildRequires: texlive-newunicodechar
BuildRequires: doxygen
%endif

# Patches for unbundling libraries and fix some errors
Patch0: %{name}-unbundle_benchmark.patch
Patch1: %{name}-cppreference.patch
Patch2: %{name}-unbundle_gtest.patch

# Upstream patches

# https://github.com/seqan/seqan3/issues/2209
Patch3: %{name}-bug2209.patch

# https://github.com/seqan/seqan3/issues/2210
Patch4: %{name}-bug2210.patch

%description
SeqAn3 is the new version of the popular SeqAn template
library for the analysis of biological sequences.
It enables the rapid development of high-performance
solutions by providing generic algorithms and
data structures for:

 - sequence representation and transformation
 - full-text indexing and efficient search
 - sequence alignment
 - input/output of common file formats

%package devel
Summary: SeqAn3 header only files
Requires: cmake%{?_isa} >= 3.4
Requires: cereal-devel%{?_isa} >= 1.2.3
Requires: zlib-devel%{?_isa} >= 1.2
Requires: bzip2-devel%{?_isa} >= 1.0
Requires: range-v3-devel%{?_isa} >= 0.11.0
Provides: bundled(sdsl-lite-devel) = 3.0.0
Provides: bundled(sdsl-devel) = 3.0.0
Provides: bundled(SDSL-devel) = 3.0.0

%description devel
C++ headers files of SeqAn3, including CMake configuration files.

%package doc
Summary: SeqAn3 documentation
BuildArch: noarch
%description doc
SeqAn3 documentation.

%prep
%autosetup -n seqan3-%{version}-Source -p1

# Unbundle libraries already on Fedora
rm -rf submodules/cereal
rm -rf submodules/range-v3

# SDSL 3.0 is a new SDSL pre-release, under development.
# See https://github.com/xxsds/sdsl-lite
cp -p submodules/sdsl-lite/LICENSE submodules/sdsl-lite/sdsl-LICENSE

# Fix file permissions
find . -type f -name "*.hpp" -exec chmod 0644 '{}' \;

%build
%if %{with check}
%if %{with test_api}
mkdir -p build
# Workaround for upstream bug#1993
export CXXFLAGS="%{build_cxxflags} -std=c++2a -fconcepts -lstdc++fs"
%cmake -S test/unit -B build -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DSEQAN3_CEREAL:BOOL=ON \
 -DSEQAN3_LEMON:BOOL=ON \
 -DSEQAN3_TEST_BUILD_OFFLINE:BOOL=ON
%make_build -C build
%endif
%if %{with test_header}
mkdir -p build-header
export CXXFLAGS="%{build_cxxflags} -std=c++2a -fconcepts -lstdc++fs"
%cmake -S test/header -B build-header -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DSEQAN3_CEREAL:BOOL=ON \
 -DSEQAN3_LEMON:BOOL=ON \
 -DSEQAN3_TEST_BUILD_OFFLINE:BOOL=ON
%make_build -C build-header
%endif
%if %{with benchmark}
mkdir -p build-performance
export CXXFLAGS="%{build_cxxflags} -std=c++2a -fconcepts -lstdc++fs"
%cmake -S test/performance -B build-performance -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DSEQAN3_CEREAL:BOOL=ON \
 -DSEQAN3_LEMON:BOOL=ON \
 -DSEQAN3_TEST_BUILD_OFFLINE:BOOL=ON
%make_build -C build-performance
%endif
%endif
%if %{with doc}
mkdir -p build-doc
export CXXFLAGS="%{build_cxxflags} -std=c++2a -fconcepts -lstdc++fs"
%cmake -S test/documentation -B build-doc -DCMAKE_BUILD_TYPE=Release 
make -j1 -C build-doc
%endif

%install
mkdir -p %{buildroot}%{_libdir}/cmake/%{name}
cp -a include %{buildroot}%{_prefix}/

rm -f submodules/sdsl-lite/include/sdsl/.gitignore
cp -a submodules/sdsl-lite/include %{buildroot}%{_prefix}/

install -pm 644 build_system/*.cmake %{buildroot}%{_libdir}/cmake/%{name}/

%if %{with check}
%check
%if %{with test_api}
# Tests the API of the library
pushd build
%ctest
popd
%endif
%if %{with test_header}
# Tests that every header includes all required headers and detects linkage issues
pushd build-header
%ctest
popd
%endif
%if %{with benchmark}
# Microbenchmarks
pushd build-performance
%ctest
popd
%endif
%endif

%files devel
%license LICENSE.md submodules/sdsl-lite/sdsl-LICENSE
%doc README.md
%{_includedir}/%{name}/
%{_includedir}/sdsl/
%{_libdir}/cmake/%{name}/

%if %{with doc}
%files doc
%doc build-doc/doc_usr/html
%license LICENSE.md
%doc README.md
%endif

%changelog
* Sun Feb 14 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-7
- Disable tests with GCC-11 (rhbz#1923593)
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-6
- Rebuild for GCC-11

* Tue Nov 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-5
- Bundle sdsl header files

* Sat Oct 17 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-4
- Remove old License file from bundled libraries
- Redefine vpath builddir

* Fri Oct 16 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-3
- Fix Requires packages

* Wed Oct 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-2
- Use -std=c++2a flag
- Patched for upstream bugs #2209 #2210

* Tue Oct 13 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-1
- Release 3.0.2

* Fri Aug 07 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-0.2.20200806gitbf04354
- Pre-release 3.0.2 with bundled range-v3

* Thu Aug 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-0.1.20200806gitbf04354
- Pre-release 3.0.2

* Thu Mar 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-1
- Execute header/performance tests
- Build docs
- First package
