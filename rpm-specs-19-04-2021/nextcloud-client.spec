%undefine __cmake_in_source_build
%undefine _cmake_skip_rpath
%global _hardened_build 1

Name:           nextcloud-client
Version:        3.2.0
Release:        1%{?dist}
Summary:        The Nextcloud Client

# -libs are LGPLv2+, rest GPLv2
License:        LGPLv2+ and GPLv2
Url:            https://nextcloud.com/install/#install-clients
Source0:        https://github.com/nextcloud/desktop/archive/v%{version}/desktop-%{version}.tar.gz
Source1:        nextcloud.appdata.xml
# The patch does 3 things:
#  - Depends on system lib for QtSingleApplication and QtLockedFile
#  - Remove the extraneous namespace when calling QtSingleApplication
#  - Fix a mismatch in the QtSingleApplication::messageReceived signal and the 
# Application::slotParseMessage slot
# These fix are needed because the system wide QtSingleApplication is slightly 
# different from the bundled one.
#Patch0:         %%{name}-%%{version}-syslibs.patch
Patch1: nextcloud-client-picpie.patch

BuildRequires:  check
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  inotify-tools-devel
BuildRequires:  libcloudproviders-devel
BuildRequires:  libappstream-glib
BuildRequires:  neon-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  python3-sphinx
BuildRequires:  qtlockedfile-qt5-devel
BuildRequires:  qtkeychain-qt5-devel
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-gui
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtwebengine-devel
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  extra-cmake-modules
# Plasma 5 Dolphin integration
%if 0%{?fedora} >= 24 || 0%{?rhel} > 7
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-rpm-macros
%endif
BuildRequires:  sqlite-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} < 33
# concerning libgnome-keyring read https://bugzilla.redhat.com/show_bug.cgi?id=1652973
Requires:       libgnome-keyring
%endif

Provides: mirall = %{version}-%{release}
Obsoletes: mirall < 1.8.0

# Read https://bugzilla.redhat.com/show_bug.cgi?id=1651261
ExcludeArch: ppc64 ppc64le s390x

%description
Nextcloud-client enables you to connect to your private Nextcloud Server.
With it you can create folders in your home directory, and keep the contents
of those folders synced with your Nextcloud server. Simply copy a file into
the directory and the Nextcloud Client does the rest.


%package libs
Summary: Common files for nextcloud-client
License: LGPLv2+
Provides: mirall-common = %{version}-%{release}
Obsoletes: mirall-common < 1.8.0
Requires: %{name}%{?_isa} = %{version}-%{release}

%description libs
Provides common files for nextcloud-client such as the
configuration file that determines the excluded files in a sync.


%package devel
Summary: Development files for nextcloud-client
License: LGPLv2+
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
Provides: mirall-devel = %{version}-%{release}
Obsoletes: mirall-devel < 1.8.0

%description devel
Development headers for use of the nextcloud-client library

%package nautilus
Summary: nextcloud client nautilus extension
Requires: nautilus
Requires: nautilus-python
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: mirall-nautilus = %{version}-%{release}
Obsoletes: mirall-nautilus < 1.8.0


%description nautilus
The nextcloud desktop client nautilus extension.

%package nemo
Summary:        Nemo overlay icons
Requires:       nemo
Requires:       nemo-python
Requires: %{name}%{?_isa} = %{version}-%{release}

%description nemo
This package provides overlay icons to visualize the sync state
in the nemo file manager.

# Only Fedora has Mate, so there is no need for Caja extension on EPEL
%if 0%{?fedora}
%package caja
Summary:        Caja overlay icons
Requires:       caja
Requires:       python3-caja
Requires: %{name}%{?_isa} = %{version}-%{release}

%description caja
This package provides overlay icons to visualize the sync state
in the caja file manager.
%endif

%if 0%{?fedora} >= 24 || 0%{?rhel} > 7
%package dolphin
Summary:        Dolphin overlay icons
Requires:       dolphin
Requires: %{name}%{?_isa} = %{version}-%{release}

%description dolphin
The nextcloud desktop client dolphin extension.
%endif

%prep
%setup -q -n desktop-%{version}
%patch1 -p1
#rm -rf src/3rdparty/qtlockedfile src/3rdparty/qtsingleapplication

