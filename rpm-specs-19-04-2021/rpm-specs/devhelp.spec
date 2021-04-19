%global tarball_version %%(echo %{version} | tr '~' '.')

Name: devhelp
Epoch: 1
Version: 40.0
Release: 1%{?dist}
Summary: API documentation browser

License: GPLv2+ and LGPL2+
URL: https://wiki.gnome.org/Apps/Devhelp
Source0: https://download.gnome.org/sources/%{name}/40/%{name}-%{tarball_version}.tar.xz

BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: itstool
BuildRequires: meson
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: libappstream-glib

Requires: devhelp-libs%{?_isa} = %{epoch}:%{version}-%{release}

# https://gitlab.gnome.org/GNOME/devhelp/-/merge_requests/21
Patch10001: 0001-Revert-Revert-Revert-the-introduction-of-the-amtk-li.patch

%description
Devhelp is an API documentation browser for the GNOME desktop.
It works natively with API documentation generated by gtk-doc.

%package libs
Summary: Library to embed Devhelp in other applications

%description libs
Devhelp is an API documentation browser for the GNOME desktop.
This package contains a library that can be used for embedding devhelp
into other applications such as IDEs.

%package devel
Summary: Library to embed Devhelp in other applications - Development files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Devhelp is an API documentation browser for the GNOME desktop.
This package contains the development files for the library that can be used
for embedding devhelp into other applications such as IDEs.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
%if 0%{?flatpak}
    -Dflatpak_build=true \
%endif
    -Dgtk_doc=true \
    -Dplugin_gedit=true \
    %{nil}

%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/devhelp

%find_lang devhelp --with-gnome

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Devhelp.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Devhelp.desktop

