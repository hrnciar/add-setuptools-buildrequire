# Created by pyp2rpm-3.3.4
%global pypi_name respx

Name:           python-%{pypi_name}
Version:        0.16.3
Release:        2%{?dist}
Summary:        Utility for mocking out the HTTPX and HTTP Core libraries

License:        BSD
URL:            https://lundberg.github.io/respx/
Source0:        https://github.com/lundberg/respx/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
An utility for mocking out the Python HTTPX and HTTP Core libraries.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(trio)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
An utility for mocking out the Python HTTPX and HTTP Core libraries.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Coverage is under 100 % due to the excluded tests
sed -i -e '/--cov-fail-under 100/d' setup.cfg

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests -k "not test_pass_through"

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.3-1
- Update to latest upstream release 0.16.3 (#1907495)

* Fri Dec 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.2-1
- Update to latest upstream release 0.16.2 (#1904258)

* Thu Dec 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.0-1
- Update to latest upstream release 0.16.0

* Sat Oct 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Initial package for Fedora