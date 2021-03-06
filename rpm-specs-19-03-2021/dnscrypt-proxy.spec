# Generated by go2rpm 1
%bcond_without check

# https://github.com/jedisct1/dnscrypt-proxy
%global goipath         github.com/jedisct1/dnscrypt-proxy
Version:                2.0.44
%global tag             2.0.44

%gometa

%global common_description %{expand:
A flexible DNS proxy, with support for modern encrypted DNS protocols such as
DNSCrypt v2 and DNS-over-HTTP/2.

Features:

 - DNS traffic encryption and authentication. Supports DNS-over-HTTPS (DoH)
 and DNSCrypt.
 - DNSSEC compatible
 - DNS query monitoring, with separate log files for regular and suspicious
 queries
 - Pattern-based local blocking of DNS names and IP addresses
 - Time-based filtering, with a flexible weekly schedule
 - Transparent redirection of specific domains to specific resolvers
 - DNS caching, to reduce latency and improve privacy
 - Local IPv6 blocking to reduce latency on IPv4-only networks
 - Load balancing: pick a set of resolvers, dnscrypt-proxy will automatically
 measure and keep track of their speed, and balance the traffic across the
 fastest available ones.
 - Cloaking: like a HOSTS file on steroids, that can return preconfigured
 addresses for specific names, or resolve and return the IP address of other
 names. This can be used for local development as well as to enforce safe
 search results on Google, Yahoo and Bing.
 - Automatic background updates of resolvers lists
 - Can force outgoing connections to use TCP; useful with tunnels such as Tor.}

Name:           dnscrypt-proxy
Release:        9%{?dist}
Summary:        Flexible DNS proxy, with support for encrypted DNS protocols

License:        ISC
URL:            %{gourl}
Source0:        %{gosource}

# Largely inspired by Arch packaging
# https://git.archlinux.org/svntogit/community.git/tree/trunk/configuration.diff?h=packages/dnscrypt-proxy
Patch0:         dnscrypt-proxy-2.0.44-custom_config.patch

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/coreos/go-systemd/activation)
BuildRequires:  golang(github.com/coreos/go-systemd/daemon)
BuildRequires:  golang(github.com/dchest/safefile)
BuildRequires:  golang(github.com/facebookgo/pidfile)
BuildRequires:  golang(github.com/hashicorp/go-immutable-radix)
BuildRequires:  golang(github.com/hashicorp/golang-lru)
BuildRequires:  golang(github.com/jedisct1/dlog)
BuildRequires:  golang(github.com/jedisct1/go-clocksmith)
BuildRequires:  golang(github.com/jedisct1/go-dnsstamps)
BuildRequires:  golang(github.com/jedisct1/go-minisign)
BuildRequires:  golang(github.com/jedisct1/xsecretbox)
BuildRequires:  golang(github.com/k-sone/critbitgo)
BuildRequires:  golang(github.com/kardianos/service)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/VividCortex/ewma)
BuildRequires:  golang(golang.org/x/crypto/curve25519)
BuildRequires:  golang(golang.org/x/crypto/ed25519)
BuildRequires:  golang(golang.org/x/crypto/nacl/box)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/proxy)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(gopkg.in/natefinch/lumberjack.v2)


# For SELinux workaround
BuildRequires: selinux-policy-devel
BuildRequires: make
Requires(post): policycoreutils
Requires(preun): policycoreutils
Requires(postun): policycoreutils

%description
%{common_description}

%prep
%goprep
%patch0 -p1

%build
for cmd in dnscrypt-proxy; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 dnscrypt-proxy/example-dnscrypt-proxy.toml %{buildroot}%{_sysconfdir}/%{name}/dnscrypt-proxy.toml
install -Dpm 0644 dnscrypt-proxy/example-blacklist.txt %{buildroot}%{_sysconfdir}/%{name}/blacklist.txt
install -Dpm 0644 dnscrypt-proxy/example-cloaking-rules.txt %{buildroot}%{_sysconfdir}/%{name}/cloaking-rules.txt
install -Dpm 0644 dnscrypt-proxy/example-forwarding-rules.txt %{buildroot}%{_sysconfdir}/%{name}/forwarding-rules.txt
install -Dpm 0644 dnscrypt-proxy/example-whitelist.txt %{buildroot}%{_sysconfdir}/%{name}/whitelist.txt

# Temporary SELinux workaround
# https://github.com/fedora-selinux/selinux-policy/issues/231
mkdir selinux
cd selinux

cat << EOF > my-ptproxy.te
module my-ptproxy 1.0;

require {
type var_t;
type init_t;
class dir { create setattr };
class lnk_file { create getattr read };
}

