%global pypi_name aresponses
%bcond_with network

Name:           python-%{pypi_name}
Version:        2.1.4
Release:        2%{?dist}
Summary:        Asyncio testing server

License:        MIT
URL:            https://github.com/circleup/aresponses
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
An asyncio testing server for mocking external services.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
An asyncio testing server for mocking external services.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with network}
%pytest -v tests
%endif
%pytest -v tests -k "not test_foo and not test_passthrough"

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 08:26:21 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Update to latest upstream release 2.1.3 (#1917037)

* Sun Jan 17 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Update to latest upstream release 2.1.2 (#1917037)

* Mon Jan 11 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0 (#1910316)

* Wed Dec 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Update to latest upstream release 2.0.2 (#1910316)

* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Initial package for Fedora
