# generated by cabal-rpm-2.0.7
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name tart
%global pkgver %{pkg_name}-%{version}

Name:           %{pkg_name}
Version:        0.3
Release:        1%{?dist}
Summary:        Terminal Art TUI

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-brick-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-microlens-platform-prof
BuildRequires:  ghc-microlens-th-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-zipper-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-vty-prof
# End cabal-rpm deps

%description
A program to make ASCII art in a terminal.


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch

%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif


%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)

%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q
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


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
# End cabal-rpm files


%files -n ghc-%{name} -f ghc-%{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGELOG.md README.md


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Sun Jan 17 10:20:19 +08 2021 Jens Petersen <petersen@redhat.com> - 0.3-1
- update to 0.3

* Tue Nov 10 2020 Jens Petersen <petersen@redhat.com> - 0.2-1
- spec file generated by cabal-rpm-2.0.7