#============= init_t ==============
allow init_t var_t:dir { create setattr };
allow init_t var_t:lnk_file create;
EOF

make -f %{_datadir}/selinux/devel/Makefile
install -p -m 644 -D my-ptproxy.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/my-ptproxy.pp

%post
if [ "$1" -le "1" ] ; then # First install
dnscrypt-proxy -service install --config %{_sysconfdir}/dnscrypt-proxy/dnscrypt-proxy.toml
semodule -i %{_datadir}/selinux/packages/%{name}/my-ptproxy.pp 2>/dev/null || :
fi
if [ "$1" -ge "2" ] ; then
# Remove in F36
rm -rf %{_unitdir}/dnscrypt-proxy.service %{_unitdir}/dnscrypt-proxy.socket
dnscrypt-proxy -service uninstall
dnscrypt-proxy -service install --config %{_sysconfdir}/dnscrypt-proxy/dnscrypt-proxy.toml
fi

%preun
if [ "$1" -lt "1" ] ; then # Final removal
dnscrypt-proxy -service uninstall
semodule -r my-ptproxy 2>/dev/null || :
fi

%postun
if [ "$1" -ge "1" ] ; then # Upgrade
dnscrypt-proxy -service uninstall
dnscrypt-proxy -service install --config %{_sysconfdir}/dnscrypt-proxy/dnscrypt-proxy.toml
semodule -i %{_datadir}/selinux/packages/%{name}/my-ptproxy.pp 2>/dev/null || :
fi

%files
%license LICENSE
%doc README.md ChangeLog
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%ghost %{_sysconfdir}/systemd/system/dnscrypt-proxy.service
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.toml
%config(noreplace) %{_sysconfdir}/%{name}/blacklist.txt
%config(noreplace) %{_sysconfdir}/%{name}/cloaking-rules.txt
%config(noreplace) %{_sysconfdir}/%{name}/forwarding-rules.txt
%config(noreplace) %{_sysconfdir}/%{name}/whitelist.txt
%{_datadir}/selinux/packages/%{name}/my-ptproxy.pp

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 10:46:59 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.44-8
- Reorder scriptlets

* Mon Dec 28 09:59:16 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.44-7
- Install service with link toward correct config file

* Mon Dec 28 09:41:32 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.44-6
- Force removal of previous service file

* Wed Dec 16 11:26:23 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.44-5
- Fallback to recommended installation

* Mon Dec 14 07:03:11 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.44-4
- Keep config(noreplace) for %{_unitdir}/%{name}.socket

* Mon Dec 14 06:32:24 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.44-3
- Use an override to specify sockets

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 21:32:58 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.44-1
- Release 2.0.44 (#1796742)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 21:04:56 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.36-2
- Mark socket file as config (#1786867)

* Sun Dec 22 23:03:34 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.36-1
- Release 2.0.36 (#1784844)

* Tue Dec 03 23:16:24 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.35-1
- Release 2.0.35 (#1782348)

* Tue Dec 03 23:16:24 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.34-1
- Release 2.0.34 (#1778003)

* Wed Nov 20 19:59:18 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.33-1
- Release 2.0.33

* Sun Oct 13 23:39:06 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.28-1
- Release 2.0.28

* Thu Sep 12 15:41:34 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.27-2
- Fix custom config patch

* Thu Sep 12 00:14:59 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.27-1
- Release 2.0.27 (#1716575)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 00:37:56 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.23-1
- Release 2.0.23

* Mon Apr 01 16:13:44 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.22-1
- Release 2.0.22

* Thu Mar 14 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.20-1
- Release 2.0.20

* Wed Feb 20 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.19-3
- Add a policy for SELinux /var/cache creation
- Removed ProtectHome from the SystemD service to use with GNU Stow

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.19-1
- Release 2.0.19

* Thu Nov 15 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.18-1
- Release 2.0.18

* Wed Oct 03 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.17-1
- Update to 2.0.17

* Mon Aug 13 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.16-2
- Add a policy for SELinux DynamicUser failures

* Tue Jul 17 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2.0.16-1
- Update to 2.0.16

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Remi Collet <remi@fedoraproject.org> - 1.9.0-5
- rebuild for libsodium

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Nikos Roussos <comzeradd@fedoraproject.org> 1.9.0-1
- Update to 1.9.0

* Tue Jul 05 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.1-4
- Add systemd support

* Mon Jun 06 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.1-3
- Fix license

* Mon Jun 06 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.1-2
- Add hardened flag
- Fix obsolete m4 macro

* Fri Apr 22 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.1-1
- Update to 1.6.1

* Sat Oct 24 2015 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.0-1
- Initial package
