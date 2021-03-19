%global appname com.github.danrabbit.harvey

Name:           harvey
Summary:        The hero that Gotham needs right now
Version:        1.0.0
Release:        11%{?dist}
# The entire source is GPLv3+:
#
#   The COPYING file is GPLv3, and while the phrase “or any later version” does
#   not appear, data/com.github.danrabbit.harvey.appdata.xml.in and
#   debian/copyright indicate GPLv3+ is intended, e.g., from the AppData file:
#
#     <project_license>GPL-3.0+</project_license>
#
#   See https://github.com/danrabbit/harvey/issues/40.
#
# …except the Vala sources, src/*.vala, and data/Application.css, which are
# GPLv2+; and data/com.github.danrabbit.harvey.appdata.xml.in, which is CC0.
License:        GPLv3+ and GPLv2+ and CC0

URL:            https://github.com/danrabbit/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme

Summary(fr):    Le héro dont Gotham a besoin dès à présent
Summary(es):    El héroe que Gotham estaba necesitando
Summary(en_AU): The hero that Gotham needs right now
Summary(en_CA): The hero that Gotham needs right now
Summary(en_GB): The hero that Gotham needs right now

%description
Calculate and visualize color contrast. Harvey checks a given set of colors for
WCAG contrast compliance.

%description -l fr
Calculez et visualisez les contrastes de couleur. Harvey vérifie qu’un jeu de
couleur est conforme aux recommandation de contraste WCAG.

%description -l es
Calcule y visualice el contraste de color, Harvey comprueba un conjunto
determinado de colorespara el cumplimiento del contraste WCAG.

%description -l en_AU
Calculate and visualize color contrast. Harvey checks a given set of colors for
WCAG contrast compliance.

%description -l en_CA
Calculate and visualize color contrast. Harvey checks a given set of colors for
WCAG contrast compliance.

%description -l en_GB
Calculate and visualize color contrast. Harvey checks a given set of colors for
WCAG contrast compliance.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Tue Mar 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.0-11
- Localize summary and description where translations are available upstream

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-10
- Rebuilt for granite 6 soname bump.

* Wed Feb 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.0-9
- Correct License from “GPLv3” to “GPLv3+ and GPLv2+ and CC0”

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-5
- Drop superfluous dependency on appstream.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Update to version 1.0.0.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.8-3
- Rebuild for granite5 soname bump.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.8-1
- Initial package.


