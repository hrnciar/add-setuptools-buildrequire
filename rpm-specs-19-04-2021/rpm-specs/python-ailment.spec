%global pypi_name ailment

Name:           python-%{pypi_name}
Version:        9.0.6136
Release:        1%{?dist}
Summary:        The angr intermediate language

License:        BSD
URL:            https://github.com/angr/ailment
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
AIL is the angr intermediate language.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
AIL is the angr intermediate language.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Circular dependency with angr
#%%check
#%%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136  (#1920600)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1920600)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1920600)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1920600)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1905670)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5327 (#1905670)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1905670)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1905670)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1905670)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901692)

* Thu Oct 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4663-1
- Update to new upstream release 9.0.4663 (#1891968)

* Sun Oct 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4495-1
- Update to new upstream release 9.0.4495 (#1880185)

* Tue Jul 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.27-1
- Update to new upstream release 8.20.7.27 (#1858211)

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.6-1
- Update to new upstream release 8.20.7.6 (#1858211)

* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.8-1
- Update to latest upstream release 8.20.6.8

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.1-1
- Update to new upstream release 8.20.6.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.20.1.7-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-1
- Initial package for Fedora
