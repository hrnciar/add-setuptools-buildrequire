%global pypi_name archinfo

Name:           python-%{pypi_name}
Version:        9.0.6136
Release:        1%{?dist}
Summary:        Collection of classes that contain architecture-specific information

License:        BSD
URL:            https://github.com/angr/archinfo
Source0:        %{pypi_source}
BuildArch:      noarch

%description
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136 (#1931981)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1920601)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1920601)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1920601)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1905651)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5327-1
- Update to latest upstream release 9.0.5327 (#1905651)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1905651)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1905651)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1905651)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901694)

* Thu Oct 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4663-1
- Update to new upstream release 9.0.4663 (#1891946)

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4495-1
- Update to new upstream release 9.0.4495 (#1880178)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4446-1
- Update to new upstream release 9.0.4446 (#1880178)

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4378-1
- Update to new upstream release 9.0.4378 (#1880178)

* Tue Jul 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.27-1
- Update to new upstream release 8.20.7.27 (#1858194)

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.6-1
- Update to new upstream release 8.20.7.6 (#1858194)

* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.8-1
- Update to latest upstream release 8.20.6.8

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.1-1
- Update to new upstream release 8.20.6.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.20.1.7-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-1
- Initial package for Fedora
