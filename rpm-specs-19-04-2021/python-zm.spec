%global pypi_name zm-py
%global pkg_name zm

Name:           python-%{pkg_name}
Version:        0.5.2
Release:        2%{?dist}
Summary:        Python wrapper around the ZoneMinder REST API

License:        ASL 2.0
URL:            https://github.com/rohankapoorcom/zm-py
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python wrapper around the ZoneMinder RESTful API.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
A Python wrapper around the ZoneMinder RESTful API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pkg_name}
%license LICENSE.md
%doc README.md
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/zoneminder
%{python3_sitelib}/zm_py-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-2
- Permission issue was fixed upstream
- Update to latest upstream release 0.5.2 (#1888351)

* Sun Oct 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Initial package for Fedora
