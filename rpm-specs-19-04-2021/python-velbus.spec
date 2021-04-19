%global pypi_name python-velbus
%global srcname velbus

Name:           python-%{srcname}
Version:        2.1.2
Release:        1%{?dist}
Summary:        Python Library for the Velbus protocol

License:        MIT
URL:            https://github.com/thomasdelaet/python-velbus
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python library to control the Velbus home automation system.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Python library to control the Velbus home automation system.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/velbus/
%{python3_sitelib}/python_velbus-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Jan 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Update to latest upstream release 2.1.2

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0

* Sun Oct 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.46-1
- Initial package for Fedora