# generated by cabal-rpm-2.0.6 --stream hackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%bcond_without manpage

Name:           cabal-rpm
Version:        2.0.8
Release:        1%{?dist}
Summary:        RPM packaging tool for Haskell Cabal-based packages

License:        GPLv3+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources
Source1:        cblrpm.1
# tweaked to add cblrpm
Source2:        bash_completion

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-static
BuildRequires:  ghc-base-static
BuildRequires:  ghc-bytestring-static
BuildRequires:  ghc-directory-static
BuildRequires:  ghc-extra-static
BuildRequires:  ghc-filepath-static
BuildRequires:  ghc-http-client-static
BuildRequires:  ghc-http-client-tls-static
BuildRequires:  ghc-http-conduit-static
BuildRequires:  ghc-optparse-applicative-static
BuildRequires:  ghc-process-static
BuildRequires:  ghc-simple-cabal-static
BuildRequires:  ghc-simple-cmd-static
BuildRequires:  ghc-simple-cmd-args-static
BuildRequires:  ghc-time-static
BuildRequires:  ghc-unix-static
# End cabal-rpm deps
%if %{with manpage}
BuildRequires:  pandoc
%endif
Obsoletes:      cabal2spec < 0.26
Provides:       cblrpm = %{version}-%{release}
Requires:       cabal-install
Requires:       ghc-rpm-macros
Requires:       rpm-build
# for repoquery
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       dnf-plugins-core
%else
Requires:       yum-utils
%endif
# for rpmdev-bumpspec
Requires:       rpmdevtools
Requires:       wget

%description
This package provides a RPM packaging tool for Haskell Cabal-based packages.

cabal-rpm has commands to generate a RPM spec file and srpm for a package.
It can rpmbuild packages, yum/dnf install their dependencies, prep packages,
and install them. There are commands to list package dependencies and missing
dependencies. The diff command compares the current spec file with a freshly
generated one, the update command updates the spec file to latest version from
Stackage or Hackage, and the refresh command updates the spec file to the
current cabal-rpm packaging. It also handles Hackage revisions of packages.
Standalone packages can also be made, built with cabal-install.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_bin_build
# End cabal-rpm build
%if %{with manpage}
pandoc -s -t man man/cabal-rpm.1.md > man/cabal-rpm.1
%endif


%install
# Begin cabal-rpm install
%ghc_bin_install
# End cabal-rpm install

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -p -m 0644 -D %{SOURCE2} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
ln -s %{name} %{buildroot}%{_datadir}/bash-completion/completions/cblrpm

%if %{with manpage}
install -p -m 0644 -D man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -p -m 0644 %SOURCE1 %{buildroot}%{_mandir}/man1/
%endif

ln -s %{name} %{buildroot}%{_bindir}/cblrpm


%files
# Begin cabal-rpm files:
%license COPYING
%doc ChangeLog README.md TODO
%{_bindir}/%{name}
# End cabal-rpm files
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*
%{_bindir}/cblrpm
%{_datadir}/bash-completion/completions/cblrpm
%{_mandir}/man1/cblrpm.1*


%changelog
* Sat Mar 27 2021 Jens Petersen <petersen@redhat.com> - 2.0.8-1
- update: make sure krb ticket exists before uploading source
- spec: executable doc files now handled by ghc-rpm-macros
- move dos2unix for revised DOS .cabal from download to spec build time
- spec: do not enable testsuite for standalone package
- spec: also bash-completion for simple-cmd-args
- spec: for bash-completions use default not filenames
- Stackage: use lts-17
- pkgInstallMissing: also install ghc-rpm-macros

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct  7 13:49:30 +08 2020 Jens Petersen <petersen@redhat.com> - 2.0.7-1
- update to 2.0.7

* Thu Aug 13 2020 Jens Petersen <petersen@redhat.com> - 2.0.6-4
- also bash completion for cblrpm alias

* Mon Aug 10 2020 Jens Petersen <petersen@redhat.com> - 2.0.6-3
- setup bash completion

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 2.0.6-1
- spec: use packager's name in %%changelog
- spec: default package versions to Stackage LTS 16
- spec now also leaves newly prepped source tree around
- spec: handle testsuite tool deps separately
- spec,refresh,update: more care about whether to revise or not
- diff: ignore release field
- prep: be quiet
- spec: add a comment for missing testsuite deps
- only allow specifying major Stackage LTS versions (not minor):
  for more progressive updating logic (lts-n -> lts-(n+1) -> nightly -> Hackage)
