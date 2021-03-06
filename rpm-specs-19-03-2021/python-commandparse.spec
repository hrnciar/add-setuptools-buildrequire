%global pypi_name commandparse

Name:           python-%{pypi_name}
Version:        1.0.8
Release:        3%{?dist}
Summary:        CLI application commands parser

License:        MIT
URL:            https://github.com/flgy/commandparse
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Module to parse command based CLI application.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Module to parse command based CLI application.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# Missing license file: https://github.com/flgy/commandparse/pull/1
#%%license LICENCE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.8-1
- Initial package for Fedora
