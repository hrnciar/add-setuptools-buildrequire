%global pypi_name pynuvo

Name:           python-%{pypi_name}
Version:        0.2
Release:        2%{?dist}
Summary:        Python API for talking to Nuvo multi zone amplifier

License:        MIT
URL:            https://github.com/ejonesnospam/pynuvo
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python API interface implementation for Nuvo zone amplifier.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python API interface implementation for Nuvo zone amplifier.


%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/ejonesnospam/pynuvo/pull/1
#%%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2-1
- Initial package for Fedora