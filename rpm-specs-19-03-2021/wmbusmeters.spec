%global with_tag 1

Name:                  wmbusmeters
%global forgeurl       https://github.com/weetmuts/%{name}

%if %{with_tag}
%global tag            1.1.0
Version:               %{tag}
%else
%global date           20201218
%global commit         9c7d7dd270dec07a8e521bf5c0bef07bd318567a
Version:               1.0.4
%endif

%forgemeta

Release:               6%{?dist}
Summary:               Read the wireless mbus protocol to acquire utility meter readings
License:               GPLv3+
Url:                   %{forgeurl}
Source0:               %{forgesource}
# Default configuration file
# Stores all logs in journald
Source1:               file://%{name}.conf
# Systemd service file
Source2:               file://%{name}.service

BuildRequires:         /usr/bin/git
BuildRequires:         /usr/bin/make
BuildRequires:         gcc-c++
BuildRequires:         systemd-rpm-macros
BuildRequires:         ncurses-devel
BuildRequires:         rtl-sdr-devel
BuildRequires:         libusbx-devel

Requires:              /usr/bin/rtl_wmbus


%description
The program receives and decodes C1,T1 or S1 telegrams
(using the wireless mbus protocol) to acquire utility meter readings.
The readings can then be published using MQTT, curled to a REST api,
inserted into a database or stored in a log file.


%prep
%forgeautosetup -S git


%build
%set_build_flags
%{make_build} STRIP=true COMMIT_HASH="" TAG=%{version} COMMIT=%{version} \
    TAG_COMMIT=%{version}%{distprefix} CHANGES=""


%install
%{make_install} STRIP=true COMMIT_HASH="" TAG=%{version} COMMIT=%{version} \
    TAG_COMMIT=%{version} CHANGES="" \
    DESTDIR=%{buildroot} EXTRA_INSTALL_OPTIONS="--no-adduser --no-udev-rules"

# We are using journald
rm -rf %{buildroot}%{_sysconfdir}/logrotate.d/

# Create directory for storing pid files.
install -m 0755 -d %{buildroot}/%{_rundir}/%{name}/

# Fix systemd unit dir location
mv %{buildroot}/lib %{buildroot}/%{_prefix}

# We are installing template version
rm -f %{buildroot}%{_unitdir}/%{name}.service

# Install default configuration file
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.conf

# Install systemd service file
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service


%files
%license LICENSE
%doc README.md CHANGES HowToAddaNewMeter.txt
%dir %{_sysconfdir}/%{name}.d/
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/wmbusmetersd
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}*
%ghost %{_rundir}/%{name}/


%post
%systemd_post %{name}.service
 
%preun
%systemd_preun %{name}.service
 
%postun
%systemd_postun_with_restart %{name}.service


%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 22 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.0-5
- Update to 1.1.0 (#1922583),
- Remove duplicate BR for make.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.4-2
- Switch (as per upstream) to non template unit file

* Mon Dec 07 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.4-1
- Update to the latest available version

* Sat Oct 31 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.36-2
- Allows to build non-released versions

* Tue Sep 08 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.36-1
- Update to the latest available version

* Mon Aug 31 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.35-1
- Update to the latest available version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.32-1
- Update to the latest available version

* Mon May 25 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.31-2
- Add missing ncurses-devel BR

* Mon May 25 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.31-1
- Update to the latest available version

* Thu Apr 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.30-1
- Update to the latest available version

* Fri Apr 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.29-1
- Update to the latest available version

* Tue Mar 24 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.28-1
- Update to the latest available version
- Drop patches upstream merged

* Mon Mar 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-6
- Remove -v from the forgemeta
- Remove instead of exclude logrotate.d directory
- Use %%{_prefix} instead of /usr
- Add %%systemd_{*} scriplets

* Wed Mar 04 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-5
- Add creation of /run/wmbusmeters dir. to the service file.

* Tue Mar 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-4
- Use %%set_build_flags

* Tue Mar 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-3
- Fix wmbusmeters.d accessability
- Store all logs in journald

* Mon Mar 02 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-2
- Add upstream reference to pathces.

* Fri Feb 28 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-1
- Initial RPM release.
