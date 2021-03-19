%global pypi_name jsonpath-ng

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        3%{?dist}
Summary:        Implementation of JSONPath for Python

# Main library: ASL 2.0
# jsonpath_ng/bin/jsonpath.py: WTFPL
License:        ASL 2.0 and WTFPL
URL:            https://github.com/h2non/jsonpath-ng
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Implementation of JSONPath for Python that aims to be standard compliant,
including arithmetic and binary comparison operators, as defined in the
original JSONPath proposal.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(ply)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(oslotest)
BuildRequires:  python3dist(testscenarios)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Implementation of JSONPath for Python that aims to be standard compliant,
including arithmetic and binary comparison operators, as defined in the
original JSONPath proposal.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' jsonpath_ng/bin/jsonpath.py
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/jsonpath_ng
%{python3_sitelib}/jsonpath_ng/
%{python3_sitelib}/jsonpath_ng-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-2
- Clarify licensing (rhbz#1871269)

* Fri Aug 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-1
- Initial package for Fedora
