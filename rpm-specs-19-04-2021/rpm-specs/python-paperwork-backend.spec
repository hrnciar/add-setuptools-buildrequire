%global srcname paperwork-backend
%global srcname_ paperwork_backend

Name:           python-%{srcname}
Version:        2.0.2
Release:        1%{?dist}
Summary:        Paperwork's backend

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork/tree/master/paperwork-backend
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand: \
Paperwork is a tool to make papers searchable. The basic idea behind Paperwork
is "scan & forget" : You should be able to just scan a new document and forget
about it until the day you need it.

This is the backend part of Paperwork. It manages:
    The work directory / Access to the documents;
    Indexing;
    Searching;
    Suggestions;
    Import;
    Export.
}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(openpaperwork-core)
BuildRequires:  python3dist(openpaperwork-gtk)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pycountry)
BuildRequires:  python3dist(pyocr)
BuildRequires:  python3dist(pypillowfight) >= 0.3
BuildRequires:  python3dist(python-levenshtein)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(simplebayes)
BuildRequires:  python3dist(whoosh)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(pycairo)

BuildRequires:  python3-gobject
BuildRequires:  libinsane-gobject
BuildRequires:  poppler-glib
BuildRequires:  sane-backends-drivers-scanners
BuildRequires:  tesseract
BuildRequires:  tesseract-osd

Requires:       libinsane-gobject
Requires:       python3dist(pygobject)
Requires:       python3dist(pycairo)
Requires:       poppler-glib
Requires:       tesseract
Requires:       tesseract-osd

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p2

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Remove spurious shebangs.
sed -i -e '/^#!\//, 1d' src/%{srcname_}/model/{extra_text,thumbnail}.py

find tests -name '*.pyc' -delete


%build
%py3_build


%install
%py3_install


%check
PATH=%{buildroot}%{_bindir}:$PATH PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{python3} -m unittest discover --verbose -s tests


%files -n python3-%{srcname}
%doc README.markdown
%license LICENSE
%{python3_sitelib}/%{srcname_}/
%{python3_sitelib}/%{srcname_}-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Mar 19 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Update to latest version (#1889059)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-1
- Initial package.
