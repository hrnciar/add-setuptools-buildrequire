%bcond_without tests

Name:           gaupol
Version:        1.9
Release:        4%{?dist}
Summary:        Editor for text-based subtitle files

# Everything is GPLv3+, except:
#
#   data/iso-codes, which is LGPLv2+; however, we treat this as a bundled
#   dependency and remove it, so it does not contribute to the overall license
#
# and:
#
#   data/io.otsaloma.gaupol.appdata.xml.in, which is CC0
License:        GPLv3+ and CC0
URL:            https://otsaloma.io/%{name}/
%global forgeurl https://github.com/otsaloma/%{name}/
%global tag %{version}
%forgemeta
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
# Note that this package does not (yet) require python3dist(setuptools)!
#
# Note also that we cannot use dynamic BuildRequires or automatic Requires
# generation, as setup.py does not have the relevant metadata. We must do it
# the old-fashioned way, by perusing READMEs, plus grepping source and
# inspecting imports.

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# For AppData file validation
BuildRequires:  libappstream-glib
%if %{with tests}
BuildRequires:  python3dist(pygobject) >= 3.12
BuildRequires:  gtk3 >= 3.12
# Not actually used in tests:
#BuildRequires:  gstreamer1 >= 1.6
#BuildRequires:  gstreamer1-plugins-base >= 1.6
#BuildRequires:  gstreamer1-plugins-good >= 1.6
#BuildRequires:  gstreamer1-plugins-good-gtk >= 1.6
#BuildRequires:  gstreamer1-vaapi >= 1.6
#BuildRequires:  gstreamer1-svt-av1
#BuildRequires:  gstreamer1-svt-vp9
BuildRequires:  iso-codes
BuildRequires:  gspell >= 1.0.0
BuildRequires:  python3dist(chardet) >= 2.2.1

BuildRequires:  python3dist(pytest)
# Support graphical tests in non-graphical environment
BuildRequires:  xorg-x11-server-Xvfb
%endif

# For /usr/share/icons/hicolor/{scalable,symbolic}/apps
Requires:  hicolor-icon-theme

Requires:       python3dist(pygobject) >= 3.12
Requires:       gtk3 >= 3.12
Requires:       iso-codes
Recommends:     gstreamer1 >= 1.6
Recommends:     gstreamer1-plugins-base >= 1.6
Recommends:     gstreamer1-plugins-good >= 1.6
Recommends:     gstreamer1-plugins-good-gtk >= 1.6
Recommends:     gstreamer1-vaapi >= 1.6
Recommends:     gstreamer1-svt-av1
Recommends:     gstreamer1-svt-vp9
Recommends:     gspell >= 1.0.0
Recommends:     python3dist(chardet) >= 2.2.1

Requires:       python3-aeidon = %{version}-%{release}

Summary(cs):    Editor pro textově založené titulky
Summary(es):    Editor de archivos de subtítulos basados en texto
Summary(fi):    Muokkain tekstimuotoisille tekstityksille
Summary(fr):    Éditeur de sous-titres au format texte
Summary(ie):    Un redactor por textual subtitules
Summary(is):    Ritill fyrir skjátexta á textaformi
Summary(nl):    Bewerker voor op tekst gebaseerde ondertitels
Summary(pl):    Edytor napisów tekstowych
Summary(pt_BR): Editor para legendas em texto
Summary(pt):    Editor para legendas em texto
Summary(ru):    Редактор текстовых субтитров
Summary(tr):    Metin tabanlı altyazılar için düzenleyici

%description
Gaupol is an editor for text-based subtitle files. It supports multiple
subtitle file formats and provides means of creating subtitles, editing texts
and timing subtitles to match video.

%description -l cs
Gaupol je editor pro textově založené soubory titulků. Podporuje více formátů
souborů titulků a poskytuje prostředky k vytváření titulků, upravování textů a
časování titulků, aby odpovídaly obrazovému záznamu.

%description -l es
Gaupol es un editor de archivos de subtítulos basados en texto. Con soporte
para diversos formatos de archivos, proporciona los medios para crear
subtítulos, manipular líneas y sincronizar subtítulos a un vídeo.

%description -l fi
Gaupol on muokkain tekstimuotoisille tekstitystiedostoille. Se tukee useita eri
tekstitystiedostomuotoja ja tarjoaa toimintoja tekstitysten luomiseen, tekstien
muokkaamiseen ja tekstitysten ajoittamiseen videoon sovittaen.

