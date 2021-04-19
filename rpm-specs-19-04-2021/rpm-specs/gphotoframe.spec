# Please check again if someone wants to import
# this also to EPEL.

# Upstream uses hg for SCM
# googlecode now no longer provide source, create
# it from SCM
#
# hg clone https://code.google.com/p/gphotoframe/
# cd gphotoframe/
# hg archive -t tbz2 "gphotoframe-<version>-hg%h.tar.bz2"

%global	hghash		2084299dffb6

%global	mainver	2.0.2
#%%define	minorver	-b1

%global	mainrel	12

%global	rpmminorver	%(echo "%minorver" | sed -e 's|^-||' | sed -e 's|\\\.||')
%global	fedorarel	%{?minorver:0.}%{mainrel}%{?minorver:.%rpmminorver}%{?hghash:.hg%hghash}

%global	build_gss	1
%if 0%{?fedora} >= 33
%global	build_gss	0
%endif

Name:		gphotoframe
Version:	%{mainver}
Release:	%{fedorarel}%{?dist}
Summary:	Photo Frame Gadget for the GNOME Desktop

# GPLv3 seems safer than GPLv3+
# Some image files are under GPLv2+
# Documents under help/ directory are under GFDL
License:	GPLv3 and GPLv2+ and GFDL
URL:		http://code.google.com/p/gphotoframe/
#Source0:	http://gphotoframe.googlecode.com/files/%{name}-%{mainver}%{?minorver}.tar.gz
Source:	%{name}-%{mainver}%{?minorver}%{?hghash:-hg%hghash}.tar.bz2
# bug 1078155
# The following file missing
#Source1:	https://gphotoframe.googlecode.com/hg/share/assistant_facebook.glade

# Handle exif file with zero denominator on geometry information
# bug 845418
Patch2:	gphotoframe-2.0a2-parseexif-geom-zerovalue.patch
# Fix yet another case on exif information with zero denominator
# bug 885377
Patch3:	gphotoframe-1.5.1-parseexif-fraction-zerodiv.patch
# Support python-twisted 13.x API
#Patch4:	gphotoframe-2.0-a3-twisted-13-API.patch
# https://git.gnome.org/browse/gdk-pixbuf/commit/?id=112eab418137df2d2f5f97e75fb48f17e7f771e7
# gdk-pixbuf 2.31.2 changed API
Patch4:	gphotoframe-2.0.1-gdk-pixbuf2-2_31_2_API.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1296817
# disable libproxy support for now
Patch5:	gphotoframe-2.0.2-disable-libproxy.patch
# F-26+: Switch to WebKit2 (on Fedora: it is webkitgtk4)
Patch6:	gphotoframe-2.0.2-WebKit2.patch
# F-31+: Switch to python3
Patch100:	gphotoframe-2.0.2-python3.patch
# F-34: Patch to support feedparser 6
Patch101:	gphotoframe-2.0.2-feedparser-6.patch
# F-33+: Patch for python3x: bunch of fixes for plugins, mainly for authentification
Patch102:	gphotoframe-2.0.2-plugin-bunch-fix-py3x.patch
# Limit number of times for checking idle status when service is not available
# to shutdown warning
Patch103:	gphotoframe-2.0.2-idle-check-limit-time.patch
# python3x: fix for urlget
Patch104:	gphotoframe-2.0.2-urlget-py3.patch
# Move help URL according to freedesktop specification
Patch105:	gphotoframe-2.0.2-help-url-spec.patch
# Again, Patch for python3x: fixes for plugins, mainly for configuring plugins
Patch106:	gphotoframe-2.0.2-plugin-bunch-fix-py3x-02.patch

BuildRequires:	GConf2
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	python3-devel
BuildRequires:	python3-distutils-extra
# For creating symlink -> python-bytecompiling
#BuildRequires:	python3-exif
# From 1.2-b6: setup.py needs this
BuildRequires:	python3-pyxdg
# Documents
BuildRequires:	%{_bindir}/xsltproc
BuildRequires:	%{_bindir}/xml2po

# Mandatory
Requires:	python3-gobject
#Requires:	python3-exif
Requires:	python3-twisted
Requires:	python3-pyxdg
# lib/plugins/tumblr/account.py
#Requires:	python2-oauth

# girepository
Requires:	gtk3
Requires:	webkitgtk4
# Optional
# see bug 1296817
# Requires:	libproxy-python
# girepository
Requires:	clutter-gtk
Requires:	python3-feedparser
# girepository
Requires:	libchamplain-gtk
# Scriptlets
%if !%{build_gss}
Obsoletes:	%{name}-gss < 2.0.2-5.9999
%endif

Requires(pre):	GConf2

BuildArch:	noarch

%description
Gnome Photo Frame is a photo frame gadget for the GNOME Desktop.

