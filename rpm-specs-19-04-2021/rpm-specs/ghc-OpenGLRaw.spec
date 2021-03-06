# generated by cabal-rpm-2.0.7
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name OpenGLRaw
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        3.3.4.0
Release:        2%{?dist}
Summary:        A raw binding for the OpenGL graphics system

License:        BSD
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
BuildRequires:  ghc-fixed-prof
BuildRequires:  ghc-half-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  libglvnd-devel
# End cabal-rpm deps

%description
OpenGLRaw is a raw Haskell binding for the OpenGL 4.6 graphics system and lots
of OpenGL extensions. It is basically a 1:1 mapping of OpenGL's C API, intended
as a basis for a nicer interface. OpenGLRaw offers access to all necessary
functions, tokens and types plus a general facility for loading extension
entries. The module hierarchy closely mirrors the naming structure of the
OpenGL extensions, making it easy to find the right module to import.
All API entries are loaded dynamically, so no special C header files are needed
for building this package. If an API entry is not found at runtime, a userError
is thrown.

OpenGL is the industry's most widely used and supported 2D and 3D graphics
application programming interface (API), incorporating a broad set of
rendering, texture mapping, special effects, and other powerful visualization
functions. For more information about OpenGL and its various extensions, please
see <http://www.opengl.org/> and <http://www.opengl.org/registry/>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       libglvnd-devel%{?_isa}
# End cabal-rpm deps

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Jens Petersen <petersen@redhat.com> - 3.3.4.0-1
- spec file generated by cabal-rpm-2.0.7
