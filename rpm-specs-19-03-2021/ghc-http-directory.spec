# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name http-directory
%global pkgver %{pkg_name}-%{version}

# requires network
%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.1.8
Release:        4%{?dist}
Summary:        Http directory listing library

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-html-conduit-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-date-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-xml-conduit-prof
%if %{with tests}
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
Library for listing the files (href's) in an http directory. It can also check
the size, existence, modtime of files, and for url redirects.


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
%doc CHANGELOG.md README.md example


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.1.8-2
- refresh to cabal-rpm-2.0.6

* Thu Mar 12 2020 Jens Petersen <petersen@redhat.com> - 0.1.8-1
- update to 0.1.8

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.1.7-1
- update to 0.1.7

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.1.5-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Jens Petersen <petersen@redhat.com> - 0.1.5-1
- update to 0.1.5

* Fri Jun 14 2019 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.4-1
- spec file generated by cabal-rpm-1.0.0
