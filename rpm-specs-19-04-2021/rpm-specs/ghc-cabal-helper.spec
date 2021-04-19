# generated by cabal-rpm-2.0.6 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name cabal-helper
%global pkgver %{pkg_name}-%{version}

%global cabalplan cabal-plan-0.7.0.0
%global opticscore optics-core-0.2
%global semialign semialign-1.1
%global topograph topograph-1.0.0.1
%global indexedprofunctors indexed-profunctors-0.1
%global subpkgs %{indexedprofunctors} %{opticscore} %{semialign} %{topograph} %{cabalplan}

# testsuite missing deps: cabal-plan

Name:           ghc-%{pkg_name}
Version:        1.1.0.0
# can only be reset when all subpkgs bumped
Release:        11%{?dist}
Summary:        Give Haskell development tools access to Cabal project environment

License:        ASL 2.0
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{cabalplan}/%{cabalplan}.tar.gz
Source2:        https://hackage.haskell.org/package/%{opticscore}/%{opticscore}.tar.gz
Source3:        https://hackage.haskell.org/package/%{semialign}/%{semialign}.tar.gz
Source4:        https://hackage.haskell.org/package/%{topograph}/%{topograph}.tar.gz
Source5:        https://hackage.haskell.org/package/%{indexedprofunctors}/%{indexedprofunctors}.tar.gz
Source6:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# build cabal-plan executable (in koji)
Patch1:         cabal-plan-exe-flag.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-SHA-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
#BuildRequires:  ghc-cabal-plan-prof
BuildRequires:  ghc-clock-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-semigroups-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-utf8-string-prof
# for missing dep 'cabal-plan':
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base16-bytestring-prof
#BuildRequires:  ghc-optics-core-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-parsec-prof
#BuildRequires:  ghc-semialign-prof
BuildRequires:  ghc-singleton-bool-prof
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-assoc-prof
#BuildRequires:  ghc-topograph-prof
BuildRequires:  ghc-vector-prof
# End cabal-rpm deps

%description
The purpose of the 'cabal-helper' library is to give Haskell development tools
access to the same environment which build tools such as 'cabal' and 'stack'
normally provide to the compiler.


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
%ghc_lib_subpackage %{cabalplan}
%ghc_lib_subpackage %{opticscore}
%ghc_lib_subpackage %{semialign}
%ghc_lib_subpackage %{topograph}
%ghc_lib_subpackage %{indexedprofunctors}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2 -a3 -a4 -a5
cp -bp %{SOURCE6} %{pkg_name}.cabal
# End cabal-rpm setup
cabal-tweak-dep-ver semigroups '< 0.19' '< 0.20'
(
cd %{cabalplan}
cabal-tweak-dep-ver base '4.11' '4.12'
cabal-tweak-dep-ver containers '^>= 0.5.0' '^>= 0.6.0'
cabal-tweak-dep-ver these '^>= 1' '^>= 1.1'
%patch1 -p1 -b .orig
)
(
cd %{semialign}
cabal-tweak-dep-ver these '<1.1' '<1.2'
)


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

echo %{_bindir}/cabal-plan >> %{cabalplan}/ghc-cabal-plan-devel.files


%check
# Don't add any servers to cabal config, so it
# doesn't try to download anything.
mkdir -p home/.cabal
echo > home/.cabal/config

# Cannot run build tests that use the network.
%global cabal_test_options ghc-session
HOME=$PWD/home %cabal_test


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
* Sun Mar 21 2021 Jens Petersen <petersen@redhat.com> - 1.1.0.0-11
- 'these' was packaged in Fedora

* Wed Mar 17 2021 Jens Petersen <petersen@redhat.com> - 1.1.0.0-10
- 'assoc' was packaged in Fedora

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jens Petersen <petersen@redhat.com> - 1.1.0.0-7
- bump cabal-plan to 0.7.0.0

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 1.1.0.0-6
- update to 1.1.0.0

* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 0.8.2.0-5
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.8.2.0-3
- update to 0.8.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 2019 Jens Petersen <petersen@redhat.com> - 0.8.1.2-1
- update to 0.8.1.2
- subpackage cabal-plan-0.4.0 dep

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.8.0.2-5
- revise .cabal
- run testsuite only on Intel archs (failing elsewhere)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0.2-3
- Build with tests enabled

* Mon Apr 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0.2-2
- Use macro-defined location for private executables (#1563863)

* Wed Apr  4 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.8.0.2-1
- spec file generated by cabal-rpm-0.12.1