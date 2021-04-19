%global appname io.github.lainsce.Notejot

Name:           notejot
Summary:        Jot your ideas
Version:        2.7.4
Release:        1%{?dist}
# The entire source is GPLv3+, except:
#   src/Widgets/NoteMenuPopover.vala
#   src/Widgets/MoveToDialog.vala
#   src/Widgets/EditNotebookDialog.vala
#   src/Widgets/HeaderBarButton.vala
# which are GPLv2+; and
#   data/io.github.lainsce.Notejot.appdata.xml.in
# which is CC0.
License:        GPLv3+ and GPLv2+ and CC0

URL:            https://github.com/lainsce/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(json-glib-1.0)

Requires:       hicolor-icon-theme

Summary(cs):    Zapiš si své nápady
Summary(da):    Notér dine ideer
Summary(de_DE): Notieren Sie Ihre Ideen
Summary(es):    Anota sus ideas
Summary(fr):    Notez vos idées
Summary(gl):    Apunte as súas ideas
Summary(it):    Annota le tue idee
Summary(ja):    アイデアをメモします
Summary(lt):    Greitai užsirašykite savo idėjas
Summary(nl):    Noteer je ideeën
Summary(pl):    Notuj swoje pomysły
Summary(pt_BR): Anote suas ideias
Summary(pt):    Anote as suas ideias
Summary(ru):    Запишите ваши идеи
Summary(sv):    Skriv ner dina idéer


%description
A stupidly-simple notes application for any type of short term notes or ideas.

  - Quit anytime with the shortcut Ctrl + Q

%description -l da
En simpel post-it note applikation for enhver type af korttids tanker eller
ideer.

  - Luk på et ethvert tidspunkt med genvejen Ctrl + Q

%description -l de-DE
Eine total einfache Notizzettel-Anwendung für so ziemlich jede Art von kleinen
Notizen oder Ideen.

  - Beenden jederzeit mit dem Kürzel Strg + Q möglich

%description -l es
Una aplicación de notas adhesivas estúpidamente simple para cualquier tipo de
notas o ideas a corto plazo.

  - Salir en cualquier momento con el atajo Ctrl + Q

%description -l fr
Une application de notes post-it stupidement simple pour tout type de notes ou
d'idées à court terme.

  - Quittez à tout moment avec le raccourci Ctrl + Q

%description -l gl
Un aplicativo de notas sinxelo para calquera tipo de notas ou ideas a curto
prazo.

  - Saia en calquera momento co atallo Ctrl + Q

%description -l it
Un’applicazione di note adesive stupidamente semplice per qualsiasi tipo di
note a breve termine o idee.

  - Esci in qualsiasi momento con la scorciatoia Ctrl + Q

%description -l ja
一時的なノートやアイデアをメモするための、非常にシンプルな付箋アプリケーショ
ンです。

  - ショートカット Ctrl + Q で、いつでも終了できます

%description -l lt
Kvailai paprasti lipnūs užrašai bet kokio tipo trumpoms pastaboms ar idėjoms.

  - Išeikite bet kuriuo metu, naudodami susiejimą Ctrl (Vald) + Q

%description -l nl
Een doodeenvoudige notitietoepassing voor het opschrijven van korte notities of
ideeën.

  - Sluit af met Ctrl + Q

%description -l pt
Uma aplicação estupidamente simples de notas aderentes para qualquer tipo
de notas a curto prazo ou ideias.

  - Saía a qualquer momento com o atalho Ctrl + Q

%description -l ru
Невероятно простое приложение для любого типа быстрых заметок или идей.

  - Выход в любой момент с помощью сочетания клавиш Ctrl + Q

%description -l sv
Ett löjligt enkelt anteckningsprogram för alla typer av kortvariga anteckningar
eller idéer.

  - Avsluta när som helst med genvägen Ctrl+Q


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
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Mar 28 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.7.4-1
- New upstream version 2.7.4
- More localized summaries and descriptions from upstream

* Sat Feb 20 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.8-2
- Add localized summaries and descriptions, where available

* Mon Feb 15 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.8-1
- Update to version 2.6.8

* Sat Feb 13 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.5-1
- Update to version 2.6.5

* Wed Feb 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.4-1
- Update to version 2.6.4

* Wed Feb 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.6.3-4
- Correct License from “GPLv3” to “GPLv3+ and GPLv2+ and CC0”

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 12 2020 Fabio Valentini <decathorpe@gmail.com> - 1.6.3-1
- Update to version 1.6.3.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Fabio Valentini <decathorpe@gmail.com> - 1.6.0-1
- Update to version 1.6.0.

* Fri Aug 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.8-1
- Update to version 1.5.8.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.5-1
- Update to version 1.5.5.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.4-1
- Update to version 1.5.4.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.3-1
- Update to version 1.5.3.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1-1
- Update to version 1.5.1.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-1
- Update to version 1.5.0.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.5-1
- Update to version 1.4.5.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.3-1
- Update to version 1.4.3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.2-1
- Update to version 1.4.2.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.0-2
- Rebuild for granite5 soname bump.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.0-1
- Update to version 1.4.0.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.8-1
- Update to version 1.3.8.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.7-1
- Initial package.

