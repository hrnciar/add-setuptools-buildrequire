Name:           libecpint
Version:        1.0.5
Release:        1%{?dist}
Summary:        Efficient evaluation of integrals over ab initio effective core potentials
License:        MIT
Url:            https://github.com/robashaw/libecpint
Source0:        https://github.com/robashaw/libecpint/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.12
BuildRequires:  pugixml-devel
BuildRequires:  gtest-devel
BuildRequires:  python3
BuildRequires:  doxygen
BuildRequires:  sphinx
Requires:       %{name}-common = %{version}-%{release}

%description
Libecpint is a C++ library for the efficient evaluation of integrals over ab
initio effective core potentials, using a mixture of generated, recursive
code and Gauss-Chebyshev quadrature. It is designed to be standalone and
generic.

%package common
Summary:        Architecture independent data files for libecpint
BuildArch:      noarch

%description common
This package contains architecture independent data files for libecpint

%package devel
Summary:        Devel package for libecpint
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers and libraries for libecpint.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest %{?testargs}

%files
%doc README.md CITATION
%{_libdir}/lib*.so.*

%files common
%{_datadir}/%{name}
%license LICENSE

%files devel
%{_includedir}/libecpint/
%{_includedir}/libecpint.hpp
%{_libdir}/cmake/ecpint
%{_libdir}/lib*.so

%changelog
* Fri Feb 05 2021 Christoph Junghans <junghans@votca.org> - 1.0.5-1
- Version bump to v1.0.5 (bug #1925367)

* Wed Jan 27 2021 Christoph Junghans <junghans@votca.org> - 1.0.4-3
- Add patch to fix memory leak

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 11:21:34 MST 2021 Christoph Junghans <junghans@lanl.gov> - 1.0.4-1
- Version bump to v1.0.4 (bug #19154510)

* Tue Oct 06 2020 Christoph Junghans <junghans@votca.org> - 1.0.2-1
- Initial add for packaging
