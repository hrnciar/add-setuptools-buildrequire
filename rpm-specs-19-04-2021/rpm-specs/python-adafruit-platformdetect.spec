%global pypi_name adafruit-platformdetect

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        Platform detection module

License:        MIT
URL:            https://github.com/adafruit/Adafruit_Python_PlatformDetect
Source0:        %{pypi_source Adafruit-PlatformDetect}
BuildArch:      noarch

%description
This library provides best-guess platform detection for a range of
single-board computers and (potentially) other platforms.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides best-guess platform detection for a range of
single-board computers and (potentially) other platforms.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for adafruit-platformdetect

BuildRequires:  python3dist(sphinx)
%description -n python-%{pypi_name}-doc
Documentation for adafruit-platformdetect.

%prep
%autosetup -n Adafruit-PlatformDetect-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%ifarch %{arm} %{arm64}
%check
%pytest -v tests
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/adafruit_platformdetect/
%{python3_sitelib}/Adafruit_PlatformDetect-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Feb 17 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.1-1
- Update to latest upstream release 3.1.1 (#1929390)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Update to latest upstream release 3.1.0 (#1916400)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.28.0-1
- Update to latest upstream release 2.28.0 (#1916400)

* Tue Jan 19 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.27.0-1
- Update to latest upstream release 2.27.0 (#1916400)

* Mon Jan 18 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.26.0-1
- Update to latest upstream release 2.26.0 (#1916400)

* Thu Jan 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.25.0-1
- Update to latest upstream release 2.25.0 (#1912539)

* Mon Jan 04 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.24.0-1
- Update to latest upstream release 2.24.0 (#1912539)

* Mon Dec 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.23.0-1
- Update to latest upstream release 2.23.0 (#1905200)

* Fri Dec 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.22.2-1
- Update to latest upstream release 2.22.2

* Tue Oct 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.18.2-1
- Initial package for Fedora