%build
%cmake_kf5 \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" \
  -DNO_SHIBBOLETH=1

%cmake_build

%install
%cmake_install

%find_lang client --with-qt
mkdir -p %{buildroot}%{_datadir}/appdata/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/nextcloud.appdata.xml


# for distros that do not have KDE Plasma 5
%if 0%{?fedora} < 24 && 0%{?rhel} <= 7
rm -f %{buildroot}%{_libdir}/libnextclouddolphinpluginhelper.so
rm -f %{buildroot}%{_kf5_plugindir}/overlayicon/nextclouddolphinoverlayplugin.so
rm -f %{buildroot}%{_qt5_plugindir}/nextclouddolphinactionplugin.so
rm -f %{buildroot}%{_kf5_datadir}/kservices5/nextclouddolphinactionplugin.desktop
%endif


# Only Fedora has Mate, so there is no need for Caja extension on EPEL
%if 0%{?rhel}
rm -rf %{buildroot}%{_datadir}/caja-python/
%endif


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/nextcloud.appdata.xml

%ldconfig_scriptlets libs

%if 0%{?fedora} >= 24 || 0%{?rhel} > 7
%ldconfig_scriptlets dolphin
%endif

%files -f client.lang
%{_bindir}/nextcloud
%{_bindir}/nextcloudcmd
%{_datadir}/mime/packages/nextcloud.xml
%{_datadir}/applications/com.nextcloud.desktopclient.nextcloud.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/appdata/nextcloud.appdata.xml
%{_datadir}/cloud-providers/com.nextcloudgmbh.Nextcloud.ini
%{_datadir}/dbus-1/services/com.nextcloudgmbh.Nextcloud.service

%files libs
%{_libdir}/libnextcloudsync.so.0
%{_libdir}/libnextcloudsync.so.%%{version}
%{_libdir}/libnextcloud_csync.so*
%doc README.md
%config %{_sysconfdir}/Nextcloud/sync-exclude.lst
%dir %{_sysconfdir}/Nextcloud

%files devel
%{_includedir}/nextcloudsync/
%{_libdir}/libnextcloudsync.so

