%global appname com.github.cassidyjames.dippi

Name:           dippi
Summary:        Calculate display info like DPI and aspect ratio
Version:        2.7.4
Release:        6%{?dist}
# The entire source is GPLv3+:
#
#   The COPYING file is GPLv3, and while the phrase “or any later version” does
#   not appear, data/com.github.cassidyjames.dippi.appdata.xml.in indicates
#   GPLv3+ is intended:
#
#     <project_license>GPL-3.0+</project_license>
#
#   See https://github.com/cassidyjames/dippi/issues/79.
#
# …except the Vala sources, src/*.vala, which are GPLv2+, and
# data/com.github.cassidyjames.dippi.appdata.xml.in, which is CC0.
License:        GPLv3+ and GPLv2+ and CC0

URL:            https://github.com/cassidyjames/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme

Summary(en_AU): Calculate display info like DPI and aspect ratio
Summary(en_CA): Calculate display info like DPI and aspect ratio
Summary(en_GB): Calculate display info like DPI and aspect ratio
Summary(es):    Cálculo de datos de la pantalla como los PPP y la relación de aspecto
Summary(fr_CA): Calculez les informations de l’écran comme le DPI ou le ratio
Summary(fr):    Calculez les informations de l’écran comme le DPI ou le ratio
Summary(lt):    Apskaičiuoti tokią ekrano informaciją kaip taškus colyje (DPI) ir proporcijas
Summary(nl):    Bereken scherminformatie, zoals DPI en beeldverhouding
Summary(pt):    Calcula informações como DPI e o Aspect Ratio


%description
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiate between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Based on the expertise of Cassidy James Blaede and the actual logic System76
uses to determine screen size and resolution combinations.

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l en_AU
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Based on the expertise of Cassidy James Blaede and the actual logic System76
uses to determine screen size and resolution combinations.

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l en_CA
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Based on the expertise of Cassidy James Blaede and the actual logic System76
uses to determine screen size and resolution combinations.

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l en_GB
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Based on the expertise of Cassidy James Blaede and the actual logic System76
uses to determine screen size and resolution combinations.

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l es
Análisis de cualquier pantalla. Proporcione unos pocos datos y averigüe la
relación de aspecto, los PPP y otros detalles sobre una pantalla concreta.
Estupendo para decidir qué portátil o monitor externo comprar y si este
puede considerarse de alta resolución.

Funcionalidades útiles:
  • Descubra si una pantalla es una buena elección en función de su tamaño y su
    resolución
  • Obtenga orientaciones sobre las distintas densidades
  • Conozca la resolución lógica
  • Distinga las pantallas para portátiles de las de escritorio
  • Sencillísimo: todo en una ventanita

Basada en los conocimientos técnicos de Cassidy James Blaede y la lógica que
System76 emplea para verificar combinaciones de tamaño y resolución en las
pantallas.

Le dice si la densidad de una pantalla es:
  • de muy pocos PPP,
  • de PPP relativamente escasos,
  • ideal para resolución baja,
  • potencialmente problemática,
  • ideal para resolución alta,
  • bastante elevada para resolución alta, o
  • de PPP demasiado elevados

%description -l fr_CA
Analysez n’importe quel écran. Entrez de simples détails à son propos et
obtenez son ratio, son DPI, et d’autres détails. Ainsi, vous pourrez plus
aisément décider quel ordinateur portable ou écran acheter, et savoir si il
sera considéré comme HiDPI.

Fonctionnalités utiles:
  • Déterminez si un écran est un bon choix en vous basant sur sa diagonale et
    sa résolution
  • Obtenez des conseils sur différentes densités d’écran
  • Apprendre la résolution logique
  • Différencie les écrans d’ordinateurs de bureau et portables
  • Stupidement simple: tout dans une p’tite fenêtre toute mignone

Basé sur l’expertise de Cassidy James Blaede et sur la logique que System76
utilise pour déterminer la résolution et la diagonale d’écran.

Vous dit si la densité d’un écran a:
  • DPI très faible
  • DPI plutôt faible
  • Densité idéale pour le LoDPI
  • DPI potentiellement problèmatique
  • Densité idéale pour le HiDPI
  • Densité plutôt haute pour le HiDPI, ou
  • DPI trop haut

%description -l fr
Analysez n’importe quel écran. Entrez de simples détails à son propos et
obtenez son ratio, son DPI, et d’autres détails. Ainsi, vous pourrez plus
aisément décider quel ordinateur portable ou écran acheter, et savoir si il
sera considéré comme HiDPI.

Fonctionnalités utiles:
  • Déterminez si un écran est un bon choix en vous basant sur sa diagonale et
    sa résolution
  • Obtenez des conseils sur différentes densités d’écran
  • Apprendre la résolution logique
  • Différencie les écrans d’ordinateurs de bureau et portables
  • Stupidement simple: tout dans une p’tite fenêtre toute mignone

Basé sur l’expertise de Cassidy James Blaede et sur la logique que System76
utilise pour déterminer la résolution et la diagonale d’écran.

