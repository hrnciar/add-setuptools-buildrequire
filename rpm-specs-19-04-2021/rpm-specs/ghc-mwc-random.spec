# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name mwc-random
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.14.0.0
Release:        7%{?dist}
Summary:        Fast, high quality pseudo random number generation

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-math-functions-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-vector-prof
# End cabal-rpm deps

%description
A library for generating high quality random numbers that follow
either a uniform or normal distribution.  The generated numbers are
suitable for use in statistical applications.

The uniform PRNG uses Marsaglia's MWC256 (also known as MWC8222)
multiply-with-carry generator, which has a period of 2^8222 and fares well in
tests of randomness. It is also extremely fast, between 2 and 3 times faster
than the Mersenne Twister.

Compared to the mersenne-random package, this package has a more
convenient API, is faster, and supports more statistical distributions.


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
%doc README.markdown changelog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.14.0.0-4
- refresh to cabal-rpm-2.0.6

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 0.14.0.0-3
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.14.0.0-1
- update to 0.14.0.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.13.6.0-6
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.13.6.0-4
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.13.6.0-1
- update to 0.13.6.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 0.13.5.0-1
- update to 0.13.5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 25 2016 Jens Petersen <petersen@redhat.com> - 0.13.4.0-1
- update to 0.13.4.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Jens Petersen <petersen@redhat.com> - 0.13.3.2-1
- update to 0.13.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jens Petersen <petersen@redhat.com> - 0.13.3.0-1
- update to 0.13.3.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Jens Petersen <petersen@redhat.com> - 0.12.0.1-4
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.12.0.1-2
- update with cabal-rpm

* Sun Oct 21 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 0.12.0.1-1
- update to 0.12.0.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.12.0.0-3
- change prof BRs to devel

* Mon May  7 2012 Jens Petersen <petersen@redhat.com> - 0.12.0.0-2
- requires ghci to build

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 0.12.0.0-1
- update to 0.12.0.0

* Thu Jan 19 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 0.11.0.0-1
- update to 0.11.0.0 version

* Wed Jan  4 2012 Jens Petersen <petersen@redhat.com> - 0.10.0.1-2
- update to cabal2spec-0.25.2
- add README file
- depends on time

* Sat Nov 19 2011 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 0.10.0.1-1
- Added dependencies. License is BSD3

* Sat Nov 19 2011 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.10.0.1-0
- initial packaging for Fedora automatically generated by cabal2spec-0.24.1