%files nautilus
%{_datadir}/nautilus-python/extensions/*

%files nemo
%{_datadir}/nemo-python/extensions/*

# Only Fedora has Mate, so there is no need for Caja extension on EPEL
%if 0%{?fedora}
%files caja
%{_datadir}/caja-python/extensions/*
%endif

%if 0%{?fedora} >= 24 || 0%{?rhel} > 7
%files dolphin
%{_libdir}/libnextclouddolphinpluginhelper.so
%{_kf5_plugindir}/overlayicon/nextclouddolphinoverlayplugin.so
%{_qt5_plugindir}/nextclouddolphinactionplugin.so
%{_kf5_datadir}/kservices5/nextclouddolphinactionplugin.desktop
%endif

%changelog
* Thu Apr 08 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Thu Mar 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Tue Dec 22 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- Add qtbase-private as buildrequires

* Fri Oct 30 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3

* Fri Oct 02 2020 Jeff Law <law@redhat.com> - 3.0.2-2
- Use -fPIC rather than -fPIE.  Re-enable LTO.

* Sat Sep 26 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Thu Sep 10 2020 Nick Bebout <nb@fedoraproject.org> - 3.0.1-2
- Disable LTO 

* Sat Sep 05 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1
- Drop upstreamed patches

* Mon Aug 31 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.6.5-9
- Only require libgnome-keyring on Fedora (not EPEL). EPEL8 is getting qtkeychain 0.10.0

* Mon Aug 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.6.5-8
- %%check: verify correct rpath/runpath

* Mon Aug 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.6.5-7
- restore use of %%cmake_kf5, explicitly undefine _cmake_skip_rpath (#1871655)

* Tue Aug 04 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.5-6
- Change cmake macros to fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.5-3
- Require libgnome-keyring only for <=f32

* Tue Jul 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.5-2
- Reinstate libgnome-keyring requires.

* Fri Jul 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.5-1
- 2.6.5

* Thu Jun 18 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.4-5
- Drop requires on libgnome-keyring (not needed with qtkeychain >= 0.10.0)

* Mon Apr 27 2020 Germano Massullo <germano.massullo@gmail.com> - 2.6.4-4
- Added Requires: libgnome-keyring Read https://bugzilla.redhat.com/show_bug.cgi?id=1652973

* Sun Apr 12 2020 Tim Klocke <taaem@mailbox.org> - 2.6.4-3
- Fixed autostart when using libcloudproviders
- Fixed recently changed files in libcloudproviders support

* Sun Apr 05 2020 Germano Massullo <germano.massullo@gmail.com> - 2.6.4-2
- Added libcloudproviders support. Thanks to Tim Klocke
- Added BuildRequires: libcloudproviders-devel BuildRequires: pkgconfig(dbus-1)

* Thu Mar 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.4-1
- 2.6.4

* Mon Feb 17 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.3-1
- Update to 2.6.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.6.2-1
- 2.6.2

* Wed Nov 06 2019 Germano Massullo <germano.massullo@gmail.com> - 2.6.1-1
- 2.6.1 release
- Replaced  Requires:python-caja with Requires:python3-caja in caja subpackage

* Fri Oct 04 2019 Germano Massullo <germano.massullo@gmail.com> - 2.6.0-1
- 2.6.0 release

* Sun Sep 08 2019 Germano Massullo <germano.massullo@gmail.com> - 2.6.0.rc1-0.1
- 2.6.0 RC1

* Wed Aug 28 2019 Germano Massullo <germano.massullo@gmail.com> - 2.5.3-1
- 2.5.3 release
- drop the icon patch because it has been fixed upstream.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Germano Massullo <germano.massullo@gmail.com> - 2.5.2-2
- added issue_1000.patch

* Thu Apr 11 2019 Germano Massullo <germano.massullo@gmail.com> - 2.5.2-1
- 2.5.2 release
- Changed python2-sphinx requirement to python3-sphinx

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Germano Massullo <germano@germanomassullo.org> - 2.5.1-1
- 2.5.1 release

* Mon Nov 19 2018 Germano Massullo <germano@germanomassullo.org> - 2.5.0-2
- added ExcludeArch: ppc64, ppc64le, s390. Read https://bugzilla.redhat.com/show_bug.cgi?id=1651261

* Thu Nov 15 2018 Germano Massullo <germano@germanomassullo.org> - 2.5.0-1
- 2.5.0 release

* Wed Aug 15 2018 Germano Massullo <germano.massullo@gmail.com> - 2.5.0-0.1
- 2.5.0 beta 1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.0-1
- 2.4.0 release
- Updated syslibs patch, thanks to Robert-Andr?? Mauchin
- Added comment to syslibs patch, thanks to Robert-Andr?? Mauchin
- updated nextcloud client theming to 2.3.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Nick Bebout <nb@fedoraproject.org> - 2.3.3-2
- Change to BR python2-sphinx instead of python-sphinx

* Mon Sep 11 2017 Nick Bebout <nb@fedoraproject.org> - 2.3.3-1
- update to 2.3.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Germano Massullo <germano.massullo@gmail.com> - 2.3.2-2
- added macros to build Caja subpackage only in Fedora, not EPEL (Mate is Fedora only)
- added macro to build Dolphin (Plasma 5) subpackage only in Fedora >= 24 && EPEL > 7 (EPEL7 ships KDE 4)

* Sat Jun 03 2017 Germano Massullo <germano.massullo@gmail.com> - 2.3.2-1
- Removed no longer necessary OpenSSL patch
- 2.3.2 release
- Remove caja extension hack. Included in upstream

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Kalev Lember <klember@redhat.com> - 2.2.4-8
- Fix appdata file name to match with desktop file name
* Mon Jan 02 2017 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.2.4-7
- Add caja extension
* Mon Jan 02 2017 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.2.4-6
- Fix the desktop icon (#1409252)
* Thu Dec 08 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.2.4-5
- Epel7: drop dolphin files since they are not included in build for Epel7
* Wed Nov 23 2016 Nick Bebout <nb@fedoraproject.org> - 2.2.4-4
- Update for review
* Wed Nov 02 2016 Germano Massullo <germano.massullo@gmail.com> 2.2.4-3
- First release
