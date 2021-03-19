# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name haskell-gi
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.24.7
Release:        1%{?dist}
Summary:        Generate Haskell bindings for GObject Introspection capable libraries

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-cabal-doctest-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-haskell-gi-base-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pretty-show-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-xdg-basedir-prof
BuildRequires:  ghc-xml-conduit-prof
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if %{with tests}
BuildRequires:  ghc-doctest-devel
%endif
# End cabal-rpm deps

%description
Generate Haskell bindings for GObject Introspection capable libraries.
This includes most notably Gtk+, but many other libraries in the GObject
ecosystem provide introspection data too.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gobject-2.0)
Requires:       pkgconfig(gobject-introspection-1.0)
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


%check
%cabal_test


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Thu Jan 28 2021 Jens Petersen <petersen@redhat.com> - 0.24.7-1
- update to 0.24.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.24.2-1
- update to 0.24.2

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 0.23.1-1
- update to 0.23.1

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.23.0-1
- update to 0.23.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.21.5-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.21.5-1
- update to 0.21.5

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.21.3-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.21.3-1
- update to 0.21.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 David Shea <dshea@redhat.com> - 0.21.0-3
- Rebuild against a new build of ghc-conduit-extra

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 David Shea <dshea@redhat.com> - 0.21.0-1
- Update to haskell-gi-0.21.0

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.20.3-2
- rebuild

* Mon Nov 13 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.20.3-1
- spec file generated by cabal-rpm-0.11.2