Vous dit si la densité d’un écran a:
  • DPI très faible
  • DPI plutôt faible
  • Densité idéale pour le LoDPI
  • DPI potentiellement problèmatique
  • Densité idéale pour le HiDPI
  • Densité plutôt haute pour le HiDPI, ou
  • DPI trop haut

%description -l lt
Išanalizuokite bet kurį ekraną. Įveskite kai kurią paprastą informaciją ir
sužinokite proporcijas, taškus colyje (DPI) ir kitą tam tikro ekrano
informaciją. Puikiai tinka sprendžiant kurį nešiojamąjį kompiuterį ar išorinį
ekraną įsigyti, ir ar jis bus laikomas HiDPI.

Naudingos ypatybės:
  • Sužinokite ar ekranas pagal savo dydį ir raišką yra geras pasirinkimas
  • Gaukite patarimus apie įvairius tankius
  • Sužinokite loginę raišką
  • Atskirkite nešiojamųjų ir stalinių kompiuterių ekranus
  • Kvailai paprasta:  viskas viename mažame lange

Paremta Cassidy James Blaede kompetencija ir tikraisiais loginiais System76
naudojimais, skirtais nustatyti ekrano dydžio ir raiškos kombinacijas.

Nurodo ar ekrano tankis yra:
  • Labai žemo DPI,
  • Pakankamai žemo DPI,
  • Idealus LoDPI,
  • Galimai problematiškas,
  • Idealus HiDPI,
  • Pakankamai didelis HiDPI ar
  • Per didelio DPI

%description -l nl
Analyseer welk scherm dan ook. Voer een paar eenvoudige gegevens in en bereken
de beeldverhouding, DPI en andere schermgegevens. Handig bij het bepalen welke
laptop of externe monitor je wilt kopen en of het scherm in kwestie HiDPI is.

Handige functies:
  • Bepaal of een scherm een goede aankoop zou zijn, op basis van grootte en
    resolutie
  • Verkrijg advies over verschillende dichtheden
  • Verkrijg informatie over logische resolutie
  • Onderscheid tussen laptop- en desktopschermen
  • Eenvoudiger kan niet: alles in een klein, handig venster

Gebaseerd op de expertise van Cassidy James Blaede en de techniek die System76
gebruikt bij het bepalen van de combinatie van schermgrootte en resolutie.

Toont je of de schermdichtheid:
  • Erg laag is,
  • Redelijk laag,
  • Ideaal voor LoDPI,
  • Wellicht problematisch,
  • Ideaal voor HiDPI,
  • Redelijk hoog voor HiDPI of
  • Té hoog

%description -l pt
Analise qualquer monitor. Insira alguns simples detalhes e descubra o aspect
ratio, o DPI, e outras informações.Ideal para ajudar a decidir que computador
portátil ou monitor comprar, e se pode ser considerado HiDPI ou não.

Recursos interessantes:
  • Descubra se um monitor é uma boa escolha baseado no seu tamanho e resolução
  • Obtenha dicas sobre diferentes densidades
  • Aprenda sobre logical resolution
  • Diferenciar entre monitores de portáteis ou de monitores de secretária.
  • Estupidamente simples: tudo numa janela pequenina

Informa se a densidade do ecrâ é:
  • Muito Baixo DPI
  • Relativamente Baixo DPI
  • Ideal para LoDPI
  • Potencialmente Problemático
  • Ideal para HiDPI
  • Relativamente Alto para HiDPI, ou
  • Demasiado Alto DPI


%prep
%autosetup

# Fix https://github.com/cassidyjames/dippi/issues/82 with
# https://github.com/cassidyjames/dippi/pull/83.
sed -r -i 's/(display)‘s/\1’s/g' \
    po/com.github.cassidyjames.dippi.pot \
    data/com.github.cassidyjames.dippi.appdata.xml.in \
    po/*.po


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
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Tue Mar 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.7.4-6
- Fix prominent typo https://github.com/cassidyjames/dippi/issues/82
- Improve and localize summary and description

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 2.7.4-5
- Rebuilt for granite 6 soname bump.

* Tue Feb 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.7.4-4
- Correct License from “GPLv3” to “GPLv3+ and GPLv2+ and CC0”

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Fabio Valentini <decathorpe@gmail.com> - 2.7.4-1
- Update to version 2.7.4.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.7.3-2
- Rebuild with Meson fix for #1699099

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.7.3-1
- Update to version 2.7.3.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.7.1-1
- Update to version 2.7.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.7.0-1
- Update to version 2.7.0.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.3-2
- Rebuild for granite5 soname bump.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.3-1
- Update to version 2.6.3.

* Wed Apr 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2-1
- Update to version 2.6.2.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1-1
- Update to version 2.6.1.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.4-1
- Update to version 2.5.4.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.3-1
- Update to version 2.5.3.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1-1
- Update to version 2.5.1.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.0-1
- Initial package.

