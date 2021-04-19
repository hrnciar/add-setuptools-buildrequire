# Created by pyp2rpm-3.3.5
%global pypi_name pytest-smartcov

%global common_description %{expand:
Smart coverage measurement and reporting for py.test test suites. Test suites
are usually structured parallel to (or integrated with) the structure of the
code they test. If you ask py.test to run a certain subset of your tests, you
shouldn't have to also tell coverage which subset of your code it should
measure coverage on for that run. With pytest-smartcov, you don't have to.}

Name:           python-%{pypi_name}
Version:        0.3
Release:        1%{?dist}
Summary:        Smart coverage plugin for pytest

License:        BSD
URL:            https://github.com/carljm/pytest-smartcov
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/smartcov.py
%{python3_sitelib}/pytest_smartcov-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Apr 02 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.3-1
- Initial package.
