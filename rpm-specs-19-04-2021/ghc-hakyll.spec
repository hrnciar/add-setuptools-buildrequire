# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hakyll
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        4.13.4.0
Release:        5%{?dist}
Summary:        A static website compiler library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptonite-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-fsnotify-prof
BuildRequires:  ghc-http-conduit-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-lrucache-prof
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-pandoc-prof
BuildRequires:  ghc-pandoc-citeproc-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-tagsoup-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-time-locale-compat-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-wai-app-static-prof
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-yaml-prof
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif
# End cabal-rpm deps

%description
Hakyll is a static website compiler library. It provides you with the tools to
create a simple or advanced static website using a Haskell DSL and formats such
as markdown or RST. You can find more information, including a tutorial, on the
website: <http://jaspervdj.be/hakyll>.


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
%{_datadir}/%{pkgver}
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG.md
%{_bindir}/hakyll-init


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Thu Mar 25 2021 Jens Petersen <petersen@redhat.com> - 4.13.4.0-5
- examples/ is used by hakyll-init (#1942237, reported by Martin Bukatovic)
- enable the testsuite

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 21:39:20 +08 2020 Jens Petersen <petersen@redhat.com> - 4.13.4.0-3
- rebuild for pandoc: cmark-gfm-0.2.2 fixes exponential parse (#1854329)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 4.13.4.0-1
- update to 4.13.4.0

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 4.13.3.0-1
- update to 4.13.3.0

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 4.13.0.1-1
- update to 4.13.0.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 4.12.5.2-1
- update to 4.12.5.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 4.12.4.0-1
- update to 4.12.4.0

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 4.12.3.0-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 4.12.3.0-1
- update to 4.12.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 4.10.0.0-1
- update to 4.10.0.0

* Mon Dec 11 2017 Jens Petersen <petersen@redhat.com> - 4.9.8.0-5
- rebuild

* Thu Nov 16 2017 Jens Petersen <petersen@fedoraproject.org> - 4.9.8.0-4
- refresh to cabal-rpm-0.12

* Fri Oct 20 2017 Jens Petersen <petersen@fedoraproject.org> - 4.9.8.0-2
- enable external link checking finally with http-conduit

* Wed Oct 11 2017 Jens Petersen <petersen@redhat.com> - 4.9.8.0-1
- update to 4.9.8.0

* Tue Oct 10 2017 Jens Petersen <petersen@redhat.com> - 4.9.7.0-5
- wai-app-static is now in Fedora

* Thu Sep 14 2017 Jens Petersen <petersen@redhat.com> - 4.9.7.0-4
- update to 4.9.7.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 4.9.5.1-1
- update to 4.9.5.1
- subpackage wai-app-static

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
%doc CHANGELOG.md

* Mon Jan 30 2017 Jens Petersen <petersen@redhat.com> - 4.8.3.2-2
- rebuild

* Thu Sep 01 2016 Jens Petersen <petersen@redhat.com> - 4.8.3.2-1
- update to 4.8.3.2

* Tue May 24 2016 Ben Boeckel <mathstuf@gmail.com> - 4.5.4.0-9
- rebuild

* Sat Apr 23 2016 Ben Boeckel <mathstuf@gmail.com> - 4.5.4.0-8
- rebuild
- sync with cabal-rpm-0.9.10

* Thu Mar 03 2016 Adam Williamson <awilliam@redhat.com> - 4.5.4.0-7
- rebuild for updated tagsoup, rebuilt pandoc and citeproc

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Jens Petersen <petersen@redhat.com> - 4.5.4.0-5
- rebuild with pandoc-citeproc-0.7.4

* Mon Sep  7 2015 Jens Petersen <petersen@redhat.com> - 4.5.4.0-4
- rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Jens Petersen <petersen@fedoraproject.org> - 4.5.4.0-2
- rebuild

* Mon Jan 26 2015 Jens Petersen <petersen@redhat.com> - 4.5.4.0-1
- update to 4.5.4.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Jens Petersen <petersen@redhat.com> - 4.5.2.0-1
- update to 4.5.2.0 and cblrpm-0.8.11
- build with pandoc-citeproc instead of citeproc-hs hack

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jens Petersen <petersen@redhat.com> - 4.5.1.0-3
- rebuild

* Tue May 13 2014 Jens Petersen <petersen@redhat.com> - 4.5.1.0-2
- reenable ARM now that pandoc is available (#992364)

* Fri May 02 2014 Jens Petersen <petersen@redhat.com> - 4.5.1.0-1
- update to 4.5.1.0
- enable previewServer and watchServer
- move example dir to devel doc

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 4.4.3.1-1
- update to 4.4.3.1
- disable watchServer (needs fsnotify)
- patch to use citeproc-hs until pandoc-citeproc packaged:
  this may cause biblio regressions

* Wed Aug 28 2013 Jens Petersen <petersen@redhat.com> - 4.3.1.0-4
- temporarily exclude armv7hl since pandoc not building there (#992364)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Jens Petersen <petersen@redhat.com> - 4.3.1.0-2
- rebuild

* Thu Jun 20 2013 Jens Petersen <petersen@redhat.com> - 4.3.1.0-1
- update to 4.3.1.0

* Fri Jun 14 2013 Jens Petersen <petersen@redhat.com> - 4.3.0.0-1
- update to 4.3.0.0
- update to new simplified Haskell Packaging Guidelines

* Sun Mar 10 2013 Jens Petersen <petersen@redhat.com> - 4.2.1.2-1
- update to 4.2.1.2
- no longer depends on hamlet
- disable checkExternal since it requires http-conduit
- add hakyll-init to devel subpackage

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Jens Petersen <petersen@redhat.com> - 3.4.0.0-2
- rebuild

* Mon Oct 29 2012 Jens Petersen <petersen@redhat.com> - 3.4.0.0-1
- update to 3.4.0.0 with cabal-rpm
- disable previewServer explicitly until snap-server packaged
- allow hamlet-1.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 3.2.7.2-5
- change prof BRs to devel

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 3.2.7.2-4
- rebuild

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 3.2.7.2-3
- rebuild

* Fri May 11 2012 Karsten Hopp <karsten@redhat.com> 3.2.7.2-2
- change exclusivearches from ghc_arches to ghc_arches_with_ghci as
  the BR ghc-hamlet is only available on those archs

* Thu Apr 26 2012 Jens Petersen <petersen@redhat.com> - 3.2.7.2-1
- update to 3.2.7.2

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 3.2.6.2-1
- update to 3.2.6.2

* Wed Mar  7 2012 Jens Petersen <petersen@redhat.com> - 3.2.6.1-1
- update to 3.2.6.1
- regex-pcre depends replaced by regex-tdfa

* Mon Feb 13 2012 Jens Petersen <petersen@redhat.com> - 3.2.6.0-1
- update to 3.2.6.0

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 3.2.5.1-2
- Rebuild against PCRE 8.30

* Tue Feb  7 2012 Jens Petersen <petersen@redhat.com> - 3.2.5.1-1
- update to 3.2.5.1

* Thu Jan 26 2012 Jens Petersen <petersen@redhat.com> - 3.2.5.0-1
- update to 3.2.5.0

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 3.2.3.2-1
- update to 3.2.3.2 and cabal2spec-0.25.2
- use ghc_add_basepkg_file

* Mon Nov  7 2011 Jens Petersen <petersen@redhat.com> - 3.2.0.10-1
- BSD license, deps, and description

* Mon Oct 31 2011 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 3.2.0.10-0
- initial packaging for Fedora automatically generated by cabal2spec-0.24.1
