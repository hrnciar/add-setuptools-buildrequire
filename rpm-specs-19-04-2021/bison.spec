Summary: A GNU general-purpose parser generator
Name: bison
Version: 3.7.6
Release: 1%{?dist}
License: GPLv3+
Source0: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
# genereted from https://ftp.gnu.org/gnu/gnu-keyring.gpg via:
# curl https://ftp.gnu.org/gnu/gnu-keyring.gpg | gpg2 --import
# gpg2 --export --export-options export-minimal 7DF84374B1EE1F9764BBE25D0DDCAA3278D5264E > gpgkey-7DF84374B1EE1F9764BBE25D0DDCAA3278D5264E.gpg
Source2: gpgkey-7DF84374B1EE1F9764BBE25D0DDCAA3278D5264E.gpg

# testsuite dependency
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: flex
BuildRequires: gnupg2

URL: http://www.gnu.org/software/%{name}/
BuildRequires: m4 >= 1.4
BuildRequires: make
#java-1.7.0-openjdk-devel
Requires: m4 >= 1.4

# bison contains a copy of gnulib.  As a copylib, gnulib was granted
# an exception that allows bundling it with other software.  For
# details, see:
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Exceptions
Provides: bundled(gnulib)

%description
Bison is a general purpose parser generator that converts a grammar
description for an LALR(1) context-free grammar into a C program to
parse that grammar. Bison can be used to develop a wide range of
language parsers, from ones used in simple desk calculators to complex
programming languages. Bison is upwardly compatible with Yacc, so any
correctly written Yacc grammar should work with Bison without any
changes. If you know Yacc, you shouldn't have any trouble using
Bison. You do need to be very proficient in C programming to be able
to use Bison. Bison is only needed on systems that are used for
development.

If your system will be used for C development, you should install
Bison.

%package devel
Summary: -ly library for development using Bison-generated parsers
Provides: bison-static = %{version}-%{release}

%description devel
The bison-devel package contains the -ly library sometimes used by
programs using Bison-generated parsers.  If you are developing programs
using Bison, you might want to link with this library.  This library
is not required by all Bison-generated parsers, but may be employed by
simple programs to supply minimal support for the generated parsers.

# -ly is kept static.  It only contains two symbols: main and yyerror,
# and both of these are extremely simple (couple lines of C total).
# It doesn't really pay off to introduce a shared library for that.
#
# Therefore -devel subpackage could have been created as -static, but
# the split was done in Jan 2005, which predates current guidelines.
# Besides there is logic to that: the library is devel in the sense
# that the generated parser could be distributed together with other
# sources, and only bison-devel would be necessary to wrap the build.

%package runtime
Summary: Runtime support files used by Bison-generated parsers

%description runtime
The bison-runtime package contains files used at runtime by parsers
that Bison generates.  Packages whose binaries contain parsers
generated by Bison should depend on bison-runtime to ensure that
these files are available.  See the Internationalization in the
Bison manual section for more information.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure
%make_build

%check
make check
#make maintainer-check

%install
%make_install

# Remove unpackaged files.
rm -f %{buildroot}/%{_bindir}/yacc
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_mandir}/man1/yacc*
rm -rf %{buildroot}/%{_docdir}/%{name}/examples/*

%find_lang %{name}
%find_lang %{name}-runtime
%find_lang %{name}-gnulib

gzip -9nf ${RPM_BUILD_ROOT}%{_infodir}/bison.info*

# The distribution contains also source files.  These are used by m4
# when the target parser file is generated.
%files -f %{name}.lang -f %{name}-gnulib.lang
%doc AUTHORS ChangeLog NEWS README THANKS TODO COPYING
%{_mandir}/*/bison*
%{_datadir}/bison
%{_infodir}/bison.info*
%{_bindir}/bison
%{_datadir}/aclocal/bison*.m4

%files -f %{name}-runtime.lang runtime
%doc COPYING

%files devel
%doc COPYING
%defattr(-,root,root)
%{_libdir}/liby.a

