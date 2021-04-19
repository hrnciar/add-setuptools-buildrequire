%global pypi_name aioflo

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        2%{?dist}
Summary:        Python library for Flo by Moen Smart Water Detectors

License:        MIT
URL:            https://github.com/bachya/aioflo
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
An asyncio-friendly Python library for Flo Smart Water Detectors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(aresponses)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-cov)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
An asyncio-friendly Python library for Flo Smart Water Detectors.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.md README.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream release 0.4.2

* Tue Sep 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-2
- Switch to GitHub as source
- Switch to pyproject-rpm-macros
- Enable tests (rhbz#1875868)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora