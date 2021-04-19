# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name wai
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        3.2.2.1
Release:        7%{?dist}
Summary:        Web Application Interface

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
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-vault-prof
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
%endif
# End cabal-rpm deps

%description
Provides a common protocol for communication between web applications
and web servers.


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
cabal-tweak-drop-dep bytestring-builder


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
%doc ChangeLog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 3.2.2.1-4
- refresh to cabal-rpm-2.0.6

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 3.2.2.1-3
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 3.2.2.1-1
- update to 3.2.2.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 3.2.1.2-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 3.2.1.2-1
- update to 3.2.1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 3.2.1.1-4
- rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 3.2.1.1-1
- update to 3.2.1.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 01 2014 Jens Petersen <petersen@redhat.com> - 3.0.1.1-1
- update to 3.0.1.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Jens Petersen <petersen@redhat.com> - 1.4.1-3
- disable debuginfo explicitly (cblrpm-0.8.11)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Jens Petersen <petersen@redhat.com> - 1.4.1-1
- update to 1.4.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Jens Petersen <petersen@redhat.com> - 1.4.0.1-1
- update to 1.4.0.1
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 1.4.0-1
- update to 1.4.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Jens Petersen <petersen@redhat.com> - 1.3.0.1-1
- update to 1.3.0.1

* Thu Jul 26 2012 Jens Petersen <petersen@redhat.com> - 1.2.0.3-1
- update to 1.2.0.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 1.2.0.2-2
- rebuild

* Wed May 16 2012 Jens Petersen <petersen@redhat.com> - 1.2.0.2-1
- update to 1.2.0.2
- license is now MIT

* Fri Mar 23 2012 Jens Petersen <petersen@redhat.com> - 0.4.3-4
- add license to ghc_files

* Thu Mar  8 2012 Jens Petersen <petersen@redhat.com> - 0.4.3-3
- rebuild

* Sat Mar  3 2012 Jens Petersen <petersen@redhat.com> - 0.4.3-2
- rebuild

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 0.4.3-1
- update to 0.4.3 and cabal2spec-0.25.2

* Sun Oct 30 2011 Jens Petersen <petersen@redhat.com> - 0.4.2-3
- rebuild against newer enumerator

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.4.2-2.1
- rebuild with new gmp without compat lib

* Fri Oct 14 2011 Jens Petersen <petersen@redhat.com> - 0.4.2-2
- rebuild for newer deps

* Tue Sep 27 2011 Jens Petersen <petersen@redhat.com> - 0.4.2-1
- update to 0.4.2

* Thu Sep  8 2011 Jens Petersen <petersen@redhat.com> - 0.4.1-1
- update to 0.4.1 and cabal2spec-0.24.1
- add dependencies

* Sat Jun 25 2011 Ben Boeckel <mathstuf@gmail.com> - 0.4.0-1
- Update to 0.4.0
- Update to cabal2spec-0.23.2

* Tue Mar 08 2011 Ben Boeckel <mathstuf@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Tue Nov 23 2010 Ben Boeckel <mathstuf@gmail.com> - 0.2.2.1-1
- Update to 0.2.2.1

* Sat Oct 30 2010 Ben Boeckel <mathstuf@gmail.com> - 0.2.2-1
- Update to 0.2.2

* Tue Sep 14 2010 Ben Boeckel <mathstuf@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Sat Sep 04 2010 Ben Boeckel <mathstuf@gmail.com> - 0.2.0-1
- Initial package

* Sat Sep  4 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.2.0-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
