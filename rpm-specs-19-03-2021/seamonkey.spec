%bcond_without	system_nspr
%bcond_without	system_nss
%bcond_without	system_libvpx
%bcond_without	system_webp
%bcond_without	system_icu
%bcond_without	system_ffi
%bcond_with	system_hunspell
%bcond_with	system_cairo
%bcond_without	system_av1

%bcond_without	langpacks
%bcond_without	clang
%bcond_with	lto
%bcond_with	stylo

%bcond_without	calendar
%bcond_without	dominspector
%bcond_without	irc
%bcond_with	debugqa

%global nspr_version	4.25.0
%global nss_version	3.53.1
%global libvpx_version	1.5.0
%global webp_version	1.0.0
%global icu_version	63.1
%global ffi_version	3.0.9
%global hunspell_version 1.6.1
%global cairo_version	1.10
%global libaom_version	1.0.0
%global dav1d_version	0.1.1

%define homepage http://start.fedoraproject.org/

%define sources_subdir %{name}-%{version}

%define seamonkey_app_id	\{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a\}


Name:           seamonkey
Summary:        Web browser, e-mail, news, IRC client, HTML editor
Version:        2.53.6
Release:        1%{?dist}
URL:            http://www.seamonkey-project.org
License:        MPLv2.0


Source0:	http://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.xz
%if %{with langpacks}
Source1:	http://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source-l10n.tar.xz
%endif

Source3:	seamonkey-2.53.6-GNUmakefile
Source4:	seamonkey.desktop
Source5:	seamonkey.svg
Source12:	seamonkey-mail.desktop
Source13:	seamonkey-mail.svg

Patch3:		firefox-62-mozilla-1516803.patch
Patch5:		firefox-35-rhbz-1173156.patch
Patch6:		firefox-56-build-prbool.patch
Patch7:		firefox-51-mozilla-1005640.patch
Patch10:	firefox-56-mozilla-440908.patch
Patch11:	firefox-60-mozilla-1436242.patch
Patch13:	seamonkey-2.53.1-mozilla-revert-1332139.patch
Patch16:	firefox-52-rhbz-1451055.patch
Patch18:	seamonkey-2.53.3-clean-distroaddons.patch
Patch19:	seamonkey-2.53.5-system-av1.patch
Patch21:	seamonkey-2.53.5-media-document.patch
Patch22:	seamonkey-2.53.6-client_mk.patch
Patch23:	seamonkey-2.53.6-mozilla-1659298.patch
Patch24:	seamonkey-2.53.6-install_man.patch
Patch30:	seamonkey-2.53.5-nss_pkcs11_v3.patch
Patch31:	seamonkey-2.53.1-mozilla-526293.patch
Patch34:	seamonkey-2.53.3-startupcache.patch
Patch36:	seamonkey-2.53.3-locale-matchos-UI.patch

%{?with_system_nspr:BuildRequires:      nspr-devel >= %{nspr_version}}
%{?with_system_nss:BuildRequires:       nss-devel >= %{nss_version}}
%{?with_system_nss:BuildRequires:       nss-static >= %{nss_version}}
%{?with_system_libvpx:BuildRequires:    libvpx-devel >= %{libvpx_version}}
%{?with_system_webp:BuildRequires:      libwebp-devel >= %{webp_version}}
%{?with_system_icu:BuildRequires:       libicu-devel >= %{icu_version}}
%{?with_system_ffi:BuildRequires:       libffi-devel >= %{ffi_version}}
%{?with_system_hunspell:BuildRequires:  hunspell-devel >= %{hunspell_version}}
%{?with_system_cairo:BuildRequires:     cairo-devel >= %{cairo_version}}
%{?with_system_av1:BuildRequires:       libaom-devel >= %{libaom_version}}
%{?with_system_av1:BuildRequires:       libdav1d-devel >= %{dav1d_version}}

