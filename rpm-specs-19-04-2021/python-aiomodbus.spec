%global pypi_name aiomodbus

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        2%{?dist}
Summary:        Lightweight Python Modbus library

License:        MIT
URL:            https://github.com/pazzarpj/aiomodbus
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A lightweight Python module for Modbus.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyserial-asyncio)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-mock)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A lightweight Python module for Modbus.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i 's/\r$//' README.md

%build
%py3_build

%install
%py3_install

%check
%pytest -v test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.2-1
- Initial package for Fedora
