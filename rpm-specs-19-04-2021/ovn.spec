# Uncomment these for snapshot releases:
# commit0 is the git sha of the last commit
# date is the date YYYYMMDD of the snapshot
#%%global commit0 f11b99776c46831184ac30065c6cdf911061bb5a
#%%global date 20190223
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# If libcap-ng isn't available and there is no need for running OVS
# as regular user, specify the '--without libcapng'
%bcond_without libcapng

# option to build ovn-docker package
%bcond_with ovn_docker

# Enable PIE, bz#955181
%global _hardened_build 1

# We would see rpmlinit error - E: hardcoded-library-path in '% {_prefix}/lib'.
# But there is no solution to fix this. Using {_lib} macro will solve the
# rpmlink error, but will install the files in /usr/lib64/.
# OVN pacemaker ocf script file is copied in /usr/lib/ocf/resource.d/ovn/
# and we are not sure if pacemaker looks into this path to find the
# OVN resource agent script.
%global ovnlibdir %{_prefix}/lib

# Use python3 on fedora/rhel8 and python2 on rhel7/centos.
# The same spec file will be used to build OVN
# pacakges for CentOS - RDO and it doesn't have
# python3 yet.
%if 0%{?rhel} > 7 || 0%{?fedora}
# Use Python3
%global with_python3 1
%endif

# openvswitch in RDO has epoch set. So set epoch if built for rhel/centos.
# Otherwise, the ovn packages build by this spec file,  doesn't obsolete
# openvswitch-ovn* packages.
%if 0%{?rhel}
%global epoch_ovs 1
%endif

Name: ovn
Summary: Open Virtual Network support
URL: http://www.openvswitch.org/
Version: 21.03.0
Release: 2%{?commit0:.%{date}git%{shortcommit0}}%{?dist}
Obsoletes: openvswitch-ovn-common < %{?epoch_ovs:%{epoch_ovs}:}2.11.0-8
Provides: openvswitch-ovn-common = %{?epoch:%{epoch}:}%{version}-%{release}

# Nearly all of openvswitch is ASL 2.0.  The bugtool is LGPLv2+, and the
# lib/sflow*.[ch] files are SISSL.
License: ASL 2.0 and LGPLv2+ and SISSL

%if 0%{?commit0:1}
Source: https://github.com/openvswitch/ovs/archive/%{commit0}.tar.gz#/openvswitch-%{shortcommit0}.tar.gz
%else
Source: https://www.openvswitch.org/releases/ovn-%{version}.tar.gz
%endif

# The OVN commit used for 2.12.0-4 is 0a51bb04f8d6194b2c706558d434b09a89196e26.
# Update the above commit whenever the sources is updated.

# Set the ovsversion to 2.14.90 which is the latest master. We always compile
# OVN with the latest OVS master. Otherwise we will see compilation issues.
# OVS is used only for compilation. The actual OVS binaries - ovs-vswitchd, ovsdb-server etc
# comes from openvswitch package.
# The ovs commit used is 5601e86c4ec("Set release date for 2.14.0.").
# The ovs tarball is generated manually by running - "make dist" in the ovs repository.
%define ovsver 2.15.90
%define ovsdir openvswitch-%{ovsver}

Source10: https://openvswitch.org/releases/openvswitch-%{ovsver}.tar.gz

# ovn-patches

Patch01: 0001-ci-Fix-handling-of-python-packages.patch
Patch02: 0002-pinctrl-Don-t-send-gARPs-for-localports.patch
Patch03: 0003-Fix-connection-string-in-case-of-changes-in-the-ovnd.patch
Patch04: 0004-controller-introduce-stats-counters-for-ovn-controll.patch
Patch05: 0005-northd-reduce-indentation-in-build_lrouter_nat_defra.patch
Patch06: 0006-northd-introduce-build_lrouter_lb_flows-routine.patch
Patch07: 0007-northd-introduce-build_lrouter_in_unsnat_flow-routin.patch
Patch08: 0008-northd-introduce-build_lrouter_in_dnat_flow-routine.patch
Patch09: 0009-northd-introduce-build_lrouter_out_undnat_flow-routi.patch
Patch10: 0010-northd-introduce-build_lrouter_out_snat_flow-routine.patch
Patch11: 0011-northd-introduce-build_lrouter_ingress_flow-routine.patch
Patch12: 0012-northd-introduce-lrouter_check_nat_entry-routine.patch
Patch13: 0013-northd-introduce-per-lb-lb_skip_snat-option.patch
Patch14: 0014-binding-Fix-the-crashes-seen-when-port-binding-type-.patch
Patch15: 0015-northd-Restore-flows-that-recirculate-packets-in-the.patch
Patch16: 0016-controller-Fix-virtual-lport-I-P-handling.patch

