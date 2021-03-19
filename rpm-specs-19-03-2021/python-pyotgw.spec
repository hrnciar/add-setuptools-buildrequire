%global pypi_name pyotgw

Name:           python-%{pypi_name}
Version:        1.0b1
Release:        2%{?dist}
Summary:        Python library to interface with the OpenTherm Gateway

License:        GPLv3+
URL:            https://github.com/mvn23/pyotgw
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python library to interface with the OpenTherm Gateway.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python library to interface with the OpenTherm Gateway

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0b1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0b1-1
- Fix license tag (#1880665)
- Update versioning
- Update to latest upstream release 1.0b1

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-0.b
- Initial package for Fedora