%global pypi_name pymochad

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Python library for interacting with moch

License:        GPLv3+
URL:            https://github.com/mtreinish/pymochad
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python library for sending commands to the mochad TCP gateway daemon
for the X10 CMA15A controller.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hacking)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(stestr)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python library for sending commands to the mochad TCP gateway daemon
for the X10 CMA15A controller.

%package -n python-%{pypi_name}-doc
Summary:        pymochad documentation

BuildRequires:  python3dist(sphinx)
%description -n python-%{pypi_name}-doc
Documentation for pymochad.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest -v pymochad/tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora
