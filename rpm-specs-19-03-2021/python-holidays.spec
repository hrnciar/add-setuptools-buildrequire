%global pypi_name holidays

Name:           python-%{pypi_name}
Version:        0.10.4
Release:        2%{?dist}
Summary:        Generate and work with holidays in Python

License:        MIT
URL:            https://github.com/dr-prodigy/python-holidays
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A fast, efficient Python library for generating country, province and state 
specific sets of holidays on the fly. It aims to make determining whether a
specific date is a holiday as fast and flexible as possible.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(convertdate)
BuildRequires:  python3dist(korean-lunar-calendar)
BuildRequires:  python3dist(flake8)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A fast, efficient Python library for generating country, province and state 
specific sets of holidays on the fly. It aims to make determining whether a
specific date is a holiday as fast and flexible as possible.

%prep
%autosetup -n %{name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.4-1
- Update to latest upstream releas 0.10.3 (#1904781)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.3-1
- Update to latest upstream release 0.10.3 (#1857281)

* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.2-1
- Update to latest upstream release 0.10.2 (#1823316)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-2
- Rebuilt for Python 3.9

* Sat Feb 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.1-1
- Update to latest upstream release 0.10.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.12-2
- Better use of wildcards (rhbz#1786940)

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.12-1
- Initial package for Fedora
