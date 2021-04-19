# generated by cabal-rpm-2.0.6 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name kan-extensions
%global pkgver %{pkg_name}-%{version}

%global invariant invariant-0.5.3
%global subpkgs %{invariant}

Name:           ghc-%{pkg_name}
Version:        5.2
# can only be reset when all subpkgs bumped
Release:        9%{?dist}
Summary:        Kan extensions & lifts, Yoneda lemma, and (co)density (co)monads

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{invariant}/%{invariant}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-adjunctions-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-distributive-prof
BuildRequires:  ghc-free-prof
#BuildRequires:  ghc-invariant-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-transformers-compat-prof
# for missing dep 'invariant':
BuildRequires:  ghc-StateVar-prof
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-prof
BuildRequires:  ghc-unordered-containers-prof
# End cabal-rpm deps

%description
Kan extensions, Kan lifts, various forms of the Yoneda lemma, and (co)density
(co)monads.


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


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage %{invariant}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%ghc_fix_rpath %{pkgver}
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Jens Petersen <petersen@redhat.com> - 5.2-8
- rebuild to fix StateVar requires hash (#1873687)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 5.2-6
- refresh to cabal-rpm-2.0.6

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 5.2-5
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 5.2-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 5.2-1
- update to 5.2
- subpackage invariant

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 5.1-5
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Jens Petersen <petersen@redhat.com> - 5.1-3
- use cabal-tweak-drop-dep
- revise .cabal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.0.2-1
- update to 5.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 5.0.2-4
- rebuild

* Sun Oct 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 5.0.2-3
- Drop ghc-fail dep.

* Fri Sep 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 5.0.2-2
- Shorten summary line.

* Fri Sep 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 5.0.2-1
- Update to latest spec template.
- Update to latest version.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 5.0.1-2
- Bump for Fedora 26.

* Sat Dec 17 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 5.0.1-1
- spec file generated by cabal-rpm-0.10.0