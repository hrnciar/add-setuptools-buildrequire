%global pypi_name pygrocy
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.23.0
Release:        2%{?dist}
Summary:        Python API client for grocy

License:        MIT
URL:            https://github.com/sebrut/pygrocy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python API client for grocy.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(iso8601)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tzlocal)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python API client for grocy.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with network}
%check
%pytest -v test
%endif

%files -n python3-%{pypi_name}
%doc CHANGELOG.md README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%exclude %{python3_sitelib}/test
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.23.0-1
- Initial package for Fedora