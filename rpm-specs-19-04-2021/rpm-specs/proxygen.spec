# fizz has link issues on some platforms:
# https://bugzilla.redhat.com/show_bug.cgi?id=1893332
%ifarch i686 x86_64
%bcond_without static
%else
%bcond_with static
%endif

# tests do not build properly at the moment
%bcond_with tests

# https://bugzilla.redhat.com/show_bug.cgi?id=1927961
%bcond_with docs

%global _static_builddir static_build

Name:           proxygen
Version:        2021.04.12.00
Release:        1%{?dist}
Summary:        A collection of C++ HTTP libraries including an easy to use HTTP server.

License:        BSD
URL:            https://github.com/facebook/proxygen
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.gz

# Folly is known not to work on big-endian CPUs
# https://bugzilla.redhat.com/show_bug.cgi?id=1892152
ExcludeArch:    s390x

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  folly-devel
BuildRequires:  fizz-devel
BuildRequires:  wangle-devel
BuildRequires:  gperf
BuildRequires:  perl
BuildRequires:  libzstd-devel
%if %{with docs}
BuildRequires:  doxygen
%endif
%if %{with static}
BuildRequires:  folly-static
BuildRequires:  fizz-static
BuildRequires:  wangle-static
BuildRequires:  libzstd-static
%endif

%description
Proxygen comprises the core C++ HTTP abstractions used at Facebook.
Internally, it is used as the basis for building many HTTP servers, proxies,
and clients. This release focuses on the common HTTP abstractions and our
simple HTTPServer framework. Future releases will provide simple client APIs
as well. The framework supports HTTP/1.1, SPDY/3, SPDY/3.1, HTTP/2, and
HTTP/3. The goal is to provide a simple, performant, and modern C++ HTTP
library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    docs
The %{name}-docs package contains additional documentation for proxygen.
%endif

%package        libs
Summary:        Shared libraries for %{name}
%description    libs
The %{name}-libs package contains shared libraries provided by proxygen.

%if %{with static}
%package        static
Summary:        Static development libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains static libraries for
developing applications that use %{name}.
%endif

%prep
%autosetup -c -p1

%build
%if %{with static}
mkdir %{_static_builddir}
pushd %{_static_builddir}
%cmake .. \
  -DBUILD_TESTS=OFF \
  -DBUILD_SHARED_LIBS=OFF \
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name}-static \
  -DPACKAGE_VERSION=%{version} \
%cmake_build
popd
%endif

%cmake \
%if %{with tests}
  -DBUILD_TESTS=ON \
%else
  -DBUILD_TESTS=OFF \
%endif
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DPACKAGE_VERSION=%{version}
%cmake_build

%if %{with docs}
doxygen
%endif

%install
%if %{with static}
# static build
pushd %{_static_builddir}
%cmake_install
popd
%endif

# shared build
%cmake_install

%if %{with tests}
%check
%ctest
%endif

%files
%license LICENSE
%{_bindir}/*

%files libs
%{_libdir}/*.so.*

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md CoreProxygenArchitecture.png
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}

%if %{with docs}
%files docs
%doc html
%endif

%if %{with static}
%files static
%{_libdir}/*.a
%{_libdir}/cmake/%{name}-static
%endif

%changelog
* Fri Apr 16 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2021.04.12.00-1
- Update to 2021.04.12.00

* Mon Mar 29 2021 Michel Alexandre Salim <michel@michel-slm.name> - 2021.03.29.00-1
- Update to 2021.03.29.00

* Wed Mar 24 2021 Michel Alexandre Salim <michel@michel-slm.name> - 2021.03.22.00-1
- Update to 2021.03.22.00

* Sun Mar 21 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2021.03.15.00-1
- Update to 2021.03.15.00

* Thu Feb 11 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2021.02.01.00-4
- Disable docs build by default for now

* Fri Feb  5 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2021.02.01.00-3
- Make proxygen-docs noarch
- Fix cmake install dir for static build

* Thu Feb  4 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2021.02.01.00-2
- Backport upstream fix to install the proxygencurl library

* Tue Feb  2 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2021.02.01.00-1
- Initial package
