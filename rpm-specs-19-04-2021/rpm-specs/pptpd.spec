# Available rpmbuild options:
#
# --without	bcrelay
#

# hardened build if not overriden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build:%{_hardened_build}}%{!?_hardened_build:0}
%global harden -Wl,-z,relro,-z,now
%endif

Summary:	PoPToP Point to Point Tunneling Server
Name:		pptpd
Version:	1.4.0
Release:	27%{?dist}
License:	GPLv2+ and LGPLv2+
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	perl-generators
BuildRequires:	ppp-devel, systemd
URL:		http://poptop.sourceforge.net/
Source0:	http://downloads.sf.net/poptop/pptpd-%{version}.tar.gz
Source1:	pptpd.service
Source2:	pptpd.sysconfig
Source3:	modules-load.conf
Source4:	20-pptpd.conf
# upstream ticket: https://sourceforge.net/p/poptop/patches/20/
Patch0:		pptpd-1.4.0-bcrelay-iflog-size-limit.patch
Requires:	ppp >= 2.4.2
Requires:	perl-interpreter

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
This implements a Virtual Private Networking Server (VPN) that is
compatible with Microsoft VPN clients. It allows windows users to
connect to an internal firewalled network using their dialup.

%if 0%{?fedora} < 23
%package sysvinit
Summary: PoPToP Point to Point Tunneling Server
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires(preun): /sbin/service

%description sysvinit
The SysV initscript for PoPToP Point to Point Tunneling Server.
%endif

%prep
%setup -q

%patch0 -p1 -b .bcrelay-iflog-size-limit

# Fix for distros with %%{_libdir} = /usr/lib64
perl -pi -e 's,/usr/lib/pptpd,%{_libdir}/pptpd,;' pptpctrl.c

%build
%configure \
	--without-libwrap \
	%{!?_without_bcrelay:--enable-bcrelay} \
	%{?_without_bcrelay:--disable-bcrelay}
(echo '#undef VERSION'; echo '#include <pppd/patchlevel.h>') >> plugins/patchlevel.h
make CFLAGS='-fno-builtin -fPIC -DSBINDIR=\"%{_sbindir}\" %{optflags} %{?harden}'

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man{5,8}

make %{?_smp_mflags} \
	DESTDIR=%{buildroot} \
	INSTALL="install -p" \
	LIBDIR=%{buildroot}%{_libdir}/pptpd \
	install
%if 0%{?fedora} < 23
install -Dpm 0755 pptpd.init %{buildroot}%{_sysconfdir}/rc.d/init.d/pptpd
%endif
install -Dpm 0644 samples/pptpd.conf %{buildroot}%{_sysconfdir}/pptpd.conf
install -Dpm 0644 samples/options.pptpd %{buildroot}%{_sysconfdir}/ppp/options.pptpd
install -pm 0755 tools/vpnuser %{buildroot}%{_bindir}/vpnuser
install -pm 0755 tools/vpnstats.pl %{buildroot}%{_bindir}/vpnstats.pl
install -pm 0755 tools/pptp-portslave %{buildroot}%{_sbindir}/pptp-portslave
install -pm 0644 pptpd.conf.5 %{buildroot}%{_mandir}/man5/pptpd.conf.5
install -pm 0644 pptpd.8 %{buildroot}%{_mandir}/man8/pptpd.8
install -pm 0644 pptpctrl.8 %{buildroot}%{_mandir}/man8/pptpctrl.8
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/pptpd.service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/pptpd
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_usr}/lib/modules-load.d/pptpd.conf
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_usr}/lib/sysctl.d/20-pptpd.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%if 0%{?fedora} < 23
%post sysvinit
/sbin/chkconfig --add pptpd >/dev/null 2>&1 ||:

%preun sysvinit
if [ "$1" = 0 ]; then
    %{_initrddir}/pptpd stop >/dev/null 2>&1 ||:
    /sbin/chkconfig --del pptpd >/dev/null 2>&1 ||:
fi

%postun sysvinit
[ "$1" -ge 1 ] && %{_initrddir}/pptpd condrestart >/dev/null 2>&1 ||:
%endif

