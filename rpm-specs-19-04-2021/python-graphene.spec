# NOTE(jpena): The project requirements specify minimum and maximum versions
#              for all packages, so disabling the automated generation
%{?python_disable_dependency_generator}

%global pypi_name graphene

Name:           python-%{pypi_name}
Version:        3.0b6
Release:        2%{?dist}
Summary:        GraphQL Framework for Python

License:        MIT
URL:            https://github.com/graphql-python/graphene
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(coveralls) >= 1.11
BuildRequires:  python3dist(iso8601) >= 0.1
BuildRequires:  python3dist(promise) >= 2.3
BuildRequires:  python3dist(pytest) >= 5.3
BuildRequires:  python3dist(pytest-asyncio) >= 0.10
BuildRequires:  python3dist(pytest-benchmark) >= 3.2
BuildRequires:  python3dist(pytest-cov) >= 2.8
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
#NOTE(jpena): some build requirements are not available in Fedora, so we have to
#             skip unit tests
# BuildRequires:  python3dist(mock) >= 4
# BuildRequires:  python3dist(pytest-mock) >= 2
# BuildRequires:  python3dist(snapshottest) >= 0.5


%description
Graphene is a Python library for building GraphQL schemas/types fast and easily.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aniso8601) >= 8
# NOTE(jpena): upstream states >= 3.1.2, we will change this when the version is built in Rawhide
Requires:       python3dist(graphql-core) >= 3.1.1
Requires:       python3dist(graphql-relay) >= 3

%description -n python3-%{pypi_name}
Graphene is a Python library for building GraphQL schemas/types fast and easily.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# %{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Javier Pe??a <jpena@redhat.com> - 3.0b6-1
- Update to release 3.0b6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Javier Pe??a <jpena@redhat.com> - 3.0b4-1
- Update to release 3.0b4

* Tue Jun 23 2020 Javier Pe??a <jpena@redhat.com> - 3.0b2-2
- Disable automated dependency generator

* Mon Jun 22 2020 Javier Pe??a <jpena@redhat.com> - 3.0b2-1
- Initial package.
