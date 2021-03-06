# generated by cabal-rpm-2.0.6 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hledger
%global pkgver %{pkg_name}-%{version}

%global utilityht utility-ht-0.0.15
%global lucid lucid-2.9.12
%global subpkgs %{utilityht} %{lucid}

# testsuite missing deps: timeit

Name:           %{pkg_name}
Version:        1.18.1
# can only be reset when all subpkgs bumped
Release:        22%{?dist}
Summary:        Command-line interface for the hledger accounting system

License:        GPLv3+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{utilityht}/%{utilityht}.tar.gz
Source2:        https://hackage.haskell.org/package/%{lucid}/%{lucid}.tar.gz
Source3:        https://hackage.haskell.org/package/%{pkgver}/%{name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-Decimal-prof
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-compat-batteries-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cmdargs-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-haskeline-prof
BuildRequires:  ghc-hledger-lib-prof
#BuildRequires:  ghc-lucid-prof
BuildRequires:  ghc-math-functions-prof
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-old-time-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-pretty-show-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-shakespeare-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-tabular-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-terminfo-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-timeit-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-utf8-string-prof
#BuildRequires:  ghc-utility-ht-prof
BuildRequires:  ghc-wizards-prof
# for missing dep 'lucid':
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-mmorph-prof
# End cabal-rpm deps

%description
The command-line interface for the hledger accounting system. Its basic
function is to read a plain text file describing financial transactions and
produce useful reports.

hledger is a robust, cross-platform set of tools for tracking money, time, or
any other commodity, using double-entry accounting and a simple, editable file
format, with command-line, terminal and web interfaces. It is a Haskell rewrite
of Ledger, and one of the leading implementations of Plain Text Accounting.
Read more at: <https://hledger.org>.


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch

%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif


%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)

%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage %{utilityht}
%ghc_lib_subpackage %{lucid}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -a1 -a2
cp -bp %{SOURCE3} %{name}.cabal
# End cabal-rpm setup
cabal-tweak-drop-dep mtl-compat


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%ghc_fix_rpath %{pkgver}
# End cabal-rpm install

install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGES.md README.md
%{_bindir}/%{name}
# End cabal-rpm files
%{_mandir}/man1/%{name}.1*


%files -n ghc-%{name} -f ghc-%{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGES.md README.md


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 1.18.1-20
- update to 1.18.1

* Fri Jun 19 2020 Jens Petersen <petersen@redhat.com> - 1.18-19
- update to 1.18

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 1.16.2-18
- https://hackage.haskell.org/package/hledger-1.16.2/changelog

* Tue Feb 25 2020 Jens Petersen <petersen@redhat.com> - 1.14.2-17
- https://hackage.haskell.org/package/hledger-1.14.2/changelog

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.12.1-15
- update to 1.12.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 31 2019 Jens Petersen <petersen@redhat.com> - 1.10-13
- haskell-src-meta and th-* packaged

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 1.10-12
- update to 1.10
- subpackage lucid dep

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Jens Petersen <petersen@redhat.com> - 1.5-10
- rebuild for static executable

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 1.5-9
- update to 1.5
- add main manpage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.4-6
- update to 1.4

* Wed Aug 30 2017 Jens Petersen <petersen@redhat.com> - 1.2-5
- no longer need to subpackage file-embed

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Jens Petersen <petersen@redhat.com> - 1.2-2
- bump release

* Fri May 26 2017 Jens Petersen <petersen@redhat.com> - 1.2-1
- update to 1.2
- add here lib and its deps

* Tue Feb 21 2017 Jens Petersen <petersen@redhat.com> - 1.0.1-1
- update to 1.0.1
- subpackage file-embed

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep  5 2016 Jens Petersen <petersen@redhat.com> - 0.27.1-1
- update to 0.27.1
- build without mtl-compat

* Tue May 24 2016 Ben Boeckel <mathstuf@gmail.com> - 0.24-5
- Rebuild for ghc-cmdargs, ghc-regexpr, ghc-split
- doc -> license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 08 2015 Ben Boeckel <mathstuf@gmail.com> - 0.24-3
- rebuild for ghc-safe and ghc-wizards

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Ben Boeckel <mathstuf@gmail.com> - 0.24-1
- update to 0.24
- cblrpm refresh

* Fri Feb  6 2015 Jens Petersen <petersen@redhat.com> - 0.23.2-1
- update to 0.23.2
- cblrpm refresh
- patch out pretty-show for now
- try re-enabling armv7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Jens Petersen <petersen@redhat.com> - 0.19.3-3
- exclude armv7hl since TemplateHaskell failing to compile (#992478)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Jens Petersen <petersen@redhat.com> - 0.19.3-1
- update to 0.19.3
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 19 2013 Jens Petersen <petersen@redhat.com> - 0.17-5
- allow haskeline-0.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov  9 2012 Jens Petersen <petersen@redhat.com> - 0.17-3
- re-enable dynamic executable
- allow building with cmdargs-0.10 and split-0.2
- update with cabal-rpm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Ben Boeckel <mathstuf@gmail.com> - 0.17-1
- Initial package
