%global pypi_name rangeparser
%global pkg_name RangeParser

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        3%{?dist}
Summary:        Parses a list of ranges or numbers

License:        BSD
URL:            https://bitbucket.org/colinwarren/rangeparser
Source0:        %{pypi_source RangeParser}
BuildArch:      noarch

%description
RangeParser is a Python package to parse ranges easily.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
RangeParser is a Python package to parse ranges easily.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -v rangeparser/test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pkg_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-2
- Update summary (#1888981)

* Fri Oct 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- Initial package for Fedora