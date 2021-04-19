# Created by pyp2rpm-3.3.5
%global pypi_name stdiomask

Name:           python-%{pypi_name}
Version:        0.0.6
Release:        2%{?dist}
Summary:        Python module for masking passwords

License:        GPLv3+
URL:            https://github.com/asweigart/stdiomask
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Stdio Mask is a cross-platform Python module for entering passwords to a stdio
terminal and displaying a **** mask, which getpass cannot do.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Stdio Mask is a cross-platform Python module for entering passwords to a stdio
terminal and displaying a **** mask, which getpass cannot do.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i 's/\r$//' README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.6-1
- Update to latest upstream release 0.0.6

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.1-1
- Initial package for Fedora
