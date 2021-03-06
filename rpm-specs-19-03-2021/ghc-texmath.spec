# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name texmath
%global pkgver %{pkg_name}-%{version}

%ifnarch armv7hl
%bcond_without tests
%endif

Name:           ghc-%{pkg_name}
Version:        0.12.0.2
Release:        4%{?dist}
Summary:        Conversion between formats used to represent mathematics

License:        GPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-xml-prof
%if %{with tests}
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-utf8-string-devel
%endif
# End cabal-rpm deps

%description
The texmath library provides functions to read and write TeX math, presentation
MathML, and OMML (Office Math Markup Language, used in Microsoft Office).
Support is also included for converting math formats to Gnu eqn and to pandoc's
native format (allowing conversion, via pandoc, to a variety of different
markup formats). The TeX reader supports basic LaTeX and AMS extensions, and it
can parse and apply LaTeX macros. (See <http://johnmacfarlane.net/texmath here>
for a live demo of bidirectional conversion between LaTeX and MathML.)


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
%doc README.markdown changelog


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 0.12.0.2-1
- update to 0.12.0.2

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.11.3-1
- update to 0.11.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.11.2.2-1
- update to 0.11.2.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.11.1.2-1
- update to 0.11.1.2

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.10.1.2-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.10.1.2-1
- update to 0.10.1.2

* Tue Jul 24 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.10.1-5
- Enable annotated build again

* Mon Jul 23 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.10.1-4
- Rebuilt for #1607054

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.10.1-1
- update to 0.10.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 0.9.1-1
- update to 0.9.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 27 2016 Jens Petersen <petersen@redhat.com> - 0.8.6.4-1
- update to 0.8.6.4

* Thu Jun 16 2016 Jens Petersen <petersen@redhat.com> - 0.8.4.2-2
- build with network-uri

* Sat Mar 05 2016 Jens Petersen <petersen@redhat.com> - 0.8.4.2-1
- update to 0.8.4.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0.1-4
- Rebuild (aarch64 vector hashes)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Jens Petersen <petersen@redhat.com> - 0.8.0.1-2
- run tests in utf8 on aarch64

* Sun Feb  1 2015 Jens Petersen <petersen@redhat.com> - 0.8.0.1-1
- update to 0.8.0.1
- disable tests on armv7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Jens Petersen <petersen@redhat.com> - 0.6.6.1-1
- update to 0.6.6.1

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 0.6.6-1
- update to 0.6.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.5-2
- update to new simplified Haskell Packaging Guidelines

* Wed Jun 05 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.5-1
- update to 0.6.1.5

* Sun Mar 10 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.3-1
- update to 0.6.1.3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Jens Petersen <petersen@redhat.com> - 0.6.1.1-1
- update to 0.6.1.1
- update summary and description

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.6-2
- change prof BRs to devel

* Wed Jun 13 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.6-1
- update to 0.6.0.6

* Fri Mar 23 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.3-2
- add license to ghc_files

* Sun Feb 12 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.3-1
- update to 0.6.0.3

* Tue Feb  7 2012 Jens Petersen <petersen@redhat.com> - 0.5.0.4-2
- rebuild

* Thu Jan  5 2012 Jens Petersen <petersen@redhat.com> - 0.5.0.4-1
- update to 0.5.0.4 and cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Ma??l????ov?? <mmaslano@redhat.com> - 0.5.0.1-3.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Ma??l????ov?? <mmaslano@redhat.com> - 0.5.0.1-3.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.5.0.1-3.1
- rebuild with new gmp

* Wed Jul 27 2011 Jens Petersen <petersen@redhat.com> - 0.5.0.1-3
- rebuild for xml-1.3.9

* Wed Jun 22 2011 Jens Petersen <petersen@redhat.com> - 0.5.0.1-2
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Sat May 28 2011 Jens Petersen <petersen@redhat.com> - 0.5.0.1-1
- update to 0.5.0.1
- update to cabal2spec-0.23: add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4-6
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 0.4-5
- rebuild for haskell-platform-2011.1 updates

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Jens Petersen <petersen@redhat.com> - 0.4-3
- update to cabal2spec-0.22.4

* Tue Dec 21 2010 Jens Petersen <petersen@redhat.com> - 0.4-2
- need depends on syb for ghc-7.0

* Fri Nov 12 2010 Jens Petersen <petersen@redhat.com> - 0.4-1
- GPLv2+
- add deps and description
- remove unused tests and cgi data files

* Fri Nov 12 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.4-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
