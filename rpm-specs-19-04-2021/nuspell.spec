Name:		nuspell
Version:	4.2.0
Release:	3%{?dist}
Summary:	Fast and safe spellchecking C++ library and command-line tool
License:	LGPLv3+
URL:		https://nuspell.github.io
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	libicu-devel
BuildRequires:	pandoc
BuildRequires:	catch-devel
Requires:		hunspell-en-US

%description
Nuspell is a fast and safe spelling checker software program. It is designed \
for languages with rich morphology and complex word compounding. Nuspell is \
written in modern C++ and it supports Hunspell dictionaries.

%package devel
Summary:	Development tools for %{name}
Requires:	libicu-devel
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and developer docs for \
%{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check
ctest

%files
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%{_libdir}/*.so.4*
%license COPYING COPYING.LESSER
%doc AUTHORS CHANGELOG.md README.md

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so

%doc %{_docdir}/nuspell/

%changelog
* Wed Feb 03 2021 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 4.2.0-3 
- SPEC file cleanup

* Tue Feb 02 2021 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 4.2.0-2 
- Update the package summary 

* Tue Feb 02 2021 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 4.2.0-1 
- New release 4.2.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.1.2-5
- Rebuilt for Boost 1.75

* Fri Oct 09 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.1.2-4
- Resolves: rhbz#1865076: FTBFS in Fedora rawhide/f33
- updated make_build and make_install to cmake_build and cmake_install macro
  
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.1.2-1 
- New release 3.1.2

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 3.1.1-3
- Rebuilt for Boost 1.73

* Wed May 20 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.1.1-2
- added tests

* Fri May 15 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.1.1-1
- Updated description and summary
- New release 3.1.1

* Mon Apr 27 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.1.0-1
- New release

* Fri Apr 3 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-5
- Added license files and doc files 

* Thu Mar 26 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-4
- renamed archive name 
- replaced cmake with %%cmake and make with %%make_build macro

* Mon Mar 02 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-3
- Update URL link
- Updated description
- Modified man page files macro

* Thu Feb 27 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-2
- Updated files to _libdir/cmake/nuspell/ instead of *.cmake files

* Tue Feb 25 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-1
- First release