- spec: take specified stream into account for subpackaging
- update: finally run prep to check update okay
- prep/srpm --verbose and local --quiet options
- spec: move chmod for docs to %%prep
- spec: check existing .spec file for detecting dropped deps and executable deps
- update: also commit revised .cabal file when no update
- fix copying of cached tarballs (longstanding defect)

* Fri Jun 19 2020 Jens Petersen <petersen@redhat.com> - 2.0.5.1-1
- refresh and update now leave newly prepped source tree around
- spec: dropped deprecated %%post and %%postun scriptlets

* Thu Feb 27 2020 Jens Petersen <petersen@redhat.com> - 2.0.4-1
- drop %%_devel compat macro
- default stream is now lts-14
- spec: detect local revised .cabal file
- sort deps of subpackages
- metapkgs don't have prof or doc
- fix generation of subpackages for a new package
- update: logic reworked to reduce redundant downloads
- quote macros in commented fields
- read --subpackage from spec header
- generate BRs for subpackages

* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 2.0.0-3
- drop %%_devel compat macro
- default stream is now lts-14
- sort deps of subpackages
- metapkgs don't have prof or doc
- fix generation of subpackages for a new package
- update: logic reworked to reduce redundant downloads

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Jens Petersen <petersen@redhat.com> - 2.0.0-1
- update to 2.0.0:
- major refactor to handle stream/pkgid more precisely and correctly
  (hence major version bump due to behavior changes)
  - eg can no longer specify both stream and pkg-ver
- check for package first in default LTS, then latest LTS, and Nightly,
  before Hackage
- respect and read/write --standalone and --stream in spec header consistently
  (note default LTS stream is not written to header)
- fix infinite loop for 'install'

* Tue Dec 31 2019 Jens Petersen <petersen@redhat.com> - 1.0.3-1
- update to 1.0.3
- define _devel for f30 packaging compatibility
- missingdeps and builddep fixes
- --standalone: adds BRs for deps of missing deps

* Mon Dec 09 2019 Jens Petersen <petersen@redhat.com> - 1.0.2-1
- minor bugfixes
- https://hackage.haskell.org/package/cabal-rpm-1.0.2/changelog

