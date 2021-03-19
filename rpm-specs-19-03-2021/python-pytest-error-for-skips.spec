%global pypi_name pytest-error-for-skips

Name:           python-%{pypi_name}
Version:        2.0.2
Release:        2%{?dist}
Summary:        Pytest plugin to treat skipped tests a test failure

License:        MIT
URL:            https://github.com/janschulz/pytest-error-for-skips
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Pytest plugin to treat skipped tests a test failures.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pytest plugin to treat skipped tests a test failures.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_error_for_skips.py
%{python3_sitelib}/pytest_error_for_skips-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Initial package for Fedora 