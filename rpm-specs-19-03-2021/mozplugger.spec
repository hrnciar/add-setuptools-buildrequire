Summary: A generic mozilla plug-in
Name: mozplugger
Version: 2.1.6
Release: 14%{?dist}
License: GPLv2+
Url: http://mozplugger.mozdev.org/
Source0: http://mozplugger.mozdev.org/files/%{name}-%{version}.tar.gz

# fix #513470, using a wrong path for executable
Patch1: mozplugger-1.13.3-path.patch

# buildroot issue
Patch2: mozplugger-2.1.6-buildroot.patch

Requires: m4
Requires: sox
Requires: mozilla-filesystem

BuildRequires: make
BuildRequires:  gcc
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: coreutils
Requires: policycoreutils

%description
MozPlugger is a generic Mozilla plug-in that allows the use of standard Linux
programs as plug-ins for media types on the Internet.

%prep
%setup -q
%patch1 -p1 -b .path
%patch2 -p1 -b .buildroot

%build
export XCFLAGS="%{optflags}"
%configure
make

%post
setsebool -P unconfined_mozilla_plugin_transition 0

%postun
if [ $1 -eq 0 ] ; then
  setsebool -P unconfined_mozilla_plugin_transition 1
fi

%install
rm -rf %{buildroot}
make install libprefix=/%{_lib} root=%{buildroot}

# convert to UTF8
file=%{buildroot}%{_mandir}/man7/mozplugger.7
iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
mv "${file}_" "$file"
iconv -f iso-8859-1 -t utf-8 < README > README_
mv README_ README

%files
%doc README COPYING
%config(noreplace) /etc/mozpluggerrc
%{_bindir}/*
%{_libdir}/mozilla/plugins/mozplugger.so
%{_mandir}/man7/mozplugger.7*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Than Ngo <than@redhat.com> - 2.1.6-2
- bz#1139028, selinux

* Tue Oct 14 2014 Than Ngo <than@redhat.com> - 2.1.6-1
- 2.1.6

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Than Ngo <than@redhat.com> - 1.14.3-1
- 1.14.3
- build with optflags

* Wed Sep 29 2010 Than Ngo <than@redhat.com> - 1.14.2-1
- 1.14.2

* Mon Aug 09 2010 Than Ngo <than@redhat.com> - 1.14.1-1
- 1.14.1

* Tue Apr 20 2010 Than Ngo <than@redhat.com> - 1.13.3-1
- 1.13.3, fix crash in mozplugger bz#553935

* Fri Aug 21 2009 Than Ngo <than@redhat.com> - 1.12.1-7
- drop Obsoletes on plugger
- add comments for the patches
- add noreplace
- convert README to utf8

* Fri Aug 21 2009 Than Ngo <than@redhat.com> - 1.12.1-6
- fix #226159, merge review

* Thu Aug 20 2009 Than Ngo <than@redhat.com> - 1.12.1-5
- fix #513470, using a wrong path for executable

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Than Ngo <than@redhat.com> - 1.12.1-3
- fix #469257, selinux policy and mozplugger do not get along 

* Thu Jul  2 2009 Ville Skytt?? <ville.skytta at iki.fi> - 1.12.1-2
- Add dependency on m4 (#453306).

* Thu May 14 2009 Than Ngo <than@redhat.com> - 1.12.1-1
- 1.12.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.10.1-3
- fix license tag

* Thu Apr 10 2008 Karsten Hopp <karsten@redhat.com> 1.10.1-2
- use RPM_OPT_FLAGS (#249976, Ville Skytt??)

* Wed Feb 06 2008 Than Ngo <than@redhat.com> 1.10.1-1
- 1.10.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.7.3-3.1
- rebuild

* Tue May 16 2006 Than Ngo <than@redhat.com> 1.7.3-3 
- fix #191969, Missing BuildRequire on libXt-devel
- adjust mozpluggerc for FC
 
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.7.3-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.7.3-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 08 2005 Than Ngo <than@redhat.com> 1.7.3-2 
- get rid of xorg-x11-devel, fix for modular X

* Fri Oct 14 2005 Florian La Roche <laroche@redhat.com>
- update to 1.7.3

* Mon Apr  4 2005 Elliot Lee <sopwith@redhat.com> - 1.7.1-4
- Remove mikmod dep

* Sat Mar 05 2005 Than Ngo <than@redhat.com> 1.7.1-3
- rebuild

* Thu Feb 03 2005 Than Ngo <than@redhat.com> 1.7.1-2
- drop xloadimage dependency

* Thu Jan 20 2005 Than Ngo <than@redhat.com> 1.7.1-1
- update to 1.7.1
- remove mozplugger-1.6-2-ia64.patch, it's included in new upstream

* Mon Dec 06 2004 Than Ngo <than@redhat.com> 1.6.2-4
- add fix for ia64
- enable s390 s390x build

* Wed Nov 24 2004 Miloslav Trmac <mitr@redhat.com> - 1.6.2-3
- Convert man page to UTF-8

* Fri Oct 29 2004 Than Ngo <than@redhat.com> 1.6.2-2
- add missing Buildprereq on XFree86-devel #137564

* Tue Sep 28 2004 Than Ngo <than@redhat.com> 1.6.2-1
- update to 1.6.2
- get rid of requires mozilla

* Tue Aug 31 2004 Than Ngo <than@redhat.com> 1.6.1-1
- update to 1.6.1

* Sun Jul 25 2004 Than Ngo <than@redhat.com> 1.6.0-1
- update to 1.6.0
- fix broken deps 

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 07 2004 Than Ngo <than@redhat.com> 1.5.2-1
- update to 1.5.2, fix #117424
- remove mozplugger-1.5.0.patch that included in upstream

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 18 2004 Than Ngo <than@redhat.com> 1.5.0-3 
- drop mozplugger-1.1.3-redhat.patch, it's included in new upstream
- add patch file to fix swallow issue, thanks to Louis Bavoil

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 16 2004 Than Ngo <than@redhat.com> 1.5.0-1
- 1.5.0

* Fri Sep 26 2003 Harald Hoyer <harald@redhat.de> 1.3.2-1
- 1.3.2

* Thu Sep 04 2003 Than Ngo <than@redhat.com> 1.3.1-1
- 1.3.1

* Wed May  7 2003 Than Ngo <than@redhat.com> 1.1.3-1
- initial build
