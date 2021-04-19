# Created by pyp2rpm-3.3.5
%global pypi_name pcicrawler

%global common_description %{expand:
pcicrawler is a CLI tool to display/filter/export information about PCI or PCI
Express devices and their topology.}

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Display/filter/export information about PCI or PCI Express devices

License:        MIT
URL:            https://github.com/facebook/pcicrawler
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{common_description}

%package -n     %{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} == 32 || 0%{?rhel} == 8
%py_provides    python3-%{pypi_name}
%endif

%description -n %{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unnecessary shebang
sed -e '\|#!/usr/bin/env python|d' -i */*.py

%build
%py3_build

%install
%py3_install

%files -n %{pypi_name}
%doc README.md
%{_bindir}/pcicrawler
%{python3_sitelib}/pci_lib
%{python3_sitelib}/pci_vpd_lib
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Mar 11 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-1
- Initial package.