%description -l fr
Gaupol est un éditeur de sous-titres au format texte. Il supporte de nombreux
formats de sous-titres et permet de créer, des sous-titres, d’éditer du texte,
et de synchroniser les sous-titres à une vidéo.

%description -l ie
Gaupol es un redactor por files de textual subtitules. It supporta multiplic
formates de file e permisse vos crear, redacter e colocar subtitules secun un
video.

%description -l is
Gaupol er ritill til meðhöndlunar á skjátextaskrám á textaformi. Hann styður
margar gerðir skjátextaskráa og býður upp á að útbúa nýja skjátexta, breytingar
texta og tímasetningu þeirra svo að þeir samsvari myndskeiðum.

%description -l nl
Gaupol is een bewerker voor op tekst gebaseerde ondertitels. Gaupol ondersteunt
meerdere soorten ondertitelformaten, en kan ook worden gebruikt om nieuwe
ondertitels te maken, teksten aan te passen en ondertitels te timen met
video’s.

%description -l pl
Gaupol to edytor tekstowych plików napisów. Obsługuje wiele formatów plików
napisów i zapewnia środki do tworzenia napisów, edycji tekstów i synchronizacji
napisów w celu dopasowania do wideo.

%description -l pt_BR
Gaupol é um editor de arquivos de legendas em texto. Ele possui suporte a
vários formatos de arquivo de legenda e fornece meios de criar legendas, editar
textos e legendas de tempo para corresponder ao vídeo.

%description -l pt
O Gaupol é um editor de ficheiros de legendas em texto. Possui suporte a vários
formatos de ficheiro de legenda e fornece meios de criar legendas, editar
textos e legendas de tempo para corresponder ao vídeo.

%description -l ru
Gaupol - редактор для текстовых субтитров. Он поддерживает множество форматов
файлов субтитров и предоставляет средства для их создания, редактирования и
синхронизации с видео.

%description -l tr
Gaupol, metin tabanlı altyazı dosyaları için bir düzenleyicidir. Birçok altyazı
dosya biçimini destekler ve video eşleştirmek için altyazı oluşturma, metinleri
düzenleme ve altyazıları zamanlama araçları sağlar.

%package -n python3-aeidon
Summary: Read, write, and manipulate text-based subtitle files
# Since only data/io.otsaloma.gaupol.appdata.xml.in is CC0, this subpackage is
# just GPLv3+.
License:        GPLv3+

Provides:       aeidon = %{version}-%{release}
Obsoletes:      aeidon <= 1.4-11
Conflicts:      aeidon <= 1.4-11

Requires:       iso-codes
Recommends:     python3dist(chardet) >= 2.2.1

%description -n python3-aeidon
aeidon is a Python package that provides classes and functions for dealing with
text-based subtitle files of many different formats. Functions exist for
reading and writing subtitle files as well as manipulating subtitle data, i.e.
positions (times or frames) and texts.

The aeidon package is part of the Gaupol subtitle editor, where the other
package, %{name}, provides the GTK user interface.

Separating a user interface independent general-purpose subtitle editing
package from Gaupol has been an afterthought and thus not well designed to be a
reusable component, but on the other hand is proven, working and maintained
code.

API documentation: https://otsaloma.io/gaupol/doc/api/aeidon.html


%prep
%forgeautosetup -p1
# Remove bundled iso-codes:
find data/iso-codes -type f -name '*.json' |
  while read -r fn
  do
    ln -svf "%{_datadir}/iso-codes/json/$(basename "${fn}")" "${fn}"
  done
# We want to install the Markdown docs in a subdirectory of the package
# documentation directory; copy them to a directory of the desired name.
cp -vrp doc using-%{name}


%build
%py3_build


%install
# From README.aeidon.md:
#
#   When packaging both aeidon and gaupol in a Linux distro, it's best to use
#   the switches in the main `setup.py` for a consistent whole.
#
#       sudo python3 setup.py --without-gaupol install --prefix=/usr/local
#       sudo python3 setup.py --without-aeidon install --prefix=/usr/local
%global py_setup_args --without-iso-codes --without-%{name}
%py3_install
%global py_setup_args --without-iso-codes --without-aeidon
%py3_install

%find_lang %{name}
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    --delete-original \
    --add-category='AudioVideoEditing' \
    %{buildroot}/%{_datadir}/applications/io.otsaloma.%{name}.desktop


