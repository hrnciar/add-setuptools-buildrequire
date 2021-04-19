# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name ansi-terminal
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.10.3
Release:        3%{?dist}
Summary:        Simple ANSI terminal support, with Windows compatibility

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-colour-prof
# End cabal-rpm deps

%description
ANSI terminal support for Haskell: allows cursor movement, screen clearing,
color output, showing or hiding the cursor, and changing the title.
Works on UNIX and Windows.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 0.10.3-1
- update to 0.10.3

* Sun Feb 09 2020 Jens Petersen <petersen@redhat.com> - 0.9.1-1
- update to 0.9.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 0.8.2-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.8.2-1
- update to 0.8.2

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.8.0.4-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.8.0.4-1
- update to 0.8.0.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.7.1.1-1
- update to 0.7.1.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.6.2.3-3
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Jens Petersen <petersen@redhat.com> - 0.6.2.3-1
- update to 0.6.2.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Jens Petersen <petersen@redhat.com> - 0.6.2.1-1
- update to 0.6.2.1

* Fri Sep 19 2014 Jens Petersen <petersen@redhat.com> - 0.6.1.1-1
- update to 0.6.1.1
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.6-2
- update to new simplified Haskell Packaging Guidelines

* Mon Mar 11 2013 Jens Petersen <petersen@redhat.com> - 0.6-1
- update to 0.6

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.5.5.1-1
- Updated to new upstream 0.5.5.1

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.5.5-8
- update with cabal-rpm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Jens Petersen <petersen@redhat.com> - 0.5.5-6
- update to cabal2spec-0.25

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5.5-4.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.5.5-4.1
- rebuild with new gmp

* Fri Jun 24 2011 Jens Petersen <petersen@redhat.com> - 0.5.5-4
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.5.5-3
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.5.5-1
- Added license info.
- Initial packaging for Fedora automatically generated by cabal2spec-0.22.2.