%files
%doc AUTHORS NEWS README.md
%license LICENSES/*

%{_bindir}/devhelp

%{_datadir}/applications/org.gnome.Devhelp.desktop
%{_datadir}/dbus-1/services/org.gnome.Devhelp.service
%{_datadir}/devhelp
%{_datadir}/glib-2.0/schemas/org.gnome.devhelp.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Devhelp.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Devhelp-symbolic.svg
%{_datadir}/metainfo/org.gnome.Devhelp.appdata.xml

%dir %{_libdir}/gedit
%dir %{_libdir}/gedit/plugins
%{_libdir}/gedit/plugins/devhelp.*
%{_mandir}/man1/devhelp.1*

%files libs -f devhelp.lang
%{_libdir}/libdevhelp-3.so.6*
%{_libdir}/girepository-1.0/Devhelp-3.0.typelib
%{_datadir}/glib-2.0/schemas/org.gnome.libdevhelp-3.gschema.xml

%files devel
%{_includedir}/devhelp-3/
%{_libdir}/libdevhelp-3.so
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/*
%{_datadir}/gir-1.0/Devhelp-3.0.gir

%changelog
* Thu Apr 15 2021 Ray Strode <rstrode@redhat.com> - 1:40.0-1
- Update to 40.0
- Drop amtk dependency

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 1:40~alpha-1
- Update to 40.alpha

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 1:3.38.1-1
- Update to 3.38.1

* Fri Sep 11 2020 Kalev Lember <klember@redhat.com> - 1:3.38.0-1
- Update to 3.38.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Kalev Lember <klember@redhat.com> - 1:3.37.1-1
- Update to 3.37.1

* Sat Apr 25 2020 Kalev Lember <klember@redhat.com> - 1:3.36.2-1
- Update to 3.36.2

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 1:3.36.1-1
- Update to 3.36.1

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 1:3.36.0-1
- Update to 3.36.0

* Tue Feb 04 2020 Kalev Lember <klember@redhat.com> - 1:3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 1:3.34.0-1
- Update to 3.34.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 1:3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.30.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Kalev Lember <klember@redhat.com> - 1:3.30.1-2
- Fix typo that prevented macro expansion

* Fri Oct 26 2018 Kalev Lember <klember@redhat.com> - 1:3.30.1-1
- Update to 3.30.1

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 1:3.30.0-2
- Rebuilt against fixed atk (#1626575)

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 1:3.30.0-1
- Update to 3.30.0
- Switch to the meson build system
- Use upstream screenshots in appdata
- Drop ldconfig scriptlets

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Kalev Lember <klember@redhat.com> - 1:3.28.1-1
- Update to 3.28.1

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 1:3.28.0-1
- Update to 3.28.0

* Tue Mar 06 2018 Kalev Lember <klember@redhat.com> - 1:3.27.90-1
- Update to 3.27.90

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.26.1-3
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.26.1-2
- Remove obsolete scriptlets

* Mon Dec 11 2017 Kalev Lember <klember@redhat.com> - 1:3.26.1-1
- Update to 3.26.1

* Sun Sep 10 2017 Kalev Lember <klember@redhat.com> - 1:3.26.0-1
- Update to 3.26.0

* Fri Aug 25 2017 Kalev Lember <klember@redhat.com> - 1:3.25.91-1
- Update to 3.25.91

* Sun Aug 06 2017 Kalev Lember <klember@redhat.com> - 1:3.25.2-1
- Update to 3.25.2
- Tighten soname globs

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.25.2-0.3.git56f8389
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.25.2-0.2.git56f8389
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Kalev Lember <klember@redhat.com> - 1:3.25.2-0.1.git56f8389
- Update to 3.25.2 git snapshot

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 1:3.25.1-1
- Update to 3.25.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 1:3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 1:3.23.92-1
- Update to 3.23.92

* Mon Feb 27 2017 Richard Hughes <rhughes@redhat.com> - 1:3.23.91-1
- Update to 3.23.91

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 1:3.22.0-1
- Update to 3.22.0

* Thu Sep 15 2016 Kalev Lember <klember@redhat.com> - 1:3.21.92-1
- Update to 3.21.92

* Wed Aug 31 2016 David King <amigadave@amigadave.com> - 3.21.91-1
- Update to 3.21.91

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 1:3.21.90-1
- Update to 3.21.90

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 1:3.20.0-3
- Run ldconfig for the new -libs subpackage

* Sat Apr 02 2016 Mathieu Bridon <bochecha@daitauha.fr> - 1:3.20.0-2
- Split the libs into their own subpackages, so that installing a dependent
  application (e.g Builder) does not bring in the Devhelp app.

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 1:3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 1:3.19.92-1
- Update to 3.19.92

* Mon Feb 15 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 1:3.19.3-1
- Update to 3.19.3

* Tue Oct 13 2015 Kalev Lember <klember@redhat.com> - 1:3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 1:3.18.0-1
- Update to 3.18.0

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 1:3.17.91-1
- Update to 3.17.91
- Use make_install macro

* Wed Jun 24 2015 David King <amigadave@amigadave.com> - 1:3.17.3-1
- Update to 3.17.3
- Add AppData validation in check
- Preserve timestamps during install

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.1-1
- Update to 3.16.1

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 1:3.16.0-2
- Use better AppData screenshots

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.15.92-1
- Update to 3.15.92

* Wed Mar 04 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 David King <amigadave@amigadave.com> - 1:3.15.90-1
- Update to 3.15.90
- Update URL
- Use license macro for COPYING
- Use pkgconfig for BuildRequires

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.92-1
- Update to 3.13.92

* Sun Aug 24 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.90-1
- Update to 3.13.90

* Fri Aug 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.4-4
- Update pkgconfig deps for webkitgtk4

* Fri Aug 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.4-3
- Switch to webkitgtk4
- Remove lib64 rpaths

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.4-1
- Update to 3.13.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 1:3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.91-1
- Update to 3.11.91

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.4-1
- Update to 3.11.4

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 1:3.10.2-1
- Update to 3.10.2

* Sun Oct 13 2013 Matthew Barnes <mbarnes@redhat.com> - 1:3.10.0-2
- Package vim and emacs support files. (#980448)

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.10.0-1
- Update to 3.10.0

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.90-1
- Update to 3.9.90

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.5-1
- Update to 3.9.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Matthias Clasen <mclasen@redhat.com> - 1:3.9.4-2
- Update url

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 1:3.9.4-1
- Update to 3.9.4

* Wed May 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.2-1
- Update to 3.8.2

* Wed Apr 17 2013 Richard Hughes <rhughes@redhat.com> - 1:3.8.1-1
- Update to 3.8.1

* Wed Mar 27 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.0-2
- Rebuilt for libwebkit2gtk soname bump

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.0-1
- Update to 3.8.0

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 1:3.7.91-1
- Update to 3.7.91

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.7.5-2
- Rebuilt for libwebkit2gtk soname bump

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.7.5-1
- Update to 3.7.5
- Remove the desktop file vendor prefix

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.7.3-1
- Update to 3.7.3
- Adapt for the GConf to gsettings conversion

* Wed Nov 14 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.1-1
- Update to 3.6.1
- Drop manual requires from -devel package; these are all picked up
  automatically with recent rpmbuild

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 1:3.6.0-1
- Update to 3.6.0

* Tue Sep 18 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.92-1
- Update to 3.5.92

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.5-1
- Update to 3.5.5

* Mon Jul 23 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.4.1-3
- Fix build (don't install icon cache)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Debarshi Ray <rishi@fedoraproject.org> - 1:3.4.0-1
- Update to 3.4.0

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.3.91-1
- Update to 3.3.91

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.3-1
- Update to 3.3.3

* Tue Oct 11 2011 Matthew Barnes <mbarnes@redhat.com> - 1:3.2.0-2
- Own /usr/lib/gedit and /usr/lib/gedit/plugins (RH bug #744884).

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 1:3.2.0-1
- Update to 3.2.0

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 1:3.0.0-2
- Update icon cache scriptlet

* Mon Apr  4 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Wed Mar 23 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.91.2-1
- Update to 2.91.91.2

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.91.1-1
- Update to 2.91.91.1

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- 2.91.90

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-4
- Rebuild for newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.91.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-2
- Rebuild

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.4-1
- Update to 2.91.4

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Mon Nov 15 2010 Kalev Lember <kalev@smartlink.ee> - 2.90.5-6
- Carry epoch over from F14 branch to preserve upgrade path
- Backported upstream patches to fix build with latest gtk3

* Thu Sep 09 2010 Bastien Nocera <bnocera@redhat.com> 2.90.5-5
- Fix broken schemas file, and "disabled_books" usage (#624198)

* Mon Aug 23 2010 Matthias Clasen <mclasen@redhat.com> - 2.90.5-4
- Incorporate a few upstream fixes

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.90.5-3
- recompiling .py files against Python 2.7 (rhbz#623286)

* Wed Jul 14 2010 Matthias Clasen <mclasen@redhat.com> - 2.90.5-2
- Fix platform check to work with GTK3

* Wed Jul 14 2010 Matthias Clasen <mclasen@redhat.com> - 2.90.5-1
- Update to 2.90.5

* Sat Jul  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-2
- Rebuild against new webkit

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Mon Feb 08 2010 Matthew Barnes <mbarnes@redhat.com> - 2.29.90-1
- Update to 2.29.90
- Remove patch for RH bug #543177 (fixed upstream).

* Wed Dec 02 2009 Matthew Barnes <mbarnes@redhat.com> - 2.29.3-2
- Add patch for RH bug #543177 (missing webkit-1.0 requirement).

* Tue Dec 01 2009 Bastien Nocera <bnocera@redhat.com> 2.29.3-1
- Update to 2.29.3

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Fri Aug 21 2009 Matthew Barnes <mbarnes@redhat.com> - 0.23.1-2
- Remove patch for GNOME bug #572022 to help fix RH bug #518481.

* Wed Aug 12 2009 Matthew Barnes <mbarnes@redhat.com> - 0.23.1-1
- Update to 0.23.1
- Remove patch for GNOME bug #588655 (fixed upstream).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Matthew Barnes <mbarnes@redhat.com> - 0.23-8
- Add patch for GNOME bug #588655 (work around GLib deprecations).

* Thu Jul  2 2009 Matthias Clasen <mclasen@redhat.com> - 0.23-7
- Shrink GConf schemas

* Sun Mar 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.23-6
Bumped to consume new soname in webkit library.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Matthew Barnes <mbarnes@redhat.com> - 0.23-4
- Disable strict-aliasing checks due to what looks like GLib breakage.

* Mon Feb 16 2009 - Bastien Nocera <bnocera@redhat.com> - 0.23-3
- Fix displaying web pages, WebKit doesn't like local filenames as URIs
- Add missing Gconf2-devel BR

* Fri Jan 23 2009 Matthias Clasen  <mclasen@redhat.com> - 0.23-2
- Cosmetic spec fixes

* Mon Jan 19 2009 Matthew Barnes <mbarnes@redhat.com> - 0.23-1
- Update to 0.23

* Fri Dec 05 2008 Matthew Barnes <mbarnes@redhat.com> - 0.22-2
- Drop the gecko requirement, since it uses WebKit now.

* Mon Dec 01 2008 Matthew Barnes <mbarnes@redhat.com> - 0.22-1
- Update to 0.22
- Add BR: WebKit-gtk-devel

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.21-4
- Rebuild for Python 2.6

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 0.21-3
- Tweak description

* Wed Sep 24 2008 Matthias Clasen <mclasen@redhat.com> - 0.21-2
- Rebuild against newer gecko

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 0.21-1
- Update to 0.21

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 0.20-1
- Update to 0.20

* Wed Jul 23 2008 Christopher Aillon <caillon@redhat.com> - 0.19.1-3
- Rebuild against newer gecko

* Mon Jul 07 2008 Matthew Barnes <mbarnes@redhat.com> - 0.19.1-2
- Rebuild, just to keep up with F9 package.

* Mon May 26 2008 Matthew Barnes <mbarnes@redhat.com> - 0.19.1-1
- Update to 0.19.1

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 0.19-5
- Fix source url

* Tue Feb 26 2008 Martin Stransky <stransky@redhat.com> - 0.19-4
- Rebuild against xulrunner

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.19-3
- Autorebuild for GCC 4.3

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 0.19-2.fc9
- Rebuild with GCC 4.3

* Thu Feb 07 2008 Matthew Barnes <mbarnes@redhat.com> - 0.19-1.fc9
- Update to 0.19

* Wed Jan 30 2008 Matthias Clasen <mclasen@redhat.com> - 0.18-1
- Update to 0.18

* Wed Jan 16 2008 Matthew Barnes <mbarnes@redhat.com> - 0.17-2.fc9
- Update version requirements based on configure.in.

* Mon Jan 07 2008 Matthew Barnes <mbarnes@redhat.com> - 0.17-1.fc9
- Update to 0.17
- Remove patch for GNOME bug #499050 (fixed upstream).

* Mon Dec 31 2007 Jeremy Katz <katzj@redhat.com> - 0.16.1-5
- Rebuild against newer xulrunner

* Thu Nov 22 2007 Martin Stransky <stransky@redhat.com> - 0.16.1-4.fc9
- Rebuild against xulrunner

* Fri Nov 09 2007 Matthew Barnes <mbarnes@redhat.com> - 0.16.1-3.fc9
- Rebuild against gecko-libs 1.8.1.9.

* Thu Nov 01 2007 Matthew Barnes <mbarnes@redhat.com> - 0.16.1-2.fc9
- Rebuild against gecko-libs 1.8.1.8.

* Sat Oct 06 2007 Matthew Barnes <mbarnes@redhat.com> - 0.16.1-1.fc8
- Update to 0.16.1

* Tue Sep 11 2007 Matthew Barnes <mbarnes@redhat.com> - 0.16-1.fc8
- Update to 0.16

* Wed Aug  8 2007 Christopher Aillon <caillon@redhat.com> - 0.15-4
- Rebuild against newer gecko

* Mon Aug  6 2007 Matthias Clasen <mclasen@redhat.com> - 0.15-3
- Update license field

* Fri Jul 20 2007 Kai Engert <kengert@redhat.com> - 0.15-2.fc8
- Rebuild against newer gecko

* Mon Jun 18 2007 Matthew Barnes <mbarnes@redhat.com> - 0.15-1.fc8
- Update to 0.15

* Tue Jun 05 2007 - Bastien Nocera <bnocera@redhat.com> - 0.14-4
- Rebuild again

* Mon Jun 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.14-3
- Rebuild against new libwnck

* Fri May 25 2007 Christopher Aillon <caillon@redhat.com> - 0.14-2
- Rebuild against newer gecko

* Fri May 18 2007 Matthew Barnes <mbarnes@redhat.com> - 0.14-1.fc8
- Update to 0.14
- Remove patch for RH bug #230837 (fixed upstream).

* Mon Apr 23 2007 Matthew Barnes <mbarnes@redhat.com> - 0.13-7.fc7
- Add patch for RH bug #230837 (initialize GThread).

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> - 0.13-6
- Don't install INSTALL

* Fri Mar 23 2007 Christopher Aillon <caillon@redhat.com> - 0.13-5
- Rebuild against newer gecko

* Wed Feb 28 2007 Matthew Barnes <mbarnes@redhat.com> - 0.13-4
- Rebuild against newer gecko.

* Mon Feb  5 2007 Matthias Clasen <mclasen@redhat.com> - 0.13-3
- Fix scriptlet errors

* Sun Feb 04 2007 Matthew Barnes <mbarnes@redhat.com> - 0.13-2.fc7
- Incorporate suggestions from package review.

* Sat Feb 03 2007 Matthew Barnes <mbarnes@redhat.com> - 0.13-1.fc7
- Update to 0.13
- Clean up the spec file.
- Remove devhelp-0.12-transparent.patch (fixed upstream).

* Thu Dec 21 2006 Christopher Aillon <caillon@redhat.com> 0.12-10
- Rebuild against newer gecko

* Sat Nov 25 2006 Matthias Clasen <mclasen@redhat.com> - 0.12-9
- Own the /usr/share/devhelp/books directory

* Fri Oct 27 2006 Christopher Aillon <caillon@redhat.com> - 0.12-8
- Rebuild against newer gecko

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 0.12-7
- Fix scripts according to the packaging guidelines
- Require pkgconfig in the -devel package

* Thu Oct 12 2006 Christopher Aillon <caillon@redhat.com> - 0.12-6.fc6
- Update requires to the virtual gecko version instead of a specific app

* Thu Sep 14 2006 Christopher Aillon <caillon@redhat.com> - 0.12-5.fc6
- Rebuild

* Mon Aug 14 2006 Matthias Clasen <mclasen@redhat.com> - 0.12-4.fc6
- Fix transparent headers

* Mon Aug 14 2006 Matthew Barnes <mbarnes@redhat.com> - 0.12-3
- Add missing Requires to devel package.

* Thu Aug 10 2006 Matthew Barnes <mbarnes@redhat.com> - 0.12-2
- Rebuild against firefox, again.

* Sat Jul 29 2006 Matthias Clasen <mclasen@redhat.com> - 0.12-1
- Update to 0.12
- Rebuild against firefox

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.11-4
- rebuild
- bump mozver

* Sun Feb 12 2006 Christopher Aillon <caillon@redhat.com> - 0.11-2
- Rebuild

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.11-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Dec 18 2005 Ray Strode <rstrode@redhat.com> - 0.11-1
- Update to 0.11

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Oct 18 2005 Christopher Aillon <caillon@redhat.com> - 0.10-6
- Build on ppc64

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 0.10-5
- fix the build

* Wed Aug 17 2005 Ray Strode <rstrode@redhat.com> 0.10.0-4
- rebuild

* Sun Jul 31 2005 Christopher Aillon <caillon@redhat.com> 0.10.0-3
- Rebuild against new mozilla

* Tue Jul 19 2005 Christopher Aillon <caillon@redhat.com> 0.10.0-2
- Rebuild against new mozilla
- Add builds for ia64 s390 s390x

* Thu May 19 2005 Ray Strode <rstrode@redhat.com> 0.10.0-1
- Update to 0.10.0 (bug #157753) 

* Fri May 13 2005 Christopher Aillon <caillon@redhat.com> 0.9.3-7
- Depend on mozilla 1.7.8

* Sat Apr 16 2005 Christopher Aillon <caillon@redhat.com> 0.9.3-6
- Depend on mozilla 1.7.7

* Thu Apr 14 2005 Ray Strode <rstrode@redhat.com> 0.9.3-5
- Don't crash on typeahead (bug #154398)

* Wed Mar  9 2005 Christopher Aillon <caillon@redhat.com> 0.9.3-4
- Depend on mozilla 1.7.6

* Sat Mar  5 2005 Christopher Aillon <caillon@redhat.com> 0.9.3-3
- Rebuild against GCC 4.0

* Sun Dec 19 2004 Christopher Aillon <caillon@redhat.com> 0.9.3-2
- Require mozilla 1.7.5

* Sun Dec 19 2004 Christopher Aillon <caillon@redhat.com> 0.9.3-1
- Update to 0.9.3

* Mon Oct 11 2004 Christopher Aillon <caillon@redhat.com> 0.9.2-2
- Rebuild to add ppc once again.

* Wed Sep 29 2004 Christopher Aillon <caillon@redhat.com> 0.9.2-1
- Update to 0.9.2
- Remove accel patch; its upstreamed now.

* Sun Sep 26 2004 Christopher Blizzard <blizzard@redhat.com> 0.9.1-6
- Rebuild without explicit mozilla release

* Fri Sep 24 2004 Christopher Blizzard <blizzard@redhat.com> 0.9.1-5
- Rebuild with explicit Mozilla version requires

* Wed Sep 22 2004 Christopher Aillon <caillon@redhat.com> 0.9.1-4
- Rebuilt to pick up new mozilla changes
- Drop ppc from the build since mozilla doesn't build there anymore.

* Wed Aug 25 2004 Christopher Aillon <caillon@redhat.com> 0.9.1-3
- Add Johan Svedberg's patch to add accelerators for back and forward 

* Mon Aug 09 2004 Christopher Aillon <caillon@redhat.com>
- Rebuild

* Wed Aug 04 2004 Christopher Aillon <caillon@redhat.com>
- Update to 0.9.1
- Remove ld-library patch. It is upstream now.

* Wed Jun 23 2004 Christopher Aillon <caillon@redhat.com>
- Update ExclusiveArch

* Tue Jun 22 2004 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 21 2004 Colin Walters <walters@redhat.com> 0.9-3
- Update patch to avoid (unlikely) security issue noticed
  by Jeremy Katz.

* Thu Apr 15 2004 Colin Walters <walters@redhat.com> 0.9-2
- Apply patch from George Karabin <gkarabin@pobox.com> to
  export LD_LIBRARY_PATH (closes bug 120220).

* Fri Apr  2 2004 Mark McLoughlin <markmc@redhat.com> 0.9-1
- Update to 0.9
- Install the schemas correctly
- Package /usr/bin/devhelp-bin
- Update requires/buildrequires
- Only build on platforms where mozilla is available

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 0.8.1-1
- update to 0.8.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Dec  1 2003 Jonathan Blandford <jrb@redhat.com> 0.7.0-1
- new version
- Remove .la and .a files.

* Wed Jul 30 2003 Jonathan Blandford <jrb@redhat.com>
- remove original devhelp desktop file.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat May 24 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add find_lang
