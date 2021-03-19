%bcond_without tests

Name:           giada
Version:        0.17.1
Release:        4%{?dist}.1
Summary:        Your hardcore loop machine

# LICENSING NOTE:
#
# The upstream source contains excerpts from the Steinberg VST 3 SDK, which has
# additional restrictions on top of the GPLv3 that make it unsuitable for
# distribution in Fedora. See
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/FMFIZU22AP36J3DOUVCXUPHQ3MNDN5P6/.
#
# These problematic components are therefore filtered from the upstream source
# archive using the script in Source1 to produce the distributable source
# archive in Source0. The VST 3 SDK is removed, as is JUCE, which contains
# components from the VST 3 SDK and is only used for VST 3 suport anyway.
#
# Note that this means Giada will *not* be built with VST3 support in Fedora.
# (The situation for VST2 is even worse, as it is available only under a
# proprietary license.)

# The entire source is GPLv3+, except:
#   - src/deps/json is (MIT and CC0), where the overall license is MIT and the
#     bundled copy of Hedley is CC0
#   - src/deps/rtaudio is MIT, except:
#     * src/deps/rtaudio/include/soundcard.h is BSD
#
# The following sources are present upstream, but not in the distributable
# source tarball:
#
#   - src/deps/juce
#   - src/deps/vst3sdk
License:        GPLv3+ and MIT and CC0 and BSD
URL:            https://www.giadamusic.com
# This macro is used by the script in Source1 as the upstream source archive.
%global upstream_source %{url}/data/%{name}-%{version}-src.tar.gz
Source0:        %{name}-%{version}-src-distributable.tar.xz
Source1:        download-and-filter-source.sh
# https://github.com/monocasual/giada/pull/358
Source2:        https://raw.githubusercontent.com/monocasual/giada/ff1ba651301a2419d6a2b7680ea8432f8e440a74/extras/com.giadamusic.Giada.desktop
# https://github.com/monocasual/giada/pull/358
Source3:        https://raw.githubusercontent.com/monocasual/giada/ff1ba651301a2419d6a2b7680ea8432f8e440a74/extras/com.giadamusic.Giada.appdata.xml

# We need to use pkg-config/pkgconf to find rtmidi and libsndfile.
# https://github.com/monocasual/giada/issues/451
Patch1:         %{name}-0.17.1-find-external-dependencies.patch
# This is a C++ logging wrapper that passes its format string parameter through
# to std::fprintf, which inherently means the format string cannot be a
# literal. We use GCC pragmas to suppress the warning in just this one spot.
# See https://github.com/monocasual/giada/issues/447, where this is discussed,
# and the patch is offered, upstream.
Patch2:         %{name}-0.17.1-suppress-format-security.patch
# Binary should be installed as /usr/bin/giada, not /usr/giada; reported
# upstream with patch at https://github.com/monocasual/giada/issues/450.
Patch3:         %{name}-0.17.1-fix-install-path.patch

BuildRequires:  desktop-file-utils
# For AppData file validation
BuildRequires:  libappstream-glib

BuildRequires:  gcc-c++
BuildRequires:  cmake
# It is our choice whether to use the make backend or the ninja backend.
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(rtmidi)

%if 0%{?fedora} == 32
BuildRequires:  fltk-devel
%else
BuildRequires:  cmake(FLTK)
%endif

BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(samplerate)

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(freetype2)

%if %{with tests}
BuildRequires:  cmake(Catch2)
# Support graphical tests in non-graphical environment
BuildRequires:  xorg-x11-server-Xvfb
%endif

# For /usr/share/icons/hicolor/*/apps
Requires:  hicolor-icon-theme

