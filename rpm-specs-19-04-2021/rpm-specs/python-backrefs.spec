# Created by pyp2rpm-3.3.5
%global pypi_name backrefs

Name:           python-%{pypi_name}
Version:        5.0.1
Release:        5%{?dist}
Summary:        A wrapper around re and regex that adds additional back references

License:        MIT
URL:            https://github.com/facelessuser/backrefs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(setuptools)

%description
Backrefs is a wrapper around Python's built-in Re and the 3rd party Regex
library. Backrefs adds various additional back references (and a couple other
features) that are known to some regular expression engines, but not to
Python's Re and/or Regex. The supported back references actually vary depending
on the regular expression engine being used as the engine may already have
support for some.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Backrefs is a wrapper around Python's built-in Re and the 3rd party Regex
library. Backrefs adds various additional back references (and a couple other
features) that are known to some regular expression engines, but not to
Python's Re and/or Regex. The supported back references actually vary depending
on the regular expression engine being used as the engine may already have
support for some.

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{pypi_name} -i %{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info extras}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Mar 04 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-5
- Drop some docs files which are not needed (rh#1929991)

* Wed Feb 24 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-4
- Drop Requires: on (backrefs[extras])

* Wed Feb 24 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-3
- Simplify URL: tag usage
- Drop unnecessary egg-info removal
- Use python-extras guidelines to provide python3.Xdist(backrefs[extras])

* Sat Feb 20 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-2
- Change Source to github to use tests

* Thu Feb 18 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-1
- Initial package.
