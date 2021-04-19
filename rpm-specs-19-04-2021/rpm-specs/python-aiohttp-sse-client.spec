%global pypi_name aiohttp-sse-client

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Server-Sent Event Python client

License:        ASL 2.0
URL:            https://github.com/rtfol/aiohttp-sse-client
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Server-Sent Event Python client that provides a simple interface to
process Server-Sent Event.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(multidict)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(yarl)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Server-Sent Event Python client that provides a simple interface to
process Server-Sent Event.

%package -n python-%{pypi_name}-doc
Summary:        aiohttp-sse-client documentation

BuildRequires:  python3dist(sphinx)

%description -n python-%{pypi_name}-doc
Documentation for aiohttp-sse-client

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc docs/readme.rst README.rst
%{python3_sitelib}/aiohttp_sse_client
%{python3_sitelib}/aiohttp_sse_client-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Fix license (#1885501)
- Update to new upstream version 0.2.0

* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.7-1
- Initial package for Fedora