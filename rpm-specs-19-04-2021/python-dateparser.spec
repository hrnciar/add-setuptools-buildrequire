%global pypi_name dateparser

Name:           python-%{pypi_name}
Version:        0.7.6
Release:        2%{?dist}
Summary:        A Python parser for human readable dates

License:        BSD
URL:            https://github.com/scrapinghub/dateparser
Source0:        https://github.com/scrapinghub/dateparser/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
dateparser provides modules to easily parse localized dates in almost any
string formats commonly found on web pages.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-convertdate
BuildRequires:  python3-dateutil
BuildRequires:  python3-nose
BuildRequires:  python3-parameterized
BuildRequires:  python3-pytest
BuildRequires:  python3-regex
BuildRequires:  python3-tzlocal
BuildRequires:  python3-mock
BuildRequires:  python3-wheel
BuildRequires:  python3-pytz
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
dateparser provides modules to easily parse localized dates in almost any
string formats commonly found on web pages.

%package -n %{name}-doc
Summary:        Documentation for python3-%{pypi_name}

BuildRequires:  python3-sphinx

%description -n %{name}-doc
This documentation for python3-%{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

#%%check
#PYTHONPATH=%%{buildroot}/%%{python3_sitelib} pytest-%%{python3_version} tests

%files -n python3-%{pypi_name}
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/dateparser_data/
%{python3_sitelib}/dateparser_scripts/

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.7.6-1
- 0.7.6, disabled tests due to missing packages.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.7.4-3
- BR python3-setuptools

* Sat May 23 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.7.4-2
- Rebuilt for Python 3.9

* Tue Mar 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.4-1
- Fix license tag (rhbz#1748956)

* Tue Nov 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-4
- Fix license tag (rhbz#1748956)

* Mon Nov 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-3
- Disable tests

* Mon Nov 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-2
- Fix BRs

* Thu Oct 17 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-1
- Update to latest upstream release 0.7.2

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Initial package for Fedora
