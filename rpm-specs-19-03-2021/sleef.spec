# We do not ship the DFT library since it has undiagnosed test failures on
# Fedora at -O2, and is not well-supported upstream. Additionally, it uses
# illegal instructions on ARM and s390x, at least on the Fedora build machines.
# See https://github.com/shibatch/sleef/issues/214.
%bcond_with dft
# We would like to ship the quad-precision library, but since it is still
# considered experimental, it may have breaking ABI or API changes without an
# soversion bump, which is a no-no in Fedora. Rather than contorting ourselves
# to accommodate this, we disable it until it stabilizes or some dependent
# package appears.
%bcond_with quad
# Similarly, Fedora packages should not ship static libraries unless absolutely
# required. Some software, like pytorch, really does rely on the inline headers
# and accompanying static support library for exceptional performance
# requirements, but no such software exists in Fedora at the moment. We will
# leave this feature disabled until someone asks for it.
%bcond_with static

Name:           sleef
Version:        3.5.1
Release:        3%{?dist}
Summary:        Vectorized math library

License:        Boost
URL:            https://sleef.org
Source0:        https://github.com/shibatch/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.4.3
BuildRequires:  gcc
BuildRequires:  ninja-build
# For tests only:
BuildRequires:  mpfr-devel
BuildRequires:  openssl-devel
%if %{with dft}
BuildRequires:  fftw-devel
%endif

%global so_version %(echo %{version} | cut -d . -f 1)
# Only out-of-source builds are supported. This is the default for F33 and
# later, but we must be explicit on older releases, including EPEL8.
%undefine __cmake_in_source_build
# See https://sleef.org/additional.xhtml#gnuabi. The gnuabi version of the
# library only applies to these architectures.
%global gnuabi_arches %{ix86} x86_64 aarch64
# See https://github.com/shibatch/sleef/pull/283.
%ifnarch %{arm32}
%if %{with static}
%global inline_enabled 1
%endif
%endif

%description
SLEEF stands for SIMD Library for Evaluating Elementary Functions. It
implements vectorized versions of all C99 real floating point math functions.
It can utilize SIMD instructions that are available on modern processors. SLEEF
is designed to efficiently perform computation with SIMD instructions by
reducing the use of conditional branches and scatter/gather memory access.

The library contains implementations of all C99 real FP math functions in
double precision and single precision. Different accuracy of the results can be
chosen for a subset of the elementary functions; for this subset there are
versions with up to 1 ULP error (which is the maximum error, not the average)
and even faster versions with a few ULPs of error. For non-finite inputs and
outputs, the functions return correct results as specified in the C99 standard.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if 0%{?inline_enabled}
%package static
Summary:        Inline headers and static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains libraries and header files for
developing applications that use %{name}.
%endif


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains detailed API documentation for developing
applications that use %{name}.


%ifarch %{gnuabi_arches}
%package gnuabi
Summary:        GNUABI version of %{name}

%global gnuabi_enabled 1

%description gnuabi
The GNUABI version of the library (libsleefgnuabi.so) is built for x86 and
aarch64 architectures. This library provides an API compatible with libmvec in
glibc, and the API conforms to the x86 vector ABI, AArch64 vector ABI and Power
Vector ABI.


%package gnuabi-devel
Summary:        Development files for GNUABI version of %{name}
Requires:       %{name}-gnuabi%{?_isa} = %{version}-%{release}

%description gnuabi-devel
The %{name}-gnuabi-devel package contains libraries for developing applications
that use the GNUABI version of %{name}. Note that this package does not contain
any header files.
%endif


%if %{with dft}
%package dft
Summary:        Discrete Fourier Transform (DFT) library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description dft
SLEEF includes subroutines for discrete Fourier transform(DFT). These
subroutines are fully vectorized, heavily unrolled, and parallelized in such a
way that modern SIMD instructions and multiple cores can be utilized for
efficient computation. It has an API similar to that of FFTW for easy
migration. The subroutines can utilize long vectors up to 2048 bits.


%package dft-devel
Summary:        Development files for %{name}-dft
Requires:       %{name}-dft%{?_isa} = %{version}-%{release}

%description dft-devel
The %{name}-dft-devel package contains libraries and header files for
developing applications that use %{name}-dft.
%endif


%if %{with quad}
%package quad
Summary:        Vectorized quad-precision math library

%description quad
An experimental quad-precision library


%package quad-devel
Summary:        Development files for %{name}-quad
Requires:       %{name}-quad%{?_isa} = %{version}-%{release}

