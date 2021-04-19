%global pypi_name aiolifx

Name:           python-%{pypi_name}
Version:        0.6.9
Release:        2%{?dist}
Summary:        Python API for local communication with LIFX devices

License:        MIT
URL:            http://github.com/frawau/aiolifx
Source0:        %{pypi_source}
BuildArch:      noarch

%description
aiolifx is a Python library to control Lifx LED light bulbs 
over your LAN.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiolifx is a Python library to control Lifx LED light bulbs 
over your LAN.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# https://github.com/frawau/aiolifx/pull/37
sed -i -e '/^#!\//, 1d' aiolifx/{__main__.py,aiolifx.py,update-products.py}
# Remove script to maintain parts of the source
rm -rf aiolifx/update-products.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.9-1
- Update to latest upstream release 0.6.9 (#1918314)

* Mon Aug 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.8-1
- Initial package for Fedora