%global pypi_name sseclient-py

Name:           python-%{pypi_name}
Version:        1.7
Release:        2%{?dist}
Summary:        SSE client for Python

License:        ASL 2.0
URL:            https://github.com/mpetazzoni/sseclient
Source0:        %{url}/archive/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python client for SSE event sources that seamlessly integrates with
urllib3 and requests.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
A Python client for SSE event sources that seamlessly integrates with
urllib3 and requests.

%prep
%autosetup -n sseclient-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests/unittests.py

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sseclient/
%{python3_sitelib}/sseclient_py-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-1
- Initial package for Fedora