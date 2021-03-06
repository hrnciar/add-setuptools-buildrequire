# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hoauth2
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.14.0
Release:        3%{?dist}
Summary:        Haskell OAuth2 authentication client

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
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-http-conduit-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-uri-bytestring-prof
BuildRequires:  ghc-uri-bytestring-aeson-prof
# End cabal-rpm deps

%description
Haskell OAuth2 authentication client. Tested with the following services:

* AzureAD:
<https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code>

* Google: <https://developers.google.com/accounts/docs/OAuth2WebServer>

* Github: <http://developer.github.com/v3/oauth/>

* Facebook: <http://developers.facebook.com/docs/facebook-login/>

* Fitbit: <http://dev.fitbit.com/docs/oauth2/>

* StackExchange: <https://api.stackexchange.com/docs/authentication>

* DropBox: <https://www.dropbox.com/developers/reference/oauth-guide>

* Weibo: <http://open.weibo.com/wiki/Oauth2>

* Douban: <http://developers.douban.com/wiki/?title=oauth2>.


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
chmod a-x README.md
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
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc README.md example


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Jens Petersen <petersen@redhat.com> - 1.14.0-1
- update to 1.14.0

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 1.11.0-1
- update to 1.11.0

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 1.8.9-1
- update to 1.8.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.8.7-1
- update to 1.8.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Jens Petersen <petersen@redhat.com> - 1.8.4-1
- update to 1.8.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.7.2-1
- spec file generated by cabal-rpm-0.12.4
