# generated by cabal-rpm-2.0.6 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name darcs
%global pkgver %{pkg_name}-%{version}

%global dataordlist data-ordlist-0.4.7.0
%global graphviz graphviz-2999.20.0.4
%global regexapplicative regex-applicative-0.3.3.1
%global regexcompattdfa regex-compat-tdfa-0.95.1.4
%global wlpprinttext wl-pprint-text-1.2.0.1
%global subpkgs %{dataordlist} %{wlpprinttext} %{graphviz} %{regexapplicative} %{regexcompattdfa}

# testsuite missing deps: FindBin test-framework test-framework-hunit test-framework-quickcheck2

Name:           %{pkg_name}
Version:        2.14.4
# can only be reset when all subpkgs bumped
Release:        27%{?dist}
Summary:        A distributed, interactive, smart revision control system

License:        GPLv2+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{dataordlist}/%{dataordlist}.tar.gz
Source2:        https://hackage.haskell.org/package/%{graphviz}/%{graphviz}.tar.gz
Source3:        https://hackage.haskell.org/package/%{regexapplicative}/%{regexapplicative}.tar.gz
Source4:        https://hackage.haskell.org/package/%{regexcompattdfa}/%{regexcompattdfa}.tar.gz
Source5:        https://hackage.haskell.org/package/%{wlpprinttext}/%{wlpprinttext}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-HTTP-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptohash-prof
#BuildRequires:  ghc-data-ordlist-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-fgl-prof
BuildRequires:  ghc-filepath-prof
#BuildRequires:  ghc-graphviz-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-haskeline-prof
BuildRequires:  ghc-html-prof
BuildRequires:  ghc-mmap-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-old-time-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
#BuildRequires:  ghc-regex-applicative-prof
#BuildRequires:  ghc-regex-compat-tdfa-prof
BuildRequires:  ghc-sandi-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tar-prof
BuildRequires:  ghc-terminfo-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-zip-archive-prof
BuildRequires:  ghc-zlib-prof
BuildRequires:  libcurl-devel
# for missing dep 'graphviz':
BuildRequires:  ghc-colour-prof
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-polyparse-prof
BuildRequires:  ghc-temporary-prof
# for missing dep 'regex-compat-tdfa':
BuildRequires:  ghc-regex-base-prof
BuildRequires:  ghc-regex-tdfa-prof
# for missing dep 'wl-pprint-text':
BuildRequires:  ghc-base-compat-prof
# End cabal-rpm deps

BuildRequires:  bash-completion
Obsoletes:      darcs-server < 2.2.1-6
# Fedora 25
Obsoletes:      darcs-common < %{version}-%{release}
Obsoletes:      darcs-static < %{version}-%{release}

%description
Darcs is a distributed, interactive, smart revision control system.
Darcs is easy to learn and efficient to use because it asks you questions
in response to simple commands, giving you choices in your workflow.
You can choose to record one change in a file, while ignoring another.
You can review each patch as you update from upstream.
Originally developed by physicist David Roundy,
darcs is based on a unique algebra of patches.


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

* Please note that hackage does not correctly display the license. It is meant
to be "GPL-2.0-or-later".


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       libcurl-devel%{?_isa}
# End cabal-rpm deps

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
%ghc_lib_subpackage %{dataordlist}
%ghc_lib_subpackage %{graphviz}
%ghc_lib_subpackage %{regexapplicative}
%ghc_lib_subpackage %{regexcompattdfa}
%ghc_lib_subpackage %{wlpprinttext}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -a1 -a2 -a3 -a4 -a5
# End cabal-rpm setup
%ifnarch %{ix86} x86_64 ppc
cabal-tweak-flag threaded False
%endif


%build
# allow dist/build/darcs/darcs to generate manpage
export LD_LIBRARY_PATH=$PWD/dist/build
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

install -Dpm 644 contrib/darcs_completion %{buildroot}%{_datadir}/bash-completion/completions/darcs


%files
# Begin cabal-rpm files:
%license COPYING
%doc CHANGELOG README.md
%{_bindir}/%{name}
# End cabal-rpm files
%doc contrib/_darcs.zsh
%{_datadir}/bash-completion/
%attr(0644,-,-) %{_mandir}/man1/darcs.1*


