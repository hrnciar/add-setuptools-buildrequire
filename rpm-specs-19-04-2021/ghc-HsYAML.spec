# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name HsYAML
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        0.2.1.0
Release:        3%{?dist}
Summary:        Pure Haskell YAML 1.2 processor

License:        GPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-text-prof
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif
# End cabal-rpm deps

%description
'HsYAML' is a [YAML 1.2](http://yaml.org/spec/1.2/spec.html) processor, i.e.
a library for parsing and serializing YAML documents.

Features of 'HsYAML' include:

* Pure Haskell implementation with small dependency footprint and emphasis on
strict compliance with the <http://yaml.org/spec/1.2/spec.html>.
* Direct decoding to native Haskell types via ('aeson'-inspired) typeclass-based
API (see "Data.YAML").
* Allows round-tripping while preserving ordering, anchors, and comments at
Event-level.
* Support for constructing custom YAML node graph representation (including
support for cyclic YAML data structures).
* Support for the standard (untyped) /Failsafe/, (strict) /JSON/, and
(flexible) /Core/ "schemas" providing implicit typing rules as defined in
the YAML 1.2 specification (including support for user-defined custom schemas).
* Support for emitting YAML using /Failsafe/, (strict) /JSON/, and (flexible)
/Core/ "schemas" (including support for user-defined custom encoding schemas
* Event-based API resembling LibYAML's Event-based API (see "Data.YAML.Event").
* Low-level API access to lexical token-based scanner (see "Data.YAML.Token").

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
chmod a-x ChangeLog.md
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
%license LICENSE.GPLv2
%license LICENSE.GPLv3
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 0.2.1.0-1
- update to 0.2.1.0

* Thu Mar  5 2020 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.2.0-1
- spec file generated by cabal-rpm-2.0.4
