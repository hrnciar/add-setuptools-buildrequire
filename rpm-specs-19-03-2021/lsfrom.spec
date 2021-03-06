# generated by cabal-rpm-2.0.8
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

# needs installed lsfrom
%bcond_with tests

Name:           lsfrom
Version:        0.1
Release:        1%{?dist}
Summary:        List directory files starting from a specific name

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-static
BuildRequires:  ghc-filepath-static
BuildRequires:  ghc-simple-cmd-static
BuildRequires:  ghc-simple-cmd-args-static
%if %{with tests}
BuildRequires:  ghc-directory-devel
%endif
# End cabal-rpm deps

%description
`lsfrom` lists all files in a directory that start with a particular sequence of
characters and those after it with respect to locale collation. This can be
useful for example for continuing a script on the files in a directory after
a failure.


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


%check
%cabal_test


%files
# Begin cabal-rpm files:
%license LICENSE
%doc ChangeLog.md README.md
%{_bindir}/%{name}
# End cabal-rpm files


%changelog
* Sat Feb 13 2021 Jens Petersen <petersen@redhat.com> - 0.1-1
- spec file generated by cabal-rpm-2.0.8