%files -n ghc-%{name} -f ghc-%{name}.files
# Begin cabal-rpm files:
%license COPYING
# End cabal-rpm files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGELOG README.md


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license COPYING
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 2.14.4-25
- update to 2.14.4

* Thu Feb  6 2020 Jens Petersen <petersen@redhat.com> - 2.14.2-24
- update graphviz to 2999.20.0.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 2.14.2-22
- update to 2.14.2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Jens Petersen <petersen@redhat.com> - 2.14.1-20
- graphviz-2999.20.0.2
- wl-pprint-text-1.2.0.0
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Jens Petersen <petersen@redhat.com> - 2.14.1-18
- rebuild for static executable

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 2.14.1-17
- update to 2.14.1
- fgl is now packaged

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Jens Petersen <petersen@redhat.com> - 2.14.0-15
- update to 2.14.0
- knob dep is gone

* Thu Feb 15 2018 Jens Petersen <petersen@redhat.com> - 2.13.0-14
- remove _isa from BR (#1545171)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 Jens Petersen <petersen@redhat.com> - 2.13.0-12
- update to 2018-01-24 snapshot which builds with ghc-8.2
- update to graphviz-2999.19.0.0
- subpackage new dep knob

* Tue Oct 10 2017 Jens Petersen <petersen@redhat.com> - 2.12.5-11
- rebuild

* Mon Oct  9 2017 Jens Petersen <petersen@redhat.com> - 2.12.5-10
- rebuild

* Fri Sep 15 2017 Jens Petersen <petersen@redhat.com> - 2.12.5-9
- sandi is in Fedora now

* Fri Sep 15 2017 Jens Petersen <petersen@redhat.com> - 2.12.5-8
- update to fgl-5.5.4.0 and sandi-0.4.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 2.12.5-5
- update to 2.12.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  9 2017 Jens Petersen <petersen@redhat.com> - 2.12.2-3
- build subpackages in main package dir

* Thu Oct 13 2016 Jens Petersen <petersen@redhat.com> - 2.12.2-2
- set LD_LIBRARY_PATH to allow darcs to output the manpage (#1383608)

* Thu Sep  8 2016 Jens Petersen <petersen@redhat.com> - 2.12.2-1
- update to 2.12.2
- subpackage new deps: data-ordlist, graphviz, regex-applicative,
  regex-compat-tdfa, sandi, wl-pprint-text
- drop static and common package
- html manual is gone

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Ben Boeckel <mathstuf@gmail.com> - 2.8.5-4
- rebuild for ghc-tar bump

* Mon Jun 15 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.8.5-3
- Install bash completion to where bash-completion.pc says
- Mark COPYING as %%license where available

* Mon Apr  6 2015 Jens Petersen <petersen@redhat.com> - 2.8.5-2
- do not own bash_completion.d/ (#1192805)

* Thu Dec 11 2014 Jens Petersen <petersen@redhat.com> - 2.8.5-1
- update to 2.8.5
- add alternative static and common subpackages
- disable html docs on armv7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 2.8.4-4
- f21 rebuild
- build html manual

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Jens Petersen <petersen@redhat.com> - 2.8.4-2
- update to new simplified Haskell Packaging Guidelines
- reenable haddock docs

* Tue Mar 19 2013 Jens Petersen <petersen@redhat.com> - 2.8.4-1
- update to 2.8.4
- libcurl-devel no longer provides curl-devel
- disable haddock since it fails with ghc-7.4.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 06 2012 Jens Petersen <petersen@redhat.com> - 2.8.3-1
- update to 2.8.3
- refresh description
- patch flags and turn on terminfo
- disable threaded on tier 2 archs
- rip out old conditional running of tests
- patch to build with tar-0.4

* Tue Sep 18 2012 Jens Petersen <petersen@redhat.com> - 2.8.2-2
- make the manpage world readable (#857999)

* Wed Sep  5 2012 Jens Petersen <petersen@redhat.com> - 2.8.2-1
- update to minor 2.8.2 release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 2.8.1-3
- change prof BRs to devel

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 2.8.1-2
- rebuild

* Thu May 24 2012 Jens Petersen <petersen@redhat.com> - 2.8.1-1
- update to 2.8.1

* Mon May  7 2012 Jens Petersen <petersen@redhat.com> - 2.8.0-2
- needs ghci to build

* Wed Apr 25 2012 Jens Petersen <petersen@redhat.com> - 2.8.0-1
- update to 2.8.0 final release

* Tue Apr 10 2012 Jens Petersen <petersen@redhat.com> - 2.7.99.2-2
- condition ghc-7.4 base44 flag for fedora 18 or later

* Mon Apr  9 2012 Jens Petersen <petersen@redhat.com> - 2.7.99.2-1
- update to 2.8 rc2

* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 2.7.98.3-3
- set base44 flag to build with ghc-7.4

* Fri Jan 20 2012 Jens Petersen <petersen@redhat.com> - 2.7.98.3-2
- turn on tests
- add obsoletes for darcs-beta

* Fri Jan 20 2012 Jens Petersen <petersen@redhat.com> - 2.7.98.3-1
- update to 2.7.98.3 beta release:
  see http://wiki.darcs.net/changes%20since%202.5
- new dependency on vector library

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 2.5.2-8
- update to cabal2spec-0.25.2
- drop Cabal-1.8 workaround for manpage permission issue
- patch .cabal for regex-compat-0.95.1 in haskell-platform-2011.4

* Tue Oct 25 2011 Jens Petersen <petersen@redhat.com> - 2.5.2-7.2
- minor package cleanup closer to cabal2spec-0.24.1

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.5.2-7.1
- rebuild with new gmp without compat lib

* Fri Oct 14 2011 Jens Petersen <petersen@redhat.com> - 2.5.2-7
- rebuild for newer hashed-storage

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 2.5.2-6.1
- rebuild with new gmp

* Wed Aug 17 2011 Jens Petersen <petersen@redhat.com> - 2.5.2-6
- rebuild for updated dataenc, terminfo, hashed-storage, and haskeline

* Wed Aug 10 2011 Jens Petersen <petersen@redhat.com> - 2.5.2-5
- rebuild for terminfo-0.3.2

* Thu Jun 23 2011 Jens Petersen <petersen@redhat.com> - 2.5.2-4
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)
- BR haskell98 for Setup

* Wed Jun  1 2011 Jens Petersen <petersen@redhat.com> - 2.5.2-3
- update to cabal2spec-0.23

* Fri May  6 2011 Jens Petersen <petersen@redhat.com> - 2.5.2-2
- rebuild for updates to hashed-storage and haskeline
- cabal2spec-0.22.6

* Mon Mar 14 2011 Jens Petersen <petersen@redhat.com> - 2.5.2-1
- update to 2.5.2

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.5.1-3
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 2.5.1-2
- rebuild for dep updates

* Sat Feb 12 2011 Jens Petersen <petersen@redhat.com> - 2.5.1-1
- update to 2.5.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jens Petersen <petersen@redhat.com> - 2.5-6
- rebuild for dynamic executable

* Wed Jan 19 2011 Jens Petersen <petersen@redhat.com> - 2.5-5
- update to cabal2spec-0.22.4

* Sun Dec  5 2010 Jens Petersen <petersen@redhat.com> - 2.5-4
- rebuild against HP 2011.1 alpha
- bump parsec

* Fri Nov 26 2010 Jens Petersen <petersen@redhat.com> - 2.5-3
- add darcs-2.5-ShellHarness-ghc70.patch for abstract directory Permissions
- add darcs-2.5-ghc7-deps.patch to bump dep versions
- add darcs-2.5-ghc7.patch for ghc-7.0.1 (thanks Ganesh Sittampalam)
- disabled tests for now with bcond
- drop -o obsoletes

* Wed Nov 17 2010 Jens Petersen <petersen@redhat.com> - 2.5-2
- rebuild for haskeline-0.6.3.2

* Mon Nov  1 2010 Jens Petersen <petersen@redhat.com> - 2.5-1
- update to 2.5 release

* Tue Oct 26 2010 Jens Petersen <petersen@redhat.com> - 2.4.99.1-1
- update to 2.4.99.1

* Wed Sep 29 2010 jkeating - 2.4.98.5-3
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Jens Petersen <petersen@redhat.com> - 2.4.98.5-2
- rebuild for newer haskeline with terminfo

* Fri Sep 17 2010 Jens Petersen <petersen@redhat.com> - 2.4.98.5-1
- 2.5 beta 5 (darcs-beta)
- new deps on tar and text

* Thu Aug 19 2010 Jens Petersen <petersen@redhat.com> - 2.4.4-4
- rebuild for newer haskeline and dataenc
- make it easier to build darcs-beta

* Mon Jul 19 2010 Jens Petersen <petersen@redhat.com> - 2.4.4-3
- rebuild for newer regex-compat from haskell-platform-2010.2.0.0
- update to cabal2spec-0.22.1:
  - bcond for hscolour
  - add doc obsoletes version

* Sun Jun 27 2010 Jens Petersen <petersen@redhat.com> - 2.4.4-2
- sync cabal2spec-0.22.1

* Thu Jun  3 2010 Jens Petersen <petersen@redhat.com> - 2.4.4-1
- update to 2.4.4

* Tue May 18 2010 Jens Petersen <petersen@redhat.com> - 2.4.3-1
- update to 2.4.3

* Thu Apr 29 2010 Jens Petersen <petersen@redhat.com> - 2.4.1-2
- rebuild against ghc-6.12.2

* Wed Apr 14 2010 Jens Petersen <petersen@redhat.com> - 2.4.1-1
- update to 2.4.1 bugfix release
- darcs-2.4-issue458.sh-attr.patch was upstreamed

* Fri Mar  5 2010 Jens Petersen <petersen@redhat.com> - 2.4-3
- make manpage attr 0644 to workaround Cabal bug (#570110)

* Fri Mar  5 2010 Jens Petersen <petersen@redhat.com> - 2.4-2
- obsolete darcs-server

* Mon Mar  1 2010 Jens Petersen <petersen@redhat.com> - 2.4-1
- new major upstream version 2.4
- darcs is now officially a cabal binlib package
- package with ghc-rpm-macros
- no longer BR autoconf, sendmail, ncurses-devel, zlib-devel
- add haskell deps: hashed-storage, haskeline, html, parsec, regex-compat, zlib
- server (subpackage) is gone
- add darcs-2.4-issue458.sh-attr.patch to workaround selinux output
- run check tests again
- replace AUTHORS with NEWS
- zsh completion filename changed

* Sun Sep 13 2009 Jens Petersen <petersen@redhat.com> - 2.2.1-5
- rebuild against ghc-6.10.4 which should fix --help hangs
- improve doc summary (#522899)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  2 2009 Jens Petersen <petersen@redhat.com> - 2.2.1-3
- drop post script since semanage now superfluous
- drop the unused alphatag for now
- simplify BRs

* Sat Apr 25 2009 Jens Petersen <petersen@redhat.com> - 2.2.1-2
- rebuild against ghc-6.10.3

* Tue Feb 24 2009 Jens Petersen <petersen@redhat.com> - 2.2.1-1
- update to 2.2.1
- own bash_completion.d (#487012)
- use ix86
- ChangeLog no longer included

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Jens Petersen <petersen@redhat.com> - 2.2.0-1
- update to 2.2.0
- update install targets

* Wed Dec 10 2008 Jens Petersen <petersen@redhat.com> - 2.1.2-1
- update to 2.1.2

* Tue Nov 11 2008 Jens Petersen <petersen@redhat.com> - 2.1.1-0.1.rc2
- update to 2.1.1rc2 which builds with ghc-6.10.1
- try to run all tests again

* Mon Sep 22 2008 Jens Petersen <petersen@redhat.com> - 2.0.2-3
- revert last change and require policycoreutils for post (mtasaka, #462221)

* Fri Sep 19 2008 Jens Petersen <petersen@redhat.com> - 2.0.2-2
- use full paths to selinux tools in %%post (Jon Stanley, #462221)

* Sat Jun 28 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 2.0.2-1
- split out the manual to a -doc rpm
- update to 2.0.2
- switch to make test
- remove skipping of tests - it doesn't appear to apply anymore

* Mon Jun 23 2008 Jens Petersen <petersen@redhat.com> - 2.0.0-1.fc10
- update to 2.0.0
- no longer require darcs-ghc-6_8-compat.patch and darcs-error_xml-missing.patch
- move utf-8 conversion to prep
- disable check for now
- manual is now doc and shell completion config lives in tools
- install bash completion

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.9-11
- Autorebuild for GCC 4.3

* Sun Jan 06 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.0.9-10
- add darcs and libxslt to darcs-server dependencies (#427489)
- add patch to fix missing install errors.xml (#427490)

* Fri Nov 30 2007 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.0.9-9
- add BuildRequires autoconf and use of autoconf in %%build to utilize
  the ghc 6.8 compatibility patches

* Thu Nov 29 2007 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.0.9-8
- add patches from darcs unstable branch to deal with ghc 6.8
  compatibility for rawhide

* Sun Nov 25 2007 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.0.9-7
- added alpha to ExcludeArch (#396501)
- cleanup rpmlint warnings
  - convert ISO-8859 text files to UTF-8
  - added %%doc files to -server subpackage
  - fixed quoting of %%macros in changelog comments

* Fri Sep 21 2007 Jens Petersen <petersen@redhat.com> - 1.0.9-6
- fix the "|| :" quoting in the post install script (#295351)

* Thu Sep 20 2007 Jens Petersen <petersen@redhat.com> - 1.0.9-5
- set selinux file-context for %%{_bindir}/darcs
  (reported by Jim Radford, #295351)

* Fri Aug 10 2007 Jens Petersen <petersen@redhat.com> - 1.0.9-4
- specify license is GPL 2 or later

* Wed Jun 27 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.0.9-3
- clean rpmlint warnings/errors
  - move PreReq to Requires(post)
  - move make check to 'check' section
  - mark config files as such

* Wed Jun 27 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.0.9-2
- added ExcludeArch: ppc64

* Wed Jun 27 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.0.9-1
- update to 1.0.9

* Mon Feb 19 2007 Jens Petersen <petersen@redhat.com> - 1.0.9-0.1.rc2
- update to 1.0.9rc2 which builds with ghc66

* Fri Feb  2 2007 Jens Petersen <petersen@redhat.com> - 1.0.8-5
- rebuild for ncurses replacing termcap (#226754)

* Wed Nov  1 2006 Jens Petersen <petersen@redhat.com> - 1.0.8-4
- rebuild for new libcurl

* Thu Sep 28 2006 Jens Petersen <petersen@redhat.com> - 1.0.8-3
- rebuild for FC6
- enable make check

* Fri Jun 23 2006 Jens Petersen <petersen@redhat.com> - 1.0.8-2
- set unconfined_execmem_exec_t context to allow running under selinux targeted
  policy (#195820)

* Wed Jun 21 2006 Jens Petersen <petersen@redhat.com> - 1.0.8-1
- update to 1.0.8

* Sun May 14 2006 Jens Petersen <petersen@redhat.com> - 1.0.7-1
- update to 1.0.7
- fix typo of propagate in description (#189651)
- disable "make check" for now since it blows up in buildsystem

* Thu Mar  2 2006 Jens Petersen <petersen@redhat.com> - 1.0.6-1
- update to 1.0.6
  - darcs-createrepo is gone

* Thu Dec  8 2005 Jens Petersen <petersen@redhat.com> - 1.0.5-1
- 1.0.5 bugfix release

* Mon Nov 14 2005 Jens Petersen <petersen@redhat.com> - 1.0.4-1
- 1.0.4 release
  - skip tests/send.sh for now since it is failing in buildsystem

* Tue Jul  5 2005 Jens Petersen <petersen@redhat.com>
- drop superfluous doc buildrequires (Karanbir Singh, #162436)

* Fri Jul  1 2005 Jens Petersen <petersen@redhat.com> - 1.0.3-2
- fix buildrequires
  - add sendmail, curl-devel, ncurses-devel, zlib-devel, and
    tetex-latex, tetex-dvips, latex2html for doc generation

* Tue May 31 2005 Jens Petersen <petersen@redhat.com> - 1.0.3-1
- initial import into Fedora Extras
- 1.0.3 release
- include bash completion file in doc dir

* Sun May  8 2005 Jens Petersen <petersen@haskell.org> - 1.0.3-0.rc1.1
- 1.0.3rc1
  - build with ghc-6.4

* Tue Feb  8 2005 Jens Petersen <petersen@haskell.org> - 1.0.2-1
- update to 1.0.2

* Thu Jul 15 2004 Jens Petersen <petersen@haskell.org> - 0.9.22-1
- 0.9.22
- darcs-0.9.21-css-symlinks.patch no longer needed

* Thu Jun 24 2004 Jens Petersen <petersen@haskell.org> - 0.9.21-1
- update to 0.9.21
- replace darcs-0.9.13-mk-include.patch with darcs-0.9.21-css-symlinks.patch

* Wed Nov  5 2003 Jens Petersen <petersen@haskell.org>
- Initial packaging.