%description quad-devel
The %{name}-quad-devel package contains libraries and header files for
developing applications that use %{name}-quad.
%endif


%prep
%autosetup


%build
# -GNinja: Upstream prominently states that parallel build is only supported
# with the Ninja generator for cmake, not with the make one. See
# https://sleef.org/compile.xhtml.
#
# -DENFORCE_TESTER3: The build should fail if we cannot build all tests.
#
# -DBUILD_INLINE_HEADERS: Do not build the “inline” headers. This would provide
#   an arch-specific collection of sleefinline_*.h headers in _includedir, as
#   well as a static support library, libsleefinline.a, in _libdir. Both the
#   static library and the headers (which are basically a header-only library,
#   and would thus also be treated as a static library in the Fedora
#   guidelines) should be omitted unless something in Fedora absolutely
#   requires them.
%cmake \
    -GNinja \
    -DENFORCE_TESTER3:BOOL=TRUE \
    -DBUILD_INLINE_HEADERS:BOOL=%{?inline_enabled:TRUE}%{?!inline_enabled:FALSE} \
    -DBUILD_GNUABI_LIBS:BOOL=%{?gnuabi_enabled:TRUE}%{?!gnuabi_enabled:FALSE} \
    -DBUILD_DFT:BOOL=%{?with_dft:TRUE}%{?!with_dft:FALSE} \
    -DBUILD_QUAD:BOOL=%{?with_quad:TRUE}%{?!with_quad:FALSE}
%cmake_build


%install
%cmake_install


%check
# Note that test coverage of SIMD extensions will be limited to those available
# on the build host; there is no way around this. We attempt to record the CPU
# features in the build log:
grep -m 1 -E '^f(lags|eatures)\b' /proc/cpuinfo || :

skips='^($.'
%ifarch s390x
# Two tests fail on s390x only, at least for the z13 (features: vx in
# /proc/cpuinfo) CPUs currently used in the Fedora s390x infrastructure. See
# https://github.com/shibatch/sleef/issues/317#issuecomment-724625861, which
# indicates this is known upstream.
skips="${skips}|iut[yi]?purecfma_scalar"
%endif
%if %{with dft}
# The DFT library has known test failures
# (https://github.com/shibatch/sleef/issues/214).
skips="${skips}|fftwtest2d[ds]p_(4_4|8_8|10_10|5_15)"
%ifarch %{arm32} aarch64 s390x
# Plus, it uses illegal instructions:
skips="${skips}|naivetest[ds]p_([2345]|10)"
skips="${skips}|fftwtest(1d[ds]p_1[26]|2d[ds]p_2_2)"
%endif
%endif
skips="${skips})$"

%ctest --exclude-regex "${skips}" --extra-verbose


%files
%license LICENSE.txt
%{_libdir}/lib%{name}.so.%{so_version}
%{_libdir}/lib%{name}.so.%{so_version}.*


%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc


%if 0%{?inline_enabled}
%files static
%{_includedir}/%{name}inline_*.h
%{_libdir}/lib%{name}inline.a
%endif


%files doc
%license LICENSE.txt
%doc CHANGELOG.md
%doc CONTRIBUTORS.md
%doc README.md
%doc doc/html


%ifarch %{gnuabi_arches}
%files gnuabi
%license LICENSE.txt
%{_libdir}/lib%{name}gnuabi.so.%{so_version}
%{_libdir}/lib%{name}gnuabi.so.%{so_version}.*


%files gnuabi-devel
%{_libdir}/lib%{name}gnuabi.so
%endif


%if %{with dft}
%files dft
%{_libdir}/lib%{name}dft.so.%{so_version}
%{_libdir}/lib%{name}dft.so.%{so_version}.*


%files dft-devel
%{_includedir}/%{name}dft.h
%{_libdir}/lib%{name}dft.so
%endif


%if %{with quad}
%files quad
%license LICENSE.txt
%{_libdir}/lib%{name}quad.so.%{so_version}
%{_libdir}/lib%{name}quad.so.%{so_version}.*


%files quad-devel
%{_includedir}/%{name}quad.h
%{_libdir}/lib%{name}quad.so
%endif


%changelog
* Wed Mar 17 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.1-3
- Improve source URL

* Thu Dec 24 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.1-2
- Drop explicit pkgconfig dependency; providing a .pc file implies it

* Fri Dec 18 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.1-1
- Initial spec file