BuildRequires:  libpng-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  zlib-devel
BuildRequires:  zip
BuildRequires:  libIDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  gtk2-devel
BuildRequires:  GConf2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  krb5-devel
BuildRequires:  pango-devel
BuildRequires:  freetype-devel >= 2.1.9
BuildRequires:  glib2-devel
BuildRequires:  libXt-devel
BuildRequires:  libXrender-devel
BuildRequires:  coreutils
BuildRequires:  alsa-lib-devel
BuildRequires:  libnotify-devel
BuildRequires:  yasm >= 1.1
BuildRequires:  mesa-libGL-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  startup-notification-devel
%if %{without system_av1}
BuildRequires:  nasm >= 2.14
%endif

BuildRequires:  make
BuildRequires:  autoconf213
BuildRequires:  python27

%if %{with clang} || %{with stylo}
BuildRequires:	clang, llvm-devel
%endif
%if %{without clang}
BuildRequires:	gcc-c++ >= 6.1
%endif

BuildRequires:	rust >= 1.37
BuildRequires:	cargo

Requires:       mozilla-filesystem
Requires:       hicolor-icon-theme
Requires:       p11-kit-trust
%{?with_system_nspr:Requires:      nspr >= %{nspr_version}}
%{?with_system_nss:Requires:       nss >= %{nss_version}}

# ppc64:   http://bugzilla.redhat.com/bugzilla/866589
# armv7hl: http://bugzilla.redhat.com/bugzilla/1035485
# %{ix86}: no more supported upstream
ExclusiveArch:  x86_64

Provides: webclient


%description
SeaMonkey is an all-in-one Internet application suite (previously made
popular by Netscape and Mozilla). It includes an Internet browser,
advanced e-mail, newsgroup and feed client, a calendar, IRC client,
HTML editor and a tool to inspect the DOM for web pages. It is derived
from the application formerly known as Mozilla Application Suite.
 

%prep

%setup -q -c

mv %{sources_subdir} mozilla

%if %{with langpacks}
%setup -q -T -D -c -n %{name}-%{version}/l10n -a 1
#  come back...
%setup -q -T -D
%endif

cd mozilla

cp %{SOURCE3} GNUmakefile

%patch3 -p1 -b .1516803
%patch5 -p2 -b .1173156
%patch6 -p1 -b .prbool
%patch7 -p1 -b .1005640
%patch10 -p1 -b .440908
%patch11 -p1 -b .1436242
%{?with_system_libvpx:%patch13 -p1 -b .1332139}
%patch16 -p1 -b .1451055
%patch18 -p1 -b .clean_distroaddons
%patch19 -p1 -b .system_av1
%patch21 -p1 -b .media-document
#%patch22 -p1 -b .client_mk
%patch23 -p1 -b .1659298
%patch24 -p0 -b .install_man

%{?with_system_nss:%patch30 -p3 -b .nss_pkcs11_v3}
%patch31 -p3 -b .526293
%patch34 -p2 -b .startupcache
pushd comm
%patch36 -p1 -b .locale_matchos
popd

%if %{without calendar}
sed -i 's/MOZ_CALENDAR/UNDEF_MOZ_CALENDAR/' comm/suite/installer/package-manifest.in
%endif


#
#   generate .mozconfig
#

cat >.mozconfig <<EOF
ac_add_options --enable-application=comm/suite

export BUILD_OFFICIAL=1
export MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1

mk_add_options MOZ_OBJDIR=../obj-@CONFIG_GUESS@

ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --mandir=%{_mandir}

#  to know where to remove extra things...
ac_add_options --datadir=%{_datadir}
ac_add_options --includedir=%{_includedir}

ac_add_options --with-system-jpeg
ac_add_options --with-system-zlib
ac_add_options --with-system-bz2
ac_add_options --disable-tests
ac_add_options --disable-install-strip
ac_add_options --enable-default-toolkit=cairo-gtk3
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --enable-chrome-format=omni
ac_add_options --disable-necko-wifi
ac_add_options --enable-startup-notification
ac_add_options --enable-optimize=-O2

