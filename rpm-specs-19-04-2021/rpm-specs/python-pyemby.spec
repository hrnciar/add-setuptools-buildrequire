%global pypi_name pyemby
%global upstream_name pyEmby

Name:           python-%{pypi_name}
Version:        1.6
Release:        2%{?dist}
Summary:        Python module to interact with a Emby media server

License:        MIT
URL:            https://github.com/mezz64/pyemby
Source0:        %{pypi_source %{upstream_name}}
BuildArch:      noarch

%description
This is a Python module aiming to interact with the Emby Media
Server API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a Python module aiming to interact with the Emby Media
Server API.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{upstream_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6-1
- Initial package for Fedora