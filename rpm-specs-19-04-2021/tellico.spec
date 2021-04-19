Name:           tellico
Version:        3.3.4
Release:        2%{?dist}
Summary:        A collection manager

License:        GPLv2
URL:            http://tellico-project.org/
Source0:        http://tellico-project.org/files/tellico-%{version}.tar.xz

%if (0%{?rhel} || (0%{?fedora} && 0%{?fedora} < 33))
%undefine __cmake_in_source_build
%endif

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)

# non mandatory
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Sane)
BuildRequires:  cmake(KF5Cddb)
BuildRequires:  cmake(KF5FileMetaData)

BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  gettext
BuildRequires:  libgcrypt-devel
BuildRequires:  taglib-devel
BuildRequires:  libyaz-devel
BuildRequires:  exempi-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  libcdio-devel
BuildRequires:  libcsv-devel
BuildRequires:  libv4l-devel
# required for btparse (as this package has the btparse.h header file)
BuildRequires:  perl-Text-BibTeX

Requires: python3

%description
Tellico is a collection manager by KDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections. Unlimited user-defined
fields are allowed. Filters are available to limit the visible entries by
definable criteria. Full customization for printing is possible through
editing the default XSLT file. It can import CSV, Bibtex, and Bibtexml and
export CSV, HTML, Bibtex, Bibtexml, and PilotDB. Entries may be imported
directly from Amazon.com.


%prep
%autosetup -p1

