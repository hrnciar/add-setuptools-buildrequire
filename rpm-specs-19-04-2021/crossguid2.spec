%global commit ca1bf4b810e2d188d04cb6286f957008ee1b7681
%global short_commit %(c=%{commit}; echo ${c:0:7})	
%global date 20190529

Name: crossguid2
Version: 0.2.2
Release: 8.%{date}git%{short_commit}%{?dist}
Summary: Lightweight cross platform C++ GUID/UUID library
License: MIT
URL: https://github.com/graeme-hill/crossguid/
Source0: %{url}/archive/%{commit}/crossguid-%{commit}.tar.gz

# Fix library and directory names
Patch0: %{name}-fix_name.patch

BuildRequires: gcc-c++, cmake
BuildRequires: libuuid-devel
BuildRequires: make

%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and has a generic class for
parsing, stringifying, and comparing IDs.


%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libuuid-devel%{?_isa}
Requires: cmake%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -n crossguid-%{commit} -N

%patch0 -p0 -b .fix_name


%build
%cmake -DCROSSGUID_SOVERSION_STRING:STRING=0 -DCROSSGUID_VERSION_STRING:STRING=0.0 \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/%{name}
%cmake_build

%install
%cmake_install

%check
pushd %{_target_platform}
./%{name}-test

%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Mar 18 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-8.20190529gitca1bf4b
- Fix CMake commands

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6.20190529gitca1bf4b
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-2.20190529gitca1bf4b
- New commit
- Fix rhbz#1721342
- Add pkgconfig file

* Sat Mar 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-1.20190126gitb151b7d
- Renamed crossguid2 to avoid conflict with older crossguid-0.1
- Post release 0.2.2
- Use CMake method