%if %{build_gss}
%package	gss
Summary:	Compatibility package of %{name} for gnome-screensaver
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-screensaver

%description	gss
This package contains scripts and desktop files of %{name}
for gnome-screensaver compatibility.
%endif

%prep
%setup -q -n %{name}-%{mainver}%{?minorver}%{?hghash:-hg%hghash}

%patch2 -p2 -b .zeroden -Z
%patch3 -p1 -b .zeroden2 -Z
%patch4 -p1 -b .pixbuf_23102 -Z
%patch5 -p1 -b .libproxy_disable -Z
%patch6 -p1 -b .wk2 -Z

# Remove unneeded shebangs
grep -rl '^#![ \t]*%{_bindir}' lib/ | \
	xargs sed -i -e '\@^#![ \t]*%{_bindir}@d'

# install missing glade file
# bug 1078155
#cp -p %%{SOURCE1} share/
sed -i.glade \
	-e "s|'share/menu.ui',|'share/menu.ui','share/assistant_facebook.glade',|" \
	setup.py

# Explicitly don't use clutter-gtk for now
# Enable again with 2.0-a3
%if 0
grep -rl 'import clutter' lib/ | \
	xargs sed -i -e 's|import clutter|import dont_use_clutter|'
%endif

%if 0
# Use system-wide EXIF
ln -sf %{python_sitelib}/EXIF.py lib/utils/EXIF.py
%endif

# Once doing this
grep -rlZ "/usr/bin/python$" . | xargs --null sed -i -e 's|/usr/bin/python$|/usr/bin/python2|'
# Then patch
%patch100 -p1 -b .py3 -Z
%patch101 -p1 -b .feedparser6 -Z
%patch102 -p1 -b .bunchfix -Z
%patch103 -p1 -b .idle -Z
%patch104 -p1 -b .urlget_py3 -Z
%patch105 -p1 -b .helpurl -Z
%patch106 -p1 -b .py3_config -Z

%build
# Do nothing
#%%{__python} setup.py build

%install
mkdir -p %{buildroot}

%{__python3} setup.py install \
%if 0
	--skip-build \
%endif
	--root %{buildroot} \
	--prefix %{_prefix} \
	%{nil}

%if 0
# And again use system-wide EXIF.py
ln -sf %{python_sitelib}/EXIF.py \
	%{buildroot}%{python_sitelib}/%{name}/utils/EXIF.py
%endif

# Gsettings Schemas
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
install -cpm 0644 \
	share/com.googlecode.gphotoframe.gschema.xml.in \
	%{buildroot}%{_datadir}/glib-2.0/schemas/com.googlecode.gphotoframe.gschema.xml

# Desktop
desktop-file-validate \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Move help documents according to freedesktop specification
for lang in \
	C it ja \
	%{nil}
do
	mkdir -p %{buildroot}%{_datadir}/help/${lang}/%{name}
	mv \
		%{buildroot}%{_datadir}/gnome/help/%{name}/${lang}/* \
		%{buildroot}%{_datadir}/help/${lang}/%{name}
	if [ -f %{buildroot}%{_datadir}/help/${lang}/%{name}/%{name}.xml ]
	then
		mv \
			%{buildroot}%{_datadir}/help/${lang}/%{name}/%{name}.xml \
			%{buildroot}%{_datadir}/help/${lang}/%{name}/index.docbook
	fi
done
# Cleanups
find %{buildroot}%{_datadir}/gnome/help/ -type d | sort -r | xargs rmdir

# gnome-screensver related
# FIXME: I don't use gnome-screensaver...
mkdir -p \
	%{buildroot}%{_libexecdir}/gnome-screensaver
# ignore failure (if any) for screensaver desktop
desktop-file-validate \
	%{buildroot}%{_datadir}/applications/screensavers/gphotoframe-screensaver.desktop || true
# lib/ is hardcoded in setup.py
mv %{buildroot}%{_prefix}/lib/gnome-screensaver/gnome-screensaver/gphotoframe-screensaver \
	%{buildroot}%{_libexecdir}/gnome-screensaver/

%if !%{build_gss}
rm -rf \
	%{buildroot}%{_libexecdir}/gnome-screensaver/ \
	%{buildroot}%{_datadir}/applications/screensavers/ \
	%{nil}
%endif

find %{buildroot}%{_prefix} -name \*.py3 -delete

%find_lang %{name}

%if 0
# Treak brp-python-bytecompile
%global	__os_install_post_orig		%{__os_install_post}
%global	__os_install_post \
	%__os_install_post_orig \
	for f in %{python_sitelib}/EXIF.py* \
	do \
		ln -sf $f %{buildroot}%{python_sitelib}/%{name}/utils/$(basename $f) \
	done \
	%{nil}
%endif

%pre
%gconf_schema_obsolete %{name}

%files	-f %{name}.lang
%defattr(-,root,root,-)
%doc	COPYING
%doc	GPL
%doc	README
%doc	changelog

%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/

%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/*.ui
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.glade
#%%{_datadir}/%{name}/*.svg
%{_datadir}/%{name}/extra/
%{_datadir}/%{name}/history/

#%%{_datadir}/gnome/help/%%{name}/
%{_datadir}/help/*/%{name}/
%{_datadir}/omf/%{name}/

