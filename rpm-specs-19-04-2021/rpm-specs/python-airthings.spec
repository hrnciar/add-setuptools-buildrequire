%global pypi_name airthings

Name:           python-%{pypi_name}
Version:        3.2.0
Release:        2%{?dist}
Summary:        Fetch sensor measurements from Airthings devices

License:        MIT
URL:            https://github.com/kotlarz/airthings
Source0:        %{pypi_source}
BuildArch:      noarch

%description
airthings is a simple python package that contains methods to communicate
with Airthings devices. The package utilizies bluepy for the communication
between python and the devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(bluepy) = 1.3
%description -n python3-%{pypi_name}
airthings is a simple python package that contains methods to communicate
with Airthings devices. The package utilizies bluepy for the communication
between python and the devices.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/kotlarz/airthings/pull/8
#%%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.2.0-1
- Initial package for Fedora