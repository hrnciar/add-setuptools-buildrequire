%global pypi_name pyhomematic

Name:           python-%{pypi_name}
Version:        0.1.71
Release:        2%{?dist}
Summary:        Python Homematic interface

License:        MIT
URL:            https://github.com/danielperna84/pyhomematic
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This library provides easy (bi-directional) control of Homematic
devices hooked up to a regular CCU or Homegear.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides easy (bi-directional) control of Homematic
devices hooked up to a regular CCU or Homegear.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i 's/\r$//' README.rst

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.71-1
- Update to latest upstream release 0.1.71

* Sun Oct 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.70-1
- Update to latest upstream release 0.1.70

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.69-1
- Enable tests
- Update to latest upstream release 0.1.69

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.67-1
- Initial package for Fedora