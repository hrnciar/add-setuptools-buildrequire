%define contentdir %{_localstatedir}/www
%bcond_without buildweb

%define pkg_description The ht://Dig system is a complete world wide web indexing and searching \
system for a small domain or intranet. This system is not meant to replace \
the need for powerful internet-wide search systems like Lycos, Infoseek, \
Webcrawler and AltaVista. Instead it is meant to cover the search needs for \
a single company, campus, or even a particular sub section of a web site. As \
opposed to some WAIS-based or web-server based search engines, ht://Dig can \
span several web servers at a site. The type of these different web servers \
doesn't matter as long as they understand the HTTP 1.0 protocol. \
ht://Dig is also used by KDE to search KDE's HTML documentation. \
\
ht://Dig was developed at San Diego State University as a way to search the \
various web servers on the campus network.

Summary: ht://Dig - Web search engine
Name: htdig
Version: 3.2.0
Release: 0.39.b6%{?dist}
Epoch: 4
License: GPLv2
Url: http://www.htdig.org/
Source: http://www.htdig.org/files/%{name}-%{version}b6.tar.bz2
Source1: htdig.conf
Patch: htdig-3.1.5-rh.patch
Patch2: htdig-3.2.0b4-xopen.patch
Patch4: htdig-3.2.0b5-overflow.patch
Patch5: htdig-3.2.0b6-robots.patch
Patch6: htdig-3.2.0b6-unescaped_output.patch
Patch8: htdig-3.2.0b6-compile-fix.patch
Patch9: htdig-3.2.0b6-opts.patch
Patch11: htdig-3.2.0b6-incremental.patch
Patch12: htdig-3.2-CVE-2007-6110.patch
Patch13: htdig-3.2.0b6-htstat-segv.patch
Patch14: htdig-3.2.0-external_parsers.patch
Patch15: htdig-3.2.0-allow_numbers.patch
Patch16: htdig-3.2.0b6-narrowing.patch
Patch17: htdig-3.2.0b6-buildfix.patch
Patch18: htdig-3.2.0b6-const.patch
BuildRequires: gcc-c++ make
BuildRequires: zlib-devel openssl-devel httpd libtool flex

%description
%{pkg_description}

%package web
Summary: Scripts and HTML code needed for using ht://Dig as a web search engine
Requires: %{name} = %{epoch}:%{version}-%{release} webserver

%description web
%{pkg_description}

The %{name}-web package includes CGI scripts and HTML code needed to use
ht://Dig on a website.


%prep
%setup -q -n %{name}-%{version}b6
%patch -p1 -b .rh
%patch2 -p1 -b .xopen
%patch4 -p1 -b .overflow
%patch5 -p1 -b .robots
%patch6 -p1 -b .unescaped_output
%patch8 -p1 -b .compile-fix
%patch9 -p1 -b .opts
%patch11 -p1 -b .incremental
%patch12 -p1 -b .CVE-2007-6110
%patch13 -p1 -b .htstat-segv
%patch14 -p1 -b .external_parsers
%patch15 -p1 -b .allow_numbers
%patch16 -p1 -b .narrowing
%patch17 -p1 -b .buildfix
%patch18 -p1 -b .const

%build
autoreconf -fiv

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS -std=c++14"

%configure \
	--enable-shared \
	--enable-tests \
	--enable-bigfile \
	--with-config-dir=%{_sysconfdir}/htdig \
	--with-common-dir=%{contentdir}/html/htdig \
	--with-database-dir=%{_sharedstatedir}/htdig \
	--localstatedir=%{_sharedstatedir}/htdig \
	--with-cgi-bin-dir=%{contentdir}/cgi-bin \
	--with-image-dir=%{contentdir}/html/htdig \
	--with-search-dir=%{contentdir}/html/htdig \
	--with-default-config-file=%{_sysconfdir}/htdig/htdig.conf \
	--with-apache=%{_sbindir}/httpd \
	--with-zlib=%{_prefix} \
	--with-ssl
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# make sure the "htsearch" is in main package
mv $RPM_BUILD_ROOT%{contentdir}/cgi-bin/htsearch $RPM_BUILD_ROOT%{_bindir}
ln -s %{_bindir}/htsearch $RPM_BUILD_ROOT%{contentdir}/cgi-bin

