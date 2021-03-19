%global pypi_name chirpstack-api

Name:           python-%{pypi_name}
Version:        3.9.4
Release:        1%{?dist}
Summary:        Chirpstack Python API

License:        MIT
URL:            https://github.com/brocaar/chirpstack-api
Source0:        %{pypi_source}
BuildArch:      noarch

%description
ChirpStack gRPC API message and service wrappers for Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
ChirpStack gRPC API message and service wrappers for Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/chirpstack_api
%{python3_sitelib}/chirpstack_api-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Mar 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.9.4-1
- Update to latest upstream release 3.9.4 (#1933686)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.9.3-1
- Update to latest upstream release 3.9.3 (#1909963)

* Thu Dec 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.9.2-1
- Update to latest upstream release 3.9.2 (#1909963)

* Tue Dec 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.9.1-1
- Update to latest upstream release 3.9.1

* Fri Dec 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.8.1-1
- Update to latest upstream release 3.8.1

* Tue Sep 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.7-1
- Initial package for Fedora
