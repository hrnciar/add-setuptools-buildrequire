Name:           mailnag
Version:        2.2.0
Release:        1%{?dist}
Summary:        Mail notification daemon

License:        GPLv2
URL:            https://github.com/pulb/%{name}
Source0:        https://github.com/pulb/%{name}/archive/v%{version}.tar.gz

Requires:       python3
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-gstreamer1
Requires:       python3-pyxdg
Requires:       gnome-keyring

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Mailnag checks POP3 and IMAP servers for new mail and when it finds one
creates a proper GNOME 3 notification that mentions sender and subject.


%prep
%setup -q -n mailnag-%{version}

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/mailnag.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/mailnag-config.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/*.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS LICENSE NEWS README.md
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/metainfo/
%{python3_sitelib}/Mailnag
%{python3_sitelib}/%{name}-*-*.egg-info
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}*png

%changelog
* Mon Feb 15 2021 Thorsten Leemhuis <fedora@leemhuis.info> - 2.2.0-1
- update to version 2.2.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Thorsten Leemhuis <fedora@leemhuis.info> - 2.1.0-1
- update to version 2.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Thorsten Leemhuis <fedora@leemhuis.info> - 2.0.0-4
- update to version 2.0

* Tue Mar 31 2020 Thorsten Leemhuis <fedora@leemhuis.info> - 2.0.0-2.20200331.2
- update to newest snapshot

* Sat Mar 21 2020 Thorsten Leemhuis <fedora@leemhuis.info> - 2.0.0-2.20200321.1
- update to newest snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-1.py3migration.20191103.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Thorsten Leemhuis <fedora@leemhuis.info> - 2.0.0-0.py3migration.20191029.1
- update to newest snapshot, which fixes a few issues we had to work around in
  the spec file

* Tue Oct 29 2019 Thorsten Leemhuis <fedora@leemhuis.info> - 1.3.0-0.py3migration.20191029.1
- switch to python3-migration snapshot, as python2 nears EOL in rawhide

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Thorsten Leemhuis <fedora@leemhuis.info> - 1.3.0-1
- update to 1.3.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Kamil Páral <kparal@redhat.com> - 1.2.1-9
- Remove python2-notify dependency. It has been retired since F29.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-6
- Remove obsolete scriptlets

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 12 2016 Thorsten Leemhuis <fedora@leemhuis.info> - 1.2.1-1
- update to 1.2.1
- add appdata stuff (use appstream-util, BR libappstream-glib)

* Sun Mar 27 2016 Thorsten Leemhuis <fedora@leemhuis.info> - 1.2.0-1
- update to 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Thorsten Leemhuis <fedora@leemhuis.info> - 1.1.0-3
- update to 1.1.0
- adjust BR: s/gstreamer-python/gstreamer1-python/
- drop require on httplib2, not needed anymore
- drop require on gnome-keyring, it's optional now
- add dbus-python as requires, as mentioned in docs

* Sun Jun 29 2014 Thorsten Leemhuis <fedora@leemhuis.info> - 1.0.0-1
- update to 1.0.0
- drop patches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Thorsten Leemhuis <fedora@leemhuis.info> - 0.5.2-4
- add patch to fix sound problem (rhbz #1015900 comment 4)

* Sun Nov 03 2013 Thorsten Leemhuis <fedora@leemhuis.info> - 0.5.2-3
- add patch to work around a API change in NotifyNotification (rhbz #1015900)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Nov 25 2012 Thorsten Leemhuis <fedora@leemhuis.info> - 0.5.2-1
- update to 0.5.2

* Sun Nov 25 2012 Thorsten Leemhuis <fedora@leemhuis.info> - 0.4.4-1
- update to 0.4.4

* Sun Oct 07 2012 Thorsten Leemhuis <fedora@leemhuis.info> - 0.4.3-1
- update to 0.4.3
- use the newly added setup.py for install, which simplifies the spec file
  a lot

* Mon Aug 13 2012 Thorsten Leemhuis <fedora@leemhuis.info> - 0.4.2-2
- apply patch that fixes a issue found during review #847512

* Sat Aug 11 2012 Thorsten Leemhuis <fedora@leemhuis.info> - 0.4.2-1
- initial build
