%global pypi_name ring-doorbell

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Python library to communicate with Ring Door Bells

License:        LGPLv3+
URL:            https://github.com/tchellomello/python-ring-doorbell
Source0:        %{url}/archive/%{version}/ring_doorbell-%{version}.tar.gz
BuildArch:      noarch

%description
Python library written that exposes the Ring.com devices as Python
objects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-oauthlib)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests-mock)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python library written that exposes the Ring.com devices as Python
objects.

%prep
%autosetup -n python-ring-doorbell-%{version}
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
%{python3_sitelib}/ring_doorbell/
%{python3_sitelib}/ring_doorbell-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Feb 06 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Update to latest upstream release 0.7.0 (#1925720)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Fix FTI (#1892889)
- Update to latest upstream release 0.6.2 (#1901864)

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Initial package for Fedora
