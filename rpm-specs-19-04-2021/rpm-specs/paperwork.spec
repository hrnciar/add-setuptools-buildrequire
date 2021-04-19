%global srcname paperwork

Name:           %{srcname}
Version:        2.0.2
Release:        1%{?dist}
Summary:        Using scanner and OCR to grep dead trees the easy way

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork
Source0:        %{pypi_source}
Patch0001:      0001-Drop-extra-icon-dirs.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       hicolor-icon-theme
Requires:       python3-%{srcname} = %{version}-%{release}

%global _description %{expand: \
Paperwork is a tool to make papers searchable.

The basic idea behind Paperwork is "scan & forget": You should be able to just
scan a new document and forget about it until the day you need it again.

Let the machine do most of the work.
}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(openpaperwork-core)
BuildRequires:  python3dist(openpaperwork-gtk)
BuildRequires:  python3dist(paperwork-backend) >= %{version}
BuildRequires:  python3dist(pycountry)
BuildRequires:  python3dist(pyocr) >= 0.3
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(python-levenshtein)
BuildRequires:  python3dist(pyxdg) >= 0.25
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-gobject
BuildRequires:  gtk3
BuildRequires:  gnome-icon-theme
BuildRequires:  libinsane-gobject
BuildRequires:  libnotify
BuildRequires:  tesseract
BuildRequires:  /usr/bin/xvfb-run

# Fallback to old orientation heuristic just freezes, so ensure this is
# available.
Requires:       tesseract-osd
Requires:       libinsane-gobject

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p2

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    xvfb-run -a \
        python3 -m paperwork_gtk.main install \
            --data_base_dir %{buildroot}%{_datadir} \
            --icon_base_dir %{buildroot}%{_datadir}/icons


%check
export PATH=%{buildroot}%{_bindir}:$PATH PYTHONPATH=%{buildroot}%{python3_sitelib}

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

xvfb-run -a paperwork-gtk chkdeps
xvfb-run -a %{python3} -m unittest discover --verbose -s tests


%files
%{_bindir}/paperwork-gtk
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml

%files -n python3-%{srcname}
%doc README.markdown
%{python3_sitelib}/paperwork_gtk
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Mar 20 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Update to latest version (#1889058)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.9

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove unused BuildRequires

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-3
- Require tesseract-osd so orientation detection doesn't freeze

* Tue Mar 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-2
- Fix icon installation

* Mon Mar 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-1
- Initial package.
