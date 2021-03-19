%global pypi_name aiohomekit

Name:           python-%{pypi_name}
Version:        0.2.60
Release:        2%{?dist}
Summary:        Python HomeKit client

License:        ASL 2.0
URL:            https://github.com/Jc2k/aiohomekit
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This library implements the HomeKit protocol for controlling Homekit
accessories.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library implements the HomeKit protocol for controlling Homekit
accessories.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{_bindir}/aiohomekitctl
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.60-1
- Update to latest upstream release 0.2.60 (#1905103)

* Fri Nov 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.57-1
- Update to latest upstream release 0.2.57 (#1896737)

* Sun Nov 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.55-1
- Update to latest upstream release 0.2.55 (#1895136)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.54-1
- Update to latest upstream release 0.2.54 (#1882732)

* Mon Sep 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.52-1
- Update to latest upstream release 0.2.52 (#1878686)

* Sat Aug 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.51-1
- Update to latest upstream release 0.2.51

* Mon Aug 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.50-1
- LICENSE file is now present (rhbz#1871908)

* Mon Aug 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.49-1
- Initial package for Fedora
