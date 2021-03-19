# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name tf-random
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.5
Release:        21%{?dist}
Summary:        High-quality splittable pseudorandom number generator

# main license is BSD
# brg_types.h is BSD and optionally GPL+
# C code by Doug Whiting is Public Domain
License:        BSD and Public Domain
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-time-prof
# End cabal-rpm deps

%description
This package contains an implementation of a high-quality splittable
pseudorandom number generator. The generator is based on a cryptographic hash
function built on top of the ThreeFish block cipher. See the paper /Splittable
Pseudorandom Number Generators Using Cryptographic Hashing/ by Claessen, Pałka
for details and the rationale of the design.

The package provides the following:

* A splittable PRNG that implements the standard 'System.Random.RandomGen'
class.

* The generator also implements an alternative version of the
'System.Random.TF.Gen.RandomGen' class (exported from "System.Random.TF.Gen"),
which requires the generator to return pseudorandom integers from the full
32-bit range, and contains an n-way split function.

* An alternative version of the 'Random' class is provided, which is linked to
the new 'RandomGen' class, together with 'Random' instances for some integral
types.

* Two functions for initialising the generator with a non-deterministic seed:
one using the system time, and one using the '/dev/urandom' UNIX special file.

The package uses an adapted version of the reference C implementation of
ThreeFish from the reference package of the Skein hash function
(<https://www.schneier.com/skein.html>), originally written by Doug Whiting.

Please note that even though the generator provides very high-quality
pseudorandom numbers, it has not been designed with cryptographic applications
in mind.


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
%license LICENSE.brg
%license LICENSE.tf
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%license LICENSE.brg
%license LICENSE.tf
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.5-18
- refresh to cabal-rpm-2.0.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.5-16
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.5-14
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.5-12
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.5-9
- rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.5-6
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar  3 2015 Jens Petersen <petersen@redhat.com> - 0.5-2
- some of the C code is Public Domain (#1196960)

* Fri Feb 27 2015 Jens Petersen <petersen@redhat.com> - 0.5-1
- improve filelists

* Mon Feb  9 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.5
- spec file generated by cabal-rpm-0.9.3
