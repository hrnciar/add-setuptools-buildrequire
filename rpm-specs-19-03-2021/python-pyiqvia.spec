%global pypi_name pyiqvia

Name:           python-%{pypi_name}
Version:        0.3.3
Release:        1%{?dist}
Summary:        Python API for IQVIA data

License:        MIT
URL:            https://github.com/bachya/pyiqvia
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python API for IQVIA data.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python API for IQVIA data.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Feb 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Update to latest upstream release 0.3.3 (#1933373)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.2-1
- Update to latest upstream release 0.3.2 (#1909962)

* Tue Dec 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to latest upstream release 0.3.1

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora
