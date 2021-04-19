%global         uuid com.github.gi_lom.dialect
%global         forgeurl https://github.com/gi-lom/dialect

Name:           dialect
Version:        1.2.0
Release:        1%{?dist}
Summary:        A translation app for GNOME based on Google Translate

%global         tag %{version}
%forgemeta

License:        GPLv3+
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gstreamer1-devel
BuildRequires:  gtk3-devel
BuildRequires:  libhandy1-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3dist(dbus-python)
BuildRequires:  python3dist(googletrans)
BuildRequires:  python3dist(gtts)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(langdetect)

Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-base
Requires:       gtk3
Requires:       libhandy1
Requires:       python3-gobject
Requires:       python3dist(dbus-python)
Requires:       python3dist(googletrans)
Requires:       python3dist(gtts)
Requires:       python3dist(httpx)
Requires:       python3dist(langdetect)

%description
A translation app for GNOME based on Google Translate.

Features:
* Text translation up to 5000 chars
* Text to speech
* History
* Automatic language detection
* Clipboard buttons


%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/%{uuid}.SearchProvider.service
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/gnome-shell/search-providers/%{uuid}.SearchProvider.ini
%{_datadir}/icons/hicolor/scalable/apps/%{uuid}*.svg
%{_metainfodir}/%{uuid}.metainfo.xml


%changelog
* Fri Mar 19 2021 Lyes Saadi <fedora@lyes.eu> - 1.2.0-1
- Updating to 1.2.0 (Fix #1936578)

* Sat Feb 20 2021 Lyes Saadi <fedora@lyes.eu> - 1.1.1-5
- Fixing Dialect's error messages by using the translate_legacy function

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Lyes Saadi <fedora@lyes.eu> - 1.1.1-1
- Updating to 1.1.1 (Fix #1905428)

* Mon Nov 02 2020 Lyes Saadi <fedora@lyes.eu> - 1.1.0-3
- Adding python3-dbus as a dependency

* Sun Nov 01 2020 Lyes Saadi <fedora@lyes.eu> - 1.1.0-2
- Adding some unpackaged files

* Sun Nov 01 2020 Lyes Saadi <fedora@lyes.eu> - 1.1.0-1
- Updating to 1.1.0 (Fix #1893399)

* Thu Oct 15 2020 Lyes Saadi <fedora@lyes.eu> - 1.0.0-1
- Initial package
