%global pypi_name pycomm3
# A physical device is needed to run the tests
%bcond_with device

Name:           python-%{pypi_name}
Version:        0.10.2
Release:        2%{?dist}
Summary:        Python library for communicating with Allen-Bradley PLCs

License:        MIT
URL:            https://github.com/ottowayi/pycomm3
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pycomm3 is a native Python library for communicating with PLCs
from Allen-Bradley using Ethernet/IP.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pycomm3 is a native Python library for communicating with PLCs
from Allen-Bradley using Ethernet/IP.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i 's/\r$//' README.rst

%build
%py3_build

%install
%py3_install

%if %{with device}
%check
%pytest -v tests
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.2-1
- Initial package for Fedora
