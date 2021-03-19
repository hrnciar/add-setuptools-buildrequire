%undefine __cmake_in_source_build

Name: cotila
Version: 1.2.1
Release: 1%{?dist}

License: ASL 2.0
URL: https://github.com/calebzulawski/cotila
Summary: Compile Time Linear Algegra
Source0: %{url}/archive/%{version}.tar.gz
BuildArch: noarch

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}

%description devel
%{summary}.

%prep
%autosetup -n cotila-%{version} -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc README.md AUTHORS
%license LICENSE
%{_datadir}/cmake/%{name}/
%{_includedir}/%{name}/

%changelog
* Thu Mar 11 2021 Alexey Gorgurov <alexfails@fedoraproject.org> - 1.2.1-1
- Initial SPEC release.
