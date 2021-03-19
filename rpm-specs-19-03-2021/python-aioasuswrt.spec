%global pypi_name aioasuswrt

Name:           python-%{pypi_name}
Version:        1.3.2
Release:        1%{?dist}
Summary:        Python API wrapper for Asuswrt devices

License:        MIT
URL:            https://github.com/kennedyshead/aioasuswrt
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python API wrapper for Asuswrt devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest-runner)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python API wrapper for Asuswrt devices.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Feb 15 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Update to latest upstream release 1.3.2 (#1928353)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Update to latest upstream release 1.3.1 (#1895903)

* Mon Nov 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0 (#1895903)

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.8-1
- Update to latest upstream release 1.2.8 (#1875715)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.7-1
- Initial package for Fedora
