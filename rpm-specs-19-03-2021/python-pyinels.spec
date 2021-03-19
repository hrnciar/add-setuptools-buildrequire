%global pypi_name pyinels

Name:           python-%{pypi_name}
Version:        0.5.5
Release:        2%{?dist}
Summary:        Python library for iNels BUS

License:        MIT
URL:            https://github.com/JH-Soft-Technology/pyinels
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python library that handles communication with proprietary home
intelligent system named iNels by ElkoEP company.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python library that handles communication with proprietary home
intelligent system named iNels by ElkoEP company.

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
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.5-1
- Initial package for Fedora