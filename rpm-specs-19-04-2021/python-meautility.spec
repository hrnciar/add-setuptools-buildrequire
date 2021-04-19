%bcond_without tests

%global pypi_name meautility
%global pretty_name MEAutility

%global _description %{expand:
Python package for multi-electrode array (MEA) handling and stimulation.
Documentation is available at https://meautility.readthedocs.io/}

Name:           python-%{pypi_name}
Version:        1.4.8
Release:        2%{?dist}
Summary:        Package for multi-electrode array (MEA) handling and stimulation

License:        GPLv3
URL:            https://github.com/alejoe91/%{pretty_name}/
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pyyaml}
BuildRequires:  %{py3_dist matplotlib}
%endif


%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pretty_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{pytest}
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pretty_name}

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.8-1
- Remove docs: bundle fonts
- Remove unneeded comments
- Use pytest macro

* Thu Nov 26 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.8-1
- Initial build
