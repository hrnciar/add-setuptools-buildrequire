%global pypi_name mysqlclient
%bcond_with mysqldb

Name:           python-%{pypi_name}
Version:        2.0.3
Release:        1%{?dist}
Summary:        MySQL/mariaDB database connector for Python

License:        GPLv2
URL:            https://github.com/PyMySQL/mysqlclient
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  mariadb-connector-c-devel

%description
MySQLdb is an interface to the popular MySQL database server that provides
the Python database API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with mysqldb}
%check
BuildRequires:  python3-pytest
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MySQLdb is an interface to the popular MySQL database server that provides
the Python database API.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

BuildRequires:  python3-sphinx
%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%if %{with mysqldb}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests
%endif

%files -n python3-%{pypi_name}
%doc README.md HISTORY.rst
%license LICENSE
%{python3_sitearch}/MySQLdb/
%{python3_sitearch}/%{pypi_name}-%{version}-py*.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-1
- Update to latest upstream release 2.0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Honza Horak <hhorak@redhat.com> - 2.0.0-2
- Use correct name for the connector package

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.6-2
- Add tests and missing BR
- Fix license (rhbz#1816295)

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.6-1
- Initial package for Fedora
