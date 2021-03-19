# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hgettext
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.1.31.0
Release:        12%{?dist}
Summary:        Haskell binding to libintl

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources
Patch1:         https://patch-diff.githubusercontent.com/raw/haskell-hvr/hgettext/pull/16.patch#/hgettext-Cabal-2.4.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-haskell-src-exts-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-setlocale-prof
BuildRequires:  ghc-uniplate-prof
# End cabal-rpm deps

%description
This package provides bindings to the 'gettext' internationalization and
localization (i18n) library.

This package provides support for custom 'Setup.hs' scripts via the
"Distribution.Simple.I18N.GetText" module.

A user-contributed tutorial can be found in the [Haskell
Wiki](https://wiki.haskell.org/Internationalization_of_Haskell_programs_using_gettext).


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
# End cabal-rpm setup
%patch1 -p1 -b .orig
cabal-tweak-dep-ver base '<4.12' '<5'
cabal-tweak-dep-ver Cabal '== 2.2.*' '> 2.2'
cabal-tweak-dep-ver containers '<0.6' '<0.7'
cabal-tweak-dep-ver haskell-src-exts '<1.21' '<1.24'


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
%{_bindir}/%{pkg_name}


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.1.31.0-10
- refresh to cabal-rpm-2.0.6

* Sun Feb 23 2020 Jens Petersen <petersen@redhat.com> - 0.1.31.0-9
- add fix for Cabal-2.4 (#1799403)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.1.31.0-7
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  1 2019 Jens Petersen <petersen@redhat.com> - 0.1.31.0-5
- refresh to cabal-rpm-0.13

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.1.31.0-4
- revise .cabal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.1.31.0-1
- update to 0.1.31.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 0.1.30-12
- patch for newer haskell-src-exts

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul  3 2015 Philip Withnall <philip@tecnocode.co.uk> - 0.1.30-9
- Rebuilt for ghc-setlocale 1.0.0.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr  3 2015 Jens Petersen <petersen@redhat.com> - 0.1.30-7
- rebuild

* Wed Jan 28 2015 Jens Petersen <petersen@redhat.com> - 0.1.30-6
- cblrpm refresh

* Fri Dec 12 2014 Philip Withnall <philip@tecnocode.co.uk> - 0.1.30-5
- Rebuilt for libHSbase changes

* Wed Sep 17 2014 Philip Withnall <philip@tecnocode.co.uk> - 0.1.30-4
- Rebuilt for ghc-setlocale 1.0.0.1

* Sun Aug 31 2014 Philip Withnall <philip@tecnocode.co.uk> - 0.1.30-3
- Rebuilt for ghc-setlocale 1.0.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Philip Withnall <philip@tecnocode.co.uk> - 0.1.30-1
- spec file generated by cabal-rpm-0.8.11
