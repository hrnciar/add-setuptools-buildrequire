%global pypi_name sortedcollections

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        2%{?dist}
Summary:        Python Sorted Collections

License:        ASL 2.0
URL:            http://www.grantjenks.com/docs/sortedcollections
Source0:        https://github.com/grantjenks/python-sortedcollections/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python Sorted Collections Sorted Collections is an Apache2 licensed Python
sorted collections library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(sortedcontainers)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python Sorted Collections Sorted Collections is an Apache2 licensed Python
sorted collections library.

%prep
%autosetup -n python-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0 (#1917090)

* Mon Jan 18 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.1-1
- Update to latest upstream release 2.0.1 (#1917090)

* Wed Jan 06 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.3-1
- Update to latest upstream release 1.2.3 (#1913147)

* Sun Sep 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-3
- Add missing BR

* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-2
- Change source to GitHub
- Run tests (rhbz#1876911)

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Initial package for Fedora