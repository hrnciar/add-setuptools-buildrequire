# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173674

%global minor_version 0.8

%global xfceversion 4.16

Name:           xfce4-xkb-plugin
Version:        0.8.2
Release:        2%{?dist}
Summary:        XKB layout switcher for the Xfce panel

License:        BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxklavier-devel >= 5.0
BuildRequires:  librsvg2-devel >= 2.18
BuildRequires:  garcon-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libwnck3-devel
Requires:       xfce4-panel >= %{xfceversion}
Requires:       xfce4-settings


%description
Xfce XKB layout switch plugin for the Xfce panel. It displays the current 
keyboard layout, and refreshes when layout changes. The layout can be 
switched by simply clicking on the plugin. For now the keyboard layouts 
cannot be configured from the plugin itself, they should be set in the 
XF86Config file or some other way (e.g. setxkbmap).

%prep
%setup -q


%build
%configure --disable-static
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%dir %{_datadir}/xfce4/xkb/
%dir %{_datadir}/xfce4/xkb/flags
%{_datadir}/xfce4/xkb/flags/*.svg

%changelog
* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.0-1
- Rebuilt for new upstream 0.8.0 release fixes, rhbz#1382421 and rhbz#1346078

* Fri Jun 16 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.1-6
- Spec clean up + silent rpmlint

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.1-2
- Added garcon-devel as buildrequires

* Sat Mar 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.5.6-5
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.6-1
- Update to 0.5.6 (fixes #965831, #970268, and #971092)

* Sat May 18 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5 (fixes #838373 and #926797)
- Also fixes several crashes: #834879, #869213, #870175, #901423, #904959

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4.3-2
- Build against libxfce4ui instead of libxfcegui4
- Make xfce4-panel version dependency conditional
- Add VCS tag
- Spec file cleanup

* Mon Oct 15 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4.3-1
- Update to 0.5.4.3 (#742744, #768737, #828307)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 0.5.4.1-5
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.5.4.1-4
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.4.1-2
- Rebuild for new libpng

* Wed May 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4.1-1
- Update to 0.5.4.1
- Remove all upstreamed patches

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Kevin Fenzi <kevin@tummy.com> - 0.5.3.3-5
- Rebuild for Xfce 4.8

* Thu Nov 25 2010 Fran??ois Cami <fcami@fedoraproject.org> - 0.5.3.3-4
- Fix segfault when adding a second keymap. Thanks to Lionel Le Folgoc (#597207)

* Fri Feb 12 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.3.3-3
- Fix various segfaults. Thanks to Lionel Le Folgoc (#525471, #547553)

* Mon Jan 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.3.3-2
- Add patch for libxklavier 5.0. Thanks to Caolan McNamara (#558083)

* Sun Aug 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.3.3-1
- Update to 0.5.3.3 (#502878)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Adam Jackson <ajax@redhat.com> 0.5.2-4
- xxp-0.5.2-xklavier-api.patch: Fix for new libxklavier API.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-2
- Rebuild for Xfce 4.6 (Beta 3)

* Thu Nov 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Thu Oct 02 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Mon Jul 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.3-5
- fix conditional comparison

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.3-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-3
- Rebuild for BuildID feature

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-2
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3 on Xfce 4.4.

* Sat Dec 09 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2.

* Fri Dec 01 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1 on Xfce 4.3.99.2.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-0.2.20060923svn
- Bump release for devel checkin.

* Sat Sep 23 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-0.1.20060923svn
- Update to svn snapshot of Sep 23rd 2006 on Xfce 4.3.99.1.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-3
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.5-2
- Require xfce4-panel.

* Fri Mar 31 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.5-1
- Update to 0.3.5.

* Fri Mar 17 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.4-1
- Update to 0.3.4.

* Fri Mar 10 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-1
- Update to 0.3.3.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-6
- Rebuild for Fedora Extras 5. 

* Fri Dec 30 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-5
- Changes for modular X: Add libXext-devel and libXpm-devel BuildReqs.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-4
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-3
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-2.fc4.cw
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-1.fc3.cw
- Initial RPM release.
