%global uuid    uk.co.ibboard.%{name}

Name:           cawbird
Version:        1.3.2
Release:        2%{?dist}
Summary:        Fork of the Corebird GTK Twitter client that continues to work with Twitter

License:        GPLv3+
URL:            https://github.com/IBBoard/cawbird
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  libappstream-glib
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gspell-1) >= 1.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(oauth)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(sqlite3)

Requires:       dbus-common
Requires:       hicolor-icon-theme

%description
Cawbird is a fork of the Corebird Twitter client from Baedert, which became
unsupported after Twitter disabled the streaming API.

Cawbird works with the new APIs and includes a few fixes and modifications
that have historically been patched in to IBBoard's custom Corebird build on
his personal Open Build Service account.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
rm -r %{buildroot}%{_datadir}/locale/es_419
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md notes.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*.1.*
%{_metainfodir}/*.xml


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.2-1
- build(update): 1.3.2

* Sun Jan  3 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.1-1
- build(update): 1.3.1

* Fri Jan  1 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3-1
- build(update): 1.3

* Sun Sep 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Sun Sep  6 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-2
- Fix parsing error in app-data | GH-157

* Sun May 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Update to 1.1.0
- Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Mon Nov 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3.1-1
- Update to 1.0.3.1

* Sun Oct 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-2
- Update to 1.0.2

* Fri Oct 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-2.20191002git870f127
- Initial package