* Tue Oct 01 2019 Jens Petersen <petersen@redhat.com> - 1.0.1-1
- doc and prof subpackages for libraries
- reworked to use optparse-applicative (simple-cmd-args)
- default to Stackage LTS 13
- F31+ uses triggers for ghc-pkg recache
- wait 10^4s (< 3 hours) between cabal update's
- refactor using simple-cabal, PackageName and LibPkgType
- handle setup-depends
- diff: autodetect subpackaging
- https://hackage.haskell.org/package/cabal-rpm-1.0.1/changelog

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 0.13.3-3
- generate manpage (#1725973)
- fix build with simple-cmd 0.2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 fedora-toolbox <petersen@redhat.com> - 0.13.3-1
- repoquery for missing deps' package .conf file to avoid modular ghc conflicts
- only --assumeyes for dnf install when not tty
- use tmpdir for tmp spec files and building missing deps
- give up if more than one spec file
- fix handling unversioned update
- map cabal build-tool to cabal-install

* Mon May 06 2019 Jens Petersen <petersen@redhat.com> - 0.13.2-1
- update to 0.13.2:
- include ANNOUNCE in docs
- if dependency parallel directory exists, don't check if installed
- fix buildDepends on Cabal-2.4
- new --standalone option for private packages built with cabal-install
- print --{missing,standalone,subpackage} options on spec file header line

* Mon Mar 18 2019 Jens Petersen <petersen@redhat.com> - 0.13.1-1
- update: fix rw git dir detection
- fix tarball downloading and copying of revised .cabal file
- show output (errors) when prepping source and prep in working dir
- include BUGS and CONTRIBUTING as docs
- need chrpath for subpackaging
- move license dir to any common subpackage

* Tue Feb 19 2019 Jens Petersen <petersen@redhat.com> - 0.13-1
- improve license and doc filtering
- backup revised .cabal files
- fallback to spectool for source downloading
- drop selfdep
- common subpackage for binlib data files
- section dividers for sources, setup, build, install, and files
- only run "cabal update" if more than 10min old

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 20 2018 Jens Petersen <petersen@redhat.com> - 0.12.6-1
- update: remove old revised .cabal
- convert revised .cabal file to unix format (using dos2unix)
- spec: support haskell-gi libraries
- most of SysCmd moved to simple-cmd library (new dep)
- can now download multiple source files
- use line-buffering for stdout
- always do cabal update
- support ghc_without_dynamic for static executables

* Tue Sep 25 2018 Jens Petersen <petersen@redhat.com> - 0.12.5-3
- Require dos2unix for converting .cabal files to unix text format

* Mon Jul 30 2018 Jens Petersen <petersen@redhat.com> - 0.12.5-2
- patch default tracked stream to lts-11

* Sun Jul 29 2018 Jens Petersen <petersen@redhat.com> - 0.12.5-1
- improvements to update and refresh
- improved revising of .cabal files
- use "fedpkg sources" to fetch current Fedora sources
- do not put doc* in docs
- better output for missing sub-deps

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Jens Petersen <petersen@redhat.com> - 0.12.4-2
- requires wget

* Thu May 31 2018 Jens Petersen <petersen@redhat.com> - 0.12.4-1
- now uses Hackage revisions of packages
- spec --stream STREAM replaces --hackage

* Tue May 15 2018 Jens Petersen <petersen@redhat.com> - 0.12.3-1
- build: remove erroneous tarball check
- refresh: use cblrpm for old cabal-rpm

* Thu Mar 29 2018 Jens Petersen <petersen@redhat.com> - 0.12.2-1
- diff: now supports CBLRPM_DIFF envvar to override "diff -u"
- build: attempt when missing rpms deps not available

* Wed Feb 21 2018 Jens Petersen <petersen@redhat.com> - 0.12.1-4
- fix build on epel7 ghc

* Wed Feb 21 2018 Jens Petersen <petersen@redhat.com> - 0.12.1-3
- add bcond for https

* Wed Feb 21 2018 Jens Petersen <petersen@redhat.com> - 0.12.1-2
- escape macro in previous changelog

* Tue Feb 20 2018 Jens Petersen <petersen@fedoraproject.org> - 0.12.1-1
- new option --missing: comments out missing dependencies
- put license files in lib subpackage
- no longer append %%_isa to C BuildRequires (#54)
- no longer leave leftover tmpdirs (#26)
- change 'cblrpm' to 'cabal-rpm' in documentation

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.12-2
- rebuild

* Fri Nov 17 2017 Jens Petersen <petersen@redhat.com> - 0.12-1
- query stackage.org directly via https
- run cabal update before cabal commands
- devel packages now provide doc subpackage for forward compatibility
- new --hackage option to get package version from Hackage not Stackage
- do not add .cabal files containing "doc" to docs
- silence mock rpmbuild -bs warnings about undefined %%ghc_version

* Mon Jul 31 2017 Jens Petersen <petersen@redhat.com> - 0.11.2-1
- fix cblrpm update --subpackage
- fix rpm installation when no sudo
- fix handling of no exposed modules
- fix license handling for selfdep binlib

* Mon Mar 13 2017 Jens Petersen <petersen@redhat.com> - 0.11.1-1
- update to 0.11.1 release:
- support for building meta (compat) lib packages
- fix invocation of optional stackage-query for updating to LTS
- preliminary --subpackage support for subpkgs of missing deps:
  including downloading, but update is not properly implemented yet
- new pkgver macro
- update do not reset release for subpkgs

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.11-3
- refresh packaging to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jens Petersen <petersen@redhat.com> - 0.11-1
- diff and update now follow package-version args
- update from Hackage now follows "Default available version"
- update tries to use stackage-query if installed to check latest Stackage
  version before falling back to latest Hackage
- refresh command now reads the cabal-rpm version header in the spec file and
  installs that version of cabal-rpm under ~/.cblrpm/ and uses it to make patch

* Tue Dec  6 2016 Jens Petersen <petersen@redhat.com> - 0.10.1-2
- quote dist macro in old changelog entry

* Tue Nov 29 2016 Jens Petersen <petersen@redhat.com> - 0.10.1-1
- update to 0.10.1:
- no longer need to remove License files from docdir
- use new ghc_fix_rpath macro
- include Contributors in docs

* Wed Jul 27 2016 Jens Petersen <petersen@redhat.com> - 0.10.0-1
- update to 0.10.0:
- add cabal-rpm version header line to spec files
- warn if unresolved clibs
- update command displays diff
- use cabal_test
- no longer duplicate docs in datadir and package datadir better

* Fri May  6 2016 Jens Petersen <petersen@redhat.com> - 0.9.11-1
- update to 0.9.11

* Thu Mar 24 2016 Jens Petersen <petersen@redhat.com> - 0.9.10-1
- update no longer tries to grep non-existent .git
- fix duplicate clibs
- tweaks for ghc-8.0 and suse

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct  8 2015 Jens Petersen <petersen@redhat.com> - 0.9.8-1
- improve license logic
- fix handling of versions without '.'
- no duplicate test deps

* Fri Aug 28 2015 Jens Petersen <petersen@redhat.com> - 0.9.7-1
- only list buildable executables in spec file
- bring back 'build' as an alias for 'local'
- use license macro
- do not warn about missing optional system programs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Jens Petersen <petersen@redhat.com> - 0.9.6-1
- make "cabal list" quiet
- filter missing packages from repoquery

* Mon Apr 20 2015 Jens Petersen <petersen@fedoraproject.org> - 0.9.5-1
- fix for dnf repoquery
- create SOURCES/ for tarball
- fixes for Cabal-1.22
- nogpgcheck for Fedora 22+
- warn about hidden backup spec files

* Tue Feb 24 2015 Jens Petersen <petersen@redhat.com> - 0.9.4-2
- require dnf-plugins-core instead of yum-utils for F22+

* Tue Feb 17 2015 Jens Petersen <petersen@fedoraproject.org> - 0.9.4-1
- use dnf if installed instead of yum for install and repoquery (#1156553)
- update now only commits changes and adds new source if git origin is ssh
- cblrpm update needs rpmdevtools

* Thu Feb  5 2015 Jens Petersen <petersen@redhat.com> - 0.9.3-2
- remove %%'s from previous changelog

* Thu Feb  5 2015 Jens Petersen <petersen@redhat.com> - 0.9.3-1
- make sure tarball destdir exists before copying
- update improvements: new-sources first, continue if patch fails, git commit changes
- sort executables and use pkg_name in ghc_fix_dynamic_rpath
- drop the debuginfo handling for C files
- ignore emacs temp ".#pkgname.spec" files
- improve output for listing missing packages

* Tue Feb  3 2015 Jens Petersen <petersen@redhat.com> - 0.9.2-2
- remove the old cblrpm-diff script

* Thu Dec 18 2014 Jens Petersen <petersen@redhat.com> - 0.9.2-1
- lots of bug fixes
- new "update" command to update spec to latest version
- improved missingdeps output
- use https for hackage URLs (codeblock)
- no longer override _sourcedir, _rpmdir, and _srcrpmdir macros, unless git dir
- use 'rpm --eval "%%{?dist}"' to determine OS type
- use TMPDIR

* Tue Aug 26 2014 Jens Petersen <petersen@redhat.com> - 0.9.1-1
- missingdeps now lists missing dependencies recursively
- do not assume package order when testing if dependencies installed
- check ~/.cabal/packages/ exists before looking for tarballs
- pass actual executable names to ghc_fix_dynamic_rpath

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Jens Petersen <petersen@redhat.com> - 0.9-1
- setup logic completely reworked to make better use of existing spec file
  and prep source tree for version properly
- default to Library packaging instead of BinLib:
  override with --binary which replaces --library
- 'install' command now does local recursive rpmbuilding
- try "rpm -qf" and then rpmquery to resolve clib devel depends
- support packaging on RHEL5
- improved output for 'depends' command
- use current dir name as a last guess of package name
- refactoring and improvements including no duplicate clibs deps

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Jens Petersen <petersen@redhat.com> - 0.8.11-1
- use .spec file to determine pkg-ver when no .cabal file around
- build command renamed again from "rpm" to "local" (like fedpkg)
- automatically generate bcond for %%check and add testsuite BRs
  when testsuites available
- disable debuginfo explicitly when no c-sources in preparation for
  ghc-rpm-macros no longer disabling debuginfo
- reset filemode of downloaded hackage tarballs to 0644:
  workaround for cabal-install setting 0600
- include release again in initial changelog

* Mon Mar  3 2014 Jens Petersen <petersen@redhat.com> - 0.8.10-1
- new diff command replaces cblrpm-diff script
- new missingdeps command
- should now work on RHEL 5 and 6: dropped use use of rpmspec
- add a temporary cblrpm-diff compat script
- refresh description

* Mon Feb 10 2014 Jens Petersen <petersen@redhat.com> - 0.8.9-1
- bugfix for error handling dir with spec file
- cblrpm-diff arg is now optional

* Sun Feb  9 2014 Jens Petersen <petersen@redhat.com> - 0.8.8-1
- use .spec file to determine package if no .cabal file (with or without arg)
- bugfix: install command now works if some dependencies not packaged
- bugfix: do not re-copy cached tarball each time
- use new shorter hackage2 URL for packages
- filter @ and \ quotes in descriptions
- capitalize start of summary and description
- new prep command (like "rpmbuild -bp" or "fedpkg prep")
- new depends and requires commands list package depends or buildrequires
- new builddep command (like yum-buildep, but allows missing packages)

* Tue Dec 31 2013 Jens Petersen <petersen@redhat.com> - 0.8.7-1
- new "install" command wrapping "cabal install"
- "build" command renamed to "rpm"
- sort devel Requires
- cblrpm-diff: allow package arg
- support copying tarball fetched from another remote-repo (codeblock)
- support AGPL license in Cabal-1.18
- update package description

* Tue Oct  8 2013 Jens Petersen <petersen@redhat.com> - 0.8.6-1
- check for _darcs or .git dir in package topdir not pwd

* Sun Sep 29 2013 Jens Petersen <petersen@redhat.com> - 0.8.5-1
- fix repoquery when a package update exists for C lib
- make cblrpm-diff quieter

* Sat Sep 28 2013 Jens Petersen <petersen@redhat.com> - 0.8.4-1
- use repoquery to determine extra C library dependencies
- quote "pkgconfig(foo)" for rpm query and yum install
- show sudo command before sudo password prompt appears
- exclude hsc2hs from build tool deps
- devel now provides ghc-<pkg>-static
- drop release from initial changelog entry for packager to add an entry
- do not try to fetch tarball for a darcs or git source dir

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Jens Petersen <petersen@redhat.com> - 0.8.3-1
- only try to install missing dependencies
- word-wrap generic descriptions
- now handles ghc_fix_dynamic_rpath for executables depending on own lib
- map ffi to libffi
- source module rearrangements

* Tue Jul  2 2013 Jens Petersen <petersen@redhat.com> - 0.8.2-1
- handle pkg-ver arg, and check cabal list is non-empty
- sort all generated deps
- use yum-builddep again to install deps
- copy tarball into cwd for rpmbuild
- wrap after end of sentence near end of line
- use _isa in requires ghc-<pkg>
- require rpm-build

* Fri Jun 21 2013 Jens Petersen <petersen@redhat.com> - 0.8.1-2
- rebuild

* Fri Jun 14 2013 Jens Petersen <petersen@redhat.com> - 0.8.1-1
- word wrapping of descriptions
- use generic description for shared subpackage
- simplify logic for summary and description processing

* Fri May 31 2013 Jens Petersen <petersen@redhat.com> - 0.8.0-1
- use simplified Fedora Haskell Packaging macros approved by
  Fedora Packaging Committee (https://fedorahosted.org/fpc/ticket/194)

* Wed Apr  3 2013 Jens Petersen <petersen@redhat.com> - 0.7.1-2
- better require cabal-install

* Fri Mar 22 2013 Jens Petersen <petersen@redhat.com> - 0.7.1-1
- add final full-stop to description if missing
- add ver-rel to initial changelog entry
- output warning when .spec already exists
- fix handling of package names that end in a digit
- output when trying a path
- map curl C dep to libcurl
- fix use of cblrpm-diff force lib option
- provide cblrpm

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Jens Petersen <petersen@redhat.com> - 0.7.0-1
- cabal-rpm and cabal-rpm-diff are now symlinks to cblrpm and cblrpm-diff
- now uses command args, initially spec, srpm, and build
- tries to sudo yum install dependencies
- https://github.com/juhp/cabal-rpm/blob/master/NEWS

* Wed Nov 21 2012 Jens Petersen <petersen@redhat.com> - 0.6.6-1
- now generates dependencies for C libs, buildtools, and pkgconfig depends
- add short cblrpm and cblrpm-diff alias symlinks
- fix handling of LGPL-2.1 license
- change backup suffix from .cabal-rpm to .cblrpm
- do not mistake non-existent tarballs for package names

* Thu Nov  1 2012 Jens Petersen <petersen@redhat.com> - 0.6.5-1
- drop hscolour BuildRequires
- simplify generated BuildRequires: drop version ranges,
  and exclude base, Cabal, etc
- use ExclusiveArch ghc_arches_with_ghci for template-haskell
- replace --name option with --library to force Lib package

* Tue Sep 25 2012 Jens Petersen <petersen@redhat.com> - 0.6.4-1
- add cabal-rpm-diff wrapper script
- fix generated manpage

* Mon Sep 24 2012 Jens Petersen <petersen@redhat.com> - 0.6.3-1
- can now handle tarball
- new manpage
- obsoletes cabal2spec

* Mon Sep 10 2012 Jens Petersen <petersen@redhat.com> - 0.6.2-1
- shorten description

* Mon Sep 10 2012 Fedora Haskell SIG <haskell@lists.fedoraproject.org>
- spec file generated by cabal-rpm-0.6.2
