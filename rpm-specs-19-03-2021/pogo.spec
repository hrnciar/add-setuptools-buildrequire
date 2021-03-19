Name:		pogo
Version:	1.0.1
Release:	2%{?dist}
Summary:	Probably the simplest and fastest audio player for Linux
Summary(de):	Möglicherweise der einfachste und schnellste Audioplayer für Linux

License:	GPLv2+
URL:		https://launchpad.net/%{name}
Source0:	https://github.com/jendrikseipp/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires: make
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	python3-devel
BuildRequires:	libappstream-glib
Requires:	python3-dbus
Requires:	python3-mutagen
Requires:	python3-pillow
Requires:	python3-inotify
Requires:	python3-gobject
Requires:	python3-gstreamer1
Obsoletes: pogo < %{version}
Obsoletes: pogo-zeitgeist < %{version}

%description
Pogo's elementary-inspired design uses the screen-space very efficiently. It is
especially well-suited for people who organize their music by albums on the
harddrive. The main interface components are a directory tree and a playlist
that groups albums in an innovative way.
Pogo is a fork of Decibel Audio Player.

%description -l de
Das Elementary-inspirierte Design von Pogo nutzt den Platz auf dem Bildschirm
effizient. Es richtet sich speziell an Benutzer, die Ihre Musik nach Alben
auf der Festplatte verwalten. Die Hauptkomponenten der Benutzeroberfläche
sind ein Ordnerbaum und eine Wiedergabeliste, die Alben auf innovative
Weise gruppiert.
Pogo ist ein Fork des Decibel Audio Players.

%prep
%autosetup

%build
#nothing to build

%install
%make_install

%find_lang %{name}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

#AppData
install -D -p -m644 %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.1-1
- Update to 1.0.1 fixes rhbz#1834633

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.0-3
- python-CDDB only works with python2, drop it for now

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-2
- Drop unused Python 2 dependencies

* Sat Aug 25 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.0-1
- new upstream version 1.0 + spec cleanup and modernization

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-2
- Rebuilt for Python 3.7

* Wed Mar 14 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.2-1
- Rebuilt for new upstream version 0.9.2, fixes rhbz #1551445
- Pogo now supports python3
- Obsoletes pogo-zeitgeist package

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.4-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.4-1
- Rebuilt for new upstream version 0.8.4

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 28 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.3-1
- Rebuilt for new upstream version 0.8.3

* Mon Jun 09 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.2-1
- Rebuilt for new upstream version 0.8.2, silent rpmlint

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Jaromir Capik <jcapik@redhat.com> - 0.8.1-4
- Fixing typo in the zeitgeist subpackage group membership (#1068996)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Mario Blättermann <mariobl@fedoraproject.org> - 0.8.1-1
- New upstream version
- Preparation for use Pillow instead of PIL

* Fri Sep 28 2012 Mario Blättermann <mariobl@fedoraproject.org> - 0.8-1
- New upstream version

* Sun Apr 01 2012 Mario Blättermann <mariobl@fedoraproject.org> 0.7-1
- New upstream version

* Sun Apr 01 2012 Mario Blättermann <mariobl@fedoraproject.org> 0.6-1
- New upstream version
- Removed patch again
- Splitted Zeitgeist functionality into a subpackage 

* Tue Mar 20 2012 Mario Blättermann <mariobl@fedoraproject.org> 0.5-2
- Added more info about the patch
- Consistent use of macros

* Sun Mar 11 2012 Mario Blättermann <mariobl@fedoraproject.org> 0.5-1
- initial package
