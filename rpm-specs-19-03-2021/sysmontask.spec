%global srcname SysMonTask
%global srcversion %{version}_beta_b

Name: sysmontask
Version: 1.1.1
Release: 0.5.beta.b%{?dist}
Summary: Linux system monitor with the compactness and usefulness of WTM
BuildArch: noarch

# The entire source code is BSD except:
#  * LGPLv2+:   sysmontask/gi_composites.py
License: BSD and LGPLv2+

URL: https://github.com/KrispyCamel4u/SysMonTask
Source0: https://github.com/KrispyCamel4u/%{srcname}/archive/v%{srcversion}/%{srcname}-%{srcversion}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: gtk3
Requires: hicolor-icon-theme

%description
Linux system monitor with the compactness and usefulness of Windows Task
Manager to allow higher control and monitoring.


%prep
%autosetup -n %{srcname}-%{srcversion} -p1

# Invalid version (double separator '-'): 1.1.1-beta-b: python3dist(sysmontask)
# = 1.1.1-beta-b
# https://github.com/KrispyCamel4u/SysMonTask/issues/34
sed -i 's|%{version}-beta-b|%{version}-beta.b|' \
    setup.py

# Lower psutil ver for f33 compatibility
sed -i 's|psutil>=5.7.3|psutil>=5.7.2|' \
    setup.py


%build
%py3_build


%install
%py3_install

sed -i 's|/usr/bin/env python3|%{__python3}|' \
    %{buildroot}%{python3_sitelib}/%{name}/*.py

# E: non-executable-script
chmod +x %{buildroot}%{python3_sitelib}/%{name}/{disk,gpu,mem,%{name}}.py


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc AUTHORS
%doc LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{srcname}.desktop
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/


%changelog
* Thu Mar 11 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.1-0.5.beta.b
- build(update): 1.1.1-0.5.beta.b

* Thu Mar 04 2021 Alessio <alessio AT fedoraproject DOT org> - 1.1.1-0beta
- Initial RPM Release