ac_add_options --enable-startupcache

%define with_sys()	ac_add_options --with%%{!?with_system_%1:out}-system-%1
%define endis_sys()	ac_add_options --%%{?with_system_%1:enable}%%{!?with_system_%1:disable}-system-%1
%define endis()		ac_add_options --%%{?with_%1:enable}%%{!?with_%1:disable}-%1

%{expand:%with_sys   nspr}
%{expand:%with_sys   nss}
%{expand:%with_sys   libvpx}
%{expand:%with_sys   webp}
%{expand:%with_sys   icu}
%{expand:%with_sys   av1}

%{expand:%endis_sys  ffi}
%{expand:%endis_sys  hunspell}
%{expand:%endis_sys  cairo}

#  always enable calendar to build needed internal components required for both bundled and external addons
ac_add_options --enable-calendar

%{expand:%endis dominspector}
%{expand:%endis irc}
%{expand:%endis debugqa}


ac_add_options --disable-webrender
ac_add_options %{?with_stylo:--enable-stylo=build}%{!?with_stylo:--disable-stylo}


%if %{with langpacks}
ac_add_options --with-l10n-base=../l10n
%endif

EOF
#  .mozconfig


#
#   generate default prefs
#
cat >all-fedora.js <<EOF

pref("app.update.auto", false);
pref("app.update.enabled", false);
pref("app.updatecheck.override", true);
pref("extensions.update.autoUpdateDefault", false);
pref("browser.display.use_system_colors", true);
pref("browser.helperApps.deleteTempFileOnExit", true);
pref("general.smoothScroll", true);
pref("intl.locale.matchOS",   true);
pref("intl.regional_prefs.use_os_locales", true);
pref("extensions.shownSelectionUI", true);
pref("extensions.autoDisableScopes", 0);
pref("shell.checkDefaultApps",   0);
pref("media.gmp-gmpopenh264.provider.enabled", false);
pref("media.gmp-gmpopenh264.autoupdate", false);
pref("media.gmp-gmpopenh264.enabled", false);
pref("gfx.xrender.enabled", true);
pref("devtools.webide.enabled", false);
pref("general.warnOnAboutConfig", false);

pref("browser.startup.homepage", "data:text/plain,browser.startup.homepage=%{homepage}");

/*  use system dictionaries (hunspell)   */
pref("spellchecker.dictionary_path", "%{_datadir}/myspell");

/* Allow sending credetials to all https:// sites */
pref("network.negotiate-auth.trusted-uris", "https://");

/* To avoid UA string garbling by the old instances of Lightning  */
lockPref("calendar.useragent.extra", "");

/* Completely mimic to Firefox for compatibility with this World nowadays...  */
pref("general.useragent.compatMode.strict-firefox", true);
/*  ...but do not confuse addon and account sites   */
pref("general.useragent.override.thunderbird.net", "Firefox/.*#SeaMonkey/%{version}");
pref("general.useragent.override.firefox.com", "Firefox/.*#SeaMonkey/%{version}");

/* Keep the same behaviour as for years  */
pref("browser.tabs.autoHide", true);

EOF
# all-fedora.js


%build

cd mozilla

%if %{with clang}
export CC=clang
export CXX=clang++
%endif

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed -e 's/-Wall//')
MOZ_LINK_FLAGS=

#  Still not handled by clang < 11
%if %{with clang}
MOZ_OPT_FLAGS=$(echo $MOZ_OPT_FLAGS | sed -e 's/-fstack-clash-protection//')
%endif

#  needed for -Werror=format-security
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -Wformat"
#  just temporary for gcc9 ...
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -Wno-format-overflow"

