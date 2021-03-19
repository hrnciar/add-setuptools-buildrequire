# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name resourcet
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        1.2.4.2
Release:        4%{?dist}
Summary:        Deterministic allocation and freeing of scarce resources

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-prof
%if %{with tests}
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
Allocate resources which are guaranteed to be released.
All register cleanup actions live in the IO monad, not the main monad.
This allows both more efficient code, and for monads to be transformed.


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


%check
%cabal_test


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 1.2.4.2-1
- update to 1.2.4.2

* Fri Jun 19 2020 Jens Petersen <petersen@redhat.com> - 1.2.4.1-1
- update to 1.2.4.1

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 1.2.4-1
- update to 1.2.4

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 1.2.2-5
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 1.2.2-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 1.2.2-1
- update to 1.2.2

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.2.1-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 1.2.1-1
- update to 1.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Jens Petersen <petersen@redhat.com> - 1.1.10-3
- unbundle unliftio-core

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.1.10-1
- update to 1.1.10
- subpackage unliftio-core

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 1.1.9-1
- update to 1.1.9

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Jens Petersen <petersen@redhat.com> - 1.1.7.4-1
- update to 1.1.7.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Jens Petersen <petersen@redhat.com> - 1.1.4.1-1
- update to 1.1.4.1

* Tue Jan 27 2015 Jens Petersen <petersen@fedoraproject.org> - 0.4.10.2-4
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Jens Petersen <petersen@redhat.com> - 0.4.10.2-1
- update to 0.4.10.2
- update packaging to cabal-rpm-0.8.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Jens Petersen <petersen@redhat.com> - 0.4.6-1
- update to 0.4.6
- update to new simplified Haskell Packaging Guidelines

* Mon Mar 11 2013 Jens Petersen <petersen@redhat.com> - 0.4.5-1
- update to 0.4.5

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Jens Petersen <petersen@redhat.com> - 0.4.0.2-1
- update to 0.4.0.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Jens Petersen <petersen@redhat.com> - 0.3.2.2-1
- update to 0.3.2.2

* Tue May  1 2012 Jens Petersen <petersen@redhat.com> - 0.3.2.1-1
- update to 0.3.2.1

* Tue Apr 10 2012 Jens Petersen <petersen@redhat.com> - 0.3.2-1
- update to 0.3.2

* Sat Mar 24 2012 Jens Petersen <petersen@redhat.com> - 0.3.1-1
- BSD
- depends on lifted-base and containers

* Sat Mar 24 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4