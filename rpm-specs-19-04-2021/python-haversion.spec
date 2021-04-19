%global pypi_name pyhaversion
%global pkg_name haversion

Name:           python-%{pkg_name}
Version:        20.12.1
Release:        2%{?dist}
Summary:        Python module to get the version number of Home Assistant

License:        MIT
URL:            https://github.com/ludeeus/pyhaversion
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python module to get the version number of Home Assistant.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(async-timeout)
BuildRequires:  python3dist(awesomeversion)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(semantic-version)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(aresponses)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pkg_name}
A Python module to get the version number of Home Assistant.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e 's/master/%{version}/g' setup.py

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pkg_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 20.12.1
- UPdate to latest upstream release 20.12.1

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0-1
- Initial package for Fedora
