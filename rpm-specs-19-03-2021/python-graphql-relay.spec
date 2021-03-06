%global pypi_name graphql-relay

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Relay library for Graphql

License:        MIT
URL:            https://github.com/graphql-python/graphql-relay-py
Source0:        %{pypi_source}
BuildArch:      noarch

%description
GraphQL-relay is the Relay library for GraphQL-core implemented in Python.
It allows the easy creation of Relay-compliant servers using GraphQL-core.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-graphql-core
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(graphql-core)
%description -n python3-%{pypi_name}
GraphQL-relay is the Relay library for GraphQL-core implemented in Python.
It allows the easy creation of Relay-compliant servers using GraphQL-core.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/graphql_relay/
%{python3_sitelib}/graphql_relay-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Update to latest upstream release 3.1.0 (#1933192)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-3
- Add missing BRs

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-2
- Remove requirement (rhbz#1836568)

* Thu May 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Initial package for Fedora
