%global pypi_name pywizlight

Name:           python-%{pypi_name}
Version:        0.4.5
Release:        1%{?dist}
Summary:        Python connector for WiZ light devices

License:        MIT
URL:            https://github.com/sbidy/pywizlight
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python connector for WiZ light devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python connector for WiZ light devices.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/wizlight
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Feb 11 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.5-1
- Update to latest upstream release 0.4.5 (#1927463)

* Fri Feb 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.4-1
- Update to latest upstream release 0.4.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream release 0.4.1 (#1910904)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.8-1
- Update to latest upstream release 0.3.8 (#1910904)

* Sat Dec 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.7-1
- Update to latest upstream release 0.3.7 (#1910904)

* Sat Dec 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.6-1
- Update to new upstream version 0.3.6 (#1908355)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.5-1
- Update to new upstream version 0.3.5

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Update to new upstream version 0.3.4 (#1884993)

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Initial package for Fedora
