%undefine __cmake_in_source_build

Name:           pystring
Version:        1.1.3
Release:        2%{?dist}
Summary:        Collection of C++ functions emulating Python's string class methods
License:        BSD
URL:            https://github.com/imageworks/pystring
Source0:        https://github.com/imageworks/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source100:      CMakeLists.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Pystring is a collection of C++ functions which match the interface and
behavior of Python's string class methods using std::string. Implemented in
C++, it does not require or make use of a Python interpreter. It provides
convenience and familiarity for common string operations not included in the
standard C++ library. It's also useful in environments where both C++ and
Python are used.

Overlapping functionality (such as index and slice/substr) of std::string is
included to match Python interfaces.

Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%autosetup -p1
cp %{SOURCE100} .


%build
%cmake
%cmake_build


%install
%cmake_install


%check
pushd %{__cmake_builddir}
./test


%files
%license LICENSE
%doc README
%{_libdir}/libpystring.so.0.0

%files devel
%{_includedir}/pystring/
%{_libdir}/libpystring.so


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Richard Shaw <hobbes1069@gmail.com> - 1.1.3-1
- Initial packaging.