chmod 644 $RPM_BUILD_ROOT%{contentdir}/html/htdig/*
ln -sf search.html $RPM_BUILD_ROOT%{contentdir}/html/htdig/index.html

# now get rid of the $RPM_BUILD_ROOT paths in the conf files
for i in %{_sysconfdir}/htdig/htdig.conf %{_bindir}/rundig ; do
	perl -pi -e "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT/$i
done
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{contentdir}/html/htdig $RPM_BUILD_ROOT%{_datadir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/htdig.conf

rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -f $RPM_BUILD_ROOT%{_libdir}/htdig/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/htdig/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/htdig_db/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/htdig_db/*.la

%ldconfig_scriptlets

%files
%doc htdoc/*html htdoc/*gif htdoc/COPYING htdoc/ChangeLog
%dir %{_sysconfdir}/htdig
%config(noreplace) %{_sysconfdir}/htdig/htdig.conf
%config(noreplace) %{_sysconfdir}/htdig/cookies.txt
%{_sysconfdir}/htdig/HtFileType-magic.mime
%{_sysconfdir}/htdig/mime.types
%dir %{_sharedstatedir}/htdig
%{_bindir}/*
%{_libdir}/htdig
%{_libdir}/htdig_db
%{_mandir}/man1/*
%{_mandir}/man8/*

%if %{with buildweb}
%files web
%{contentdir}/cgi-bin/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/htdig.conf
%dir %{_datadir}/htdig
%{_datadir}/htdig/*
%endif

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.39.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 4:3.2.0-0.38.b6
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.37.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.36.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.35.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.34.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.33.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Men????k <pemensik@redhat.com> - 4:3.2.0-0.32.b6
- Do not call ldconfig if not necessary

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.31.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Petr Men????k <pemensik@redhat.com> - 4:3.2.0-0.30.b6
- Fix htdig crash (#1497837)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.29.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.28.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Petr Men????k <pemensik@redhat.com> - 4:3.2.0-0.27.b6
- Fix build and remove some warnings

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.26.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 17 2016 Tomas Hozza <thozza@redhat.com> - 4:3.2.0-0.25.b6
- Moved htsearch to main package (#1230897)

* Sun Feb 14 2016 Ralf Cors??pius <corsepiu@fedoraproject.org> - 4:3.2.0-0.24.b6
- Add htdig-3.2.0b6-narrowing.patch (F24FTBFS, RHBZ#1307623).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.2.0-0.23.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.22.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4:3.2.0-0.21.b6
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 16 2015 Tomas Hozza <thozza@redhat.com> - 4:3.2.0-0.20.b6
- Address issues from merge review (#225889)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.19.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.18.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.17.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.16.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Jindrich Novy <jnovy@redhat.com> - 4:3.2.0-0.15.b6
- remove bogus relocation from spec

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.14.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.13.b6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.12.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.11.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 31 2010 Adam Tkac <atkac redhat com> - 4:3.2.0-0.10.b6
- build with -fno-strict-aliasing to get rid of useless error messages

* Mon Nov 30 2009 Adam Tkac <atkac redhat com> - 4:3.2.0-0.9.b6
- merge review related fixes (#225889)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4:3.2.0-0.8.b6
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.7.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.2.0-0.6.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Adam Tkac <atkac redhat com> 4:3.2.0-0.5.b6
- removed unneeded htdig-3.2.0b-versioncheck.patch

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> 4:3.2.0-0.4.b6
- rebuild with new openssl

* Tue Jul 29 2008 Adam Tkac <atkac redhat com> 4:3.2.0-0.3.b6
- removed unneded patches
  - htdig-3.2.0b3-glibc222.patch and htdig-3.2.0b4-h_hash.patch

* Mon Jul 28 2008 Adam Tkac <atkac redhat com> 4:3.2.0-0.2.b6
- mark configuration files as noreplace

* Wed Apr 23 2008 Adam Tkac <atkac redhat com> 4:3.2.0-0.1.b6
- report proper error message when external parser fails (#435741)
- ignore numbers when using allow_numbers: true and soundex (#435743)
- correct N-V-R

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3:3.2.0b6-16
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Adam Tkac <atkac redhat com> 3:3.2.0b6-15
- fixed htstat sigsegv when number of words is zero

* Wed Dec 05 2007 Adam Tkac <atkac redhat com> 3:3.2.0b6-14
- rebuild against new openssl

* Wed Nov 28 2007 Adam Tkac <atkac redhat com> 3:3.2.0b6-13
- CVE-2007-6110

* Wed Aug 22 2007 Adam Tkac <atkac redhat com> 3:3.2.0b6-12
- rebuild (BuildID feature)
- changed licence to GPLv2

* Wed Mar 07 2007 Adam Tkac <atkac redhat com> 3:3.2.0b6-11
- added upstream's segfault patch
- added ?_smp_mflags macro to make

* Thu Feb 01 2007 Adam Tkac <atkac redhat com> 3:3.2.0b6-10
- removed sigfault patch because it isn't stable yet
- changed common_dir in htdig.conf to /var/www/html/htdig (#220390)

* Tue Jan 09 2007 Adam Tkac <atkac redhat com> 3:3.2.0b6-9
- added +i option to rundig script. This option enables incremental digging

* Wed Dec 20 2006 Adam Tkac <atkac redhat com> 3:3.2.0b6-8
- fixed htfuzzy's sigfaults (#130528)

* Mon Dec 18 2006 Adam Tkac <atkac redhat com> 3:3.2.0b6-7
- really fixed #130528
- started using dist macro

* Tue Aug 8 2006 Jitka Kudrnacova <jkudrnac@redhat.com> - 3:3.2.0b6-6.4.3
- built with --with-ssl (#174162) to enable indexing ssl pages, BuildRequires openssl-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3:3.2.0b6-6.4.2.2.1
- rebuild

* Fri Feb 24 2006 Jitka Kudrnacova <jkudrnac@redhat.com> - 3:3.2.0b6-6.4.2.2 
- rebuilt

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3:3.2.0b6-6.4.2.1
- bump again for double-long bug on ppc(64)

* Thu Feb 09 2006 Jitka Kudrnacova <jkudrnac@redhat.com> - 3:3.2.0b6-6.4.2
- fixed building in rawhide (#176894)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3:3.2.0b6-6.4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt
- patched to not fail on apache version 2.x

* Mon Sep 05 2005 Phil Knirsch <pknirsch@redhat.com> 3:3.2.0b6-6
- Fixed missing $opts in rundig command (#130528)

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 3:3.2.0b6-5
- bump release and rebuild with gcc 4

* Tue Jan 25 2005 Phil Knirsch <pknirsch@redhat.com> 3:3.2.0b6-4
- Fixed security bug with unescaped output in htsearch and qtest (#144127)
- Removed .la and .a libs from package (#145649)

* Wed Aug 04 2004 Phil Knirsch <pknirsch@redhat.com> 3:3.2.0b6-3
- Corrected the htdig-web requires line.

* Tue Aug 03 2004 Phil Knirsch <pknirsch@redhat.com> 3:3.2.0b6-2
- Added Epoch to allow updates from older releases to this version.

* Tue Jul 06 2004 Phil Knirsch <pknirsch@redhat.com> 3.2.0b6-1
- Update to htdig-3.2.0b6
- Removed obsolete patches (already included upstream).
- Added manpages to basic package.
- Added missing httpd BuildPreReq (#125037)
- Added fix for broken behaviour with robots.txt (#126482)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar 29 2004 Karsten Hopp <karsten@redhat.de> 3.2.0b5-7 
- really fix buildroot path in HtFileType-magic.mime (#116442)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Phil Knirsch <pknirsch@redhat.com> 3.2.0b5-6
- Removed buildroot cruft from HtFileFype (#116442).
- Use mktemp in HtFileFype to create temporary file (#116443).

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 15 2004 Phil Knirsch <pknirsch@redhat.com> 3.2.0b5-4
- Fixed missing & in if clause.

* Tue Jan 13 2004 Phil Knirsch <pknirsch@redhat.com> 3.2.0b5-3
- Fixed latin1 char translation (#71921).
- Fixed overflow bug in WordDBPage.cc (#110802).

* Mon Jan 12 2004 Phil Knirsch <pknirsch@redhat.com> 3.2.0b5-2
- Moved /usr/share/htdig files to web package (#111938).

* Fri Dec 12 2003 Phil Knirsch <pknirsch@redhat.com> 3.2.0b5-1
- Update to latest stable upstream version htdig-3.2.0b5.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Phil Knirsch <pknirsch@redhat.com> 3.2.0-18.20030601
- Update to htdig-3.2.0b4-20030601 snapshot.
- Fixed build problems.

* Thu Mar 06 2003 Phil Knirsch <pknirsch@redhat.com> 3.2.0-17.20030302
- Update to htdig-3.2.0b4-20030302 snapshot.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan  8 2003 Jeff Johnson <jbj@redhat.com> 3.2.0-15.20021103
- don't include -debuginfo files in package.

* Tue Dec 17 2002 Phil Knirsch <pknirsch@redhat.com> 3.2.0-14.20021103
- Forgot to create conf.d directory. Fixed.
- Fixed wrong files section.

* Tue Dec 10 2002 Phil Knirsch <pknirsch@redhat.com> 3.2.0-13.20021103
- Removed symlink from %%{contentdir}/html and replaced it with httpd.d conf
  file (#73518).

* Tue Dec 10 2002 Phil Knirsch <pknirsch@redhat.com> 3.2.0-12.20021103
- Added webserver requirement for htdig-web package (#73986).

* Wed Dec 04 2002 Phil Knirsch <pknirsch@redhat.com> 3.2.0-11.20021103
- Fix for autoFOO patch.
- Fix x64_64 build.

* Wed Nov 27 2002 Tim Powers <timp@redhat.com> 3.2.0-9.20021103
- rebuild on all arches

* Fri Nov 08 2002 Phil Knirsch <pknirsch@redhat.com> 3.2.0-8.20021103
- Updated to htdig-3.2.0b4-20021103.
- Fixed %%files section errors.

* Sat Aug 10 2002 Elliot Lee <sopwith@redhat.com> 3.2.0-7.20020505
- rebuilt with gcc-3.2 (we hope)

* Tue Jul 23 2002 Tim Powers <timp@redhat.com> 3.2.0-6.20020505
- build using gcc-3.2-0.1

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 3.2.0-5.20020505
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 3.2.0-4.20020505
- Don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May  6 2002 Bernhard Rosenkraenzer <bero@linux-easy.com> 3.2.0-2.20020505
- Fix build with current toolchain (automake 1.6, autoconf 2.53 changes)
- Update snapshot, fixes some more problems

* Thu Jan 24 2002 Phil Knirsch <pknirsch@redhat.com>
- Updated to latest snapshot to fix several problems.
- Fixed a problem with htdig segfaulting on s390 (#58202).

* Fri Jul 20 2001 Philipp Knirsch <pknirsch@redhat.de>
- Added missing BuildRequires: zlib-devel (#49500)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Apr 27 2001 Bill Nottingham <notting@redhat.com>
- rebuild for C++ exception handling on ia64

* Wed Mar 21 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.2.0-0.b3.4
- move pictures etc. to base package and to a directory outside of
  /var/www - The current KDevelop search function doesn't work without
  them.

* Mon Mar  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add htsearch to the base package, kdevelop needs it

* Wed Jan 10 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Move the web related files to a separate package

* Tue Oct  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 3.2.0b2
- fix build with glibc 2.2 and gcc 2.96

* Sat Aug 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix syntax error introduced in our patch (#16598)

* Tue Aug 1 2000 Tim Powers <timp@redhat.com>
- fixed group to be a valid one

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild for Power Tools

* Thu Jun 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild for Power Tools

* Sat Feb 26 2000 Nalin Dahyabhai <nalin@redhat.com>
- 3.1.5

* Wed Jan 12 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 3.1.4
- fix URL and source location

* Tue Sep 28 1999 Preston Brown <pbrown@redhat.com>
- 3.1.3 for SWS 3.1

* Wed May 05 1999 Preston Brown <pbrown@redhat.com>
- updates for SWS 3.0

* Mon Aug 31 1998 Preston Brown <pbrown@redhat.com>
- Updates for SWS 2.0

* Sat Feb 07 1998 Cristian Gafton <gafton@redhat.com>
- built against glibc
- build all the fuzzy databases before packaging, because it is time
  consuming operation and we don't want the user to be impatient
