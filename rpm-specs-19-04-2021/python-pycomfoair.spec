%global pypi_name pycomfoair

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        2%{?dist}
Summary:        Interface for Zehnder ComfoAir 350 ventilation units

License:        MIT
URL:            https://github.com/mtdcr/pycomfoair
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pycomfoair Python library to monitor and control Zehnder
ComfoAir 350 units.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(async-timeout)
BuildRequires:  python3dist(bitstring)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyserial-asyncio)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pycomfoair Python library to monitor and control Zehnder
ComfoAir 350 units.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# https://github.com/mtdcr/pycomfoair/issues/2
%check
%pytest -v test -k "not test_create_parse and not test_create_parse_hex and not test_bytes"

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/comfoair/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Initial package for Fedora