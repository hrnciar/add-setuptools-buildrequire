%global appname com.github.donadigo.appeditor

Name:           appeditor
Summary:        Edit application menu
Version:        1.1.1
Release:        7%{?dist}
# The entire source is GPLv3, except the Vala source files src/*.vala which are
# LGPLv2+, and data/com.github.donadigo.appeditor.appdata.xml.in which is CC0.
#
# See https://github.com/donadigo/appeditor/issues/106 regarding missing LGPLv2
# and GPLv2 license text.
License:        GPLv3 and LGPLv2+ and CC0

URL:            https://github.com/donadigo/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       contractor
Requires:       hicolor-icon-theme

Summary(ca):    Modifiqueu el menú d’aplicacions
Summary(de):    Keine Anwendungen gefunden
Summary(es):    Editar el menú de aplicaciones
Summary(fr):    Modifier le menu des applications
Summary(it):    Modifica Menù Applicazione
Summary(ja):    アプリケーションメニューを編集します
Summary(lt):    Programų nerasta
Summary(nl_NL): Toepassingenmenu bewerken
Summary(pt_BR): Nenhum aplicativo encontrado
Summary(ru):    Изменяйте меню приложений
Summary(tr):    Uygulama menülerini düzenle

%description
Edit application entries shown in application menu and their properties.

Features include:

  • Hide and show applications from the application menu
  • Create new application entries
  • Change application’s display name, icon and more

%description -l ca
Modifiqueu les entrades mostrades al menú d’aplicacions i les seves propietats.

Funcionalitats distintives:

  • Amagueu i mostreu entrades al menú d’aplicacions
  • Creeu-ne de noves
  • Canvieu el nom visible, la icona i molt més per cada aplicació

# %%description -l de
# (only partially translated upstream)

%description -l es
Edite las entradas del menú de aplicaciones y sus propiedades.

Algunas de las funcionalidades son:

  • Ocultar y mostrar entradas del menú de aplicaciones
  • Crear entradas de aplicación nuevas
  • Cambiar el nombre mostrado de una aplicación, su icono y más

%description -l fr
Modifiez les raccourcis et leurs propriétés dans le menu des applications.

Fonctionnalités incluses:

  • Masquer et afficher les applications du menu des applications
  • Créer de nouveaux raccourcis d’application
  • Changer le nom d’une application, son icône, etc

%description -l it
Modifica le voci dell’applicazione visualizzate nel menu le relative proprietà.

Funzionalità incluse:

  • Mostra e nascondi le applicazioni nel Menù Applicazioni
  • Crea nuova voce applicazione
  • Cambia il nome visualizzato dell’applicazione, la sua icona ed altro

%description -l ja
アプリケーションメニューに表示されるアプリケーションのエントリーとプロパティ
を編集します。

含まれる機能:

  • アプリケーションをアプリケーションメニューから隠したり表示したりします
  • 新しいアプリケーションのエントリーを作成します
  • アプリケーションの表示名やアイコンなどを変更します

# %%description -l lt
# (only partially translated upstream)

%description -l nl_NL
Bewerk menu-items uit het toepassingenmenu, inclusief hun eigenschappen.

Het bevat de volgende mogelijkheden:

  • Toon en verberg items uit het toepassingenmenu
  • Maak nieuwe menu-items
  • Pas de weergavenaam, het pictogram en meer aan

# %%description -l pt_BR
# (only partially translated upstream)

%description -l ru
Редактирование описания и свойств программ в меню приложений.

Доступные возможности:

  • Скрытие и отображение программ в меню приложений
  • Создание новых записей о приложениях
  • Изменение отображаемого имени приложение, значка и многого другого

%description -l tr
Uygulama menüsünde gösterilen uygulama girişlerini ve özelliklerini düzenleyin.

Özellikler şunlardır:

  • Uygulama menüsünden uygulamaları gizleme ve gösterme
  • Yeni uygulama girişleri oluşturma
  • Uygulamanın görünen adını, simgesini ve daha fazlasını değiştirin


%prep
%autosetup -p1


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
%{_datadir}/contractor/%{appname}.contract
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon Mar 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.1-7
- Localize summary and description where translations are available upstream

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-6
- Rebuilt for granite 6 soname bump.

* Tue Feb 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.1-5
- Correct License from “LGPLv2+” to “GPLv3 and LGPLv2+ and CC0”

* Tue Feb 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.1-4
- Package LICENSE file

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 17 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-1
- Update to version 1.1.1.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-4
- Include a simple patch to fix compilation with newer vala versions.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Initial package for fedora.