# ============================================================================
# “JSON for Modern C++”, https://github.com/nlohmann/json
#
# The version comes from the initial comment header, and from “#define
# NLOHMANN_JSON_VERSION_MAJOR”, “#define NLOHMANN_JSON_VERSION_MINOR”, and
# “#define NLOHMANN_JSON_VERSION_PATCH”, in
# src/deps/json/single_include/nlohmann/json.hpp for version
#
# See https://github.com/nlohmann/json/issues/2651, where support for
# unbundling Hedley was requested.
Provides:  bundled(nlohmann-json) = 3.9.1
# That, in turn, bundles “Hedley”, https://nemequ.github.io/hedley
#
# The version comes from “#define JSON_HEDLEY_VERSION” in
# src/deps/json/single_include/nlohmann/json.hpp.
Provides:  bundled(hedley) = 13
# ============================================================================

# ============================================================================
# RtAudio (https://github.com/thestk/rtaudio)
#
# This version is slightly forked, so it is not possible to build with the
# system copy of RtAudio. See
# https://giadamusic.com/forum/viewtopic.php?f=2&t=177, where upstream
# discusses the decision to maintain a forked copy of RtAudio in the Giada
# source tree.
#
# The version comes from “#define RTAUDIO_VERSION” in
# src/deps/rtaudio/RtAudio.h.
Provides:  bundled(rtaudio) = 5.1.0
# ============================================================================

# Consistent behavior on F32
%undefine __cmake_in_source_build

%description
Giada is an open source, minimalistic and hardcore music production tool.
Designed for DJs, live performers and electronic musicians.


%prep
%autosetup -n %{name}-%{version}-src -p1

# This is a last safeguard against something with an inappropriate license
# slipping into the source tarball. It is no substitute for manual auditing.
echo 'Checking for inappropriate source files:'
echo '> Possible Steinberg proprietary license?'
if grep -Frl 'This Software Development Kit may not be' .
then
  echo 'Found some concerning files!'
  exit 1
else
  echo '> No concerning files were found.'
fi
echo '> Possible Steinberg VST 3 SDK (GPLv3 with conditions)?'
if grep -Erli 'Project[[:blank:]]*:[[:blank:]]*VST SDK' .
then
  echo 'Found some concerning files!'
  exit 1
else
  echo '> No concerning files were found.'
fi

# At least on Fedora, this keeps CMake from expecting the static FLTK library.
# It is not clear whether this is an FLTK bug (upstream or Fedora), or a Giada
# bug, so we have not attempted to report it to any upstream.
sed -r -i 's/(FLTK)[[:blank:]]+CONFIG/\1/' CMakeLists.txt


%build
# VST 2 SDK is only available under a proprietary license, and VST 3 SDK is
# dual-licensed with a proprietary license and GPLv3, but additional
# trademark-related conditions are imposed that are not acceptable in Fedora.
# See the notes near the beginning of this spec file. Therefore the VST 3 SDK
# and JUCE sources have been excluded, and all VST support must be disabled at
# build time.
%cmake \
    -DWITH_VST2:BOOL=OFF -DWITH_VST3:BOOL=OFF \
    -DWITH_TESTS:BOOL=%{?with_tests:ON}%{?!with_tests:OFF} \
    -GNinja
%cmake_build


%install 
%cmake_install
# https://github.com/monocasual/giada/pull/358
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
# https://github.com/monocasual/giada/pull/358
install -m 0644 -p -D -t %{buildroot}%{_metainfodir} %{SOURCE3}
install -m 0644 -p -D -t %{buildroot}%{_datadir}/icons/hicolor/128x128/apps \
    extras/%{name}-logo.png


%check
# Validate the installed AppData file. Fedora guidelines require validate-relax
# to pass (but not validate-strict), and do require validation at build time.
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/com.giadamusic.Giada.appdata.xml

%if %{with tests}
xvfb-run -a %{buildroot}%{_bindir}/giada --run-tests
%endif


%files
%license COPYING
%doc ChangeLog README.md

%{_bindir}/%{name}

