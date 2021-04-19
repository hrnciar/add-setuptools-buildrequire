Name:       miniupnpd
Version:    2.2.0
Release:    3%{?dist}
Summary:    Daemon to offer UPnP-IGD and NAT-PMP support

License:    BSD
URL:        http://miniupnp.free.fr/
Source0:    http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
Source1:    miniupnpd.service

BuildRequires:  gcc
%{?systemd_requires}
BuildRequires:  systemd
%if 0%{?with_nftables}
Buildrequires:  libmnl-devel
Buildrequires:  libnftnl-devel
%else
BuildRequires:  iptables-devel
%endif
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  procps-ng


%description
The MiniUPnP daemon is a UPnP Internet Gateway Device.

UPnP and NAT-PMP are used to improve internet connectivity for devices behind
a NAT router. Any peer to peer network application such as games, IM, etc. can
benefit from a NAT router supporting UPnP and/or NAT-PMP.


%prep
%setup -q


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
./configure \
 --ipv6 \
 --igd2 \
%if 0%{?with_nftables}
 --firewall=nftables
%else
 --firewall=iptables
%endif
sed -i 's/OS_NAME.*$/OS_NAME "Fedora"/' config.h
sed -i 's/OS_VERSION.*$/OS_VERSION "%{fedora}"/' config.h
sed -i 's/OS_URL.*$/OS_URL "https:\/\/getfedora.org"/' config.h
sed -i 's/^CFLAGS.*$//g' Makefile
sed -i 's/^LDFLAGS.*$//g' Makefile
make %{?_smp_mflags}


%install
export STRIP="/bin/true"
%make_install

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

#Do not ship SysVinit script
rm -f %{buildroot}/etc/init.d/%{name}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc INSTALL README
%{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/ip6tables_init.sh
%{_sysconfdir}/%{name}/ip6tables_removeall.sh
%{_sysconfdir}/%{name}/iptables_init.sh
%{_sysconfdir}/%{name}/iptables_removeall.sh
%{_sysconfdir}/%{name}/miniupnpd_functions.sh
%config(noreplace) %{_sysconfdir}/%{name}/miniupnpd.conf
%{_mandir}/man8/%{name}.8.gz
%{_unitdir}/%{name}.service


%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 - Michael Cronenworth <mike@cchtml.com> - 2.2.0-1
- Version update

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 2.1-7
- Patch CVEs (RHBZ#1714990,1715005,1715006,1715007)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 2.1-5
- Rebuilt (iptables)

* Sun Feb 03 2019 - Michael Cronenworth <mike@cchtml.com> - 2.1-4
- Upstream patch for kernel 5.0 changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 - Michael Cronenworth <mike@cchtml.com> - 2.1-1
- Initial release

