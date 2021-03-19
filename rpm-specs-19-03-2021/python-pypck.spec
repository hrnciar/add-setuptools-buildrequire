# Created by pyp2rpm-3.3.5
%global pypi_name pypck

Name:           python-%{pypi_name}
Version:        0.7.9
Release:        2%{?dist}
Summary:        Python LCN-PCK library

License:        EPL-2.0
URL:            https://github.com/alengwenus/pypck
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pypck is an open source library written in Python which allows the
connection to the LCN (local control network) system. It uses the
vendor protocol LCN-PCK.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%description -n python3-%{pypi_name}
pypck is an open source library written in Python which allows the
connection to the LCN (local control network) system. It uses the
vendor protocol LCN-PCK.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Tests require asynctest -> issues with Python > 3.8
#%%check
#%%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.9-1
- Update to latest upstream release 0.7.9

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.7-1
- Initial package for Fedora
