%global pypi_name pytile

Name:           python-%{pypi_name}
Version:        5.2.1
Release:        1%{?dist}
Summary:        Python API for Tile Bluetooth trackers

License:        MIT
URL:            https://github.com/bachya/pytile
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pytile is a simple Python library for retrieving information on Tile
Bluetooth trackers (including last location and more).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(aresponses)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(yarl)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pytile is a simple Python library for retrieving information on Tile
Bluetooth trackers (including last location and more).

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/pylint/d' pyproject.toml      

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# Tests have dependency issue (yarl is not detected)
#%%check
#%%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Wed Mar 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.2.1-1
- Update to latest upstream release 5.1. (fedora#1934437)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.1.1-1
- Update to latest upstream release 5.1.1

* Sat Sep 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.1-1
- Initial package for Fedora