# https://github.com/monocasual/giada/pull/358
%{_metainfodir}/com.giadamusic.Giada.appdata.xml
# https://github.com/monocasual/giada/pull/358
%{_datadir}/applications/com.giadamusic.Giada.desktop
# https://github.com/monocasual/giada/pull/358
%{_datadir}/icons/hicolor/128x128/apps/%{name}-logo.png


%changelog
* Fri Feb 26 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.17.1-4.1
- Add Fedora 32 compatibility

* Thu Feb 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.17.1-4
- Remove VST 3 SDK and JUCE from source tarball for legal reasons; disable all
  VST support
- Update License field to reflect the removed bundled dependencies
- Remove stray debugging “find” commands

* Tue Feb 23 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.17.1-3
- Add link to upstream issue for format-security patch
- Add commentary on forked bundled rtaudio, with a link to upstream discussion

* Tue Feb 23 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.17.1-2
- Disable VST3 on PPC64LE due to a non-obvious linker error

* Mon Feb 22 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.17.1-2
- New upstream release 0.17.1
- Switch to CMake build system
- Add AppData and updated desktop file from
  https://github.com/monocasual/giada/pull/358
- Add virtual Provides, and update License field, for bundled dependencies
- Update summary and description from upstream
- Build Giada with tests, and run them at build time

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.17.0-1
- New upstream release
- Add CMake build system
- VST3 support
- Show descriptive plug-in names in Plug-in List Window
- Resizable plug-in list
- New persistence mechanism for Plug-ins state
- Improved text truncation for small buttons and text boxes
- Beautify Sample Editor window
- Resizable plug-in list window
- Show descriptive plug-in name in plug-in list
- Update JUCE, version 6.0.4
- Update Catch2 to version 2.13.2
- Replace old filesystem functions in fs.h with std::filesystem
- Add VST3 SDK as git submodule
- Set minimum macOS version to 10.14
- Statically link the MSVC runtime library on Windows
- Avoid crash on opening plug-in list with invalid plug-ins
- Rewind sample channels in loop.once.bar mode on bar, if still playing (fix #403)
- Modernize log::print() function to handle std::string arguments (PR #402)
- Fix playStatus logic for ending sample channels in loop-once-bar mode (#404)
- Fix shrinking beats that could glitch the output (#361)

* Thu Oct 08 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.16.4-1
- New upstream release
- Support for mono inputs
- Overdub mode for Sample Channels with optional overdub protection
- Disable record-on-signal mode when sequencer is running
- Shift + [click on R button] kills action reading when "Treat one-shot
  channels with actions as loops" option is on
- Start MIDI channels automatically after action recording session
- Fix wrong sample rate conversion when project rate != system rate
- Fix Wrong begin/end sample markers when loading a project with samplerate != 
  system.samplerate
- Fix wrong MIDI learn mapping for master parameters
- Fix BPM button disabled after audio recording session

* Fri Aug 07 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.16.3.1-1
- New upstream release
- Resolves: rhbz #1863622

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.16.3-1
- New upstream version

* Thu Mar 26 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.16.2.2-1
- New upstream version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.15.4-1
- Update to 0.15.4 fixes rhbz#1604101 rhbz#1674963 and rhbz#1703719

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot] com> - 0.14.4-1
- Update to 0.14.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-7
- Fix FTBFS (gcc5?), don't build with -Werror

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-6
- rebuild (fltk)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.7.0-2
- Add missing libsamplerate

* Wed Jun 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.7.0-1
- New upstream 0.7.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.6-1
- New upstream release

* Tue Dec 11 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.4-2
- Rebuild for new rtaudio

* Thu Nov 29 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.4-1
- New upstream, removing vst patch
- Apply desktop translation patch from Ismael Olea
- Remove unecessary scriptlets and add a more descriptive summary

* Mon Nov 26 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-4
- Missing BR libXext-devel

* Sun Nov 25 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-3
- Add missing BR rtaudio

* Sun Oct 21 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-2
- correct description and URL, add make flags

* Sun Oct 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-1
- Initial package