%check
if [ "$(find data/iso-codes -type f ! -name 'README*' | wc -l)" != 0 ]
then
  echo 'Failed to fully remove bundled iso-codes' 1>&2
  false
fi
# Validate the installed AppData file. Fedora guidelines require validate-relax
# to pass (but not validate-strict), and do require validation at build time.
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/io.otsaloma.%{name}.appdata.xml

%if %{with tests}
%global __pytest %{_bindir}/xvfb-run -a %{_bindir}/pytest
# The skipped test passes in a real Fedora desktop session, but fails under
# xvfb; we do not understand why, although it smells like a trivial font
# issue.
%pytest -k 'not (TestModule and test_char_to_px__font)'
%endif


%files -f %{name}.lang
%license COPYING
%doc AUTHORS.md
%doc README.md
%doc NEWS.md
%doc using-%{name}

%{_bindir}/%{name}

%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%{_datadir}/%{name}
%{_metainfodir}/io.otsaloma.%{name}.appdata.xml
%{_datadir}/applications/io.otsaloma.%{name}.desktop
%{_datadir}/icons/hicolor/symbolic/apps/io.otsaloma.%{name}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/io.otsaloma.%{name}.svg
%{_mandir}/man1/gaupol.1*


%files -n python3-aeidon
%license COPYING
%doc AUTHORS.md
%doc README.aeidon.md
%doc NEWS.md

%{python3_sitelib}/aeidon
%{python3_sitelib}/aeidon-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Mar 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.9-4
- Localize summary and description of main package where translations are
  available upstream

* Tue Feb 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.9-3
- Correct License from “GPLv3+” to “GPLv3+ and CC0”

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.9-1
- Update to 1.9
- Update aeidon package description
- Require minimum python-chardet version 2.2.1

* Sun Dec 20 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.8-2
- Drop BR on hicolor-icon-theme; needed only at install time
- Switch URL from HTTP to HTTPS

* Tue Dec  8 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.8-1
- New upstream version 1.8
- Unbundle iso-codes data dependency
- Use modern RPM macros throughout
- Update summaries and descriptions from upstream
- Enable test suite
- Rename aeidon subpackage to python3-aeidon
- More detailed and accurate dependencies and BR’s
- Make dependency on python3-aeidon subpackage require the exact matching
  version and release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Lucian Langa <lucilanga@gnome.eu.org> - 1.4-1
- metainfo files installed into 'metainfo', not 'appdata'
- new upstream release

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-7
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuild for Python 3.6

* Tue Nov 22 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.0-2
- upped minimum aeidon version requirement

* Tue Nov 22 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.0-1
- misc cleanups
- new upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.25-3
- Attempt to fix FTBFS by adding BR: python3-devel

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Richard Hughes <rhughes@redhat.com> - 0.25-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Lucian Langa <cooly@gnome.eu.org> - 0.19.2-1
- new upstream release

* Mon Sep 26 2011 cooly@gnome.eu.org - 0.19.1-1
- new upstream release

* Sun Jul 31 2011 Lucian Langa <cooly@gnome.eu.org> - 0.19-1
- new upstream release

* Sat Jun 18 2011 Lucian Langa <cooly@gnome.eu.org> - 0.18-1
- new upstream release

* Sun Apr 24 2011 Lucian Langa <cooly@gnome.eu.org> - 0.17.2-1
- drop version from supackage (to match main version)
- new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 18 2010 Lucian Langa <cooly@gnome.eu.org> - 0.17.1-1
- new upstream release

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 08 2010 Lucian Langa <cooly@gnome.eu.org> - 0.17-1
- new supackage aeidon the subtitle engine
- new upstream release

* Fri Apr 02 2010 Lucian Langa <cooly@gnome.eu.org> - 0.15.1-1
- update to 0.15.1

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.15-5
- Update desktop file according to F-12 FedoraStudio feature

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.15-4
- Use bzipped upstream tarball.

* Sun Aug 02 2009 Lucian Langa <cooly@gnome.eu.org> - 0.15-3
- do not remove required file (b.g.o #590537)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Lucian Langa <cooly@gnome.eu.org> - 0.15-1
- add python-chardet as requirement
- new upstream release

* Mon Apr 13 2009 Lucian Langa <cooly@gnome.eu.org> - 0.14-1
- fix Source url
- new upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Lucian Langa <cooly@gnome.eu.org> - 0.13.1-1
- initial package


