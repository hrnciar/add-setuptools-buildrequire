# what it's called on pypi
%global srcname flask-restplus
# what it's imported as
%global libname flask_restplus
# package name fragment
%global pkgname %{srcname}

Name:           python-%{pkgname}
Version:        0.13.0
Release:        6%{?dist}
Summary:        Framework for fast, easy and documented API development with Flask
License:        BSD
URL:            https://github.com/noirbizarre/flask-restplus
Source0:        %pypi_source
BuildArch:      noarch

%global _description %{expand:
Flask-RESTPlus is an extension for Flask that adds support for quickly
building REST APIs. It encourages best practices with minimal setup.
If you are familiar with Flask, Flask-RESTPlus should be easy to pick up.
It provides a coherent collection of decorators and tools to describe your API
and expose its documentation properly using Swagger.}

%description %_description


%package -n     python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{pkgname} %_description


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{libname}.egg-info
rm -f %{libname}/static/files/.npmignore

%build
%py3_build

%install
%py3_install

# Upstream requires pinned dependencies versions
# %%check
# python3 setup.py test

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{libname}-*.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Jiri Popelka <jpopelka@redhat.com> - 0.13.0-2
- add CHANGELOG.rst

* Tue Oct 22 2019 Jiri Popelka <jpopelka@redhat.com> - 0.13.0-1
- init
