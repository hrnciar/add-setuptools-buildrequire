Name: sqm-scripts
Version: 1.5.0
Release: 2%{?dist}
Summary: Traffic shaper scripts of the CeroWrt project
License: GPLv2
URL: https://www.bufferbloat.net/projects/cerowrt/wiki/Smart_Queue_Management/
Source0: https://github.com/tohojo/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Workaround for network-manager bug: https://github.com/tohojo/sqm-scripts/pull/129
Patch0: %{name}-1.4.0-run_service_after_network.patch
BuildArch: noarch
BuildRequires: make
%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
"Smart Queue Management", or "SQM" is shorthand for an integrated network
system that performs better per-packet/per flow network scheduling, active
queue length management (AQM), traffic shaping/rate limiting, and QoS
(prioritization).

%prep
%autosetup -p1

%build
%{make_build}

%install
%{make_install} UNIT_DIR=%{?buildroot}%{_unitdir}

%files
%doc README.md
%dir %{_sysconfdir}/sqm
%{_sysconfdir}/sqm/default.conf
%config(noreplace) %{_sysconfdir}/sqm/sqm.conf
%{_bindir}/sqm
%{_prefix}/lib/sqm
%{_unitdir}/sqm@.service
%{_tmpfilesdir}/sqm.conf

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Toke Høiland-Jørgensen <toke@redhat.com> - 1.5.0-1
- Bump to upstream 1.5.0
- Set UNIT_DIR on 'make install'

* Tue Dec 08 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.0-3
- Start service after network-online.target

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.0-1
- Initial release
