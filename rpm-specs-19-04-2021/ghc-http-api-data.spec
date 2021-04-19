# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name http-api-data
%global pkgver %{pkg_name}-%{version}

# testsuite missing deps: quickcheck-instances

Name:           ghc-%{pkg_name}
Version:        0.4.1.1
Release:        4%{?dist}
Summary:        Converting to/from HTTP API data

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-attoparsec-iso8601-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cookie-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-compat-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-uuid-types-prof
# End cabal-rpm deps

%description
This package defines typeclasses used for converting Haskell data types to and
from HTTP API data. Haskell types like booleans, numbers, strings and dates are
supported.


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
cp -bp %{SOURCE1} %{pkg_name}.cabal
chmod a-x CHANGELOG.md README.md
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.4.1.1-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.4.1.1-1
- update to 0.4.1.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.4-1
- update to 0.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.3.8.1-1
- update to 0.3.8.1

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.3.7.2-5
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.3.7.2-3
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.7.2-1
- update to 0.3.7.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.3.7.1-4
- rebuild

* Mon Oct 23 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.7.1-3
- rebuilt

* Thu Aug 31 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.3.7.1-2
- Add a more reasonable description.

* Sat Jul 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.3.7.1-1
- Update to latest version.

* Mon Jul 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.2.2-5
- Re-add dist tag to release numbers.

* Mon Jul 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.2.2-4
- Bump for Fedora 26.

* Thu Dec 15 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-3
- Update release to be newer than previous builds

* Thu Dec 15 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.2-1
- spec file generated by cabal-rpm-0.10.0