%global pypi_name aioesphomeapi

Name:           python-%{pypi_name}
Version:        2.6.6
Release:        1%{?dist}
Summary:        Library to interact with devices flashed with esphome

License:        MIT
URL:            https://esphome.io/
Source0:        https://github.com/esphome/aioesphomeapi/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aioesphomeapi allows you to interact with devices flashed with esphome.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aioesphomeapi allows you to interact with devices flashed with esphome.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Mar 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.6-1
- Update to latest upstream release 2.6.6 (#1939523)

* Mon Feb 15 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.5-1
- Update to latest upstream release 2.6.5 (#1928793)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.4-1
- Update to latest upstream release 2.6.4

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.3-1
- Update to latest upstream release 2.6.3

* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.2-1
- Update to latest upstream release 2.6.2

* Fri Jun 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.1-1
- Initial package for Fedora
