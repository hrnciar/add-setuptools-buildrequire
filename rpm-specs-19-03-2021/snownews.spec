Name:		snownews
Version: 	1.6.10
Release: 	3%{?dist}
Summary: 	A text mode RSS/RDF newsreader
License: 	GPLv3
Url:		https://github.com/kouya/snownews
Source0:	https://github.com/kouya/snownews/archive/%{version}/snownews-%{version}.tar.gz
Patch0:		snownews-1.6.10-debugflags.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	gettext
BuildRequires:	perl-generators

%description
Snownews  is  a text mode RSS/RDF newsreader. It supports all versions
of RSS natively and supports other formats via plugins.

The program depends on ncurses for the user interface and uses libxml2 
for XML parsing. ncurses must be at least version 5.0. It should work
with any version of libxml2.

%prep
%setup -q
%patch0 -p1

%build
%set_build_flags
./configure --prefix=%{_prefix}
EXTRA_CFLAGS="$RPM_OPT_FLAGS -fPIE -DUTF_8" EXTRA_LDFLAGS="-pie" make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" PREFIX="$RPM_BUILD_ROOT%{_prefix}" install
%find_lang %name

%files -f %name.lang
%doc README* AUTHOR COPYING CREDITS Changes
%{_bindir}/opml2snow
%{_bindir}/snow2opml
%{_bindir}/snownews
%{_mandir}/man1/*
%{_mandir}/*/man1/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 David Kaufmann <astra@ionic.at> - 1.6.10-2
- Add rpminspect suggested build flags

* Sat Dec 05 2020 David Kaufmann <astra@ionic.at> - 1.6.10-1
- New version, fix build issues

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Petr Pisar <ppisar@redhat.com> - 1.5.12-21
- Build with openssl-1.0.2 (bug #1606839)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5.12-11
- Fix FTBFS with -Werror=format-security (#1037331, #1107349)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 22 2013 Zing <zing@fastmail.fm> - 1.5.12-9
- new URL

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.5.12-7
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 14 2009 Zing <zing@fastmail.fm> - 1.5.12-2
- Bring back link with ncursesw, set -DUTF_8 for xmlUTF8Strlen #546431
  mistakenly dropped when charset patch went upstream

* Mon Oct  5 2009 Zing <zing@fastmail.fm> - 1.5.12-1
- Bug fixes + openssl added as a requirement
- Corrected two crashes when using mark unread and open URL on
  non-existent items.
- Use OpenSSL for MD5 calculations and remove all old MD5 code.
- Fix 64bit digest calc. Readstatus wasn't remembered on 64bit versions.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Zing <zing@fastmail.fm> - 1.5.10-5
- possible pie fix for sparc build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug  2 2008 Zing <zing@fastmail.fm> - 1.5.10-3
- watchout! fuzz cops in town!

* Sat Aug  2 2008 Zing <zing@fastmail.fm> - 1.5.10-1
- update to 1.5.10
- drop charset patch (upstream)

* Thu Apr 17 2008 Zing <zing@fastmail.fm> - 1.5.9-1
- update to 1.5.9

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.8-2
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Zing <zing@fastmail.fm> - 1.5.8-1
- update to 1.5.8
- remove manpath and softlink patch (upstream)
- update charset patch (utf-8 enabled in configure)
- snowsync program removed

* Thu Aug 16 2007 Zing <zing@fastmail.fm> - 1.5.7-7
- License too verbose, just GPLv2 is fine

* Thu Aug  9 2007 Zing <zing@fastmail.fm> - 1.5.7-6
- conform to Fedora Licensing Guidelines

* Sat Sep  9 2006 Zing <zing@fastmail.fm> - 1.5.7-5
- remove mention of update checking from man page
- rebuild for FE6

* Tue Feb 14 2006 Zing <shishz@hotpop.com> - 1.5.7-4
- rebuild for FE5

* Mon Aug 29 2005 Zing <shishz@hotpop.com> - 1.5.7-3
- cleanups related to runtime charset detection
-   get rid of configure --charset=UTF-8 hardcoding
-   link with ncursesw, set -DUTF_8 for xmlUTF8Strlen

* Mon Aug  6 2005 Zing <shishz@hotpop.com> - 1.5.7-2
- add runtime charset detection, #155073
- use dist macro

* Fri Jul 29 2005 Zing <shishz@hotpop.com> - 1.5.7-1
- update to 1.5.7
- drop destdir patch, fixed upstream
- fixup softlink for snow2opml

* Thu Mar 24 2005 Warren Togami <wtogami@redhat.com> - 1.5.6.1-3
- macroize dirs

* Tue Mar 15 2005 Zing <shishz@hotpop.com> - 1.5.6.1-2
- enable snowsync

* Thu Feb 24 2005 Zing <shishz@hotpop.com> - 1.5.6.1-1
- new upstream
- remove snowsync for now. (we need perl-XML-LibXSLT)

* Fri Jul 23 2004 Zing <shishz@hotpop.com> - 1.5.3-0.fdr.4
- More cleanups from QA (M.Schwendt)
-	do the buildroot better (grrr hopefully)
-	locales & paths should now be working

* Fri Jul 23 2004 Zing <shishz@hotpop.com> - 1.5.3-0.fdr.3
- More cleanups from QA (M.Schwendt)
-	fix man path directory ownerships
-	don't let installer strip-install
-	fix file permissions in src.rpm to 0644
-	use find_lang macro

* Fri Jul 23 2004 Zing <shishz@hotpop.com> - 1.5.3-0.fdr.2
- disable auto version check
- build executables as PIEs
- QA from Michael Schwendt:
-	Buildrequires: gettext
-	install man pages to /usr/share/man
-	unneeded version check for ncurses-devel
-	add SMP make flag
-	add RPM_OPT_FLAGS

* Thu Jul 22 2004 Zing <shishz@hotpop.com> - 1.5.3-0.fdr.1
- Initial RPM release.
