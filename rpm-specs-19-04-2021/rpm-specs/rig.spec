Name:       rig
Summary:    Monitor a system for events and trigger specific actions
Version:    1.0
Release:    2%{?dist}
Url:        https://github.com/TurboTurtle/rig
Source0:    %{url}/archive/%{name}-%{version}.tar.gz
License:    GPLv2
BuildArch:  noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(systemd-python)
BuildRequires: python3dist(psutil)

%description
Rig is a utility designed to watch or monitor specific system resources (e.g.
log files, journals, system activity, etc...) and then take specific action
when the trigger condition is met. Its primary aim is to assist in
troubleshooting and data collection for randomly occurring events.

%prep
%setup -q

%build
%py3_build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m644 man/en/rig.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
%py3_install

%files
%{_bindir}/rig
%{_mandir}/man1/*

%{python3_sitelib}/rig-*.egg-info/
%{python3_sitelib}/rigging/

%license LICENSE
%doc README.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jake Hunsaker <jhunsake@redhat.com> - 1.0-1
- Version 1.0 release