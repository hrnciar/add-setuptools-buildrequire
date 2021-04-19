%global pypi_name databay

Name:           python-%{pypi_name}
Version:        0.1.6
Release:        2%{?dist}
Summary:        Python interface for scheduled data transfer

License:        ASL 2.0
URL:            https://github.com/Voyz/databay
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Databay is a Python interface for scheduled data transfer. It facilitates
transfer of (any) data from A to B, on a scheduled interval.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-APScheduler
BuildRequires:  python3-pymongo
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(schedule)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(mongomock)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Databay is a Python interface for scheduled data transfer. It facilitates
transfer of (any) data from A to B, on a scheduled interval.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# https://github.com/Voyz/databay/issues/9
#%%check
#%%pytest -v test -k "not test_event_loop_policy_3_8 and not test_event_loop_policy_3_7"

%files -n python3-%{pypi_name}
%doc README.md
# Was not added to PyPI by upstream
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.6-1
- Disable tests because of asynctest (#1875782)
- Update to latest upstream release 0.1.6

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.5-1
- Initial package for Fedora