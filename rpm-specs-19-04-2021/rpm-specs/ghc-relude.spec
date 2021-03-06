# generated by cabal-rpm-2.0.7
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name relude
%global pkgver %{pkg_name}-%{version}

# testsuite missing deps: hedgehog

Name:           ghc-%{pkg_name}
Version:        0.7.0.0
Release:        1%{?dist}
Summary:        An alternative Haskell prelude for productivity and safety
License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-prof
# End cabal-rpm deps

%description
'relude' is an alternative prelude library. If you find the default
'Prelude' unsatisfying, despite its advantages, consider using 'relude'
instead.

== Relude goals and design principles

* Productivity: You can be more productive with a "non-standard"
standard library, and 'relude' helps you with writing safer and more
efficient code faster.

* Total programming: Usage of partial functions can lead to unexpected
bugs and runtime exceptions in pure code. The types of partial
functions lie about their behavior. And even if it is not always
possible to rely only on total functions, 'relude' strives to
encourage best-practices and reduce the chances of introducing a bug.

* Type-safety: We use the "make invalid states unrepresentable" motto as
one of our guiding principles. If it is possible, we express this concept
through the types. Example: ' whenNotNull :: Applicative f => [a] ->
(NonEmpty a -> f ()) -> f () '

* Performance: We prefer 'Text' over 'String', use space-leaks-free
functions (e.g. our custom performant 'sum' and 'product'),
introduce 'INLINE' and 'SPECIALIZE' pragmas where appropriate,
and make efficient container types (e.g. 'Map', 'HashMap', 'Set') more
accessible.

* Minimalism (low number of dependencies): We do not force users of
'relude' to stick to any specific lens or text formatting or logging library.
Where possible, 'relude' depends only on boot libraries.

* Convenience: Despite minimalism, we want to bring commonly used types and
functions into scope, and make available functions easier to use.

* Excellent documentation:
1. Tutorial
2. Migration guide from 'Prelude'
3. Haddock for every function with examples tested by doctest
4. Documentation regarding internal module structure
5. 'relude'-specific HLint rules

* User-friendliness: Anyone should be able to quickly migrate to 'relude'.
Only some basic familiarity with the common libraries like 'text' and
'containers' should be enough (but not necessary).

* Exploration: We have space to experiment with new ideas and proposals
without introducing breaking changes. 'relude' uses the approach with 'Extra.*'
modules which are not exported by default. The chosen approach makes it quite
easy for us to provide new functionality without breaking anything and let the
users decide to use it or not.


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
* Sun Jan 17 2021 Jens Petersen <petersen@redhat.com> - 0.7.0.0-1
- spec file generated by cabal-rpm-2.0.7
