# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name dataenc
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.14.0.7
Release:        18%{?dist}
Summary:        Data encoding library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
# End cabal-rpm deps

%description
Data encoding library currently providing Base16, Base32, Base32Hex, Base64,
Base64Url, Base85, Python string escaping, Quoted-Printable, URL encoding,
uuencode, xxencode, and yEncoding.


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
cabal-tweak-dep-ver base '< 4.8' '< 5'


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


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.14.0.7-16
- refresh to cabal-rpm-2.0.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 0.14.0.7-14
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.14.0.7-12
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.14.0.7-8
- rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.14.0.7-5
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 28 2015 Jens Petersen <petersen@redhat.com> - 0.14.0.7-2
- allow building with ghc 7.10 base

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 29 2014 Jens Petersen <petersen@redhat.com> - 0.14.0.7-1
- update to 0.14.0.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 0.14.0.5-4
- update to cblrpm-0.8.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.14.0.5-2
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 0.14.0.5-1
- update to 0.14.0.5

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Jens Petersen <petersen@redhat.com> - 0.14.0.4-1
- update to 0.14.0.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.14.0.3-3
- change prof BRs to devel

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 0.14.0.3-2
- add license to ghc_files

* Wed Jan  4 2012 Jens Petersen <petersen@redhat.com> - 0.14.0.3-1
- update to 0.14.0.3 and cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14.0.2-1.3
- rebuild with new gmp without compat lib

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14.0.2-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.14.0.2-1.1
- rebuild with new gmp

* Wed Aug 17 2011 Jens Petersen <petersen@redhat.com> - 0.14.0.2-1
- update to 0.14.0.2

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.14-2
- BR ghc-Cabal-devel instead of ghc-prof (cabal2spec-0.23.2)

* Fri Mar 11 2011 Jens Petersen <petersen@redhat.com> - 0.14-1
- update to 0.14

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.13.0.5-2
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 0.13.0.5-1
- update to 0.13.0.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Jens Petersen <petersen@redhat.com> - 0.13.0.4-3
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.4-2
- update url

* Mon Nov  1 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.4-1
- update to 0.13.0.4

* Thu Aug 19 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.3-1
- update to 0.13.0.3
- build with hscolour and ghc-rpm-macros-0.8.1

* Sat Jun 26 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.2-3
- sync cabal2spec-0.22

* Sat Apr 24 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.2-2
- rebuild against ghc-6.12.2
- condition ghc_lib_package

* Sat Jan 23 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.2-1
- BSD license
- summary and description from hackage

* Sat Jan 23 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.13.0.2-0
- initial packaging for Fedora automatically generated by cabal2spec-0.21.1
