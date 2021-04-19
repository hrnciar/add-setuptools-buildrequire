# Created by pyp2rpm-3.3.5
%global pypi_name bracex

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        2%{?dist}
Summary:        Bash style brace expander

License:        MIT
URL:            https://github.com/facelessuser/bracex
Source0:        https://github.com/facelessuser/bracex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
Bracex is a brace expanding library (à la Bash) for Python.
Brace expanding is used to generate arbitrary strings.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Bracex is a brace expanding library (à la Bash) for Python.
Brace expanding is used to generate arbitrary strings.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.md docs/src/markdown/about/license.md
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Feb 20 2021 Parag Nemade <pnemade AT redhat DOT com> - 2.1.1-2
- Fix this package as per package review (#1929990)
- Change Source to github to use tests

* Thu Feb 18 2021 Parag Nemade <pnemade AT redhat DOT com> - 2.1.1-1
- Initial package.
