# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name wreq
%global pkgver %{pkg_name}-%{version}

# testsuite missing deps: test-framework test-framework-hunit test-framework-quickcheck2

Name:           ghc-%{pkg_name}
Version:        0.5.3.2
Release:        5%{?dist}
Summary:        An easy-to-use HTTP client library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-cabal-doctest-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-authenticate-oauth-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptonite-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-lens-aeson-prof
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-mime-types-prof
BuildRequires:  ghc-psqueues-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-time-locale-compat-prof
BuildRequires:  ghc-unordered-containers-prof
# End cabal-rpm deps

%description
A web client library that is designed for ease of use.

Tutorial: <http://www.serpentine.com/wreq/tutorial.html>

Features include:

* Simple but powerful `lens`-based API

* A solid test suite, and built on reliable libraries like http-client and lens

* Session handling includes connection keep-alive and pooling, and cookie
persistence

* Automatic response body decompression

* Powerful multipart form and file upload handling

* Support for JSON requests and responses, including navigation of schema-less
responses

* Basic and OAuth2 bearer authentication

* Early TLS support via the tls package.


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
%license LICENSE.md
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc README.md TODO.md changelog.md examples


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE.md
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.5.3.2-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.5.3.2-1
- update to 0.5.3.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.5.3.1-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.5.3.1-1
- update to 0.5.3.1

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.5.2.1-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.5.2.1-1
- update to 0.5.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.5.2.0-1
- update to 0.5.2.0

* Wed Sep 13 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.5.1.0-1
- spec file generated by cabal-rpm-0.11.2
