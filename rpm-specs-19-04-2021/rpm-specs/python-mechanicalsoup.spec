%global pypi_name mechanicalsoup

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        2%{?dist}
Summary:        Python library for automating interaction with websites

License:        MIT
URL:            https://mechanicalsoup.readthedocs.io
Source0:        https://github.com/MechanicalSoup/MechanicalSoup/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
MechanicalSoup automatically stores and sends cookies, follows redirects,
and can follow links and submit forms. It doesn't do JavaScript.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-httpbin)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-mock)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MechanicalSoup automatically stores and sends cookies, follows redirects,
and can follow links and submit forms. It doesn't do JavaScript.

%package -n python-%{pypi_name}-doc
Summary:        mechanicalsoup documentation

BuildRequires:  python3dist(sphinx)
%description -n python-%{pypi_name}-doc
Documentation for mechanicalsoup.

%prep
%autosetup -n MechanicalSoup-%{version}
rm -rf %{pypi_name}.egg-info
# No linting
sed -i -e 's/--flake8//g' setup.cfg

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
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/MechanicalSoup-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to latest upstream release 1.0.0 (#1913059)

* Sat Sep 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Initial package for Fedora