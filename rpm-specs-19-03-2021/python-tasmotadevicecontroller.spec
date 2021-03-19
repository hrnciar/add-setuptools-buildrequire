# Created by pyp2rpm-3.3.4
%global pypi_name tasmotadevicecontroller

Name:           python-%{pypi_name}
Version:        0.0.8
Release:        2%{?dist}
Summary:        Control Tasmota devices via their web API

License:        GPLv3
URL:            https://github.com/chaptergy/tasmota-device-controller
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This Python package provides async wrappers for Tasmota's web request API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This Python package provides async wrappers for Tasmota's web request API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/chaptergy/tasmota-device-controller/pull/2
#%%license LICENSE.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.8-1
- Initial package for Fedora