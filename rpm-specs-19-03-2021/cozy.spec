Name: cozy
%global rtld_name com.github.geigi.cozy

Summary: Modern audiobook player
License: GPLv3+

Version: 0.8.1
Release: 1%{?dist}

URL: https://cozy.geigi.de
Source0: https://github.com/geigi/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0: %{name}--unbundle-inject.patch

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: gtk3-devel >= 3.22
BuildRequires: libappstream-glib
BuildRequires: libhandy1-devel >= 1.0.0
BuildRequires: meson >= 0.40.0
BuildRequires: python3-devel
BuildRequires: xmlstarlet

%global with_tests 1

%if 0%{?with_tests}
BuildRequires: gstreamer1-plugins-base

BuildRequires: python3dist(distro)
BuildRequires: python3dist(inject) >= 4.3.1
BuildRequires: python3dist(mutagen)
BuildRequires: python3dist(packaging)
BuildRequires: python3dist(peewee) >= 3.9.6
BuildRequires: python3dist(pygobject)
BuildRequires: python3dist(pytest-runner)
BuildRequires: python3dist(pytest-mock)
BuildRequires: python3dist(pytz)
BuildRequires: python3dist(requests)
%endif

Requires: file
Requires: glib2
Requires: gstreamer1-plugins-bad-free
Requires: gstreamer1-plugins-good
Requires: gstreamer1-plugins-ugly-free
Requires: hicolor-icon-theme

# For whatever reason, the Python dependency generator doesn't seem to work
# for this RPM, so we'll just copy-paste the BuildRequires list
Requires: python3dist(distro)
Requires: python3dist(inject) >= 4.3.1
Requires: python3dist(mutagen)
Requires: python3dist(packaging)
Requires: python3dist(peewee) >= 3.9.6
Requires: python3dist(pygobject)
Requires: python3dist(pytz)
Requires: python3dist(requests)

# Not available in official Fedora repos
# Requires: gstreamer1-libav


%description
Cozy is a modern audiobook player for Linux.

Here are some of the current features:
- Import your audiobooks into Cozy to browse them comfortably
- Sort your audio books by author, reader & name
- Remembers your playback position
- Sleep timer
- Playback speed control
- Search your library
- Offline Mode! This allows you to keep an audio book on your internal storage
  if you store your audiobooks on an external or network drive.
  Perfect for listening on the go!
- Add mulitple storage locations
- Drag & Drop to import new audio books
- Support for DRM free mp3, m4a (aac, ALAC, …), flac, ogg, opus, wav files
- Mpris integration (Media keys & playback info for desktop environment)


%prep
%setup -q

# Unbundle inject
%patch0 -p1
rm -rf cozy/ext/inject

# Add a nonsensical <p> tag at the beginning of <description> for every
# <release> in the appdata XML - needed to pass validation
xmlstarlet ed \
	--insert component/releases/release/description/ul \
	--type elem -n p -v 'List of changes:' \
	< "data/%{rtld_name}.appdata.xml" > appdata.patched
mv ./appdata.patched "data/%{rtld_name}.appdata.xml"


%build
%meson
%meson_build
%meson_build com.github.geigi.cozy-update-po
%meson_build extra-update-po


%install
%meson_install
%find_lang %{rtld_name}

# Remove the "devel" icon
rm %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{rtld_name}.Devel.svg


%check
%if 0%{?with_tests}
%pytest
%endif
appstream-util validate --nonet %{buildroot}/%{_datadir}/metainfo/%{rtld_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop


%files -f %{rtld_name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{rtld_name}
%{_datadir}/%{rtld_name}/
%{_datadir}/applications/%{rtld_name}.desktop
%{_datadir}/glib-2.0/schemas/%{rtld_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{rtld_name}.svg
%{_datadir}/icons/hicolor/scalable/actions/*-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{rtld_name}-symbolic.svg
%{_metainfodir}/%{rtld_name}.appdata.xml
%{python3_sitelib}/%{name}/


%changelog
* Mon Feb 08 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8.1-1
- Update to latest release
- Fix license tag - cozy is GPLv3, the "and ASL 2.0" part
  came from a bundled library, which has been un-bundled

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.8-1
- Update to latest release

* Mon Nov 30 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.7-1
- Update to latest release

* Sun Nov 15 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.5-1
- Update to latest release

* Sat Nov 14 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.3-1
- Update to latest release

* Thu Oct 01 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.2-2
- Unbundle python3-inject

* Mon Sep 28 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.2-1
- Update to latest release
- Use python3dist() for specifying dependencies

* Fri Sep 25 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.1-1
- Update to latest release

* Fri Sep 25 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7-1
- Update to latest release
- Put tests behind an enable/disable macro

* Fri Sep 11 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.19-1
- Initial packaging