# OpenvSwitch backports (400-) if required.
# Address crpto policy for fedora
%if 0%{?fedora}
Patch400: 0001-fedora-Use-PROFILE-SYSTEM-in-SSL_CTX_set_cipher_list.patch
%endif

BuildRequires: make
BuildRequires: gcc autoconf automake libtool
BuildRequires: systemd openssl openssl-devel

%if 0%{?with_python3}
BuildRequires: python3-devel python3-six python3-setuptools
%else
BuildRequires: python2-devel python2-six python2-setuptools
%endif

BuildRequires: /usr/bin/sphinx-build
BuildRequires: desktop-file-utils
BuildRequires: groff-base groff graphviz
BuildRequires: unbound-devel
# make check dependencies
BuildRequires: procps-ng

%if 0%{?with_python3}
BuildRequires: python3-pyOpenSSL
%else
BuildRequires: pyOpenSSL
%endif

%if %{with libcapng}
BuildRequires: libcap-ng-devel
%endif

Requires: openssl hostname iproute module-init-tools openvswitch libibverbs
%{?systemd_requires}

# to skip running checks, pass --without check
%bcond_without check

%description
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package central
Summary: Open Virtual Network support
License: ASL 2.0
Requires: ovn = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: firewalld-filesystem
Obsoletes: openvswitch-ovn-central < %{?epoch_ovs:%{epoch_ovs}:}2.11.0-8
Provides: openvswitch-ovn-central = %{?epoch:%{epoch}:}%{version}-%{release}

%description central
OVN DB servers and ovn-northd running on a central node.

%package host
Summary: Open Virtual Network support
License: ASL 2.0
Requires: ovn = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: firewalld-filesystem
Obsoletes: openvswitch-ovn-host < %{?epoch_ovs:%{epoch_ovs}:}2.11.0-8
Provides: openvswitch-ovn-host = %{?epoch:%{epoch}:}%{version}-%{release}

%description host
OVN controller running on each host.

%package vtep
Summary: Open Virtual Network support
License: ASL 2.0
Requires: ovn = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: openvswitch-ovn-vtep < %{?epoch_ovs:%{epoch_ovs}:}2.11.0-8
Provides: openvswitch-ovn-vtep = %{?epoch:%{epoch}:}%{version}-%{release}

%description vtep
OVN vtep controller

%if %{with ovn_docker}
%package docker
Summary: Open Virtual Network support
License: ASL 2.0
Requires: ovn = %{?epoch:%{epoch}:}%{version}-%{release} %{_py}-openvswitch
Obsoletes: openvswitch-ovn-docker < %{?epoch_ovs:%{epoch_ovs}:}2.11.0-8
Provides: openvswitch-ovn-docker = %{?epoch:%{epoch}:}%{version}-%{release}

%description docker
Docker network plugins for OVN.
%endif

%prep
%if 0%{?commit0:1}
%autosetup -v -n ovs-%{commit0} -p 1
%else
%autosetup -n ovn-%{version} -a 10 -p 1
%endif

%build
%if 0%{?commit0:1}
# fix the snapshot unreleased version to be the released one.
sed -i.old -e "s/^AC_INIT(openvswitch,.*,/AC_INIT(openvswitch, %{version},/" configure.ac
%endif
./boot.sh

# OVN source code is now separate.
# Build openvswitch first.
# Build openvswitch first
cd openvswitch-%{ovsver}
./boot.sh
%configure \
%if %{with libcapng}
        --enable-libcapng \
%else
        --disable-libcapng \
%endif
        --enable-ssl \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
%if 0%{?with_python3}
        PYTHON3=%{__python3} \
        PYTHON=%{__python3}
%else
        PYTHON=%{__python2}
%endif

make %{?_smp_mflags}
cd -

# Build OVN.
%configure \
        --with-ovs-source=$PWD/openvswitch-%{ovsver} \
%if %{with libcapng}
        --enable-libcapng \
%else
        --disable-libcapng \
%endif
        --enable-ssl \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
%if 0%{?with_python3}
        PYTHON3=%{__python3} \
        PYTHON=%{__python3}
%else
        PYTHON=%{__python2}
%endif

make %{?_smp_mflags}

%install
%make_install

install -p -D -m 0644 \
        rhel/usr_share_ovn_scripts_systemd_sysconfig.template \
        $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/ovn

