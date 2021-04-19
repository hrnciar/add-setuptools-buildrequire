# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name cpphs
%global pkgver %{pkg_name}-%{version}

Name:           %{pkg_name}
Version:        1.20.9.1
Release:        3%{?dist}
Summary:        A liberalised C pre-processor for Haskell

License:        GPL+ and LGPLv2+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-polyparse-prof
BuildRequires:  ghc-time-prof
# End cabal-rpm deps

%description
Cpphs is a re-implementation of the C pre-processor that is both more
compatible with Haskell, and itself written in Haskell so that it can be
distributed with compilers.

This version of the C pre-processor is pretty-much feature-complete and
compatible with traditional (K&R) pre-processors. Additional features include:
a plain-text mode; an option to unlit literate code files; and an option to
turn off macro-expansion.


%package -n ghc-%{name}
Summary:        Haskell %{name} library
License:        LGPLv2+

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
License:        LGPLv2+
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


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install

install -D -p -m 0644 docs/cpphs.1 %{buildroot}%{_mandir}/man1/%{name}.1

# main package binary is GPL
rm %{buildroot}%{_defaultlicensedir}/%{name}/LICENCE-LGPL


%files
# Begin cabal-rpm files:
%license LICENCE-GPL
%doc CHANGELOG README
%{_bindir}/%{name}
# End cabal-rpm files
%{_mandir}/man1/%{name}.1*
%doc docs/index.html

%files -n ghc-%{name} -f ghc-%{name}.files
# Begin cabal-rpm files:
%license LICENCE-GPL
%license LICENCE-LGPL
# End cabal-rpm files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGELOG README


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENCE-GPL
%license LICENCE-LGPL
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 1.20.9.1-1
- update to 1.20.9.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 1.20.8-9
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Jens Petersen <petersen@redhat.com> - 1.20.8-7
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Jens Petersen <petersen@redhat.com> - 1.20.8-5
- rebuild for static executable

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 1.20.8-4
- rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.20.8-1
- update to 1.20.8

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 1.20.3-1
- update to 1.20.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Jens Petersen <petersen@redhat.com> - 1.20.1-2
- drop the modified BSD license since it is unmodified binary only
- remove LGPL license file from the base package

* Thu Jun 23 2016 Jens Petersen <petersen@redhat.com> - 1.20.1-1
- update to 1.20.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr  2 2015 Jens Petersen <petersen@redhat.com> - 1.18.9-1
- update to 1.18.9

* Fri Aug 29 2014 Jens Petersen <petersen@redhat.com> - 1.18.2-1
- update to 1.18.2
- refresh to cblrpm-0.8.11
- add alternative BSD license tag: cpphs has been dual licensed for a while

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Jens Petersen <petersen@redhat.com> - 1.16-5
- replace ghc_docdir by _pkgdocdir

* Fri Jul 26 2013 Jens Petersen <petersen@redhat.com> - 1.16-4
- use ghc_docdir to handle F20 unversioned docdir

* Tue Jun 11 2013 Jens Petersen <petersen@redhat.com>
- update to new approved simplified Haskell Packaging Guidelines

* Wed Apr 24 2013 Jens Petersen <petersen@redhat.com> - 1.16-2
- update to revised simplified Haskell Packaging Guidelines (cabal-rpm-0.8)

* Mon Mar 11 2013 Jens Petersen <petersen@redhat.com> - 1.16-1
- update to 1.16

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 1.14-3
- add LICENCE-GPL and manpage
- update with cabal-rpm

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 1.14-1
- update to 1.14
- drop haskell98 BR

* Tue Feb  7 2012 Jens Petersen <petersen@redhat.com> - 1.13.3-1
- update to 1.13.3

* Thu Jan 19 2012 Jens Petersen <petersen@redhat.com> - 1.13.2-3
- update to cabal2spec-0.25.2, fixing anomalous ghc-cpphs requires ghc-compiler

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.13.2-1.1
- rebuild with new gmp without compat lib

* Sat Oct 15 2011 Jens Petersen <petersen@redhat.com> - 1.13.2-1
- update to 1.13.2
- update to cabal2spec-0.24.1
- use ghc_exclude_docdir from ghc-rpm-macros-0.13.12

* Fri Oct 14 2011 Jens Petersen <petersen@redhat.com> - 1.13.1-1
- update to 1.13.1

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 1.12-1.1
- rebuild with new gmp

* Fri Jul 22 2011 Jens Petersen <petersen@redhat.com> - 1.12-1
- update to 1.12
- missing LICENCE-GPL reported upstream

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 1.11-10
- BR ghc-Cabal-devel instead of ghc-prof (cabal2spec-0.23.2)

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.11-9
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jens Petersen <petersen@redhat.com> - 1.11-7
- rebuild

* Sat Jan 15 2011 Jens Petersen <petersen@redhat.com> - 1.11-6
- update to cabal2spec-0.22.4

* Mon Nov 29 2010 Jens Petersen <petersen@redhat.com> - 1.11-5
- update url and drop -o obsoletes

* Sat Sep  4 2010 Jens Petersen <petersen@redhat.com> - 1.11-4
- update to ghc-rpm-macros-0.8.1, hscolour and drop doc pkg (cabal2spec-0.22.2)

* Sat Jun 26 2010 Jens Petersen <petersen@redhat.com> - 1.11-3
- strip dynlinked files (cabal2spec-0.21.4)

* Sat Apr 24 2010 Jens Petersen <petersen@redhat.com> - 1.11-2
- rebuild for ghc-6.12.2

* Mon Feb 15 2010 Conrad Meyer <konrad@tylerc.org> - 1.11-1
- Bump to 1.11

* Mon Jan 11 2010 Jens Petersen <petersen@redhat.com> - 1.9-4
- update to ghc-rpm-macros-0.5.1 and cabal2spec-0.21.1:
- drop doc and prof bcond
- common summary and common_description
- use ghc_binlib_package with license arg

* Wed Dec 23 2009 Jens Petersen <petersen@redhat.com> - 1.9-3
- devel package requires shared library not base

* Tue Dec 22 2009 Jens Petersen <petersen@redhat.com> - 1.9-2
- update spec for ghc-6.12.1
- added shared library support: needs ghc-rpm-macros 0.3.1
- drop -dynamic for now since Cabal chokes with prof looking for p_dyn
- use ghc-cpphs for ghc_gen_filelists

* Fri Sep 18 2009 Jens Petersen <petersen@redhat.com> - 1.9-1
- update to 1.9

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Jens Petersen <petersen@redhat.com> - 1.6-8
- buildrequires ghc-rpm-macros (cabal2spec-0.16)

* Fri Apr 24 2009 Jens Petersen <petersen@redhat.com> - 1.6-7
- update to cabal2spec-0.14

* Mon Mar  2 2009 Jens Petersen <petersen@redhat.com> - 1.6-6
- update to cabal2spec-0.12:
  - add devel subpackage
  - use global
  - update archs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Conrad Meyer <konrad@tylerc.org> - 1.6-4
- update to new template (haskell-packaging 0.4-1)

* Wed Jan 14 2009 Jens Petersen <petersen@redhat.com> - 1.6-3
- simplify summaries
- move lgpl license file to ghc-cpphs
- add html doc

* Tue Jan 13 2009 Jens Petersen <petersen@redhat.com> - 1.6-2
- make this a proper binlib package
- use bcond

* Mon Jan 12 2009 Conrad Meyer <konrad@tylerc.org> - 1.6-1
- initial packaging for Fedora created by cabal2spec