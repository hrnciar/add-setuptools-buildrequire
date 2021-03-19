# Many modules not packaged. Some of them deprecated.
%bcond_with tests

%global pypi_name linux_thermaltake_rgb
%global sys_name linux_thermaltake_riing

Name: linux-thermaltake-rgb
Version: 0.2.0
Release: 1%{?dist}
Summary: Python driver and daemon to control thermaltake Riing fans and pumps
BuildArch: noarch

License: GPLv2
URL: https://github.com/chestm007/linux_thermaltake_riing

# GitHub source because pypi version outdated
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros
BuildRequires: python3dist(setuptools)

%if %{with tests}
# BuildRequires: python3dist(base_test_object)
# BuildRequires: python3dist(pep8)
# BuildRequires: python3dist(usb)
BuildRequires: python3dist(pytest)
%endif

%description
Linux driver and daemon for Thermaltake Riing

Currently supported devices are (as they show up in thermaltakes TTRGBPLUS
software:

- Flow Riing RGB
- Lumi Plus LED Strip
- Pacific PR22-D5 Plus
- Pacific Rad Plus LED Panel
- Pacific V-GTX 1080Ti Plus GPU Waterblock
- Pacific W4 Plus CPU Waterblock
- Riing Plus


%prep
%autosetup -n %{sys_name}-%{version} -p1
sed -i 's/PROJECTVERSION/%{version}/g' setup.py

# fix wrong package requirement for GObject
# https://github.com/chestm007/linux_thermaltake_riing/pull/37
sed -i 's/GObject/PyGObject/g' setup.py

# Remove bundled egg-info
rm -rf %{name}.egg-info


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_datadir}/%{pypi_name}/%{name}.service \
    %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_sysconfdir}/%{pypi_name}
mv %{buildroot}%{_datadir}/%{pypi_name}/config.yml \
    %{buildroot}%{_sysconfdir}/%{pypi_name}


%if %{with tests}
%check
%{python3} -m pytest -v
%endif


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE.txt
%doc README.md roadmap.txt protocol.txt
%config(noreplace) %{_sysconfdir}/%{pypi_name}/config.yml
%dir %{_sysconfdir}/%{pypi_name}
%{_bindir}/%{name}
%{_unitdir}/*.service
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/
%{python3_sitelib}/%{pypi_name}/


%changelog
* Sun Jan 31 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Initial package
