Name: eth-tools
Version: 11.0.0.0
Release: 163%{?dist}
Summary: Intel Ethernet Fabric Suite basic tools and libraries for fabric management

License: BSD
Url: https://github.com/intel/eth-fast-fabric
Source: %url/archive/%{version_no_tilde}/eth-fast-fabric-%{version_no_tilde}.tar.gz
ExclusiveArch: x86_64
# The Intel(R) Ethernet Fabric Suite product line is only available on x86_64 platforms at this time.

%description
This package contains the tools necessary to manage an Intel Ethernet fabric.

%package basic
Summary: Management level tools and scripts

Requires: rdma bc

Requires: expect%{?_isa}, tcl%{?_isa}, net-snmp-utils%{?_isa}
BuildRequires: make
BuildRequires: expat-devel
BuildRequires: gcc-c++
BuildRequires: openssl-devel
BuildRequires: ncurses-devel
BuildRequires: tcl-devel
BuildRequires: zlib-devel
BuildRequires: rdma-core-devel
BuildRequires: ibacm-devel
BuildRequires: net-snmp-devel

Epoch: 1

%description basic
Contains basic tools for fabric management necessary on all compute nodes.

%package fastfabric
Summary: Management level tools and scripts
Requires: eth-tools-basic%{?_isa} >= %{version}-%{release}
Requires: cronie

Epoch: 1

%description fastfabric
Contains tools for managing fabric on a management node.

%prep
%autosetup -n eth-fast-fabric-%{version_no_tilde}

%build
cd OpenIb_Host
OPA_FEATURE_SET= CLOCAL='%build_cflags' CCLOCAL='%build_cxxflags' LDLOCAL='%build_ldflags' ./ff_build.sh %{_builddir}

%install
BUILDDIR=%{_builddir} DESTDIR=%{buildroot} LIBDIR=%{_prefix}/lib DSAP_LIBDIR=%{_libdir} ./OpenIb_Host/ff_install.sh

%files basic
%{_sbindir}/ethcapture
%{_prefix}/lib/eth-tools/setup_self_ssh
%{_prefix}/lib/eth-tools/usemem
%{_prefix}/lib/eth-tools/ethipcalc
%{_prefix}/lib/eth-tools/stream
%{_mandir}/man1/ethcapture.1*
%{_datadir}/eth-tools/samples/mgt_config.xml-sample
%dir %{_sysconfdir}/eth-tools/
%config(noreplace) %{_sysconfdir}/eth-tools/mgt_config.xml

%files fastfabric
%{_sbindir}/*
%exclude %{_sbindir}/ethcapture
%{_prefix}/lib/eth-tools/*
%exclude %{_prefix}/lib/eth-tools/setup_self_ssh
%exclude %{_prefix}/lib/eth-tools/usemem
%exclude %{_prefix}/lib/eth-tools/ethipcalc
%exclude %{_prefix}/lib/eth-tools/stream
%{_datadir}/eth-tools/*
%exclude %{_datadir}/eth-tools/samples/mgt_config.xml-sample
%{_mandir}/man8/eth*.8*
%{_usrsrc}/eth/*
%{_sysconfdir}/eth-tools/ethmon.si.conf
# Replace ethmon.si.conf, as it's a template config file.
%config(noreplace) %{_sysconfdir}/eth-tools/ethfastfabric.conf
%config(noreplace) %{_sysconfdir}/eth-tools/ethmon.conf
%config(noreplace) %{_sysconfdir}/eth-tools/allhosts
%config(noreplace) %{_sysconfdir}/eth-tools/chassis
%config(noreplace) %{_sysconfdir}/eth-tools/hosts
%config(noreplace) %{_sysconfdir}/eth-tools/switches
%config(noreplace) /usr/lib/eth-tools/osid_wrapper


%changelog
* Fri Feb 05 2021 Jijun Wang <jijun.wang@intel.com> - 11.0.0.0-163
- Cleaned up for upstream

* Mon Feb 26 2018 Jijun Wang <jijun.wang@intel.com> - 10.8.0.0-1
- Added epoch for RHEL address-resolution, basic and fastfabric
- Added component information in description for all rpms

* Thu Apr 13 2017 Scott Breyer <scott.j.breyer@intel.com> - 10.5.0.0-1
- Updates for spec file cleanup

* Fri Oct 10 2014 Erik E. Kahn <erik.kahn@intel.com> - 1.0.0-ifs-1
- Initial version
