%bcond_without tests

%global pretty_name openant
%global extract_name ant

%global _description %{expand:
A python library to download and upload files from ANT-FS 
compliant devices (Garmin products).Any compliant ANT-FS 
device should in theory work, but those specific devices 
have been reported as working: Garmin Forerunner 60,
Garmin Forerunner 405CX, Garmin Forerunner 310XT, Garmin 
Forerunner 610, Garmin Forerunner 910XT, Garmin FR70, 
Garmin Swim}

Name:           python-%{pretty_name}
Version:        0.4
Release:        3%{?dist}
Summary:        A python library to communicate with ANT-FS compliant devices

License:        MIT
URL:            https://github.com/Tigge/openant
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz
Source2:        ant-usb-sticks.rules

# We do not trigger udev installation from Python setup.py
Patch0:         0001-Remove-udev-install.patch

BuildArch:      noarch

# For the patch
BuildRequires:  git-core

# For udev-rules	
BuildRequires:  systemd

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist pyusb}

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pretty_name}-%{version}

%build
%py3_build

%install
%{!?_udevrulesdir: %global _udevrulesdir %{_sysconfdir}/udev/rules.d}

%py3_install
mkdir -pm 755 %{buildroot}/%{_udevrulesdir}	
install -pm 644 %{SOURCE2} %{buildroot}/%{_udevrulesdir}

%check
%{python3} setup.py test

%post
%udev_rules_update

%postun
%udev_rules_update

%files -n python3-%{pretty_name}
%license LICENCE
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{extract_name}
%config(noreplace) %{_udevrulesdir}/*

%changelog
* Sun Mar 28 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4-3
- Added macro for udev rules update

* Sat Mar 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4-2
- Cosmetic changes

* Fri Feb 26 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4-1
- Added comment for patch
- Fixed Unowned Directories

* Mon Feb 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4-1
- Initial package
