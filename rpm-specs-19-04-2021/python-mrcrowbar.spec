%global pypi_name mrcrowbar

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        2%{?dist}
Summary:        Library and framework for reverse engineering binary file formats

License:        BSD
URL:            https://github.com/moralrecordings/mrcrowbar
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Mr. Crowbar is a Django-esque model framework that makes it super easy
to work with proprietary binary formats while reverse engineering.

File formats are described with Python classes that allow ORM-like free
modification of structures and properties, which in turn can be validated
and converted back to the binary equivalent at any time.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Mr. Crowbar is a Django-esque model framework that makes it super easy
to work with proprietary binary formats while reverse engineering.

File formats are described with Python classes that allow ORM-like free
modification of structures and properties, which in turn can be validated
and converted back to the binary equivalent at any time.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-argparse)

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove shebang
sed -i -e '/^#!\//, 1d' mrcrowbar/lib/games/{boppin.py,keen.py,sam.py,titus.py}
sed -i -e '/^#!\//, 1d' mrcrowbar/lib/hardware/{ibm_pc.py,megadrive.py}
sed -i -e '/^#!\//, 1d' mrcrowbar/lib/os/{dos.py,win16.py}

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{_bindir}/mrc*
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Initial package for Fedora