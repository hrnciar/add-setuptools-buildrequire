Name:           mumble
Version:        1.3.4
Release:        2%{?dist}
Summary:        Low-latency and high-quality voice-chat program
# The main source code is BSD licensed.
# The bundled libraries used are licensed as follows:
#   - arc4random: ISC
#   - celt-*: BSD, except for tools/getopt* files which are GPLv2+
#   - qqbonjour: BSD
#   - smallft: BSD
License:        BSD and ISC and GPLv2+
URL:            https://www.mumble.info
Source0:        https://github.com/mumble-voip/mumble/releases/download/%{version}/mumble-%{version}.tar.gz
Source2:        murmur.service
Source3:        mumble.appdata.xml

# downstream only patch
# https://docs.fedoraproject.org/en-US/packaging-guidelines/CryptoPolicies/
Patch0:         mumble-1.3.0-fedora-crypto-policy-cipher-list.patch

# https://github.com/mumble-voip/mumble/pull/3675
Patch1:         0001-Added-DBus-calls-to-activate-and-deactivate-push-to-talk.patch

# https://github.com/mumble-voip/mumble/commit/a8e0797f51877db699d01c37d962a75c08e38a92
Patch2:         0001-FIX-client-Update-rnnoise-src-submodule.patch

BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# qmake/lrelease.pri
BuildRequires:  qt5-linguist
# qmake/openssl.pri
BuildRequires:  pkgconfig(openssl)
# qmake/protobuf.pri
BuildRequires:  pkgconfig(protobuf)
# qmake/protoc.pri
BuildRequires:  protobuf-compiler
# qmake/python.pri
BuildRequires:  python3
# src/mumble/AudioInput.cpp
BuildRequires:  rnnoise-devel
# src/mumble/GlobalShortcut_unix.h
BuildRequires:  libXi-devel
# src/mumble/main.cpp
BuildRequires:  qt5-qtsvg-devel
# src/mumble/mumble_pch.hpp
BuildRequires:  boost-devel
# src/mumble/mumble.pro
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(speech-dispatcher)

# multiple files in 3rdparty/celt-0.7.0-src and 3rdparty/celt-0.11.0-src
BuildRequires:  libogg-devel

# appstream-util in %%check
BuildRequires:  libappstream-glib
# desktop-file-validate in %%check
BuildRequires:  desktop-file-utils

Provides:       bundled(arc4random)
Provides:       bundled(celt) = 0.7.0
Provides:       bundled(celt) = 0.11.0
Provides:       bundled(qqbonjour)
Provides:       bundled(smallft)


%description
Mumble is an Open Source, low-latency and high-quality voice-chat program
written on top of Qt and Opus.


%package -n murmur
Summary:        Mumble voice chat server
Provides:       mumble-server = %{version}-%{release}
# src/murmur/murmur_pch.h
BuildRequires:  libcap-devel
Requires(pre):  shadow-utils
# To be able to announce the presence of the server via Bonjour.
Recommends:     avahi

%{?systemd_requires}


%description -n murmur
Murmur(also called mumble-server) is part of the VoIP suite Mumble primarily
aimed at gamers. Murmur is the server component of the suite.


%package plugins
Summary:        Plugins for VoIP program Mumble
Requires:       %{name} = %{version}-%{release}


%description plugins
Mumble-plugins is part of VoIP suite Mumble primarily intended for gamers. This
plugin allows game linking so the voice of players will come from the direction
of their characters.


%package overlay
Summary:        Start games with the mumble overlay
Requires:       %{name} = %{version}-%{release}


%description overlay
Mumble-overlay is part of the Mumble VoIP suite aimed at gamers. If supported,
starting your game with this script will enable an ingame Mumble overlay.


%prep
%autosetup -p 1

pushd 3rdparty

# remove bundled libraries that we have system copies of
rm -r opus-src rnnoise-src speex-src speexdsp-src

# remove bundled libraries for windows
rm -r GL minhook-src xinputcheck-src

# remove bundled libraries for mac
rm -r mach-override-src

popd

# fix https://github.com/mumble-voip/mumble/issues/4857
sed -e '/VERSION = / s/1\.3\.3/1.3.4/' -i overlay_gl/overlay_gl.pro