%if %{with lto}
%if %{with clang}
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -flto=thin"
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -flto=thin -fuse-ld=lld -Wl,-plugin-opt=-import-instr-limit=10"
export AR=llvm-ar
export RANLIB=llvm-ranlib
%else
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -flto -flifetime-dse=1"
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -flto=${MOZ_SMP_FLAGS#-j} -flifetime-dse=1"
export AR=gcc-ar
export RANLIB=gcc-ranlib
%endif
%else
#  avoid system-wide lto
%define _lto_cflags %{nil}
%endif

%if %(awk '/^MemTotal:/ { print $2 }' /proc/meminfo) <= 4200000
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -Wl,--no-keep-memory"
${CC:-%{__cc}} -x c $MOZ_LINK_FLAGS -Wl,--version -o /dev/null /dev/null | grep '^GNU ld ' && \
	MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -Wl,--reduce-memory-overheads"
%endif
  
export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS=$MOZ_OPT_FLAGS
export LDFLAGS=$MOZ_LINK_FLAGS


make %{?_smp_mflags}

%if %{with langpacks}
make -j1 locales
%endif


%install

cd mozilla

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_libdir}/seamonkey/removed-files
rm -f $RPM_BUILD_ROOT/%{_libdir}/seamonkey/libnssckbi.so

#   default prefs
install -p -m 644 all-fedora.js \
	$RPM_BUILD_ROOT/%{_libdir}/seamonkey/defaults/pref/all-fedora.js

install -d -m 755 $RPM_BUILD_ROOT/%{_libdir}/seamonkey/plugins || :


