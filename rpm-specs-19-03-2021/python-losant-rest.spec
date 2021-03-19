# Created by pyp2rpm-3.3.4
%global pypi_name losant-rest

Name:           python-%{pypi_name}
Version:        1.11.0
Release:        2%{?dist}
Summary:        REST client for the Losant API

License:        MIT
URL:            https://github.com/Losant/losant-rest-python
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The REST API client provides a simple way to use the comprehensive Losant API.
You can authenticate either as a Losant device or with your user account, and
have access to all the functionality of the Losant platform.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests-mock)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The REST API client provides a simple way to use the comprehensive Losant API.
You can authenticate either as a Losant device or with your user account, and
have access to all the functionality of the Losant platform.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-python-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# The test suite is not pick-up automatically
%pytest -v tests/losantrest_tests.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/losantrest/
%{python3_sitelib}/losant_rest-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc docs/
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.11.0-1
- Add -doc subpackage
- Update to latest upstream release 1.11.0 (#1883151)

* Sat Sep 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.4-1
- Initial package for Fedora