%build
%{qmake_qt5} \
CONFIG+=no-bundled-speex \
CONFIG+=no-bundled-opus \
CONFIG+=no-bundled-rnnoise \
CONFIG+=no-g15 \
CONFIG+=no-oss \
CONFIG+=no-update \
CONFIG+=no-embed-qt-translations \
CONFIG+=no-ice \
CONFIG+=packaged \
CONFIG+=c++11 \
DEFINES+="PLUGIN_PATH=%{_libdir}/mumble" \
main.pro

%make_build release


%install
install -D -p -m 0755 release/mumble %{buildroot}%{_bindir}/mumble
install -D -p -m 0755 release/murmurd %{buildroot}%{_sbindir}/murmurd
ln -s murmurd %{buildroot}%{_sbindir}/mumble-server

# translations
install -d -m 0755 %{buildroot}%{_datadir}/mumble/translations
install -p -m 0644 src/mumble/*.qm %{buildroot}%{_datadir}/mumble/translations

# libraries
install -d -m 0755 %{buildroot}%{_libdir}/mumble
for f in release/*.so* release/plugins/*.so; do
    if [[ -L "$f" ]]; then
        cp -P "$f" %{buildroot}%{_libdir}/mumble/
    else
        install -p -m 0755 "$f" %{buildroot}%{_libdir}/mumble/
    fi
done

install -D -p -m 0664 scripts/murmur.ini %{buildroot}%{_sysconfdir}/murmur/murmur.ini
ln -s murmur/murmur.ini %{buildroot}%{_sysconfdir}/mumble-server.ini
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/murmur.service

install -D -p -m 0755 scripts/mumble-overlay %{buildroot}%{_bindir}/mumble-overlay

# man pages
install -D -p -m 0644 man/mumble.1 %{buildroot}%{_mandir}/man1/mumble.1
install -D -p -m 0644 man/murmurd.1 %{buildroot}%{_mandir}/man1/murmurd.1
install -D -p -m 0644 man/mumble-overlay.1 %{buildroot}%{_mandir}/man1/mumble-overlay.1

# icons
install -D -p -m 0644 icons/mumble.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mumble.svg

# desktop file
install -D -p -m 0644 scripts/mumble.desktop %{buildroot}%{_datadir}/applications/mumble.desktop

# appdata
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_metainfodir}/mumble.appdata.xml

# dir for mumble-server.sqlite
mkdir -p %{buildroot}%{_localstatedir}/lib/mumble-server/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/mumble.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/mumble.desktop


%pre -n murmur
getent group mumble-server >/dev/null || groupadd -r mumble-server
getent passwd mumble-server >/dev/null || \
    useradd -r -g mumble-server -d %{_localstatedir}/lib/mumble-server/ -s /sbin/nologin \
    -c "Mumble-server (murmur) user" mumble-server
exit 0


%post -n murmur
%systemd_post murmur.service


%preun -n murmur
%systemd_preun murmur.service


%postun -n murmur
%systemd_postun_with_restart murmur.service


%files
%license LICENSE
%doc README README.Linux CHANGES
%{_bindir}/mumble
%{_mandir}/man1/mumble.1*
%{_datadir}/icons/hicolor/scalable/apps/mumble.svg
%{_datadir}/applications/mumble.desktop
%{_metainfodir}/mumble.appdata.xml
%{_datadir}/mumble/
%dir %{_libdir}/mumble
%{_libdir}/mumble/libcelt0.so
%{_libdir}/mumble/libcelt0.so.0
%{_libdir}/mumble/libcelt0.so.0.7*
%{_libdir}/mumble/libcelt0.so.0.11*


%files -n murmur
%license LICENSE
%doc README README.Linux CHANGES
%{_sbindir}/murmurd
%{_unitdir}/murmur.service
%{_sbindir}/mumble-server
%config(noreplace) %attr(664,mumble-server,mumble-server) %{_sysconfdir}/murmur/murmur.ini
%config(noreplace) %{_sysconfdir}/mumble-server.ini
%{_mandir}/man1/murmurd.1*
%dir %attr(-,mumble-server,mumble-server) %{_localstatedir}/lib/mumble-server/


%files plugins
%{_libdir}/mumble/libl4d2.so
%{_libdir}/mumble/liblink.so
%{_libdir}/mumble/librl.so


%files overlay
%{_bindir}/mumble-overlay
%{_libdir}/mumble/libmumble.so
%{_libdir}/mumble/libmumble.so.1
%{_libdir}/mumble/libmumble.so.1.3
%{_libdir}/mumble/libmumble.so.%{version}
%{_mandir}/man1/mumble-overlay.1*


%changelog
* Wed Mar 17 2021 Carl George <carl@george.computer> - 1.3.4-2
- Enable RNNoise noise suppression
- Fixes: rhbz#1921721

* Sun Mar 14 2021 Carl George <carl@george.computer> - 1.3.4-1
- Latest upstream

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.3-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:32:14 CET 2021 Adrian Reber <adrian@lisas.de> - 1.3.3-2
- Rebuilt for protobuf 3.14

* Mon Dec 21 2020 Carl George <carl@george.computer> - 1.3.3-1
- Latest upstream rhbz#1885088
- Update license to reflect bundled libraries
- Add virtual provides for bundled libraries
- Remove celt071 dependency rhbz#1904471
- Remove obsolete for mumble-protocol
- Remove non-root ownership of murmurd
- Remove weblist perl and php scripts from %%doc

* Fri Sep 25 2020 Adrian Reber <adrian@lisas.de> - 1.3.2-2
- Rebuilt(2) for protobuf 3.13

* Fri Sep 25 2020 Carl George <carl@george.computer> - 1.3.2-1
- Latest upstream
- Add upstream patch for push-to-talk dbus calls

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.3.0-7
- Rebuilt for protobuf 3.13

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.3.0-4
- Rebuilt for protobuf 3.12

* Wed Jun 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-3
- mumble: drop qt5-qtbase-sqlite dep (#1832458)

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-2
- fix Qt5 deps

* Fri Mar 20 2020 Nils Philippsen <nils@tiptoe.de> - 1.3.0-1
- version 1.3.0
- update build deps, patches and drop obsolete ones
- build with Qt 5

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.2.19-14
- mumble-1.2.19-13: Unable to find matching CELT codecs with other clients (#1711435)
- support no_bundled_celt macro

* Thu May 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.2.19-13
- pull in more upstream fixes (ssl ciphers, opengl link flags)
- CONFIG+=no-oss

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.19-11
- Rebuild for protobuf 3.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.19-9
- drop deprecated libXevie-devel usage to fix FTBFS on rawhide

* Wed Mar 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.2.19-8
- fix FTBFS (#1555858)
- pull in upstream appdata (#1501525)
- use %%make_build %%{?systemd_requires}
- build in c++-11 mode (fixes FTBFS on s390x wrt protobuf)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.19-6
- Remove obsolete scriptlets

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2.19-5
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.19-4
- Rebuild for protobuf 3.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.19-1
- Rebuilt for new upstream release 1.2.19, fixes rhbz#1417330
- Added a patch to fix rhbz#1454438 until upstream fixes it
- Fixes rhbz#1462279 regarding desktop file

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.18-4
- Rebuild for protobuf 3.3.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.18-2
- Rebuild for protobuf 3.2.0

* Thu Dec 15 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.18-1
- Rebuilt for new upstream release 1.2.18, fixes rhbz #1293181

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.11-4
- Rebuild for protobuf 3.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 7 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.11-2
- Removed perl dependency and all deprecated d-bus rpc support

* Sun Dec 6 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.11-1
- Update to 1.2.11
- Added mumble-FixNoBindAtBoot.patch mumble-murmur_exit_on_no_bind.patch

* Wed Nov 25 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.10-4
- Hardened murmur.service
- Added patch to disable murmur.ini d-bus rpc - remove on 1.3.0

* Wed Nov 25 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.10-3
- Added ppc support
- Marked LICENSE with license tag
- Added patch to modify murmur.ini with PROFILE=SYSTEM sslCipher= setting

* Tue Nov 24 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.10-2
- Removed protocol subpkg, added Obsoletes mumble-protocol < 1.2.10-2
- Made recommended review changes (qmake_qt4, added parallel make, qt4-devel in favor of qt-devel)

* Tue Nov 24 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.10-1
- Update to 1.2.10
- Drop ice

* Tue Jan 13 2015 Carlos O'Donell <codonell@redhat.com> - 1.2.6-5
- Rebuilt against new ice-devel.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.2.6-2
- Rebuild for boost 1.55.0

* Sat May 17 2014 Christian Krause <chkr@fedoraproject.org> - 1.2.6-1
- Update 1.2.6
- Update fixes CVE-2014-3755 (BZ 1098231) and CVE-2014-3756 (BZ 1098233)

* Fri Apr 25 2014 Christian Krause <chkr@fedoraproject.org> - 1.2.5-1
- Update 1.2.5 (BZ 1062209)
- Update fixes CVE-2014-0044 (BZ 1061857) and CVE-2014-0045 (BZ 1061858)
- Add patch to fix an compile error with g++ 4.9.0
- Remove upstreamed patch for CVE-2012-0863

* Tue Aug 27 2013 Christian Krause <chkr@fedoraproject.org> - 1.2.4-1
- Update 1.2.4 (BZ 976001)
- New systemd-rpm macros (BZ 850218)
- Cleanup

* Mon Aug 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-16
- Fix FTBFS due to speechd
- Drop alsa-oss support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.2.3-14
- Rebuild for boost 1.54.0

* Wed Apr 03 2013 Christian Krause <chkr@fedoraproject.org> - 1.2.3-13
- Rebuild against new ice package
- Updated Ice version in patch0

* Sun Mar 17 2013 Christian Krause <chkr@fedoraproject.org> - 1.2.3-12
- Rebuild against new protobuf package

* Wed Feb 06 2013 Christian Krause <chkr@fedoraproject.org> - 1.2.3-11
- Rebuild against new ice package
- Updated Ice version in patch0
- Use new systemd-rpm macros (BZ 850218)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 Christian Krause <chkr@fedoraproject.org> - 1.2.3-9
- Fix startup issues of murmurd (BZ 711711, BZ 770469, BZ 771423)
- Fix migration to systemd
  http://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
- Fix directory ownership of %%{_libdir}/mumble and %%{_datadir}/mumble*
  (BZ 744886)
- Add upstream patch for CVE-2012-0863 (BZ 791058)
- Fix broken logrotate config file (BZ 730129)
- Add dependency for qt4-sqlite (BZ 660221)
- Remove /sbin/ldconfig from %%post(un) since mumble does not
  contain any libraries in %%{_libdir}
- Some minor cleanup

* Wed Apr 18 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.3-8
- Migrate to systemd, BZ 790040.

* Fri Mar 16 2012 Tom Callaway <spot@fedoraproject.org> - 1.2.3-7
- rebuild against fixed ice

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-5
- Updated Ice version in patch0
- Added new patch to build against celt071 includes thanks to Florent Le Coz

* Thu Nov 10 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-4
- rebuilt for protobuf update

* Mon Sep 12 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-3
- Rebuild for newer protobuf

* Tue May 17 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-2
- Added celt071 functionality
- Fixed the qmake args

* Wed Mar 30 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-1
- Update to 1.2.3
- Fixes vulnerability #610845
- Added patch to make it compile with Ice 3.4.0
- Added tmpfile.d config file for murmur

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 25 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-10
- Actually removed the requirement for redhat-lsb

* Tue Aug 03 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-9
- Removed redhat-lsb from Requires for murmur
- Updated initscript for murmur

* Sun May 16 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-8
- Rebuild for protobuf ABI change
- Added redhat-lsb to the Requires for murmur

* Sun May  2 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-7
- Fixed murmur's init script

* Sun Apr 18 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-6
- Fix for missing dbus-qt-devel on >F12

* Sun Apr 18 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-5
- Merged Mary Ellen Foster's changelog entry

* Tue Mar 30 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-4
- Marked the files in /etc as config entries

* Tue Mar 23 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-3
- Added desktop file for mumble11x

* Mon Feb 22 2010 Julian Golderer <j.golderer@novij.at> - 1.2.2-2
- Added mumble11x
- Added svg icons
- Added language files

* Sun Feb 21 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-1
- Update to 1.2.2