# There are just two scripts
sed \
  -i.python \
  -e "s|^#!/usr/bin/env python$|#!%{__python3}|g" \
  src/fetch/scripts/*.py

%build
%{cmake_kf5} -DENABLE_WEBCAM:BOOL=ON
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-kde --with-html


%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_kf5_bindir}/tellico
%{_kf5_datadir}/applications/org.kde.tellico.desktop
%{_kf5_datadir}/kconf_update/*
%{_kf5_datadir}/tellico/
%{_kf5_datadir}/config.kcfg/tellico_config.kcfg
%{_kf5_datadir}/kxmlgui5/tellico/
%{_sysconfdir}/xdg/tellicorc
%{_sysconfdir}/xdg/tellico-script.knsrc
%{_sysconfdir}/xdg/tellico-template.knsrc
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/mime/packages/tellico.xml
%{_kf5_metainfodir}/org.kde.tellico.appdata.xml


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 José Matos <jamatos@fedoraproject.org> - 3.3.4-1
- update to 3.3.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Fix cmake changes
- Apply upstream patch to allow for new FindTaglib.cmake in ECM 5.72

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul  3 2020 José Matos <jamatos@fedoraproject.org> - 3.3.1-1
- update to 3.3.1

* Tue Mar 31 2020 Adrian Reber <adrian@lisas.de> - 3.2.3-2
- Rebuilt for libcdio-2.1.0

* Thu Feb 13 2020 José Matos <jamatos@fedoraproject.org> - 3.2.3-1
- update to 3.2.3
- update python scripts to be python3 compatible

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Nikola Forró <nforro@redhat.com> - 3.2.1-4
- rebuilt for exempi 2.5.1

* Mon Sep 02 2019 Nikola Forró <nforro@redhat.com> - 3.2.1-3
- fix FTBFS (bug #1746013)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 José Matos <jamatos@fedoraproject.org> - 3.2.1-1
- update to 3.2.1 (qimageblitz dependecy was removed from the project)

* Wed May 29 2019 José Matos <jamatos@fedoraproject.org> - 3.2-3
- disable qimageblitz since it brings Qt 4 and it crashes tellico

* Tue May 28 2019 José Matos <jamatos@fedoraproject.org> - 3.2-2
- Add the remaing unsupported optional extensions

* Tue May 28 2019 José Matos <jamatos@fedoraproject.org> - 3.2-1
- 3.2

* Thu Feb 14 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.1.4-1
- 3.1.4
- use %%autosetup %%make_build

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 05 2018 Luigi Toscano <luigi.toscano@tiscali.it> - 3.1.2-1
- Update to 3.1.2
- Adapt the spec file to the base requirements (Qt5/KF5)
- Add two new dependencies (libcdio and libcsv) and remove the old
  tcp_wrapper dependency

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.12-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.12-7
- Rebuilt to fix FTBFS

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.12-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.3.12-1
- 2.3.12, .spec cleanup, fix kdemm detection, drop BR: libart_gpl (kde3)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 José Matos <jamatos@fedoraproject.org> - 2.3.11-1
- update to 2.3.11
- drop nepomuk dependency

* Fri Feb 19 2016 Rex Dieter <rdieter@fedoraproject.org> 2.3.10-5
- rebuild (dropping nepomuk support for f24+)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.10-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 José Matos <jamatos@fedoraproject.org> - 2.3.10-1
- update to 2.3.10
- x-tellico.desktop is gone

* Wed Sep 24 2014 José Matos <jamatos@fedoraproject.org> - 2.3.9-1
- update to 2.3.9
- add appdata file

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.8-6
- update scriptlets, BR: +libkcddb-devel -kdemultimedia-devel

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 José Matos <jamatos@fedoraproject.org> - 2.3.8-3
- rebuild for new yaz version (applies to Fedora 21+)

* Fri Jul 12 2013 José Matos <jamatos@fedoraproject.org> - 2.3.8-1
- update to 2.3.8

* Fri Feb  8 2013 José Matos <jamatos@fedoraproject.org> - 2.3.7-1
- New bugfix release
- Add qjson as build requirement

* Thu Jul 26 2012 José Matos <jamatos@fedoraproject.org> - 2.3.6-1
- New bug fix release
- Remove conditional code for releases older than Fedora 7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 2.3.5-2
- Rebuild (poppler-0.20.0)

* Tue Mar  6 2012 José Matos <jamatos@fedoraproject.org> - 2.3.5-1
- New bugfix release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 José Matos <jamatos@fedoraproject.org> - 2.3.4-1
- New upstream release

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 2.3.3-2
- Rebuild (poppler-0.17.3)

* Mon Sep  5 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.3.3-1
- Update to upstream 2.3.3
- Drop GCC 4.6 and libvl patches, applied upstream

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 2.3.2-3
- Rebuild (poppler-0.17.0)

* Fri Jul 01 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.2-2
- s/kdegraphics-devel/pkgconfig(libksane)/

* Fri Feb 11 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.3.2-1
- Update to upstream 2.3.2.  Fixes bugs with bibtex, amongst others.
- Add patches from upstream SVN to fix build with GCC 4.6.x and use
  version 1 of v4l API for barcode support so that it compiles with
  newer kernels.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 26 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.3-1
- Update to tellico 2.3 (#622431)

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.2-3
- recompiling .py files against Python 2.7 (rhbz#623410)

* Wed Apr  7 2010 José Matos <jamatos@fc.up.pt> - 2.2-2
- Rebuild for new libyaz (F14+).

* Wed Feb 24 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.2-1
- Update to upstream version 2.2

* Sat Nov 21 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.1.1-1
- Update to 2.1.1, fixes data loss issue with filters

* Wed Nov 18 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.1-2
- Add BR: libv4l-devel and re-enable webcam support

* Sat Nov  7 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.1-1
- Update to latest upstream 2.1

* Mon Sep 21 2009 José Matos <jamatos@fc.up.pt> - 2.0-1
- stable release

* Sat Sep 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.0-0.2.pre2
- use %%_kde4_* macros
- optimize scriptlets
- update URL, Source0

* Fri Sep 11 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.0-0.1.pre2
- Update to upstream version 2.0 pre-release 2
- Drop gcc4 patch, now upstream

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.3.5-1
- Update to latest upstream (1.3.5)
- Add a patch from upstream SVN r3410 which fixes build with GCC 4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.4-3
- Rebuild for Python 2.6

* Fri Nov 28 2008 Caolán McNamara <caolanm@redhat.com> - 1.3.4-2
- rebuild for dependencies

* Thu Sep 18 2008 José Matos <jamatos@fc.up.pt> - 1.3.4-1
- update to 1.3.4

* Thu Jul 17 2008 José Matos <jamatos[AT]fc.up.pt> - 1.3.3-1
- update to 1.3.3

* Sun May 25 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.3.2.1-1
- Updated to latest upstream (1.3.2.1)

* Thu May 22 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.3.1-3
- Only kdepim3-devel if <= F-9, the KDE3 version of kdepim has been been
  removed from F-10/rawhide.

* Tue May 20 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.3.1-2
- Rebuild for new deps.

* Wed Mar 19 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.3.1-1
- New upstream release (1.3.1)

* Mon Feb  4 2008 José Matos <jamatos[AT]fc.up.pt> - 1.3-5
- Unify spec file for F7-F9.

* Sat Feb  2 2008 José Matos <jamatos[AT]fc.up.pt> - 1.3-4
- Fix build dependency on poppler (qt version).

* Fri Feb  1 2008 José Matos <jamatos[AT]fc.up.pt> - 1.3-3
- Add support to parse pdf metadata.

* Wed Jan 30 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.3-2
- Enable webcam support.
- Install missing MIME file.

* Wed Jan 30 2008 José Matos <jamatos[AT]fc.up.pt> - 1.3-1
- New release.

* Wed Dec 12 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> - 1.2.14-6
- Remove BR: kdemultimedia3-devel, no longer available

* Wed Dec 12 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> - 1.2.14-5
- Rebuild for new kdemultimedia

* Fri Dec 07 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> - 1.2.14-4
- Specify kde{libs,multimedia,pim}3-devel for BR (kdelibs-devel now provides KDE 4)

* Thu Dec  6 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.14-3
- Rebuild for new libssl (F9+).

* Thu Sep 27 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.14-2
- Declare new file (due to the fix for Fedora 7).

* Thu Sep 27 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.14-1
- New upstream version (fixes problem with settings not being saved on Fedora).

* Mon Aug 27 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.13-2
- License fix, rebuild for devel (F8).

* Sat Aug 11 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.13-1
- New upstream version.

* Wed Jul 25 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.12-1
- New upstream version.

* Thu Jun  7 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.11-1
- New upstream version.

* Sat Apr 21 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.10-1
- New upstream version.

* Thu Mar  8 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.9-1
- Update to 1.2.9.

* Tue Feb  6 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.8-1
- New upstream version.

* Mon Feb  5 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.7-3
- Condicionalize the BR for tcp_wrappers, it has a proper devel file
  for Fedora >= 7.

* Tue Jan 30 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.7-2
- BR tcp_wrappers.

* Tue Jan 30 2007 José Matos <jamatos[AT]fc.up.pt> - 1.2.7-1
- New upstream version.

* Mon Dec  4 2006 José Matos <jamatos[AT]fc.up.pt> - 1.2.6-1
- New upstream version.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.2.2-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 José Matos <jamatos[AT]fc.up.pt> - 1.2.2-1
- Revert desktop file to original one, and drop vendor.
- New upstream release.
- Pass --disable-rpath to configure.

* Sun Sep  3 2006 José Matos <jamatos[AT]fc.up.pt> - 1.2-2
- --vendor=fedora
- Use correct capitalization for Summary
- Remove useless entries in docs.

* Fri Sep  1 2006 José Matos <jamatos[AT]fc.up.pt> - 1.2-1
- Submitted to Fedora Extras (loosely based on Dag and Dries version)
