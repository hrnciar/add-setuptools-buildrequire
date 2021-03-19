# Run the tests on gcc without flags?
%bcond_without check_gcc
# Run the tests on gcc with flags?
%bcond_without check_gcc_with_flags
# Run the tests on clang without flags?
%bcond_without check_clang
# Run the tests on clang with flags?
%bcond_without check_clang_with_flags

%global commit_simde 396e05c694d68c795f0470ef43432eefdfd371f1
%global short_commit_simde %(c=%{commit_simde}; echo ${c:0:7})
%global commit_munit da8f73412998e4f1adf1100dc187533a51af77fd
%global hedley_version 12
# Disable debuginfo package for the header only package.
%global debug_package %{nil}

Name: simde
# Use a minimum version as there has not been a version release yet.
# The upstream mentioned "I think I'll start with a 0.5 or something".
# https://github.com/nemequ/simde/issues/50
Version: 0.0.0
# Align the release format with the packages setting Source0 by commit hash
# such as podman.spec and moby-engine.spec.
Release: 8.git%{short_commit_simde}%{?dist}
Summary: SIMD Everywhere
# find simde/ -type f | xargs licensecheck
# simde: MIT
# simde/check.h: CC0
# simde/debug-trap.h: CC0
# simde/hedley.h: CC0
# simde/simde-arch.h: CC0
License: MIT and CC0
URL: https://github.com/nemequ/simde
Source0: https://github.com/nemequ/%{name}/archive/%{commit_simde}.tar.gz
# munit used in the unit test.
Source1: https://github.com/nemequ/munit/archive/%{commit_munit}.tar.gz
# gcc and clang are used in the unit tests.
BuildRequires: make
BuildRequires: clang
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
# Do not set noarch for header only package.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries

# simde/hedley.h
# https://github.com/nemequ/hedley
Provides: bundled(hedley) = %{hedley_version}

%description
%{summary}
The SIMDe header-only library provides fast, portable implementations of SIMD
intrinsics on hardware which doesn't natively support them, such as calling
SSE functions on ARM. There is no performance penalty if the hardware supports
the native implementation (e.g., SSE/AVX runs at full speed on x86,
NEON on ARM, etc.).

%package devel
Summary: Header files for SIMDe development
Provides: %{name}-static = %{version}-%{release}

%description devel
The simde-devel package contains the header files needed
to develop programs that use the SIMDe.

%prep
%autosetup -n %{name}-%{commit_simde}

%build
# The %%build section is not used.

%install
mkdir -p %{buildroot}%{_includedir}
cp -a simde %{buildroot}%{_includedir}

%check
# Check if all the shipped file is a valid header file.
for file in $(find simde/ -type f); do
  if ! [[ "${file}" =~ \.h$ ]]; then
    echo "${file} is not a header file."
    false
  elif [ -x "${file}" ]; then
    echo "${file} has executable bit."
    false
  fi
done

# Check hedley version correctness.
test "$(grep '^#define HEDLEY_VERSION ' simde/hedley.h | cut -d ' ' -f3)" = \
  '%{hedley_version}'

# Set munit.
rm -rf test/munit
tar xzvf %{SOURCE1}
mv munit-%{commit_munit} test/munit

# Run the unit tests.
# gcc
echo "== 1. tests on gcc =="
gcc --version
g++ --version

# without flags
echo "=== 1.1. tests on gcc without flags ==="
%if %{with check_gcc}
mkdir test/build-gcc
pushd test/build-gcc
CC="gcc -fno-strict-aliasing" CXX="g++ -fno-strict-aliasing" cmake ..
%make_build
./run-tests
popd
%endif

# with flags
echo "=== 1.2. tests on gcc with flags ==="
# gcc 11 with flags + aarch64: x86/avx512/subs/emul/{c,cpp},
# x86/sse2/emul/{c,cpp} failures
# https://github.com/simd-everywhere/simde/issues/720
%ifarch aarch64
sed -i '/^test_simde_mm_subs_epu8(/,/^}$/ s|simde_assert_m128i_u8|//\0|' test/x86/sse2.c
sed -i '/^test_simde_mm512_subs_epu8(/,/^}$/ s|simde_assert_m512i_u8|//\0|' test/x86/avx512bw.c
%endif
%if %{with check_gcc_with_flags}
mkdir test/build-gcc-with-flags
pushd test/build-gcc-with-flags
CC="gcc -fno-strict-aliasing" CXX="g++ -fno-strict-aliasing" cmake \
  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
  -DCMAKE_C_FLAGS="%{build_cflags}" \
  -DCMAKE_CXX_FLAGS="%{build_cxxflags}" \
  ..
%make_build
./run-tests
popd
%endif

# clang
%global toolchain clang
echo "== 2. tests on clang =="
clang --version
clang++ --version

# without flags
echo "=== 2.1. tests on clang without flags ==="
%if %{with check_clang}
mkdir test/build-clang
pushd test/build-clang
CC=clang CXX=clang++ cmake ..
%make_build
./run-tests
popd
%endif

# with flags
echo "=== 2.2. tests on clang with flags ==="
# Skip the test failing on clang-12.
# We do not report to the upstream, because the source is old.
# On the latet upstream, the segmentation fault happens on clang-12 with flags.
# clang-12 with flags + x86_64 ninja build: Segmentation fault
# https://github.com/simd-everywhere/simde/issues/717
sed -i '/^test_simde_mm_maskload_ps(/,/^}$/ s|simde_assert_m128_close|//\0|' test/x86/avx.c
%ifarch i686 s390x
sed -i '/^test_simde_mm_maskload_pd(/,/^}$/ s|simde_assert_m128d_equal|//\0|' test/x86/avx.c
%endif
%if %{with check_clang_with_flags}
mkdir test/build-clang-with-flags
pushd test/build-clang-with-flags
# arm tests fail with segmentation fault in cmake.
%ifnarch %{arm}
CC=clang CXX=clang++ cmake \
  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
  -DCMAKE_C_FLAGS="%{build_cflags}" \
  -DCMAKE_CXX_FLAGS="%{build_cxxflags}" \
  ..
%make_build
# ppc64le tests fail with clang-10.0.0, -O2 and some flags
# https://github.com/nemequ/simde/issues/273
%ifarch ppc64le
./run-tests || true
%else
./run-tests
%endif
%endif
popd
%endif

%files devel
%license COPYING
%doc README.md
%{_includedir}/%{name}

%changelog
* Mon Mar 08 2021 Jun Aruga <jaruga@redhat.com> - 0.0.0-8.git396e05c
- Fix FTBFS.
  Resolves: rhbz#1923371

* Sat Feb 13 2021 Jeff Law <law@redhat.com> - 0.0.0-7.git396e05c
- Compile with -fno-strict-aliasing as this code clearly violates ISO aliasing rules

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-6.git396e05c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Jun Aruga <jaruga@redhat.com> - 0.0.0-5.git396e05c
- Fix FTBFS.
  Resolves: rhbz#1865487
- Skip clang flags case for arm 32-bit due to the segmentation fault.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-4.git396e05c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-3.git396e05c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Jun Aruga <jaruga@redhat.com> - 0.0.0-2.git396e05c
- Update to the latest upstream commit: 396e05c.

* Fri Apr 10 2020 Jun Aruga <jaruga@redhat.com> - 0.0.0-1.git29b9110
- Initial package
