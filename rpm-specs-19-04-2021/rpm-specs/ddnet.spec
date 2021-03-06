# Enable Ninja build
%bcond_without ninja_build

Name:           ddnet
Version:        15.3.2
Release:        1%{?dist}
Summary:        DDraceNetwork, a cooperative racing mod of Teeworlds

# Disabled while can't fix build
ExcludeArch: s390x

#
# CC-BY-SA
# --------------------------------------
# data/languages/
# data/fonts/DejaVuSans.ttf
# data/fonts/SourceHanSansSC-Regular.otf
#
# ASL 2.0
# --------------------------------------
# data/
#
# MIT
# --------------------------------------
# man/
#
# Public domain
# --------------------------------------
# src/base/hash_libtomcrypt.c
#


License:        zlib and CC-BY-SA and ASL 2.0 and MIT and Public Domain
URL:            https://ddnet.tw/
Source0:        https://github.com/ddnet/ddnet/archive/%{version}/%{name}-%{version}.tar.gz

# Disable network lookup test because without internet access tests not pass
Patch1:         0001-Disabled-network-lookup-test.patch

# Unbundle md5
Patch2:         0002-Unbundle-md5.patch

# Unbundle json-parser
Patch3:         0003-Unbundle-json-parser.patch

# Fix missing header for gcc-11
Patch4:         ddnet-gcc11.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%if %{with ninja_build}
BuildRequires:  ninja-build
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3

BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(json-parser)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)

# pkgconfig not available
BuildRequires:  pnglite-devel

Requires:       %{name}-data = %{version}-%{release}

# https://github.com/ddnet/ddnet/issues/2019
Provides:       bundled(dejavu-sans-cjkname-fonts)
Provides:       bundled(adobe-source-han-sans-sc-fonts)


%description
DDraceNetwork (DDNet) is an actively maintained version of DDRace,
a Teeworlds modification with a unique cooperative gameplay.
Help each other play through custom maps with up to 64 players,
compete against the best in international tournaments, design your
own maps, or run your own server.


%package        data
Summary:        Data files for %{name}

Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme

BuildArch:      noarch

%description    data
Data files for %{name}.


%package        server
Summary:        Standalone server for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    server
Standalone server for %{name}.


%prep
%autosetup -p1
touch CMakeLists.txt

# Remove bundled stuff...
rm -rf src/engine/external


%build
# WebSockets disable because it freezes all GUI | https://github.com/ddnet/ddnet/issues/1900
%cmake \
    %{?with_ninja_build: -GNinja} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPREFER_BUNDLED_LIBS=OFF \
    -DAUTOUPDATE=OFF \
    ..

%if %{with ninja_build}
%ninja_build -C %{_target_platform}
%else
%cmake_build -C %{_target_platform}
%endif


%install
%if %{with ninja_build}
%ninja_install -C %{_target_platform}
%else
%cmake_install -C %{_target_platform}
%endif

# Install man pages...
install -Dp -m 0644 man/DDNet.6 %{buildroot}%{_mandir}/man6/DDNet.6
install -Dp -m 0644 man/DDNet-Server.6 %{buildroot}%{_mandir}/man6/DDNet-Server.6


%check
%if %{with ninja_build}
%ninja_build run_tests -C %{_target_platform}
%else
%cmake_build run_tests -C %{_target_platform}
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%license license.txt
%doc README.md
%{_mandir}/man6/DDNet.6*

%{_bindir}/DDNet
%{_libdir}/%{name}/

