# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name io-streams
%global pkgver %{pkg_name}-%{version}

# testsuite missing deps: test-framework test-framework-hunit test-framework-quickcheck2

Name:           ghc-%{pkg_name}
Version:        1.5.1.0
Release:        6%{?dist}
Summary:        Simple, composable, easy-to-use stream I/O

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-zlib-bindings-prof
# End cabal-rpm deps

%description
The io-streams library contains simple and easy-to-use primitives for I/O using
streams. Most users will want to import the top-level convenience module
"System.IO.Streams", which re-exports most of the library:

For first-time users, 'io-streams' comes with an included tutorial, which can
be found in the "System.IO.Streams.Tutorial" module.

'io-streams' comes with:
* functions to use files, handles, concurrent channels, sockets, lists,
vectors, and more as streams.
* a variety of combinators for wrapping and transforming streams, including
compression and decompression using zlib, controlling precisely how many bytes
are read from or written to a stream, buffering output using bytestring
builders, folds, maps, filters, zips, etc.
* support for parsing from streams using 'attoparsec'.
* support for spawning processes and communicating with them using streams.


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

cabal-tweak-drop-dep bytestring-builder


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
%doc CONTRIBUTORS README.md changelog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 1.5.1.0-4
- refresh to cabal-rpm-2.0.6

* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 1.5.1.0-3
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.5.1.0-1
- update to 1.5.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.5.0.1-6
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 1.5.0.1-4
- revise .cabal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.5.0.1-1
- update to 1.5.0.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 1.3.6.0-1
- update to 1.3.6.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Jens Petersen <petersen@redhat.com> - 1.3.2.0-1
- update to 1.3.2.0
- patch out bytestring-builder

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 1.2.1.1-1
- update to 1.2.1.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Jens Petersen <petersen@redhat.com> - 1.1.4.5-3
- rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Jens Petersen <petersen@redhat.com> - 1.1.4.5-1
- update to 1.1.4.5 with cblrpm-0.8.11

* Wed May  7 2014 Jens Petersen <petersen@redhat.com> - 1.1.4.3-1
- update to 1.1.4.3

* Tue Feb  4 2014 Jens Petersen <petersen@redhat.com> - 1.1.4.0-1
- edit summary and description

* Tue Feb  4 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.1.4.0
- spec file generated by cabal-rpm-0.8.8
