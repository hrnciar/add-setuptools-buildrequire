%global pypi_name policyuniverse

Name:           python-%{pypi_name}
Version:        1.3.2.20201012
Release:        2%{?dist}
Summary:        Parse and process AWS IAM policies, statements, ARNs and wildcards

License:        ASL 2.0
URL:            https://github.com/Netflix-Skunkworks/policyuniverse
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The PolicyUniverse package provides classes to parse AWS IAM
and Resource Policies.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The PolicyUniverse package provides classes to parse AWS IAM
and Resource Policies.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2.20201012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2.20201012-1
- Initial package for Fedora
