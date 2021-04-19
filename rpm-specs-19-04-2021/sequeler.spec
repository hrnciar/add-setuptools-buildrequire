%global appname com.github.alecaddd.sequeler

Name:           sequeler
Summary:        Friendly SQL Client
Version:        0.8.0
Release:        6%{?dist}
# The entire source is GPLv3+ (the LICENSE file is GPLv3, and both
# data/com.github.alecaddd.sequeler.appdata.xml.in.in and debian/copyright
# indicate GPLv3+ is intended), except the Vala sources (all .vala files under
# src/ or its subdirectories), which is GPLv2+; vapi/linux.vapi, which is
# LGPLv2+; and data/com.github.alecaddd.sequeler.appdata.xml.in.in, which is
# CC0.
License:        GPLv3+ and GPLv2+ and LGPLv2+ and CC0

URL:            https://github.com/Alecaddd/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       hicolor-icon-theme

Recommends:     libgda-mysql
Recommends:     libgda-postgres
Recommends:     libgda-sqlite

Summary(de):    Benutzerfreundlicher SQL-Client
Summary(fr):    Un simple client SQL
Summary(lt):    Draugiška SQL kliento programa

%description
Easily connect to your local or remote database.

Store your Database Connections in the library, connect over SSH tunnel, type
and execute SQL commands directly in the app, and do everything you need to do
without the necessity of opening the terminal.

Supported Databases:
  • SQLite
  • MySQL
  • MariaDB
  • PostgreSQL

Features Include:
  • Test Connections before saving them
  • View Table structure, content, and relations
  • Write multiple custom SQL Queries
  • Switch between light and dark mode
  • Handy keyboard shortcuts to quit (ctrl+q), create new connection
    (ctrl+shift+n), open a new window (ctrl+n)

%description -l de
Verbinden Sie sich mit einer beliebigen lokalen oder externen Datenbank.

Speichern Sie Ihre Datenbankverbindungen in der integrierten Bibliothek, führen
Sie SQL-Befehle direkt in der Anwendung aus, und tun Sie alles, was Sie tun
müssen, ohne das Terminal öffnen zu müssen.

  • SQLite
  • MySQL
  • MariaDB
  • PostgreSQL

Zu den Funktionen gehören:
  • Verbindung vor dem Speichern testen
  • Anzeigen von Tabellenstruktur, Inhalt und Beziehungen
  • Mehrere benutzerdefinierte SQL-Abfragen schreiben
  • Zwischen dem hellen und dunklen Modus umschalten
  • Tastenkombinationen zum Beenden (Strg+q), Erstellen einer neuen Verbindung
    (Strg+Shift+n), mehrere Instanzen (Strg+n)

%description -l fr
Connectez-vous facilement à une base de données locale ou distante.

Stockez vos connexions de base de données dans la bibliothèque intégrée, tapez
et exécutez les commandes SQL directement dans l’application, et faites tout ce
dont vous avez besoin pour vous passer la nécessité d’ouvrir le terminal.

  • SQLite
  • MySQL
  • MariaDB
  • PostgreSQL

Fonctionnalités incluses :
  • Tester les connexions avant de les enregistrer
  • Voir la structure, le contenu et les relations des tables
  • Écrire plusieurs requêtes SQL personnalisées
  • Changer entre le thème clair et le thème sombre
  • Raccourcis clavier pour quitter (Ctrl+Q), créer une nouvelle
    connexion(Ctrl+Maj+N), Ouvrir une nouvelle instance (Ctrl+N)

%description -l lt
Lengvai prisijunkite prie bet kurios vietinės ar nuotolinės duomenų bazės.

Laikykite savo duomenų bazių ryšius įtaisytoje bibliotekoje, tiesiogiai
programoje rašykite ir vykdykite SQL komandas ir atlikite viską, ką reikia be
būtinybės atverti terminalą.

  • SQLite
  • MySQL
  • MariaDB
  • PostgreSQL

Ypatybės:
  • Prieš įrašant ryšius, juos išbandyti
  • Rodyti lentelės struktūrą, turinį ir sąsajos ryšius
  • Rašyti keletą tinkintų SQL užklausų
  • Perjungti tarp šviesios ir tamsios veiksenos
  • Patogūs klaviatūros susiejimai, norint išeiti (ctrl (vald)+q), sukurti
    naują ryšį (ctrl (vald)+shift (lyg2)+n), keli egzemplioriai (ctrl (vald)+n)


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
%doc AUTHORS README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{appname}.svg
%{_datadir}/icons/hicolor/{16x16,24x24}/{actions,status}/*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Mar 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.0-6
- Localize summary and description where translations are available upstream

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 0.8.0-5
- Rebuilt for granite 6 soname bump.

* Wed Feb 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.0-4
- Correct License from “GPLv3” to “GPLv3+ and GPLv2+ and LGPLv2+ and CC0”

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.0-1
- Update to version 0.8.0.

* Sun May 24 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.91-1
- Update to version 0.7.91.

* Sun Apr 12 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.9-1
- Update to version 0.7.9.

* Fri Apr 10 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.6-1
- Update to version 0.7.6.

* Sun Apr 05 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.5-1
- Update to version 0.7.5.

* Wed Apr 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.4-1
- Update to version 0.7.4.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.3-1
- Update to version 0.7.3.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.2-1
- Update to version 0.7.2.

* Sun Aug 04 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.1-1
- Update to version 0.7.1.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.7.0-2
- Rebuild with Meson fix for #1699099

* Mon Apr 15 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.0-1
- Update to version 0.7.0.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 0.6.9-1
- Update to version 0.6.9.

* Sun Mar 24 2019 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-1
- Update to version 0.6.8.

* Wed Feb 27 2019 Fabio Valentini <decathorpe@gmail.com> - 0.6.7-1
- Update to version 0.6.7.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.5-1
- Update to version 0.6.5.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.4-1
- Update to version 0.6.4.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.3-1
- Update to version 0.6.3.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.2-1
- Update to version 0.6.2.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.1-1
- Update to version 0.6.1.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.0-1
- Update to version 0.6.0.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.9-1
- Update to version 0.5.9.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.7-1
- Update to version 0.5.7.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.5-2
- Rebuild for granite5 soname bump.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.5-1
- Update to version 0.5.5.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.4-1
- Update to version 0.5.4.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-1
- Update to version 0.5.3.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.0-1
- Update to version 0.5.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3-1
- Update to version 0.4.3.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-1
- Update to version 0.4.2.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1-1
- Initial package for fedora.

