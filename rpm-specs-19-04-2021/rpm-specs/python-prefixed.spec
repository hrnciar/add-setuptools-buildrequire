%global pypi_name prefixed
%global desc %{expand:
Prefixed provides an alternative implementation of the built-in float which
supports formatted output with SI (decimal) and IEC (binary) prefixes.}

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        2%{?dist}
Summary:        Prefixed alternative numeric library

License:        MPLv2.0
URL:            https://github.com/Rockhopper-Technologies/prefixed
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-devel

%description %{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest

%files -n python3-%{pypi_name}
%doc README*
%license LICENSE
%{python3_sitelib}/prefixed*

%changelog
* Sun Jan 31 2021 Avram Lubkin <aviso@rockhopper.net> - 0.3.2-2
- Implement review feedback

* Mon Jan 18 2021 Avram Lubkin <aviso@rockhopper.net> - 0.3.2-1
- Initial package.