#%%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/glib-2.0/schemas/com.googlecode.%{name}.gschema.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*

%{_datadir}/appdata/%{name}.appdata.xml

%if %{build_gss}
%files	gss
%defattr(-,root,root,-)
%{_libexecdir}/gnome-screensaver/%{name}-screensaver
%{_datadir}/applications/screensavers/%{name}-screensaver.desktop
%endif

%changelog
* Tue Mar 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-12.hg2084299dffb6
- Another fix for python3 for plugins - mainly for configuration

* Sun Mar 28 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-11.hg2084299dffb6
- Move help documentation according to freedesktop specification

* Wed Mar 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-10.hg2084299dffb6
- py3: fix for urlget

* Tue Mar 16 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-9.hg2084299dffb6
- python3x: bunch of fixes, mainly for plugins
- Limit number of times for checking idle status when service is not available
  to shutdown warnings

* Sat Mar 13 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-8.hg2084299dffb6
- Make tumblr plugin work again
- set timestamp when applying patch

* Fri Mar 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-7.hg2084299dffb6
- Support feedparser 6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6.hg2084299dffb6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-6.hg2084299dffb6
- Kill gss support on F-33+

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-5.hg2084299dffb6.3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5.hg2084299dffb6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-5.hg2084299dffb6.1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-5.hg2084299dffb6
- Switch to python3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-4.hg2084299dffb6
- Explicitly use python2 on shebang

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.2-3.hg2084299dffb6.3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.2
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-3.hg2084299dffb6
- F-26+: switch to WebKit2 (on Fedora: webkitgtk4)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2.hg2084299dffb6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2.hg2084299dffb6.2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-2.hg2084299dffb6
- F-23+: disable libproxy support for now (bug 1296817)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-1.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-1.hg2084299dffb6
- 2.0.2

* Thu Jan  1 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-3.hg0eed26d75481
- A Happy New Year
- Adjust for gdk-pixbuf 2.31.2 API

* Fri Dec  5 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-2.hg0eed26d75481
- Add appdata

* Tue Dec  2 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-1.hg82fdb3350fbd
- 2.0.1

* Wed Nov 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-0.1.b1.hga78a9b1d0cee
- 2.0.1-b1

* Sun Nov  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-1.hg4fb32b74a755
- 2.0 release, and hg 1 commit ahead

* Mon Jul 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-0.6.a3
- Support python-twisted 13.x API

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.5.a3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-0.5.a3
- Add missing glade file for tumblr authentification (bug 1078155)

* Wed Nov 13 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-0.4.a3
- 2.0-a3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.a2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.a2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-0.3.a2
- Fix yet another case on exif information with zero denominator
  (bug 885377)

* Mon Aug 19 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0-0.2.a2
- Fix traceback when choosing photo source on setting gui
- Fix traceback when choosing folder plugin on setting gui
- Handle exif file with zero denominator on geometry information

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.1.a2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0-0.1.a2
- 2.0-a2

* Thu Mar 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.1-2
- Fix scriptlet type name

* Mon Mar  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.1-1
- 1.5.1

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5-1
- 1.5

* Sun Jan  8 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5-0.2.rc1
- 1.5 rc1

* Tue Dec 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5-0.1.b1
- 1.5 b1

* Wed Nov 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.1-1
- 1.4.1

* Fri Nov 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.1-0.1.b1
- 1.4.1-b1

* Tue Jul  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4-1
- 1.4

* Thu Jun 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4-0.2.rc1
- 1.4 rc1

* Sun Jun 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4-0.1.b2
- 1.4 b2

* Sun Apr 17 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3-1
- 1.3

* Tue Apr 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3-0.3.rc2
- 1.3 rc2

* Sat Apr  2 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.2.b2
- 1.3 b2

* Thu Mar 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3-0.1.b1
- Try 1.3 b1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2-1
- 1.2 formal

* Thu Jan 27 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2-0.3.rc1
- 1.2 rc1

* Tue Jan 18 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2-0.2.b6
- Update to 1.2b6

* Mon Dec 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2-0.1.b4
- Update to 1.2b4
- And pull patch from hg head to fix gnome-screensaver related dbus error

* Sat Oct 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1-1
- Update to 1.1

* Tue Jul 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-14: rebuild against python 2.7

* Sun Jul 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-2
- Fix license tag
- Remove unneeded macro definition

* Sat Jul 24 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-1
- Initial packaging

