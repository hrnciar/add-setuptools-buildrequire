# Created by pyp2rpm-3.3.4
%global pypi_name waterfurnace

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        2%{?dist}
Summary:        Python interface for Waterfurnace geothermal systems

License:        ASL 2.0
URL:            https://github.com/sdague/waterfurnace
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python interface for waterfurnace geothermal systems.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(websocket-client)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python interface for Waterfurnace geothermal systems.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}

BuildRequires:  python3dist(sphinx)

%description -n python-%{pypi_name}-doc
Documentation for python-%{pypi_name}.

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
%doc README.rst
%{_bindir}/waterfurnace-debug
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora