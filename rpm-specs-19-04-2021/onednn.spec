%global _default_patch_fuzz 4

Name:           onednn
Version:        2.2
Release:        1%{?dist}
Summary:        Deep Neural Network Library

License:        ASL 2.0 and BSD and Boost and MIT
URL:            https://github.com/oneapi-src/oneDNN/
Source0:        %{url}/archive/v%{version}/onednn-%{version}.tar.gz
# Fuzz is need to apply upstream patch
Patch0:         0001-Add-thread-for-gcc-11.patch

# This package only work in few arches for now
ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

# Optionals not yet enabled
BuildRequires:  pkgconfig(OpenCL)
#BuildRequires:  pkgconfig(tbb)

# Virtual provides mkldnn
Provides: mkldnn = %{version}-%{release}
Provides: mkl-dnn = %{version}-%{release}
Obsoletes: mkl-dnn < 1.3
# Provides oneDNN
Provides: oneDNN = %{version}-%{release}


%description
one-API Deep Neural Network Library (oneDNN) is an open-source performance
library for deep learning applications. The library includes basic
building blocks for neural networks optimized for Intel Architecture
Processors and Intel Processor Graphics.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on Intel CPUs and
GPUs. Deep learning practitioners should use one of the applications
enabled with oneDNN:

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n oneDNN-%{version}


%build
%cmake \
  -DDNNL_ARCH_OPT_FLAGS="" \
  -DDNNL_GPU_RUNTIME=OCL

%cmake_build


%install
%cmake_install

# Remove docs
rm -rf %{buildroot}%{_docdir}/dnnl


%ldconfig_scriptlets


%files
%license LICENSE THIRD-PARTY-PROGRAMS
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%{_libdir}/libdnnl.so.2
%{_libdir}/libdnnl.so.2.*
%{_libdir}/libmkldnn.so.2
%{_libdir}/libmkldnn.so.2.*

%files devel
%dir %{_includedir}/oneapi
%{_includedir}/oneapi/dnnl
%{_includedir}/mkldnn*.h*
%{_includedir}/dnnl*.h*
%{_libdir}/libdnnl.so
%{_libdir}/libmkldnn.so
%dir %{_libdir}/cmake/dnnl
%{_libdir}/cmake/dnnl/*.cmake
%dir %{_libdir}/cmake/mkldnn
%{_libdir}/cmake/mkldnn/*.cmake


%changelog
* Sat Apr 03 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2-1
- Update to 2.2

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.1-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Feb 17 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.1-1
- Update to 2.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.6-1
- Update to 1.6

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.5-1
- Update to 1.5
- Enable aarch64

* Mon Apr 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4-1
- Update to 1.4

* Sat Apr 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.3-1
- Update to 1.3
- Switch to onednn

* Sat Apr  6 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.18.1-1
- Initial spec file.