%files
%doc AUTHORS COPYING README* TODO ChangeLog* samples
%{_sbindir}/pptpd
%{_sbindir}/pptpctrl
%{_sbindir}/pptp-portslave
%{!?_without_bcrelay:%{_sbindir}/bcrelay}
%dir %{_libdir}/pptpd
%{_libdir}/pptpd/pptpd-logwtmp.so
%{_bindir}/vpnuser
%{_bindir}/vpnstats.pl
%{_mandir}/man5/pptpd.conf.5*
%{_mandir}/man8/*.8*
%{_unitdir}/pptpd.service
%{_usr}/lib/modules-load.d/pptpd.conf
%{_usr}/lib/sysctl.d/20-pptpd.conf

%config(noreplace) %{_sysconfdir}/sysconfig/pptpd
%config(noreplace) %{_sysconfdir}/pptpd.conf
%config(noreplace) %{_sysconfdir}/ppp/options.pptpd

%if 0%{?fedora} < 23
%files sysvinit
%attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/pptpd
%endif

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-27
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-25
- Rebuilt for new ppp
  Resolves: rhbz#1913426
- Relaxed ppp deps

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-23
- Rebuilt for new ppp
  Resolves: rhbz#1807075

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-17
- Updated patch fixing bcrelay segfault
  Related: rhbz#1523645

* Wed Dec 13 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-16
- Fixed bcrelay segfault due to long ifname
  Resolves: rhbz#1523645

* Thu Nov 30 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-15
- Dropped tcp_wrappers support
  Resolves: rhbz#1518773

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.4.0-12
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov  4 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-10
- Autoloaded nf_conntrack_pptp kernel module and enabled IP forwarding
  Resolves: rhbz#1391538

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 Adam Jackson <ajax@redhat.com> 1.4.0-7
- Drop sysvinit subpackage from F23+

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-5
- Rebuilt for new ppp

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-3
- Rebuilt for new ppp

* Mon Nov 11 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-2
- Fixed license tag
  Related: rhbz#632853

* Fri Oct 25 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-1
- New version
- Dropped pppd-unbundle patch (upstreamed)

* Tue Oct 22 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3.4-4
- Various fixes according to Fedora review
  Related: rhbz#632853

* Fri Oct 18 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3.4-3
- Modified for Fedora
  Resolves: rhbz#632853

* Fri May 21 2010 Paul Howarth <paul@city-fan.org> - 1.3.4-2
- Define RPM macros in global scope
- Clarify license as GPL version 2 or later
- Add betabuild suffix to dist tag

* Fri Apr 20 2007 Paul Howarth <paul@city-fan.org> - 1.3.4-1.1
- Rebuild against ppp 2.4.4

* Fri Apr 20 2007 Paul Howarth <paul@city-fan.org> - 1.3.4-1
- Update to 1.3.4
- Use downloads.sf.net URL instead of dl.sf.net for source
- Use "install -p" to try to preserve upstream timestamps
- Remove bsdppp and slirp build options (package requires standard ppp)
- Remove ipalloc build option (not supported by upstream configure script)
- Use enable/disable rather than with/without for bcrelay configure option

* Wed Jan 10 2007 Paul Howarth <paul@city-fan.org> - 1.3.3-2
- Use file-based build dependency on /usr/include/tcpd.h instead of
  tcp_wrappers package, since some distributions have this file in
  tcp_wrappers-devel
- Set VERSION using pppd's patchlevel.h rather than using the constant "2.4.3"
- Buildrequire /usr/include/pppd/patchlevel.h (recent-ish pppd)
- Add dependency on the exact version of ppp that pptpd is built against
- Use tabs rather than spaces for indentation

* Tue Sep  5 2006 Paul Howarth <paul@city-fan.org> - 1.3.3-1
- Update to 1.3.3
- Add dist tag
- Add %%postun scriptlet dependency for /sbin/service
- Fix doc permissions

* Fri Mar 31 2006 Paul Howarth <paul@city-fan.org> - 1.3.1-1
- Update to 1.3.1

* Fri Mar 31 2006 Paul Howarth <paul@city-fan.org> - 1.3.0-1
- update to 1.3.0
- remove redundant macro definitions
- change Group: to one listed in rpm's GROUPS file
- use full URL for source
- simplify conditional build code
- use macros for destination directories
- honour %%{optflags}
- general spec file cleanup
- initscript updates:
	don't enable the service by default
	add reload and condrestart options
- condrestart service on package upgrade
- fix build on x86_64
- add buildreq tcp_wrappers

* Fri Feb 18 2005 James Cameron <james.cameron@hp.com>
- fix to use ppp 2.4.3 for plugin

* Thu Nov 11 2004 James Cameron <james.cameron@hp.com>
- adjust for building on Red Hat Enterprise Linux, per Charlie Brady
- remove vpnstats, superceded by vpnstats.pl

* Fri May 21 2004 James Cameron <james.cameron@hp.com>
- adjust for packaging naming and test

* Fri Apr 23 2004 James Cameron <james.cameron@hp.com>
- include vpnwho.pl

* Thu Apr 22 2004 James Cameron <james.cameron@hp.com>
- change description wording
- change URL for upstream
- release first candidate for 1.2.0

* Fri Jul 18 2003 R. de Vroede <richard@oip.tudelft.nl>
- Check the ChangeLog files.

