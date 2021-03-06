# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name happstack-server
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        7.6.1
Release:        3%{?dist}
Summary:        Web related tools and services

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-extensible-exceptions-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hslogger-prof
BuildRequires:  ghc-html-prof
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-bsd-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-semigroups-prof
BuildRequires:  ghc-sendfile-prof
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-system-filepath-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-threads-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-xhtml-prof
BuildRequires:  ghc-zlib-prof
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
%endif
# End cabal-rpm deps

%description
Happstack Server provides an HTTP server and a rich set of functions for
routing requests, handling query parameters, generating responses, working with
cookies, serving files, and more. For in-depth documentation see the Happstack
Crash Course <http://happstack.com/docs/crashcourse/index.html>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


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
%license COPYING
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license COPYING
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 7.6.1-1
- update to 7.6.1

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 7.6.0-1
- update to 7.6.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 7.5.1.3-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 7.5.1.3-1
- update to 7.5.1.3

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 7.5.1.1-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 7.5.1.1-1
- update to 7.5.1.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 7.5.0.1-1
- update to 7.5.0.1

* Tue Oct 17 2017 Jens Petersen <petersen@redhat.com> - 7.4.6.4-1
- update to 7.4.6.4

* Tue Oct 17 2017 Jens Petersen <petersen@redhat.com> - 7.4.6.3-6
- time-compat is now in Fedora

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 7.4.6.3-3
- update to 7.4.6.3

* Thu Feb  9 2017 Jens Petersen <petersen@redhat.com> - 7.4.6.2-2
- build subpackage in main package dir

* Wed Aug 17 2016 Jens Petersen <petersen@redhat.com> - 7.4.6.2-1
- update to 7.4.6.2
- subpackage (bundle) time-compat-0.1.0.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Jens Petersen <petersen@fedoraproject.org> - 7.3.9-1
- update to 7.3.9

* Mon Sep 01 2014 Jens Petersen <petersen@redhat.com> - 7.3.8-1
- update to 7.3.8
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Jens Petersen <petersen@redhat.com> - 7.1.0-3
- rebuild

* Fri Nov 29 2013 Jens Petersen <petersen@redhat.com> - 7.1.0-2
- rebuild

* Wed Sep 04 2013 Jens Petersen <petersen@redhat.com> - 7.1.0-1
- update to 7.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 7.0.0-9
- update to new simplified Haskell Packaging Guidelines
- patch for newer time lib in ghc-7.6

* Tue Mar 19 2013 Jens Petersen <petersen@redhat.com> - 7.0.0-8
- allow blaze-html-0.6

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov  9 2012 Jens Petersen <petersen@redhat.com> - 7.0.0-6
- build with base64-bytestring-1.0 and blaze-html-0.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 7.0.0-4
- rebuild

* Mon Jun 11 2012 Jens Petersen <petersen@redhat.com> - 7.0.0-3
- allow building with mtl-2.1 and transformers-0.3

* Mon May  7 2012 Jens Petersen <petersen@redhat.com> - 7.0.0-2
- turn on base4 flag
- add syb depends

* Fri Apr 13 2012 Jens Petersen <petersen@redhat.com> - 7.0.0-1
- BSD license
- dependencies

* Fri Apr 13 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.5
