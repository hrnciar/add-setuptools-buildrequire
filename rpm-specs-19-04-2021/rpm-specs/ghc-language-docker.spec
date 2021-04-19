# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name language-docker
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        9.1.2
Release:        2%{?dist}
Summary:        Dockerfile parser, pretty-printer and embedded DSL

License:        GPLv3+
URL:            https://github.com/hadolint/%{pkg_name}/
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
%endif
# End cabal-rpm deps

%description
Dockerfile parser, pretty-printer and embedded DSL

Provides the ability to parse Docker files, a pretty-printer and EDSL for
writting Dockerfiles in Haskell.


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
%doc README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 9.1.2-1
- Update to 9.1.2

* Thu Sep 03 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 9.1.1-1
- Initial RPM release, from spec file generated by cabal-rpm-2.0.6
