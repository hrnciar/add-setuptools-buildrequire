%global pypi_name pyvlx

Name:           python-%{pypi_name}
Version:        0.2.19
Release:        2%{?dist}
Summary:        Python wrapper for the Velux KLF 200 API

License:        LGPLv3+
URL:            https://github.com/Julius2342/pyvlx
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyVLX allow you to control VELUX windows with Python. It uses the Velux
KLF 200 interface to control io-Homecontrol devices, e.g., Velux
Windows.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PyVLX allow you to control VELUX windows with Python. It uses the Velux
KLF 200 interface to control io-Homecontrol devices, e.g., Velux
Windows.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v test

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.19-1
- Update to latest upstream release 0.2.19

* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.17-1
- Initial package for Fedora
