# Spec file for rhdb-utils.
# Authors: Liam Stewart <liams@redhat.com>, Andrew Overholt
# <overholt@redhat.com>, Tom Lane <tgl@redhat.com>
# Copyright (C) 2002-2012 Red Hat, Inc.

Summary: Miscellaneous utilities for PostgreSQL - Red Hat Edition
Name: rhdb-utils
Version: 13.1
Release: 1%{?dist}
# URL: http://pgfoundry.org/projects/pgfiledump/
URL: https://wiki.postgresql.org/wiki/Pg_filedump
License: GPLv2+

BuildRequires: make
BuildRequires: clang
BuildRequires: postgresql-server-devel, postgresql-static, libpq-devel

# This is kind of work-around;  even though we don't install PostgreSQL server
# modules in this package, we still want to depend on the major version of
# PostgreSQL server (or rather we want to be notified that new rebuild is needed
# for new major version of PostgreSQL)
%{?postgresql_module_requires}

Provides: pg_filedump = %version-%release

# Source0: http://pgfoundry.org/frs/download.php/3391/pg_filedump-%%{version}.tar.gz
%global tarballname pg_filedump-REL_13_1-9c9700e

# Download by wget --content-disposition \
#    'https://git.postgresql.org/gitweb/?p=pg_filedump.git;a=snapshot;h=REL_13_1;sf=tgz'
Source0: %tarballname.tar.gz
Source1: pg_filedump.1

%description
This package contains miscellaneous, non-graphical tools originally
developed for PostgreSQL - Red Hat Edition.


%prep
%autosetup -n %tarballname -p1


%build
make %{?_smp_mflags} PG_CONFIG=%_bindir/pg_server_config


%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -p -m 755 pg_filedump ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m 0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_mandir}/man1


%files
%{_bindir}/pg_filedump
%doc README.pg_filedump
%{_mandir}/man1/pg_filedump.1*


%changelog
* Wed Jan 13 2021 Patrik Novotný <panovotn@redhat.com> - 13.1-1
- Rebase for postgresql 13.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 14 2020 Honza Horak <hhorak@redhat.com> - 12.0-2
- Rebuild with PostgreSQL v12 with JIT

* Fri Feb 28 2020 Nils Philippsen <nils@tiptoe.de> - 12.0-1
- version 12.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Pavel Raiskup <praiskup@redhat.com> - 11.0-1
- build against libpq-devel, too
- rebase to the latest upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Pavel Raiskup <praiskup@redhat.com> - 10.0-5
- rebuild against postgresql-server-devel

* Mon Jul 23 2018 Pavel Raiskup <praiskup@redhat.com> - 10.0-4
- gcc BR and tiny cleanup

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Pavel Raiskup <praiskup@redhat.com> - 9.6.0-4
- rebase to version 10.0, per upstream announcement
  https://www.postgresql.org/message-id/20171022183831.uxt3jkbilbn35o3m%40msg.df7cb.de
