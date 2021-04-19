# Created by pyp2rpm-3.3.4
%global pypi_name waqiasync

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        2%{?dist}
Summary:        Python API for aqicn.org

License:        MIT
URL:            https://github.com/andrey-git/waqi-async
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Asyncio-friendly Python API for World Air Quality Index.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Asyncio-friendly Python API for World Air Quality Index

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
# https://github.com/andrey-git/waqi-async/pull/2
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package
