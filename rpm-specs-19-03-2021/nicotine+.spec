%global altname nicotine
%global appdata_id org.nicotine_plus.Nicotine

Name:           nicotine+
Version:        3.0.2
Release:        1%{?dist}
Summary:        A graphical client for Soulseek

# - IP2Location Country Database (pynicotine/geoip/ipcountrydb.bin) is CC-BY-SA
#   (see pynicotine/geoip/README.md)
# - some icons are GPLv3+ and MIT (see files/icons/themes/original/CREDITS.md)
License:        GPLv3+ and CC-BY-SA and MIT
URL:            https://nicotine-plus.github.io/nicotine-plus/
Source0:        https://github.com/nicotine-plus/nicotine-plus/archive/%{version}/%{name}-%{version}.tar.gz

# NOTE: setuptools is NOT required (see
# https://github.com/Nicotine-Plus/nicotine-plus/commit/74bd408)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
Requires:       gdbm
Requires:       gspell
Requires:       gtk3
Requires:       libappindicator-gtk3
Requires:       %{py3_dist pygobject}
BuildArch:      noarch

%description
Nicotine+ is a graphical client for the Soulseek peer-to-peer file sharing
network. It is an attempt to keep Nicotine working with the latest libraries,
kill bugs, keep current with the Soulseek protocol, and add some new features
that users want and/or need.


%prep
%autosetup -n nicotine-plus-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install

# Remove installed documentation/license files. Useful ones are installed using
# %%doc/%%license
rm -r $RPM_BUILD_ROOT%{_defaultdocdir}/%{altname}/
rm $RPM_BUILD_ROOT%{python3_sitelib}/pynicotine/*/README.md

%find_lang %{altname}


%check
# Tests requiring an Internet connection are disabled
%pytest --deselect=test/unit/test_version.py

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{appdata_id}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{appdata_id}.metainfo.xml


%files -f %{altname}.lang
%doc AUTHORS.md NEWS.md README.md TRANSLATORS.md
%license COPYING files/icons/themes/original/CREDITS.md pynicotine/geoip/README.md
%{_bindir}/%{altname}
%{python3_sitelib}/pynicotine/
%{python3_sitelib}/nicotine_plus-*.egg-info
%{_datadir}/applications/%{appdata_id}.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_metainfodir}/%{appdata_id}.metainfo.xml
%{_mandir}/man1/%{altname}.1.*


%changelog
* Mon Mar 01 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Sun Feb 28 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Sat Dec  5 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.0-2
- Remove useless dependency on xdg-utils

* Sat Dec  5 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- Update License tag

* Tue Oct 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Sun Sep 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- Update License tag

* Sat Sep 12 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.1-1
- Initial RPM release
