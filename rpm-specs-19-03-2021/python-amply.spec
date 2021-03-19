%bcond_without tests

%global pypi_name amply

%global _description %{expand:
Amply allows you to load and manipulate AMPL data as Python data
structures.

Amply only supports a specific subset of the AMPL syntax:

> set declarations
> set data statements
> parameter declarations
> parameter data statements}

Name:           python-%{pypi_name}
Version:        0.1.4
Release:        1%{?dist}
Summary:        A Python package for AMPL/GMPL datafile parsing

License:        EPL-1.0
URL:            https://github.com/willu47/amply
Source0:        %{pypi_source}

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}
BuildRequires:  %{py3_dist setuptools_scm}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Feb 16 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 0.1.4-1
- Initial build
