Name:           goodvibes
Version:        0.6.3
Release:        1%{?dist}
Summary:        Lightweight Radio Player

License:        GPLv3+
URL:            https://goodvibes.readthedocs.io/en/stable/index.html
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(amtk-5)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
Requires:       dconf
Requires:       gstreamer1-plugins-ugly-free
Requires:       hicolor-icon-theme

%description
Goodvibes is an Internet radio player for GNU/Linux. It aims to be light,
simple, straightforward.

%prep
%autosetup -n %{name}-v%{version}

%build
export CFLAGS="%build_cflags -fPIE"
%meson -Dc_args="%build_cflags -fPIE"
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/*.desktop
%meson_test

%files -f %{name}.lang
%license COPYING
%doc HACKING.md NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-client
%{_datadir}/applications/io.gitlab.Goodvibes.desktop
%{_datadir}/dbus-1/services/io.gitlab.Goodvibes.service
%{_datadir}/glib-2.0/schemas/io.gitlab.Goodvibes.enums.xml
%{_datadir}/glib-2.0/schemas/io.gitlab.Goodvibes.gschema.xml
%{_datadir}/icons/hicolor/*/apps/io.gitlab.Goodvibes.png
%{_datadir}/icons/hicolor/symbolic/apps/io.gitlab.Goodvibes-symbolic.svg
%{_mandir}/man1/%{name}-client.1.*
%{_mandir}/man1/%{name}.1.*
%{_metainfodir}/io.gitlab.Goodvibes.appdata.xml

%changelog
* Fri Mar  5 11:30:53 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.3-1
- Update to 0.6.3
- Close: rhbz#1916560

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 20:51:18 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.1-1
- Update to 0.6.1
- Close rhbz#1904320

* Wed Nov 11 10:31:24 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.6-1
- Update to 0.6
- Close rhbz#1880795

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 21:13:21 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.3-1
- Update to 0.5.3 (#1855132)

* Thu Jun 18 17:15:53 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.2-1
- Update to 0.5.2

* Thu Feb 06 22:29:07 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 01:16:10 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5-1
- Initial packaging
