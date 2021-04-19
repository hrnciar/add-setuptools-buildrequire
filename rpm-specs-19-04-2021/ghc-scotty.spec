# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name scotty
%global pkgver %{pkg_name}-%{version}

# testsuite missing deps: hspec-wai

Name:           ghc-%{pkg_name}
Version:        0.11.6
Release:        4%{?dist}
Summary:        Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-compat-batteries-prof
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-regex-compat-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-warp-prof
# End cabal-rpm deps

%description
A Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp.

Scotty is the cheap and cheerful way to write RESTful, declarative web
applications.

* A page is as simple as defining the verb, url pattern, and Text content.
* It is template-language agnostic. Anything that returns a Text value will do.
* Conforms to WAI Application interface.
* Uses very fast Warp webserver by default.

As for the name: Sinatra + Warp = Scotty.


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
chmod a-x README.md changelog.md
# End cabal-rpm setup
cabal-tweak-drop-dep fail
cabal-tweak-drop-dep nats


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
%doc README.md changelog.md examples


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 0.11.6-1
- update to 0.11.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.11.5-1
- update to 0.11.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.11.4-1
- update to 0.11.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.11.2-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.11.2-1
- update to 0.11.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.11.0-5
- rebuild

* Sat Oct 21 2017 Jens Petersen <petersen@fedoraproject.org> - 0.11.0-4
- no longer need fail

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 0.11.0-1
- update to 0.11.0
- subpackage fail

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct  5 2016 Jens Petersen <petersen@redhat.com> - 0.10.0-1
- update to 0.10.0
- allow http-types-0.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep  7 2015 Jens Petersen <petersen@redhat.com> - 0.9.0-4
- use license macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Jens Petersen <petersen@fedoraproject.org> - 0.9.0-2
- cblrpm refresh

* Mon Sep 08 2014 Jens Petersen <petersen@redhat.com> - 0.9.0-1
- update to 0.9.0

* Mon Sep 01 2014 Jens Petersen <petersen@redhat.com> - 0.8.2-1
- update to 0.8.2
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  8 2014 Jens Petersen <petersen@redhat.com> - 0.5.0-4
- enable ARM

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 0.5.0-3
- rebuild

* Thu Nov 21 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-2
- Skip ARM for now.

* Mon Nov 18 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.5.0
- spec file generated by cabal-rpm-0.8.6