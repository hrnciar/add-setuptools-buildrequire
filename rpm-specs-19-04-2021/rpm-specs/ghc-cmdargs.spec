# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name cmdargs
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.10.20
Release:        9%{?dist}
Summary:        Command line argument processing

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-transformers-prof
# End cabal-rpm deps

%description
This library provides an easy way to define command line parsers.


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


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.10.20-7
- refresh to cabal-rpm-2.0.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 0.10.20-5
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.10.20-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.10.20-1
- update to 0.10.20

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.10.19-1
- update to 0.10.19

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.10.14-4
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 30 2016 Jens Petersen <petersen@redhat.com> - 0.10.14-2
- rebuild

* Sat Apr 23 2016 Ben Boeckel <mathstuf@gmail.com> - 0.10.14-1
- update to 0.10.14

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.10.12-3
- rebuild for aarch64 hash issue

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 0.10.12-1
- update to 0.10.12

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Jens Petersen <petersen@redhat.com> - 0.10.3-3
- disable quotation on archs without ghci

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.10.3-1
- update to 0.10.3
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 0.10.2-1
- update to 0.10.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Jens Petersen <petersen@redhat.com> - 0.10-1
- update to 0.10 with cabal-rpm
- disable building testprog in .cabal

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.9.5-2
- change prof BRs to devel

* Sun Jun 10 2012 Jens Petersen <petersen@redhat.com> - 0.9.5-1
- update to 0.9.5
- disable dynamic linking of test program

* Sun Mar 18 2012 Jens Petersen <petersen@redhat.com> - 0.9.3-2
- update to cabal2spec-0.25

* Tue Feb 28 2012 Ben Boeckel <mathstuf@gmail.com> - 0.9.3-1
- Update to 0.9.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Marcela Ma??l????ov?? <mmaslano@redhat.com> - 0.8-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.8-1.1
- rebuild with new gmp

* Mon Oct  3 2011 Jens Petersen <petersen@redhat.com> - 0.8-1
- update to 0.8 and cabal2spec-0.24.1

* Sat Jul 09 2011 Ben Boeckel <mathstuf@gmail.com> - 0.7-4
- Update to cabal2spec-0.24

* Fri Jun 24 2011 Jens Petersen <petersen@redhat.com> - 0.7-3
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Wed May 11 2011 Ben Boeckel <mathstuf@gmail.com> - 0.7-2
- Update to cabal2spec-0.22.7

* Tue May 10 2011 Ben Boeckel <mathstuf@gmail.com> - 0.7-1
- Update to cabal2spec-0.22.6

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.6.8-2
- Enable build on sparcv9

* Thu Feb 17 2011 Ben Boeckel <mathstuf@gmail.com> - 0.6.8-1
- Update to 0.6.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Ben Boeckel <mathstuf@gmail.com> - 0.6.7-1
- Update to 0.6.7

* Sat Jan 15 2011 Ben Boeckel <mathstuf@gmail.com> - 0.6.5-2
- Update to cabal2spec-0.22.4
- Rebuild

* Fri Dec 17 2010 Ben Boeckel <mathstuf@gmail.com> - 0.6.5-1
- Update to 0.6.5

* Fri Dec 03 2010 Ben Boeckel <mathstuf@gmail.com> - 0.6.4-1
- Update to 0.6.4

* Mon Nov 29 2010 Jens Petersen <petersen@redhat.com> - 0.6.3-2
- BR transformers

* Fri Nov 12 2010 Ben Boeckel <mathstuf@gmail.com> - 0.6.3-1
- Update to 0.6.3

* Mon Oct 18 2010 Ben Boeckel <mathstuf@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Sat Sep 18 2010 Ben Boeckel <mathstuf@gmail.com> - 0.6-1
- Update to 0.6

* Thu Sep 16 2010 Ben Boeckel <mathstuf@gmail.com> - 0.5-1
- Update to 0.5

* Sun Sep 05 2010 Ben Boeckel <mathstuf@gmail.com> - 0.4-1
- Update to 0.4

* Wed Sep 01 2010 Ben Boeckel <mathstuf@gmail.com> - 0.2-2
- Don't ship the demo program

* Wed Sep 01 2010 Ben Boeckel <mathstuf@gmail.com> - 0.2-1
- Initial package

* Wed Sep  1 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.2-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
