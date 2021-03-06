# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name cmark
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        0.6
Release:        4%{?dist}
Summary:        Fast, accurate CommonMark (Markdown) parser and renderer

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
BuildRequires:  ghc-text-prof
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
%endif
# End cabal-rpm deps
Provides:       bundled(cmark) = 0.28.0

%description
This package provides Haskell bindings for <https://github.com/jgm/cmark
libcmark>, the reference parser for <http://commonmark.org CommonMark>, a fully
specified variant of Markdown. It includes sources for libcmark (0.29.0) and
does not require prior installation of the C library.


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
%doc README.md changelog


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.6-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.6-1
- update to 0.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.5.6.3-1
- update to 0.5.6.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.5.6-7
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.5.6-5
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.5.6-2
- rebuild

* Mon Dec 11 2017 Jens Petersen <petersen@redhat.com> - 0.5.6-1
- update to 0.5.6
- enable tests on armv7hl too

* Mon Dec 11 2017 Jens Petersen <petersen@redhat.com> - 0.5.5-4
- use bundled cmark
  (so that cmark package is not locked to this version)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 0.5.5-1
- update to 0.5.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 03 2016 Jens Petersen <petersen@redhat.com> - 0.5.2.1-1
- update to 0.5.2.1

* Tue May 03 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5.1-2
- Rebuild for cmark 0.25

* Fri Feb  5 2016 Jens Petersen <petersen@redhat.com> - 0.5.1-1
- patch to build with system cmark
- disable tests on armv7

* Wed Feb  3 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org>
- spec file generated by cabal-rpm-0.9.9