%changelog
* Tue Mar 16 2021 Arjun Shankar <arjun@redhat.com> - 3.7.6-1
- Update to bison 3.7.6 (#1920078)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Arjun Shankar <arjun@redhat.com> - 3.7.4-1
- Update to bison 3.7.4 (#1897780)

* Tue Nov 10 2020 Arjun Shankar <arjun@redhat.com> - 3.7.3-1
- Update to bison 3.7.3 (#1887766)

* Tue Sep  8 2020 Arjun Shankar <arjun@redhat.com> - 3.7.2-1
- Update to bison 3.7.2 (#1876120)

* Thu Aug 27 2020 Arjun Shankar <arjun@redhat.com> - 3.7.1-1
- Update to bison 3.7.1 (#1859887)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 3.6.4-1
- Update to bison 3.6.4 (#1792738, #1847608)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Arjun Shankar <arjun@redhat.com> - 3.5-1
- Update to bison 3.5 (#1751843)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Arjun Shankar <arjun@redhat.com> - 3.4.1-1
- Update to bison 3.4.1 (#1631912)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Patsy Griffin Franklin <pfrankli@redhat.com> - 3.0.5-1
- _IO_ftrylockfile is obsolete as part of the removal of libio.h
- Build requires gcc-c++ to fix build failure. (#1603491)
- Update to bison 3.0.5 (#1583179)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Patsy Franklin <pfrankli@redhat.com> - 3.0.4-6
- Proposed upstream patch to fix testsuite failures for tests 430-432.
  BZ #1422261

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Patsy Franklin <pfrankli@redhat.com> - 3.0.4-3
- Remove unpackaged files.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Patsy Franklin <pfrankli@redhat.com> - 2.0.4-1
- Rebase to 3.0.4.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 09 2013 Patsy Franklin <pfrankli@redhat.com> - 3.0.2-1
- Rebase to 3.0.2.  Add BuildRequires: flex for testsuite.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Petr Machata <pmachata@redhat.com> - 2.7-2
- Drop unused options --raw, -n, -e, --include and -I

* Thu Mar 21 2013 Petr Machata <pmachata@redhat.com> - 2.7-1
- Rebase to 2.7

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov  2 2012 Orion Poplawski <orion@cora.nwra.com> - 2.6.4-1
- Update to 2.6.4

* Tue Jul 31 2012 Petr Machata <pmachata@redhat.com> - 2.6.1-1
- Rebase to 2.6.1
  - Drop bison-2.4.2-drop-test-67.patch
- Resolves: #829028

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Petr Machata <pmachata@redhat.com> - 2.5-4
- Add a virtual provides for bundled(gnulib).
- Resolves: #821746

* Tue Apr 17 2012 Bill Nottingham <notting@redhat.com> - 2.5-2
- swap java-openjdk-1.6.0 for 1.7.0 in buildrequirements

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Petr Machata <pmachata@redhat.com> - 2.5-1
- Upstream 2.5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 Petr Machata <pmachata@redhat.com> - 2.4.3-1
- Rebase to 2.4.3
- Resolves: #621854

* Thu Jul  1 2010 Petr Machata <pmachata@redhat.com> - 2.4.2-3
- Devel subpackage now provides boost-static, as per Fedora
  guidelines.
- Resolves: #609599

* Thu Apr  8 2010 Petr Machata <pmachata@redhat.com> - 2.4.2-2
- Disable the mysteriously failing test no. 67.  Details in associated
  bugreport. (bison-2.4.2-drop-test-67.patch)
- Resolves: #576513

* Wed Apr  7 2010 Petr Machata <pmachata@redhat.com> - 2.4.2-1
- Rebase to 2.4.2
- Drop reap_subpipe patch, upstream has a fix
- Resolves: #576513

* Fri Mar  5 2010 Petr Machata <pmachata@redhat.com> - 2.4.1-5
- Fix the license tag
- Install COPYING

* Mon Aug 24 2009 Petr Machata <pmachata@redhat.com> - 2.4.1-4
- Fix installation with --excludedocs
- Resolves: #515939

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 28 2008 Petr Machata <pmachata@redhat.com> - 2.4.1-1
- Rebase to 2.4.1
- Resolves: #478348

* Wed Nov 12 2008 Petr Machata <pmachata@redhat.com> - 2.4-2
- Rebase to 2.4
- Resolves: #471183

* Mon Sep 15 2008 Petr Machata <pmachata@redhat.com> - 2.3-6
- Merge review:
  - Drop terminating dot from Summary
  - Escape macros inadvertently left in changelog
  - Explain why are there source files in the main package

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3-5
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Roland McGrath <roland@redhat.com> - 2.3-4
- Canonicalize License tag.

* Sun Jan 21 2007 Roland McGrath <roland@redhat.com> - 2.3-3
- Canonicalize post/preun use of install-info.
- Resolves: 223679

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.3-2.1
- rebuild

* Wed Jun  7 2006 Roland McGrath <roland@redhat.com> - 2.3-2
- Add BuildRequires on m4.

* Wed Jun  7 2006 Roland McGrath <roland@redhat.com> - 2.3-1
- New upstream version 2.3

* Mon May 22 2006 Roland McGrath <roland@redhat.com> - 2.2-1
- New upstream version 2.2

* Mon May  1 2006 Roland McGrath <roland@redhat.com> - 2.1-3
- Fix K&R parser definition when it has no arguments (#190376).

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Oct 14 2005 Roland McGrath <roland@redhat.com> - 2.1-1
- New upstream version 2.1
- New subpackage bison-runtime for i18n support files used by parsers.

* Thu Apr  7 2005 Roland McGrath <roland@redhat.com> - 2.0-6
- run test suite in %%check

* Mon Mar 14 2005 Roland McGrath <roland@redhat.com> - 2.0-5
- rebuilt

* Thu Jan  6 2005 Roland McGrath <roland@redhat.com> - 2.0-4
- update upstream URLs, add doc files (#144346)

* Thu Jan  6 2005 Roland McGrath <roland@redhat.com> - 2.0-3
- missing %%defattr for subpackage

* Thu Jan  6 2005 Roland McGrath <roland@redhat.com> - 2.0-2
- split liby.a into bison-devel package

* Tue Jan  4 2005 Roland McGrath <roland@redhat.com> - 2.0-1
- new upstream version

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jun  4 2004 Roland McGrath <roland@redhat.com> 1.875c-1
- new upstream version (fixes bug #116823)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Oct 30 2003 Roland McGrath <roland@redhat.com> 1.875-6
- add dependency on m4 (bug #108655)

* Wed Sep 24 2003 Roland McGrath <roland@redhat.com> 1.875-5
- remove problematic __attribute__ use for label (bug #105034)

* Fri Aug  1 2003 Havoc Pennington <hp@redhat.com> 1.875-3
- put #ifndef __cplusplus around attribute(unused) on goto label in yacc.c

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Mar 22 2003 Roland McGrath <roland@redhat.com> 1.875-2
- update specs for new files installed by new version

* Wed Mar 19 2003 Roland McGrath <roland@redhat.com> 1.875-1
- new upstream version 1.875 (bug #83184)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 27 2002 Than Ngo <than@redhat.com> 1.35-5
- rebuild in new build enviroment
- remove unneeded file

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 18 2002 Than Ngo <than@redhat.com> 1.35-3
- don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 27 2002 Than Ngo <than@redhat.com> 1.35-1
- 1.35 fix incompatible with C++ compilers (bug #62121)

* Sun Mar 17 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.34

* Sat Feb 09 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.33

* Sat Jan 26 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.32

* Tue Jan 15 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.31

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Nov 27 2001 Than Ngo <than@redhat.com> 1.30-4
- add missing Url

* Sun Nov 25 2001 Than Ngo <than@redhat.com> 1.30-3
- fixed coredumps on some input bug #56607i, thanks to Enrico for locating this bug

* Tue Nov 06 2001 Than Ngo <than@redhat.com> 1.30-2
- FHS packaging
- use find_lang

* Sun Nov 04 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.30

* Mon Oct 15 2001 Than Ngo <than@redhat.de> 1.29-1
- update to 1.29
- update Url (bug #54597)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Than Ngo <than@redhat.de>
- rebuilt in the new build environment
- FHS packaging

* Sat May 27 2000 Ngo Than <than@redhat.de>
- rebuild for 7.0
- put man pages and info files to correct place

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- rebuild to gzip man page.

* Fri Jul 16 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.28.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Mon Mar  8 1999 Jeff Johnson <jbj@redhat.com>
- configure with datadir=/usr/lib (#1386).

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- updated text in spec file.
- update to 1.27

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- built for Manhattan
- added build root

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- various spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
