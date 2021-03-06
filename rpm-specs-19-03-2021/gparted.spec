Summary:	Gnome Partition Editor
Name:		gparted
Version:	1.2.0
Release:	1%{?dist}
License:	GPLv2+
URL:		http://gparted.org
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	gtkmm30-devel
BuildRequires:	parted-devel
BuildRequires:	libuuid-devel
BuildRequires:	gettext
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	polkit
BuildRequires:	libappstream-glib
BuildRequires:	itstool
BuildRequires:	gcc-c++
BuildRequires: make

Requires:	PolicyKit-authentication-agent

%description
GParted stands for Gnome Partition Editor and is a graphical frontend to
libparted. Among other features it supports creating, resizing, moving
and copying of partitions. Also several (optional) filesystem tools provide
support for filesystems not included in libparted. These optional packages
will be detected at runtime and don't require a rebuild of GParted

%prep
%setup -q

%build
%configure --enable-libparted-dmraid --enable-online-resize --enable-xhost-root
%make_build

%install
%make_install

sed -i 's#_X-GNOME-FullName#X-GNOME-FullName#' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's#sbin#bin#' %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --delete-original			\
	--dir %{buildroot}%{_datadir}/applications	\
	--mode 0644					\
	--add-category X-Fedora				\
	--add-category GTK				\
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
%{__install} -p -m755 %{name}.appdata.xml %{buildroot}%{_datadir}/metainfo

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_sbindir}/gpartedbin
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/gparted.*
%{_datadir}/polkit-1/actions/org.gnome.gparted.policy
%{_datadir}/appdata/gparted.appdata.xml
%{_datadir}/help/*/gparted/*
%{_mandir}/man8/gparted.*

%changelog
* Sat Jan 30 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Mon Aug 26 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.0-3
- Drop gnome-doc-utils as BR

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Update gtkmm buildrequires
- Add itstool as buildrequires

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.33.0-1
- Update to 0.33.0

* Fri Aug 24 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.32.0-2
- Drop upstreamed patch

* Fri Aug 24 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.32.0-1
- Update to 0.32.0

* Mon Jul 16 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.0-6
- Add gcc-c++ as BR

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.0-4
- Add patch to fix gparted shrink action on LVM PV
- Fixes bug# 1596416

* Fri Jun 08 2018 Mike Fleetwood <mike.fleetwood@googlemail.com> - 0.31.0-3
- Remove obsolete edit to the desktop file

* Fri May 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.0-2
- Drop BR:rarian-compat

* Mon Mar 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.0-1
- Update to 0.31.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.30.0-1
- Update to 0.30.0
- Add appdata files
- Drop fedora pkexec scripts
- Use pkexec policy from upstream

* Fri Sep 15 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.29.0-1
- Update to 0.29.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 18 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.28.1-1
- Update to 0.28.1
- Bugfix release

* Tue Feb 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.28.0-1
- Update to 0.28.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.27.0-2
- Fix package url

* Sat Oct 22 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.27.0-1
- Update to 0.27.0

* Sat Jun 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.26.1-1
- Update to bugfix release 0.26.1

* Sat Apr 30 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.26.0-3
- Get rid of conditionals entirely.

* Sat Apr 30 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.26.0-2
- Fix if fedora conditionals and add EL conditionals

* Thu Apr 28 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.26.0-1
- Update to 0.26.0

* Mon Mar 21 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.25.0-4
- Change requires to PolicyKit-authentication-agent

* Tue Feb 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.25.0-3
- Make pixmaps gparted.png conditional to < Fedora 24
- Fixes Rawhide/F24 FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.25.0-1
- Updated to 0.25.0
- source tarball is now gz - so source fixed in spec

* Wed Oct 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.24.0-1
- Update to 0.24.0
- Remove upstreamed NVME patch
- spec clean up

* Sat Sep 19 2015 Mukundan Ragavan <nonamedotc@gmail.com> - 0.23.0-3
- Add patch to correctly recognize NVME devices
- Fixes bug #1258891

* Mon Sep 14 2015 Mukundan Ragavan <nonamedotc@gmail.com> - 0.23.0-2
- Removed hard dependencies on hdparm and btrfs-progs

* Mon Aug 03 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.23.0-1
- Update to 0.23.0
- Added btrfs-progs and hdparm as dependencies

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.22.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.22.0-1
- Update to 0.22.0

* Tue Mar 03 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.21.0-2
- Rebuild against updated glibmm to fix crash upon start

* Tue Jan 27 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.21.0-1
- Update to version 0.21.0

* Thu Dec 18 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.20.0-1
- Update to version 0.20.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Mukundan Ragavan <nonamedotc@gmail.com> - 0.19.1-2
- rebuilt to update

* Sun Aug 10 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.19.1-1
- Updated to latest upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Deji Akingunola <dakingun@gmail.com> - 0.18.0-1
- Update to version 0.18.0
- Replace consolehelper with PolicyKit for authenticating users

* Tue Jun 11 2013 Deji Akingunola <dakingun@gmail.com> - 0.16.1-2
- Explicitly requires usermode-gtk (BZ #827728) 

* Mon Jun 10 2013 Deji Akingunola <dakingun@gmail.com> - 0.16.1-1
- Update to version 0.16.1

* Fri Feb 22 2013 Deji Akingunola <dakingun@gmail.com> - 0.14.1-1
- Update to version 0.14.1
- Clean-up spec

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Deji Akingunola <dakingun@gmail.com> - 0.13.1-1
- Update to 0.13.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Rex Dieter <rdieter@fedoraproject.org> 0.12.0-3
- rebuild (parted)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2
- Rebuilt for c++ ABI breakage

* Wed Feb 22 2012 Deji Akingunola <dakingun@gmail.com> - 0.12.0-1
- Update to version 0.12.0

* Fri Jan 27 2012 Deji Akingunola <dakingun@gmail.com> - 0.11.0-1
- Update to version 0.11.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Deji Akingunola <dakingun@gmail.com> - 0.10.0-1
- Update to version 0.10.0

* Wed Oct 19 2011 Deji Akingunola <dakingun@gmail.com> - 0.9.1-1
- Update to version 0.9.1

* Wed Jul 20 2011 Deji Akingunola <dakingun@gmail.com> - 0.9.0-1
- Update to version 0.9.0

* Mon Jul 04 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.1-2
- Apply upstream patch to build with parted-3.0
- Enable parted dmraid support

* Sun Jun 26 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.1-1
- Update to version 0.8.1

* Thu Feb 17 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.0-1
- Update to version 0.8.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Deji Akingunola <dakingun@gmail.com> - 0.7.1-1
- Update to version 0.7.1

* Fri Oct 29 2010 Deji Akingunola <dakingun@gmail.com> - 0.7.0-1
- Update to version 0.7.0

* Sun Oct 17 2010 Deji Akingunola <dakingun@gmail.com> - 0.6.4-1
- Update to version 0.6.4

* Fri Aug 06 2010 Deji Akingunola <dakingun@gmail.com> - 0.6.2-1
- Update to version 0.6.2

* Mon Jun 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.6.0-1
- Update to version 0.6.0

* Thu Apr 01 2010 Mike McGrath <mmcgrath@redhat.com> - 0.5.2-1.1
- Rebuilt to fix broken parted dep

* Fri Mar 12 2010 Deji Akingunola <dakingun@gmail.com> - 0.5.2-1
- Update to version 0.5.2

* Tue Jan 26 2010 Deji Akingunola <dakingun@gmail.com> - 0.5.1-1
- Update to version 0.5.1

* Wed Jan 13 2010 Deji Akingunola <dakingun@gmail.com> - 0.5.0-1
- Update to version 0.5.0

* Mon Nov 16 2009 Deji Akingunola <dakingun@gmail.com> - 0.4.8-1
- New upstream version

* Mon Aug 10 2009 Deji Akingunola <dakingun@gmail.com> - 0.4.6-1
- New upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Deji Akingunola <dakingun@gmail.com> - 0.4.5-2
- Change e2fsprog-devel BR to libuuid-devel, and rebuild for parted soname bump

* Sat May 09 2009 Deji Akingunola <dakingun@gmail.com> - 0.4.5-1
- New upstream version

* Mon Apr 06 2009 Deji Akingunola <dakingun@gmail.com> - 0.4.4-1
- New upstream version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Deji Akingunola <dakingun@gmail.com> - 0.4.3-1
- New upstream version, fixes the automounting bug (RH #468953)

* Tue Feb 10 2009 Deji Akingunola <dakingun@gmail.com> - 0.4.2-1
- New upstream version

* Mon Dec 15 2008 Deji Akingunola <dakingun@gmail.com> - 0.4.1-1
- New upstream version

* Mon Sep 22 2008 Deji Akingunola <dakingun@gmail.com> - 0.3.9-1
- New upstream version
- Finally removed the 'preun' call that ensures the old gparted fdi (pre-FC6)
  file is removed on update

* Sun Jul 13 2008 Deji Akingunola <dakingun@gmail.com> - 0.3.8-1
- New upstream version

* Wed Apr 30 2008 Deji Akingunola <dakingun@gmail.com> - 0.3.7-1
- New upstream version

* Fri Mar 28 2008 Deji Akingunola <dakingun@gmail.com> - 0.3.6-1
- New upstream version

* Thu Feb 07 2008 Deji Akingunola <dakingun@gmail.com> - 0.3.5-1
- New upstream version

* Thu Nov 22 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-14
- Fix to detect full path to device/partition pathname (Bug #395071)

* Tue Oct 30 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-13
- Fix crash after refresh bug (Bug #309251, patch by Jim Hayward)
- Fix to use realpath properly (Bug #313281, patch by Jim Hayward)

* Wed Aug 22 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-12
- Rebuild

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-12
- License tag update

* Mon Jun 11 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-11
- Apply patch to only detect real devices, useful for correcting gparted slow 
 startup in situations when floppy drives don't exist but are enabled in bios
 (BZ #208821).

* Wed Apr 18 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-10
- Fix another typos in the run-gparted script

* Mon Apr 16 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-9
- Fix the typos and stupidity in the consolehelper and hal-lock files

* Wed Apr 04 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-8
- Explicitly require hal >= 0.5.9
- Remove the hal policy file created by gparted (if it's still there) on upgrade

* Tue Apr 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-7
- Patch gparted to not create a hal fdi file but use hal-lock instead, this will hopefully fix BZ #215657
- Clean up the spec file

* Wed Mar 21 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-6
- Rebuild for GNU parted-1.8.6

* Tue Mar 20 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-5
- Rebuild for GNU parted-1.8.5

* Wed Jan 24 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-4
- Re-write the consolehelpher stuff to work with latest pam

* Tue Jan 16 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-3
- The new parted is back, rebuild again

* Sat Jan 13 2007 Deji Akingunola <dakingun@gmail.com> - 0.3.3-2
- Rebuild for new parted

* Thu Dec 07 2006 Deji Akingunola <dakingun@gmail.com> - 0.3.3-1
- Bug fix release

* Tue Dec 05 2006 Deji Akingunola <dakingun@gmail.com> - 0.3.2-1
- New release

* Mon Nov 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.3.1-5
- Add more BRs

* Mon Nov 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.3.1-4
- Complete fix for parted check and apply patch on configure.in

* Thu Nov 23 2006 Deji Akingunola <dakingun@gmail.com> - 0.3.1-3
- Backport a fix from cvs to properly check for libparted version

* Tue Nov 21 2006 Deji Akingunola <dakingun@gmail.com> - 0.3.1-2
- Rebuild for new parted

* Wed Sep 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.3.1-1
- New version 0.3.1

* Tue Sep 05 2006 Deji Akingunola <dakingun@gmail.com> - 0.3-1
- New version 0.3

* Mon Aug 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.5-3
- Rebuild for FC6

* Mon May 22 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.5-2
- Rebuild

* Mon May 22 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.5-1
- Update to version 0.2.5

* Mon Apr 17 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.4-2
- Rebuild for new parted

* Wed Apr 12 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.4-1
- Update to newer version

* Thu Mar 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.3-1
- Update to newer version

* Tue Mar 07 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.2-1
- New release

* Mon Feb 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.2-2
- Rebuild for Fedora Extras 5

* Mon Jan 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.2-1
- New release

* Wed Jan 11 2006 Deji Akingunola <dakingun@gmail.com> - 0.1-1
- New release

* Fri Nov 25 2005 Deji Akingunola <dakingun@gmail.com> - 0.0.9-3
- Use correct source url

* Fri Nov 25 2005 Deji Akingunola <dakingun@gmail.com> - 0.0.9-2
- Add more buildrequires and cleanup spec file

* Fri Nov 25 2005 Deji Akingunola <dakingun@gmail.com> - 0.0.9-1 
- Update to latest released version

* Wed Oct 26 2005 Deji Akingunola <dakingun@gmail.com> - 0.0.8-1
- initial Extras release