- rebuild for PostgreSQL 10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Pavel Raiskup <praiskup@redhat.com> - 9.6.0-1
- rebase to the latest upstream release (fixes rhbz#1307992)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Pavel Raiskup <praiskup@redhat.com> - 9.3.0-1
- rebase to most recent release, fix FTBFS (#1107018)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Pavel Raiskup <praiskup@redhat.com> - 9.2.0-5
- fix manual page to not cause fail of lexgrog (private #948934)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Pavel Raiskup <praiskup@redhat.com> - 9.2.0-3
- add manual page generated by help2man utility (private #948934)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Tom Lane <tgl@redhat.com> 9.2.0-1
- Update pg_filedump to version 9.2.0, to support PostgreSQL 9.2.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Tom Lane <tgl@redhat.com> 9.1.0-1
- Update pg_filedump to version 9.1.0, to support PostgreSQL 9.1.
- Point to new upstream home at pgfoundry.org.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Tom Lane <tgl@redhat.com> 9.0.0-1
- Update pg_filedump to version 9.0.0, to support PostgreSQL 9.0.
- Relabel license as PostgreSQL now that that's separately recognized by OSI.

* Wed Sep 29 2010 jkeating - 8.4.0-5
- Rebuilt for gcc bug 634757

* Sat Sep 11 2010 Parag Nemade <paragn AT fedoraproject.org> 8.4.0-4
- Merge-review cleanup (#226370)

* Fri Jun  4 2010 Tom Lane <tgl@redhat.com> 8.4.0-3
- Add -fno-strict-aliasing to CFLAGS per rpmdiff complaint, and -fwrapv
  too just to be on the safe side.
Related: #596204

* Tue Jan 19 2010 Tom Lane <tgl@redhat.com> 8.4.0-2
- Correct License: tag to reflect that pg_crc.c is copied from postgresql.

* Tue Aug 18 2009 Tom Lane <tgl@redhat.com> 8.4.0-1
- Update pg_filedump to version 8.4.0, to support PostgreSQL 8.4.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom Lane <tgl@redhat.com> 8.3.0-1
- Update pg_filedump to version 8.3.0, to support PostgreSQL 8.3.

* Thu Aug  2 2007 Tom Lane <tgl@redhat.com> 8.2.0-2
- Update License tag to match code.

* Wed Feb 14 2007 Tom Lane <tgl@redhat.com> 8.2.0-1
- Update pg_filedump to version 8.2.0, to support PostgreSQL 8.2.
Resolves: #224175

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 8.1.1-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 8.1.1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 8.1.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 21 2005 Tom Lane <tgl@redhat.com> 8.1.1-1
- Update pg_filedump to version 8.1.1, to fix a couple of oversights.
- Simplify specfile a bit.

* Mon Nov 21 2005 Tom Lane <tgl@redhat.com> 8.1-1
- Update pg_filedump to version 8.1, to support PostgreSQL 8.1.
- Change version numbering so that major version matches corresponding
  PostgreSQL version.

* Wed Mar  2 2005 Tom Lane <tgl@redhat.com> 4.0-3
- Rebuild for gcc4 update.

* Fri Feb 11 2005 Tom Lane <tgl@redhat.com> 4.0-2
- Adjust build to honor $RPM_OPT_FLAGS.

* Thu Feb 10 2005 Tom Lane <tgl@redhat.com> 4.0-1
- Update pg_filedump to version 4.0, to support PostgreSQL 8.0.
- Keep pg_crc.c on hand as a plain source file instead of a patch.
  Easier to compare to main PG sources that way.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr  5 2004 Tom Lane <tgl@redhat.com>
- Update outdated URL.

* Fri Feb 20 2004 Tom Lane <tgl@redhat.com>
- Remove beta label from pg_filedump.

* Fri Feb 20 2004 Tom Lane <tgl@redhat.com>
- Update to version 3.0.
- Increment Buildrequires to >= PostgreSQL 7.4
- Rebuild for Fedora Core 2.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Nov 21 2003 David Jee <djee@redhat.com> 2.0-2
- Remove Distribution tag.
- Rebuild for Fedora Core 1.

* Thu May 29 2003 Andrew Overholt <overholt@redhat.com>
- Bump to version 2.0.
- Modify distribution.
- Increment Buildrequires to >= PostgreSQL 7.3

* Wed Sep 11 2002 Andrew Overholt <overholt@redhat.com>
- Changed revision to 1.

* Mon Jul  8 2002 Liam Stewart <liams@redhat.com>
- Updated summary and description.

* Thu Jul  4 2002 Liam Stewart <liams@redhat.com>
- Updated Source0 entry.

* Wed Jun 26 2002 Liam Stewart <liams@redhat.com>
- Group fix.

* Mon Jun 24 2002 Liam Stewart <liams@redhat.com>
- Initial build.


