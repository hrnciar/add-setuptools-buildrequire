# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

Name:           pagure-cli
Version:        0.2
Release:        5%{?dist}
Summary:        Pagure client

License:        GPLv2+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-static
BuildRequires:  ghc-base-static
BuildRequires:  ghc-bytestring-static
BuildRequires:  ghc-filepath-static
BuildRequires:  ghc-http-conduit-static
BuildRequires:  ghc-lens-static
BuildRequires:  ghc-lens-aeson-static
BuildRequires:  ghc-optparse-applicative-static
BuildRequires:  ghc-simple-cmd-args-static
BuildRequires:  ghc-text-static
# End cabal-rpm deps

%description
A command-line Pagure client for querying projects and users.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_bin_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_bin_install
# End cabal-rpm install

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/pagure --bash-completion-script pagure > %{buildroot}%{_datadir}/bash-completion/completions/pagure


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/pagure
# End cabal-rpm files
%{_datadir}/bash-completion/completions/pagure


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Jens Petersen <petersen@redhat.com> - 0.2-4
- setup bash completion

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.2-2
- refresh to cabal-rpm-2.0.6

* Mon Apr  6 2020 Jens Petersen <petersen@redhat.com> - 0.2-1
- spec file generated by cabal-rpm-2.0.5
