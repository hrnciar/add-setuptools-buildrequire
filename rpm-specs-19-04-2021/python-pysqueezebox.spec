%global pypi_name pysqueezebox

Name:           python-%{pypi_name}
Version:        0.5.5
Release:        2%{?dist}
Summary:        Python library to control Logitech Media Server

License:        ASL 2.0
URL:            https://github.com/rajlaud/pysqueezebox
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python library to control a Logitech Media Server asynchronously.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiohttp)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python library to control a Logitech Media Server asynchronously.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests --ignore tests/test_integration.py

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.5-1
- Enable tests
- Update to latest upstream release 0.5.5

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Update to latest upstream release 0.5.2 (#1884991)

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Initial package for Fedora
