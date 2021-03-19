%global pypi_name awesomeversion

Name:           python-%{pypi_name}
Version:        21.2.3
Release:        1%{?dist}
Summary:        Python module to deal with versions

License:        MIT
URL:            https://github.com/ludeeus/awesomeversion
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python module to deal with versions if it comes to comparing them. Make
anything a version object, and compare against a vast section of other
version formats.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
Python module to deal with versions if it comes to comparing them. Make
anything a version object, and compare against a vast section of other
version formats.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Only the PyPI source set the version properly
sed -i -e 's/main/%{version}/g' setup.py

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENCE.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Feb 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.2.3-1
- Update to latest upstream release 21.2.3 (#1932296)

* Fri Feb 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.2.2-1
- Update to latest upstream release 21.2.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.1.3-1
- Remove BR and obsolete macro
- Update to latest upstream release 21.1.3 (#1914195)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 20.12.5-1
- Initial package for Fedora