for service in ovn-controller ovn-controller-vtep ovn-northd; do
        install -p -D -m 0644 \
                        rhel/usr_lib_systemd_system_${service}.service \
                        $RPM_BUILD_ROOT%{_unitdir}/${service}.service
done

install -d -m 0755 $RPM_BUILD_ROOT/%{_sharedstatedir}/ovn

install -d $RPM_BUILD_ROOT%{ovnlibdir}/firewalld/services/
install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-central-firewall-service.xml \
        $RPM_BUILD_ROOT%{ovnlibdir}/firewalld/services/ovn-central-firewall-service.xml
install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-host-firewall-service.xml \
        $RPM_BUILD_ROOT%{ovnlibdir}/firewalld/services/ovn-host-firewall-service.xml

install -d -m 0755 $RPM_BUILD_ROOT%{ovnlibdir}/ocf/resource.d/ovn
ln -s %{_datadir}/ovn/scripts/ovndb-servers.ocf \
      $RPM_BUILD_ROOT%{ovnlibdir}/ocf/resource.d/ovn/ovndb-servers

install -p -D -m 0644 rhel/etc_logrotate.d_ovn \
        $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/ovn

# remove OVS unpackages files
rm -f $RPM_BUILD_ROOT%{_bindir}/ovs*
rm -f $RPM_BUILD_ROOT%{_bindir}/vtep-ctl
rm -f $RPM_BUILD_ROOT%{_sbindir}/ovs*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ovs*
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/ovs*
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/vtep*
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/ovs*
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/ovs*
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/vtep*
rm -rf $RPM_BUILD_ROOT%{_datadir}/ovn/python
rm -f $RPM_BUILD_ROOT%{_datadir}/ovn/scripts/ovs*
rm -rf $RPM_BUILD_ROOT%{_datadir}/ovn/bugtool-plugins
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc
rm -f $RPM_BUILD_ROOT%{_includedir}/ovn/*
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/ovs-appctl-bashcomp.bash
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/ovs-vsctl-bashcomp.bash
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/openvswitch
rm -f $RPM_BUILD_ROOT%{_datadir}/ovn/scripts/ovn-bugtool*


%if %{without ovn_docker}
rm -f $RPM_BUILD_ROOT/%{_bindir}/ovn-docker-overlay-driver \
        $RPM_BUILD_ROOT/%{_bindir}/ovn-docker-underlay-driver
%endif

%check
%if %{with check}
    touch resolv.conf
    export OVS_RESOLV_CONF=$(pwd)/resolv.conf
    if make check TESTSUITEFLAGS='%{_smp_mflags} -k ovn' ||
       make check TESTSUITEFLAGS='--recheck -k ovn'; then :;
    else
        cat tests/testsuite.log
    fi
%endif

%pre central
if [ $1 -eq 1 ] ; then
    # Package install.
    /bin/systemctl status ovn-northd.service >/dev/null
    ovn_status=$?
    if [[ "$ovn_status" = "0" ]]; then
        # ovn-northd service is running which means old openvswitch-ovn-central
        # is possibly installed and it will be cleaned up. So start ovn-northd
        # service when posttrans central is called.
        touch %{_localstatedir}/lib/rpm-state/ovn-northd
    fi
fi

%pre host
if [ $1 -eq 1 ] ; then
    # Package install.
    /bin/systemctl status ovn-controller.service >/dev/null
    ovn_status=$?
    if [[ "$ovn_status" = "0" ]]; then
        # ovn-controller service is running which means old
        # openvswitch-ovn-host is possibly installed and it will be cleaned up. So
        # start ovn-controller service when posttrans host is called.
        touch %{_localstatedir}/lib/rpm-state/ovn-controller
    fi
fi

%pre vtep
if [ $1 -eq 1 ] ; then
    # Package install.
    /bin/systemctl status ovn-controller-vtep.service >/dev/null
    ovn_status=$?
    if [[ "$ovn_status" = "0" ]]; then
        # ovn-controller-vtep service is running which means old
        # openvswitch-ovn-vtep is possibly installed and it will be cleaned up. So
        # start ovn-controller-vtep service when posttrans host is called.
        touch %{_localstatedir}/lib/rpm-state/ovn-controller-vtep
    fi
fi

%preun central
%systemd_preun ovn-northd.service

%preun host
%systemd_preun ovn-controller.service

%preun vtep
%systemd_preun ovn-controller-vtep.service

%post
%if %{with libcapng}
if [ $1 -eq 1 ]; then
    sed -i 's:^#OVN_USER_ID=:OVN_USER_ID=:' %{_sysconfdir}/sysconfig/ovn
    sed -i 's:\(.*su\).*:\1 openvswitch openvswitch:' %{_sysconfdir}/logrotate.d/ovn
fi
%endif

%post central
%systemd_post ovn-northd.service

%post host
%systemd_post ovn-controller.service

%post vtep
%systemd_post ovn-controller-vtep.service

%posttrans central
if [ $1 -eq 1 ]; then
    # Package install, not upgrade
    if [ -e %{_localstatedir}/lib/rpm-state/ovn-northd ]; then
        unlink %{_localstatedir}/lib/rpm-state/ovn-northd
        /bin/systemctl start ovn-northd.service >/dev/null 2>&1 || :
    fi
fi

%posttrans host
if [ $1 -eq 1 ]; then
    # Package install, not upgrade
    if [ -e %{_localstatedir}/lib/rpm-state/ovn-controller ]; then
        unlink %{_localstatedir}/lib/rpm-state/ovn-controller
        /bin/systemctl start ovn-controller.service >/dev/null 2>&1 || :
    fi
fi

%posttrans vtep
if [ $1 -eq 1 ]; then
    # Package install, not upgrade
    if [ -e %{_localstatedir}/lib/rpm-state/ovn-controller-vtep ]; then
        unlink %{_localstatedir}/lib/rpm-state/ovn-controller-vtep
        /bin/systemctl start ovn-controller-vtep.service >/dev/null 2>&1 || :
    fi
fi

%files
%{_bindir}/ovn-nbctl
%{_bindir}/ovn-sbctl
%{_bindir}/ovn-trace
%{_bindir}/ovn-detrace
%{_bindir}/ovn-appctl
%{_bindir}/ovn-ic-nbctl
%{_bindir}/ovn-ic-sbctl
%dir %{_datadir}/ovn/
%dir %{_datadir}/ovn/scripts/
%{_datadir}/ovn/scripts/ovn-ctl
%{_datadir}/ovn/scripts/ovn-lib
%{_datadir}/ovn/scripts/ovndb-servers.ocf
%{_mandir}/man8/ovn-ctl.8*
%{_mandir}/man8/ovn-appctl.8*
%{_mandir}/man8/ovn-nbctl.8*
%{_mandir}/man8/ovn-trace.8*
%{_mandir}/man1/ovn-detrace.1*
%{_mandir}/man7/ovn-architecture.7*
%{_mandir}/man8/ovn-sbctl.8*
%{_mandir}/man5/ovn-nb.5*
%{_mandir}/man5/ovn-sb.5*
%{_mandir}/man8/ovn-ic-nbctl.8*
%{_mandir}/man8/ovn-ic-sbctl.8*
%{_mandir}/man5/ovn-ic-nb.5*
%{_mandir}/man5/ovn-ic-sb.5*
%dir %{ovnlibdir}/ocf/resource.d/ovn/
%{ovnlibdir}/ocf/resource.d/ovn/ovndb-servers
%config(noreplace) %{_sysconfdir}/logrotate.d/ovn
%config(noreplace) %{_sysconfdir}/sysconfig/ovn
%license LICENSE

%if %{with ovn_docker}
%files docker
%{_bindir}/ovn-docker-overlay-driver
%{_bindir}/ovn-docker-underlay-driver
%endif

%files central
%{_bindir}/ovn-northd
%{_bindir}/ovn-ic
%{_mandir}/man8/ovn-northd.8*
%{_mandir}/man8/ovn-ic.8*
%{_datadir}/ovn/ovn-nb.ovsschema
%{_datadir}/ovn/ovn-sb.ovsschema
%{_datadir}/ovn/ovn-ic-nb.ovsschema
%{_datadir}/ovn/ovn-ic-sb.ovsschema
%{_unitdir}/ovn-northd.service
%{ovnlibdir}/firewalld/services/ovn-central-firewall-service.xml

%files host
%{_bindir}/ovn-controller
%{_mandir}/man8/ovn-controller.8*
%{_unitdir}/ovn-controller.service
%{ovnlibdir}/firewalld/services/ovn-host-firewall-service.xml

%files vtep
%{_bindir}/ovn-controller-vtep
%{_mandir}/man8/ovn-controller-vtep.8*
%{_unitdir}/ovn-controller-vtep.service

%changelog
* Thu Apr 15 2021 Numan Siddique <numans@ovn.org> - 21.03.0-2
- Backport the required patches.

* Thu Apr 15 2021 Numan Siddique <numans@ovn.org> - 21.03.0-1
- Rebase to OVN v21.03.0.
- Use ovs sources from submodule commit used in ovn - ac85cdb38c1("ovsdb-idl: Mark arc sources as updated when destination is deleted.").

* Sat Mar 06 2021 Numan Siddique <numans@ovn.org> - 20.12.0-25
- Backport "northd: Fix the missing force_snat_for_lb flows when router_ip is configured." (#1931319)
- Backport "binding: Fix potential NULL dereference of lbinding."

* Mon Mar 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-24
- Backport "tests: Eliminate most "sleep" calls."
- Backport "tests: Add more checking to "3 HVs, 1 LS, 3 lports/HV" test."
- Backport "tests: Improve debuggability of tests."
- Backport "Implement SCTP-specific reject() action." (#1841009)
- Backport "Add sctp_abort logical flow action." (#1841009)
- Backport "controller: Split mac learning code to a separate file."  (#1672625)
- Backport "MAC learning: Add a new FDB table in southbound db." (#1672625)
- Backport "MAC learning: Add new actions - put_fdb, get_fdb and lookup_fdb." (#1672625)
- Backport "controller: MAC learning: Add OF rules for the FDB entries." (#1672625)
- Backport "northd: MAC learning: Add logical flows for fdb." (#1672625)
- Backport "Fix the failing test case - ovn -- ACL skip hints for stateless config." (#1672625)
- Backport "northd: Cleanup stale FDB entries." (#1672625)
- Backport "mac-learn: Fix build due to missing newline at EOF." (#1672625)
- Backport "Properly handle hairpin traffic for VIPs with shared backends." (#1931599)
- Backport "lflow: Avoid matching on conntrack original tuple if possible."
- Backport "northd: Avoid matching on ct.dnat flags for load balancers."

* Mon Mar 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-23
- Backport "ofctrl: Fix the assert seen when flood removing flows with conj actions." (#1929978)

* Mon Feb 22 2021 Numan Siddique <numans@ovn.org> - 20.12.0-22
- Backport "binding: Fix potential crash when binding_seqno_run is skipped." (#1930030)
- Backport "ofctrl: Do not link a desired flow twice."

* Mon Feb 22 2021 Numan Siddique <numans@ovn.org> - 20.12.0-21
- Backport "northd: Provide the Gateway router option 'lb_force_snat_ip' to take router port ips." (#1931319)

* Mon Feb 22 2021 Numan Siddique <numans@ovn.org> - 20.12.0-20
- Backport "ofctrl: Fix the assert seen when flood removing flows." (#1928012)

* Mon Feb 22 2021 Numan Siddique <numans@ovn.org> - 20.12.0-19
- Backport "controller: Fix toggling ct zone ids." (#1903210)

* Mon Feb 22 2021 Numan Siddique <numans@ovn.org> - 20.12.0-18
- Backport "ovn-nbctl: do not allow duplicated ECMP routes" (#1916842)

* Thu Feb 11 2021 Numan Siddique <numans@ovn.org> - 20.12.0-17
- Backport "northd: Skip matching on ct flags for stateless" (#1927230)

* Thu Feb 11 2021 Numan Siddique <numans@ovn.org> - 20.12.0-16
- Backport "Support configuring Load Balancer hairpin source IP." (#1908540)
- Backport "lflow: Use learn() action to generate LB hairpin reply flows." (#1917875)

* Thu Feb 11 2021 Numan Siddique <numans@ovn.org> - 20.12.0-15
- Backport "binding: Correctly set Port_Binding.up for container/virtual ports." (#1926165)
- Backport "binding: Set Port_Binding.up only if supported." (#1926165)
- Backport "northd: Allow backwards compatibility for Logical_Switch_Port.up." (#1926165)
- Backport "tests: Fix Port_Binding up test." (#1926165)

* Thu Feb 11 2021 Numan Siddique <numans@ovn.org> - 20.12.0-14
- Backport "ovn-nbctl: add --bfd option to lr-route-add" (#1918997)

* Mon Feb 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-13
- Backport "ofctrl: Rename 'nb_cfg' to 'req_cfg'." (#1839102)
- Backport "controller: Implement a generic barrier based on ofctrl cur_cfg sync." (#1839102)
- Backport "binding: Set Logical_Switch_Port.up when all OVS flows are installed." (#1839102)

* Mon Feb 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-12
- Backport "northd: add --event option to enable controller_event for empty_lb" (#1918422)

* Mon Feb 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-11
- Backport "ovn-nbctl: add bfd report to lr-route-list command" (#1915958)
- Backport "ovn-nbctl: add ecmp/ecmp-symmetric-reply to lr-route-list command"

* Mon Feb 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-10
- Backport "controller: fix pkt_marking with IP buffering" (#1857106)

* Mon Feb 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-9
- Backport "ovn-ctl: Add support for ovsdb-server --disable-file-column-diff." (#1917979)

* Mon Feb 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-8
- Backport "ovn-controller: Fix wrong conj_id match flows when caching is enabled." (#1919812)

* Mon Feb 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-7
- Backport "northd: Fix duplicate logical port detection." (#1918582)

* Mon Feb 01 2021 Numan Siddique <numans@ovn.org> - 20.12.0-6
- Backport "northd: Fix ACL fair log meters for Port_Group ACLs." (#1918004)
- Backport "binding: Fix container port removal from local bindings." (#1917533)
- Backport "binding: Always delete child port bindings first." (#1917533)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Numan Siddique <numans@ovn.org> - 20.12.0-5
- Backport "bfd: introduce IPv6 support" (#1915739)

* Wed Jan 13 2021 Numan Siddique <numans@ovn.org> - 20.12.0-4
- Backport "introduce BFD support in ovn-controller" (#1847570)
- Backport "ovn-northd: Move lswitch ARP/ND Responder to functions"
- Backport "ovn-northd: Move DHCP Options and Response to a function"
- Backport "ovn-northd: Move lswitch DNS lookup and response to a function"
- Backport "ovn-northd: Move DNS and DHCP defaults to a function"
- Backport "ovn-northd: Move ARP response for external ports to a function."
- Backport "ovn-northd: Move broadcast and multicast lookup in lswitch to a function"
- Backport "ovn-northd: Move destination handling into functions."
- Backport "ovn-northd: split build_lswitch_output_port_sec into iterators"
- Backport "ovn-northd: Move lrouter arp and nd datapath processing to a function"
- Backport "ovn-northd: Move ipv4 input to a function"
- Backport "ovn-northd: move NAT, Defrag and lb to a function"

* Mon Jan 11 2021 Numan Siddique <numans@ovn.org> - 20.12.0-3
- Backport "binding: Do not clear container lbinding->pb when parent is deleted." (#1914304)

* Mon Jan 11 2021 Numan Siddique <numans@ovn.org> - 20.12.0-2
- Backport "ovn-trace: fix trigger_event warning" (#1909650)

* Mon Jan 11 2021 Numan Siddique <numans@ovn.org> - 20.12.0-1
- Rebase to OVN v20.12.0.
- Re-backport patches for #1883957 and #1881826 as there are not in v20.12.0.
- Use ovs sources from master commit - 252e1e576443("dpdk: Update to use DPDK v20.11.").

* Tue Dec 15 2020 Numan Siddique <nusiddiq@redhat.com> - 20.09.0-4
- Backport "northd: Add ECMP support to router policies." (#1881826)
- Backport "Add missing documentation for router policy and ecmp sym reply stage." (#1881826)
- Backport "northd: add reject action for lb with no backends" (#1883957)
- Backport "northd: Fix iteration over vip backends." (#1904489)
- Backport "pinctrl: Honor always_learn_from_arp_request for self created MAC_Bindings." (#1903199)

* Tue Dec 01 2020 Numan Siddique <nusiddiq@redhat.com> - 20.09.0-3
- Backport "Allow explicit setting of the SNAT zone on a gateway router" (#1892311)
- Backport "Clear port binding flows when datapath CT zone changes."
- Backport "pinctrl: Fix segfault seen when creating mac_binding for local GARPs." (#1901880)
- Backport "Fix OVN update issue when ovn-controller is updated first from 20.06 to 20.09. (#1900484)
- Backport "controller: Allow pinctrl thread to handle packet-ins when version mismatch with northd." (#1899936)
- Backport memory leak fix patches.
- Backport "Provide the option to pin ovn-controller and ovn-northd to a specific version." (#1899936)
- Backport Load balancer hairpin improvement patches. (#1833373)
- Backport "northd: Fix lb_action when there are no active backends for lb health_check" (#1888445)
- Backport "Allow VLAN traffic when LS:vlan-passthru=true" (#1846018)
- Backport "northd: Don't poll ovsdb before the connection is fully established" (#1896671)
- Backport "pinctrl: Directly update MAC_Bindings created by self originated GARPs." (#1894478)
- Backport "ovn-northd: Limit self originated ARP/ND broadcast domain." (#1894478)
- Backport "dhcp: add iPXE support to OVN" (#1765506) 

* Tue Nov 03 2020 Numan Siddique <nusiddiq@redhat.com> - 20.09.0-2
- Backport "ovn-detrace: Only decode br-int OVS interfaces." (#1890803)
- Backport "ovn-detrace: Improve DB connection error messages." (#1890803)
- Backport "northd: Use 'enum ovn_stage' for the table value in the 'next' OVN action." (#1876990)
- Backport "ovn-trace: Don't assert for next(stage=ingress,..) (#1876990)
- Backport "actions: Add a new OVN action - reject {}." (#1876990)
- Backport "ovn-northd: Optimize logical flow generation for reject ACLs." (#1876990)
- Backport "ovn-trace: Handle IPv6 packets for tcp_reset action." (#1876990)
- Backport "controller: IPv6 Prefix-Delegation: introduce RENEW/REBIND msg support" (#1826686)
- Backport "ofctrl.c: Fix duplicated flow handling in I-P while" (#1871931)
- Backport "ofctrl.c: Avoid repeatedly linking an installed flow and" (#1871931)
- Backport "ofctrl.c: Only merge actions for conjunctive flows." (#1871931)
- Backport "ofctrl.c: Do not change flow ordering when merging" (#1871931)
- Backport "ofctrl.c: Simplify active desired flow selection." (#1871931)
- Backport "ofctrl.c: Always log the most recent flow changes." (#1871931)
- Backport "ofctrl.c: Add a predictable resolution for conflicting" (#1871931)
- Backport "northd: properly reconfigure ipam when subnet is changed" (#1865866)
- Backport "ovn-northd: Add localnet ports to Multicast_Groups created by IGMP_Group." (#1886314)

* Wed Sep 30 2020 Numan Siddique <nusiddiq@redhat.com> - 20.09.0-1
- Sync to upstream OVN v20.09.0.

* Tue Sep 22 2020 Numan Siddique <numans@ovn.org> - 20.06.2-4
- Backport many bug fix patches.

* Tue Sep 01 2020 Numan Siddique <numans@ovn.org> - 20.06.2-3
- Backport "ovn-controller: Fix incremental processing of Port_Binding deletes." (#1871961)

* Tue Sep 01 2020 Numan Siddique <numans@ovn.org> - 20.06.2-2
- Backport "Fix ovn-controller crash when a lport of type 'virtual' is deleted." (#1872681)

* Mon Aug 24 2020 Numan Siddique <numans@ovn.org> - 20.06.2-1
- Sync the OVN sources with the upstream v20.06.2 release and reorder
  the other patches.

* Wed Jul 29 2020 Numan Siddique <numans@ovn.org> - 20.06.1-6
- Backport "ovn-controller: Release lport if the ofport of the VIF is -1.". (#1861298)
- Backport "ovn-controller: Fix the missing flows when logical router port is added after its peer." (#1860053)
- Backport "ovn-controller: Clear flows not associated with db rows in physical flow change handler." (#1861042)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.06.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Numan Siddique <nusiddiq@redhat.com> - 20.06.1-4
- Backport "ovn-controller: Fix the missing ct zone entries for container ports." (#1858191)

* Thu Jul 16 2020 Numan Siddique <nusiddiq@redhat.com> - 20.06.1-3
- Backport "ovn-controller: Fix the missing flows with monitor-all set to True" (#1857537)

* Thu Jul 16 2020 Numan Siddique <nusiddiq@redhat.com> - 20.06.1-2
- Backport "Introduce icmp6_error action" (#1846300)
- Backport "Introduce icmp6.frag_mtu action" (#1846300)
- Backport "northd: introduce icmp6_error logical flows in router pipeline" (#1846300)

* Thu Jul 16 2020 Numan Siddique <nusiddiq@redhat.com> - 20.06.1-1
- Backport "Support packet metadata marking for logical router policies." (#1828933)
- Backport "ovn-nbctl: Enhance lr-policy-add to set the options."(#1828933)
- Backport "pinctrl: Support DHCPRELEASE and DHCPINFORM in native OVN dhcp responder." (#1801258)

* Fri Jul 10 2020 Numan Siddique <nusiddiq@redhat.com> - 20.06.1-0
- Sync the ovn tar ball to the ovn v20.06.1 release.
- Sync the ovs (openvswitch-2.13.90) tar ball to the commit fa31efd211143f1adb06a62faad803a5aca1e400

* Mon Jun 22 2020 Numan Siddique <nusiddiq@redhat.com> - 20.03.0-4
- Backport "northd: By pass IPv6 Router Adv and Router Solicitation packets  from ACL stages."

* Tue Apr 28 2020 Numan Siddique <nusiddiq@redhat.com> - 20.03.0-3
- Sync the ovn tar ball to the ovn master with the commit - b4b68177eb2fcbc9d25e38eb58d8704ba7dd4177
- Fix required to address the conntrack entry leaks.

* Mon Mar 30 2020 Numan Siddique <nusiddiq@redhat.com> - 20.03.0-2
- Removed the Revert "ovsdb-idl: Avoid sending redundant conditional monitoring updates"
  as openvswitch compilation is failing in the build.

* Mon Mar 30 2020 Numan Siddique <nusiddiq@redhat.com> - 20.03.0-1
- Sync the ovn tar ball to the ovn master with the commit - c4700eed17da8615107553aec82852a37d401821
- SCTP load balancer feature is requried for ovn-kubernetes
- Revert "ovsdb-idl: Avoid sending redundant conditional monitoring updates"

* Tue Mar 03 2020 Numan Siddique <nusiddiq@redhat.com> - 20.03.0-0
- Release upstream OVN v20.03.0

* Fri Feb 21 2020 Numan Siddique <nusiddiq@redhat.com> - 2.12.1-1
- Version bump required for correcting the changelog

* Fri Feb 21 2020 Numan Siddique <nusiddiq@redhat.com> - 2.12.1-0
- Sync the ovn tar ball to the ovn master with the commit - eb9a406cefeb6ac0b0176039c586f982642a41f8
- Sync the ovs tar ball to the ovs master with the commit - ac23d20fc90da3b1c9b2117d1e22102e99fba006

* Tue Feb 11 2020 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-12
- Sync the ovn tar ball to the ovn master with the commit - b02d366e6268462d637b7a5047ff65b2536408af.
- Fix the tcp_reset issue. Fix required for ovn kuberenetes.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-9
- Use the ovs commit 91157afbd83aefb0c9f558d2841fece388b3b0cb as ovn
  build for centos 7 was still failing.

* Mon Nov 25 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-8
- Reverse the previous commit.
- Fix the compilation error seen in Centos7 by using
  ovs commit - 36e5d97f9b09262ccc584ccb45fb06482b0cfc46.
  The commit 1ca0323e7c29d("Require Python 3 and remove support for Python 2.") removed
  Python 2 support because of which compilation is failing in Centos 7.

* Mon Nov 25 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-7
- Build with python 3 support as ovs requires python 3.

* Mon Nov 25 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-6
- Fix the changelog date errors.

* Wed Nov 06 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-5
- Fix the logrotate issue - (#1769200).

* Tue Oct 29 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-4
- Sync the ovn tar ball to the latest master with the commit - 0a51bb04f8d6194b2c706558d434b09a89196e26.

* Wed Oct 09 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-3
- Sync the ovn tar ball to the latest master with the commit - 1a3e6dfb5e2fd5bbb625f637792f91a02767ff3b.

* Tue Oct 08 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-2
- Use the official openvswitch 2.12.0 tar file.

* Thu Sep 26 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-1
- Apply fedora only patch only on fedora builds.

* Sat Sep 14 2019 Numan Siddique <nusiddiq@redhat.com> - 2.12.0-0
- 2.12.0 from new OVN repo

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 3 2019 Numan Siddique <nusiddiq@redhat.com> - 2.11.1-1
- Fix the version information in configure.ac

* Wed May 29 2019 Numan Siddique <nusiddiq@redhat.com> - 2.11.1-0
- Use the latest openvswitch sources with the commit - 4992e00012e7

* Tue Apr 9 2019 Numan Siddique <nusiddiq@redhat.com> - 2.11.0-9
- Fix epoch issue for RDO.

* Tue Apr 9 2019 Numan Siddique <nusiddiq@redhat.com> - 2.11.0-8
- Fix Obsoletes version

* Mon Apr 8 2019 Numan Siddique <nusiddiq@redhat.com> - 2.11.0-7
- Fix build error on centos builds.

* Mon Apr 8 2019 Numan Siddique <nusiddiq@redhat.com> - 2.11.0-6
- Fix spec file - %if error for centos builds.

* Mon Apr 8 2019 Numan Siddique <nusiddiq@redhat.com> - 2.11.0-5
- Support building OVN packages for Centos7/RDO.

* Fri Apr 5 2019 Numan Siddique <nusiddiq@redhat.com> - 2.11.0-4
- Provide new OVN packages splitting from openvswitch for fedora
