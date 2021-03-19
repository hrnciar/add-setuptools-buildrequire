%global pypi_name hatasmota

Name:           python-%{pypi_name}
Version:        0.2.9
Release:        1%{?dist}
Summary:        Python module to help parse and construct Tasmota MQTT messages

License:        MIT
URL:            https://github.com/emontnemery/hatasmota
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python module to help parse and construct Tasmota MQTT messages.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python module to help parse and construct Tasmota MQTT messages.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/HATasmota-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.9-1
- Update to new upstream release 0.2.9 (#1907567)

* Wed Feb 10 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.8-1
- Update to new upstream release 0.2.8 (#1907567)

* Wed Jan 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.7-1
- Update to new upstream release 0.2.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-1
- Update to new upstream release 0.2.5

* Fri Dec 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Update to new upstream release 0.2.2 (#1899295)

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Update to new upstream release 0.2.0 (#1899295)

* Sat Nov 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Update to new upstream release 0.1.2 (#1899295)

* Mon Nov 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Update to new upstream release 0.1.0 (#1899295)

* Tue Nov 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.31-1
- Update to latest upstream release 0.0.31 (#1894704)

* Fri Nov 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.30-1
- Update to latest upstream release 0.0.30 (#1894704)

* Sun Nov 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.27-1
- Update to latest upstream release 0.0.27

* Fri Oct 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.26-1
- Update to latest upstream release 0.0.26 (#1892998)

* Fri Oct 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.25-1
- Update to latest upstream release 0.0.25 (#1892998)

* Wed Oct 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.24-1
- Update to latest upstream release 0.0.24 (#1891925)

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.23-1
- Update to latest upstream release 0.0.23 (#1889169)

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.22-1
- Update to latest upstream release 0.0.22 (#1889169)

* Mon Oct 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20-1
- Update to latest upstream release 0.0.20 (#1889169)

* Sun Oct 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.18-1
- Update to latest upstream release 0.0.18 (#1889106)

* Sat Oct 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.17-1
- Update to latest upstream release 0.0.17 (#1888814)

* Fri Oct 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.16-1
- Update to latest upstream release 0.0.16 (#1888814)

* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.15-1
- Update to latest upstream release 0.0.15

* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Initial package for Fedora