%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/*.appdata.xml

%files data
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files server
%{_mandir}/man6/DDNet-Server.6*

%{_bindir}/DDNet-Server


%changelog
* Sun Feb 21 2021 ElXreno <elxreno@gmail.com> - 15.3.2-1
- Update to version 15.3.2

* Mon Feb 15 2021 ElXreno <elxreno@gmail.com> - 15.3.1-1
- Update to version 15.3.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 ElXreno <elxreno@gmail.com> - 15.2.5-2
- Drop gdb workaround

* Sat Jan  2 14:07:53 +03 2021 ElXreno <elxreno@gmail.com> - 15.2.5-1
- Update to version 15.2.5

* Thu Dec 17 09:29:16 +03 2020 ElXreno <elxreno@gmail.com> - 15.2.4-1
- Update to version 15.2.4

* Tue Nov 17 23:28:01 +03 2020 ElXreno <elxreno@gmail.com> - 15.2.2-1
- Update to version 15.2.2

* Thu Oct 15 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 15.1.3-1
- Update to 15.1.3 (#1888766)

* Tue Oct 13 2020 Jeff Law <law@redhat.com> - 15.1.2-2
- Fix missing #include for gcc-11
* Mon Oct 12 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 15.1.2-1
- Update to 15.1.2 (#1887463)

* Sun Oct 11 21:25:06 +03 2020 ElXreno <elxreno@gmail.com> - 15.1.1-1
- Update to version 15.1.1

* Sun Sep 27 20:47:43 +03 2020 ElXreno <elxreno@gmail.com> - 15.0.5-1
- Update to version 15.0.5

* Mon Sep 21 2020 ElXreno <elxreno@gmail.com> - 15.0.4-1
- Update to version 15.0.4

* Wed Sep 09 2020 ElXreno <elxreno@gmail.com> - 14.7.1-1
- Update to version 14.7.1

* Sun Aug 30 2020 ElXreno <elxreno@gmail.com> - 14.5.1-1
- Update to version 14.5.1

* Wed Aug 19 2020 ElXreno <elxreno@gmail.com> - 14.4-1
- Update to version 14.4

* Tue Aug 11 2020 ElXreno <elxreno@gmail.com> - 14.3.2-1
- Update to version 14.3.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 ElXreno <elxreno@gmail.com> - 14.2-1
- Updated to version 14.2

* Tue Jul 07 2020 ElXreno <elxreno@gmail.com> - 14.1-1
- Updated to version 14.1

* Mon Jun 29 2020 ElXreno <elxreno@gmail.com> - 14.0.3-1
- Updated to version 14.0.3

* Sat Jun 06 2020 ElXreno <elxreno@gmail.com> - 13.2.2-1
- Updated to version 13.2.2

* Fri May 29 2020 ElXreno <elxreno@gmail.com> - 13.2.1-1
- Updated to version 13.2.1

* Thu May 28 2020 ElXreno <elxreno@gmail.com> - 13.2-1
- Updated to version 13.2

* Fri May 01 2020 ElXreno <elxreno@gmail.com> - 13.1-1
- Updated to version 13.1

* Tue Apr 14 2020 ElXreno <elxreno@gmail.com> - 13.0.2-1
- Updated to version 13.0.2

* Wed Apr 08 2020 ElXreno <elxreno@gmail.com> - 13.0.1-1
- Updated to version 13.0.1

* Tue Apr 07 2020 ElXreno <elxreno@gmail.com> - 13.0-1
- Updated to version 13.0

* Sat Feb 22 2020 ElXreno <elxreno@gmail.com> - 12.9.2-1
- Updated to version 12.9.2

* Fri Feb 14 2020 ElXreno <elxreno@gmail.com> - 12.9.1-1
- Updated to version 12.9.1
- Disabled build for s390x arch

* Thu Feb 13 2020 ElXreno <elxreno@gmail.com> - 12.9-2
- Fixed build error for Rawhide

* Thu Feb 13 2020 ElXreno <elxreno@gmail.com> - 12.9-1
- Updated to version 12.9

* Wed Jan 01 2020 ElXreno <elxreno@gmail.com> - 12.8.1-6
- Applied patch by @atim
- Added license breakdown explanation
- Unbundled md5 and json-parser
- Removed hicolor-icon-theme from main package

* Tue Dec 31 2019 ElXreno <elxreno@gmail.com> - 12.8.1-5
- Added AppData manifest
- Disabled websockets

* Mon Dec 30 2019 ElXreno <elxreno@gmail.com> - 12.8.1-4
- Fixed man pages and license

* Mon Dec 30 2019 ElXreno <elxreno@gmail.com> - 12.8.1-3
- Ninja build

* Mon Dec 30 2019 ElXreno <elxreno@gmail.com> - 12.8.1-2
- WebSockets support for server

* Mon Dec 23 2019 ElXreno <elxreno@gmail.com> - 12.8.1-1
- Updated to version 12.8.1

* Wed Dec 18 2019 ElXreno <elxreno@gmail.com> - 12.8-1
- Updated to version 12.8

* Sun Dec 08 2019 ElXreno <elxreno@gmail.com> - 12.7.3-6
- Extracted ddnet-maps into ddnet-maps.spec, enabled tests

* Sat Dec 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 12.7.3-5
- Spec file fixes

* Sat Dec 07 2019 ElXreno <elxreno@gmail.com> - 12.7.3-4
- Updated maps to commit 950f9ec7a40814759c78241816903a236ab8de93

* Fri Dec 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 12.7.3-3
- Tim was here :)

* Fri Dec 06 2019 ElXreno <elxreno@gmail.com> - 12.7.3-2
- More docs, tests, and additions

* Sat Nov 30 2019 ElXreno <elxreno@gmail.com> - 12.7.3-1
- Initial packaging