for ext in $RPM_BUILD_ROOT/%{_libdir}/seamonkey/extensions/langpack-*@seamonkey.mozilla.org.xpi
do
    lang=${ext##*langpack-}
    lang=${lang%@*}
    lang=${lang/-/_}
    echo "%%lang($lang) ${ext#$RPM_BUILD_ROOT}"
done >../seamonkey.lang


# install desktop files in correct directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE12}

# install icons
pushd $RPM_BUILD_ROOT%{_libdir}/seamonkey/chrome/icons/default
icons=$RPM_BUILD_ROOT%{_datadir}/icons/hicolor
# seamonkey icons
install -p -m 644 -D default16.png	$icons/16x16/apps/seamonkey.png
install -p -m 644 -D default.png	$icons/32x32/apps/seamonkey.png
install -p -m 644 -D default48.png	$icons/48x48/apps/seamonkey.png
install -p -m 644 -D default64.png	$icons/64x64/apps/seamonkey.png
install -p -m 644 -D default128.png	$icons/128x128/apps/seamonkey.png
install -p -m 644 -D %{SOURCE5}		$icons/scalable/apps/seamonkey.svg
# seamonkey mail icons
install -p -m 644 -D messengerWindow16.png	$icons/16x16/apps/seamonkey-mail.png
install -p -m 644 -D messengerWindow.png	$icons/32x32/apps/seamonkey-mail.png
install -p -m 644 -D messengerWindow48.png	$icons/48x48/apps/seamonkey-mail.png
install -p -m 644 -D %{SOURCE13}		$icons/scalable/apps/seamonkey-mail.svg
popd


# System extensions
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mozilla/extensions/%{seamonkey_app_id}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/extensions/%{seamonkey_app_id}


#  Only now and just define (not global)
%define __provides_exclude_from ^%{_libdir}/seamonkey
%define __requires_exclude     ^(%(find %{buildroot}%{_libdir}/seamonkey -name "lib*.so" -printf "%%f " | sed -e 's/.so /|/g' -e 's/|$//'))\\.so.*


%files -f seamonkey.lang

%license %{_libdir}/seamonkey/license.txt

%{_libdir}/seamonkey

%{_bindir}/seamonkey
%{_mandir}/*/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop

%dir %{_datadir}/mozilla/extensions/%{seamonkey_app_id}
%dir %{_libdir}/mozilla/extensions/%{seamonkey_app_id}


%changelog
* Fri Jan 22 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.6-1
- update to 2.53.6
- build with own GNUmakefile, spec file cleanup

* Tue Nov 17 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.5-3
- add media-document patch (mozbz#1677768)
- add packed_simd patch (mozbz#1617782)

* Sun Nov 15 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.5-2
- fix for av1 (mozbz#1490877)
- fix main svg icon

* Thu Nov 12 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.5-1
- update to 2.53.5
- add patch to build with system libaom and libdav1d
- add official logo icon in svg format

* Wed Sep  9 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.4-1
- update to 2.53.4
- replace all the distributed extensions (calendar, dominspector and irc)
  as intergated app-global extensions (ie. moved from distribution/extensions/
  just to extensions/ , mozbz#1659298)
- update seamonkey(1) manual page
- update description in spec file

* Thu Jul 30 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.3-3
- fix requires filter

* Wed Jul 29 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.3-2
- add "Default zoom" support (mozbz#1655362)
- add "Use system locale" switch in preferences (mozbz#1655842)
- backport WebP image format support (mozbz#1653869)
- update elfhack code up to esr68
- add fix for rust >= 1.45 (mozbz#1654465)
- properly filter provides and requires from the application dir
- spec file cleanups and fixes

* Mon Jul  6 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.3-1
- update to 2.53.3
- use sql nss databases (cert9.db, key4.db etc.) since the old format
  is stopping be supported.

* Mon May  4 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.2-1
- update to 2.53.2
- drop startup shell script (no more needed)

* Thu Apr  9 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-5
- rebuild with rust-1.42

* Wed Mar 25 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-4
- drop system-bookmarks dependencies

* Sat Mar 21 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-3
- fix localization for bundled calendar and chatzilla (#1815109)
- clear obsolete stuff from desktop-file-install

* Tue Mar  3 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.53.1-2
- add patch for classic theme (#1808197)

* Fri Feb 28 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.53.1-1
- Upgrade to 2.53.1
- use clang to build

* Mon Sep  9 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.5-2
- rebuid to properly handle external lightning extension (#1750450)

* Sat Aug 24 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.5-1
- update to 2.49.5
- add support for conditional build of inspector and irc

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.4-5
- add patch for new gettid() in glibc >= 2.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 2.49.4-4
- rebuilt (libvpx)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.49.4-2
- Rebuild with fixed binutils

* Fri Jul 27 2018 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.4-1
- update to 2.49.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.3-3
- Rebuild for ICU 62

* Wed May 16 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.3-2
- Rebuild for ICU 61.1

* Fri May  4 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.3-1
- update to 2.49.3

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.2-3
- Rebuild for ICU 61.1

* Sun Feb 18 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.2-2
- revert some upstream gtk3-related changes to avoid regressions
  since we still build with gtk2 (mozbz#1269145, mozbz#1398973)
- spec file cleanup from old deprecated stuff

* Sat Feb 17 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.2-1
- update to 2.49.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.1-4
- rebuild for libvpx 1.7.0

* Fri Jan 26 2018 Tom Callaway <spot@fedoraproject.org> 2.49.1-3
- rebuild for new libvpx

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> 2.49.1-2
- rebuild for hunspell 1.6.2

* Sat Oct 21 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.1-1
- update to 2.49.1
- apply some patches from firefox-52.4.0 package
- disable webide by default to avoid autoload of broken addons

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.48-1
- update to 2.48
- apply some patches from firefox-51 package
- use standard optimize level -O2 for compiling
- new langpacks obtaining stuff for more easier maintaining
- revert broken mozbz#1148544 changes for site-specific overrides

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.46-2
- fix for new system nss (#1414982, mozbz#1290037)
- fix build with system icu (mozbz#1329272)

* Fri Dec 23 2016 Dmitry Butskoy <Dmitry@Butskoy.name> 2.46-1
- update to 2.46
- apply some patches from firefox-49 package
- avoid runtime linking with too old ffmpeg libraries (#1330898)
- still enable XRender extension by default

