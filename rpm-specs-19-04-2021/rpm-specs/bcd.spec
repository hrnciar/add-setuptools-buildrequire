%global commit0 d94c9fa77c11afe7d04670d92b3930c417e19f4b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20180610

Name:           bcd
Version:        1.1
Release:        4.%{?date0}git%{?shortcommit0}%{?dist}
Summary:        Bayesian Collaborative Denoiser for Monte-Carlo Rendering
# BSD: main program
# AGPLv3+: src/io/exr
License:        BSD and AGPLv3+
URL:            https://github.com/superboubek/bcd
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# Many patches are tight to upstream accepting building shared
# and removing bundled dependencies
# https://github.com/superboubek/bcd/issues/12
# don't use bundled deps
Patch0:         bcd-nodeps.patch
# Missing includes
# https://github.com/superboubek/bcd/pull/11
Patch1:         bcd-gcc.patch
# Use system eigen3
Patch2:         bcd-eigen3.patch
# Turn into a shared library forging SONAME (no ABI stability expected)
Patch3:         bcd-links.patch
# Remove cuda arch - not supported in current nvcc
Patch4:         bcd-cuda.patch
# Use system json
Patch5:         bcd-json.patch
# TODO
# BCD calls exit
#https://github.com/superboubek/bcd/issues/13

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  OpenEXR-devel
BuildRequires:  eigen3-devel
BuildRequires:  json-devel
BuildRequires:  zlib-devel


%description
BCD allows to denoise images rendered with Monte Carlo path tracing and
provided in the form of their samples statistics (average, distribution
and covariance of per-pixel color samples). BCD can run in CPU (e.g.,
renderfarm) or GPU (e.g., desktop) mode. It can be integrated as a library
to any Monte Carlo renderer, using the provided sample accumulator to
interface the Monte Carlo simulation with the BCD internals, and comes
with a graphics user interface for designing interactively the denoising
parameters, which can be saved in JSON format and later reused in batch.

BCD has been designed for easy integration and low invasiveness in the
host renderer, in a high spp context (production rendering). There are
at least three ways to integrate BCD in a rendering pipeline, by either:

* Dumping all samples in a raw file, using the raw2bcd tool to generate
the rendering statistics from this file and then running the BCD using
the CLI tool.

* Exporting the mandatory statistics from the rendering loop in EXR
format and running the BCD CLI tool to obtain a denoised image.

* Directly integrating the BCD library into the renderer, using the
sample accumulator to post samples to BCD during the path tracing and
denoising the accumulated values after rendering using the library.


%package        cli
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    cli
The %{name}-cli package contains libraries and header files for
developing applications that use %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
export CXXFLAGS="%{optflags} $(pkgconf --cflags eigen3 OpenEXR) -I%{_includedir}/nlohmann"
export LDFLAGS="%{build_ldflags} $(pkgconf --libs eigen3 OpenEXR)"
%cmake \
  -DBCD_BUILD_GUI=OFF \
  %{?_with_cuda: \
   -DCUDA_TOOLKIT_ROOT_DIR=%{_cuda_prefix} \
   -DCUDA_USE_STATIC_CUDA_RUNTIME=OFF \
  } \
  %{!?_with_cuda:-DBCD_USE_CUDA=OFF}

%cmake_build


%install
%cmake_install

%if "%{_lib}" == "lib64"
mv %{buildroot}%{_prefix}/lib \
  %{buildroot}%{_libdir}
%endif

mkdir -p %{buildroot}%{_includedir}
cp -pr include/* %{buildroot}%{_includedir}


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so.0*

%files cli
%{_bindir}/bcd-cli
%{_bindir}/bcd-raw-converter

%files devel
%{_includedir}/bcd
%{_libdir}/*.so


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4.20180610gitd94c9fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1-3.20180610gitd94c9fa
- rebuild against New OpenEXR

* Sat Nov 07 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.1-2.20180610gitd94c9fa
- Improve patch description
- Enforce soversion
- Mention AGPLv3+

* Wed Jul  1 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.1-1.20180610gitd94c9fa
- Initial spec file
