%global pypi_name adafruit-pureio

Name:           python-%{pypi_name}
Version:        1.1.8
Release:        2%{?dist}
Summary:        Python access to Linux IO including I2C and SPI

License:        MIT
URL:            https://github.com/adafruit/Adafruit_Python_PureIO
Source0:        %{pypi_source Adafruit_PureIO}
BuildArch:      noarch

%description
Pure Python (i.e. no native extensions) access to Linux IO
including I2C and SPI. Drop in replacement for smbus and
spidev modules.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools-scm)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pure Python (i.e. no native extensions) access to Linux IO
including I2C and SPI. Drop in replacement for smbus and
spidev modules.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for adafruit-pureio

BuildRequires:  python3dist(sphinx)

%description -n python-%{pypi_name}-doc
Documentation for adafruit-pureio.

%prep
%autosetup -n Adafruit_PureIO-%{version}
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
%{python3_sitelib}/Adafruit_PureIO
%{python3_sitelib}/Adafruit_PureIO-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.8-1
- Update to latest upstream release 1.1.8 (#1905102)

* Mon Oct 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.7-1
- Initial package for Fedora