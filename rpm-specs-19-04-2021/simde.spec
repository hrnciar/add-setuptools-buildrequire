# Run the tests on gcc?
%bcond_without check_gcc
# Run the tests on clang?
%bcond_without check_clang

%global commit_simde 22609d4661340098a17bddb9b3a7b8b18680079a
%global short_commit_simde %(c=%{commit_simde}; echo ${c:0:7})
%global commit_munit da8f73412998e4f1adf1100dc187533a51af77fd
# Disable debuginfo package for the header only package.
%global debug_package %{nil}

Name: simde
Version: 0.7.2
# Align the release format with the packages setting Source0 by commit hash
# such as podman.spec and moby-engine.spec.
Release: 1.git%{short_commit_simde}%{?dist}
Summary: SIMD Everywhere
# find simde/ -type f | xargs licensecheck
#   simde: MIT
#   simde/check.h: CC0
#   simde/debug-trap.h: CC0
#   simde/simde-arch.h: CC0
# removed in %%prep (unbundled):
#   simde/hedley.h: CC0
License: MIT and CC0
URL: https://github.com/simd-everywhere/simde
Source0: https://github.com/simd-everywhere/%{name}/archive/%{commit_simde}.tar.gz
# munit used in the unit test.
Source1: https://github.com/nemequ/munit/archive/%{commit_munit}.tar.gz
# gcc and clang are used in the unit tests.
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
# Header-only library dependency
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires: hedley-devel
BuildRequires: hedley-static
BuildRequires: %{_bindir}/time
# Do not set noarch for header only package.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries

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
# The API includes the hedley header-only library.
Requires: hedley-devel%{?_isa}
Requires: hedley-static

%description devel
The simde-devel package contains the header files needed
to develop programs that use the SIMDe.

%prep
%autosetup -n %{name}-%{commit_simde}
ln -svf %{_includedir}/hedley.h %{name}/

%build
# The %%build section is not used.

%install
mkdir -p %{buildroot}%{_includedir}
cp -a simde %{buildroot}%{_includedir}
ln -svf ../hedley.h %{buildroot}%{_includedir}/%{name}/

%check
# Check if all the shipped file is a valid header file.
# Suppress the command logging during the check by running on bash.
bash - <<\EOF
for file in $(find simde/ -type f); do
  if ! [[ "${file}" =~ \.h$ ]]; then
    echo "${file} is not a header file."
    false
  elif [ -x "${file}" ]; then
    echo "${file} has executable bit."
    false
  fi
done
EOF

# Set munit.
rm -rf test/munit
tar xzvf %{SOURCE1}
mv munit-%{commit_munit} test/munit

# Define functions.
JOB_NUM="$(nproc)"

function _time {
  %{_bindir}/time -f '=> [%E]' ${@}
}

function _setup {
  meson setup "${BUILD_DIR}" || (
    cat "${BUILD_DIR}/meson-logs/meson-log.txt"
    false
  )
}

function _build {
  rm -f build.log
  _time ninja -C "${BUILD_DIR}" -v -j "${JOB_NUM}" >& build.log || (
    cat build.log
    false
  )
  head -4 build.log
  tail -3 build.log
}

function _test {
  _time meson test -C "${BUILD_DIR}" -q --no-rebuild --print-errorlogs
}

# Run the unit tests.
# gcc
%if %{with check_gcc}
bash - <<\EOF
echo "== 1. tests on gcc =="
EOF
gcc --version
g++ --version

bash - <<\EOF
echo "=== 1.1. tests on gcc without flags ==="
EOF
BUILD_DIR="build/gcc"
CC="gcc -fno-strict-aliasing" CXX="g++ -fno-strict-aliasing" \
  _setup
_build
_test

bash - <<\EOF
echo "=== 1.2. tests on gcc with O2 flag ==="
EOF
BUILD_DIR="build/gcc-O2"
CC="gcc -fno-strict-aliasing" CXX="g++ -fno-strict-aliasing" \
CFLAGS="-O2" CXXFLAGS="-O2" \
  _setup
_build
_test

bash - <<\EOF
echo "=== 1.3. tests on gcc with flags macro ==="
EOF
BUILD_DIR="build/gcc-flags-macro"
CC="gcc -fno-strict-aliasing" CXX="g++ -fno-strict-aliasing" \
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" \
  _setup
_build
# gcc 11 with flags + i686 sse/{emul,native}/{c,cpp} sse2/native/{c,cpp} failures
# https://github.com/simd-everywhere/simde/issues/719
%ifnarch i686
_test
%endif

# with check_gcc
%endif

# clang
%if %{with check_clang}
%global toolchain clang
bash - <<\EOF
echo "== 2. tests on clang =="
EOF
clang --version
clang++ --version

bash - <<\EOF
echo "=== 2.1. tests on clang without flags ==="
EOF
BUILD_DIR="build/clang"
CC=clang CXX=clang++ \
  _setup
_build
# clang 12 + i686 {x86/sse,x86/sse2,arm/neon} failures
# https://github.com/simd-everywhere/simde/issues/721
%ifnarch i686
_test
%endif

bash - <<\EOF
echo "=== 2.2. tests on clang with O2 flag ==="
EOF
BUILD_DIR="build/clang-O2"
CC="clang" CXX="clang++" \
CFLAGS="-O2" CXXFLAGS="-O2" \
  _setup
_build
# clang 12 with -O2 + i686 x86/sse2/native/{c,cpp} failures
# https://github.com/simd-everywhere/simde/issues/740
%ifnarch i686
_test
%endif

bash - <<\EOF
echo "=== 2.3. tests on clang with flags macro ==="
EOF
BUILD_DIR="build/clang-flags-macro"
# clang-12 with flags + armv7hl: meson setup: Segmentation fault
# https://github.com/simd-everywhere/simde/issues/737
%ifnarch %{arm}
CC="clang" CXX="clang++" \
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" \
  _setup
_build
# clang 12 with flags + ppc64le TAP parsing error: Too few tests run
# https://github.com/simd-everywhere/simde/issues/745
  %ifnarch i686 ppc64le
_test
  %endif
%endif

# with check_clang
%endif

%files devel
%license COPYING
%doc README.md
%{_includedir}/%{name}

%changelog
* Sun Apr 04 2021 Jun Aruga <jaruga@redhat.com> - 0.7.2-1.git22609d4
- Upgrade to SIMDe 0.7.2.
  Resolves: rhbz#1940179

* Wed Mar 24 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.0-10.git396e05c
- Fix incorrectly-arched dependency on hedley-static

* Tue Mar 23 2021 Jun Aruga <jaruga@redhat.com> - 0.0.0-9.git396e05c
- Fix a warning by the rpmlint.

* Mon Mar 22 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.0-9.git396e05c
- Unbundle hedley dependency

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
