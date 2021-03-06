
%global _hardened_build 1

%if ( 0%{?suse_version} )
BuildRequires: distribution-release
%if ( ! 0%{?is_opensuse} )
BuildRequires: sles-release >= 12
Requires: sles-release >= 12
%else
BuildRequires: openSUSE-release
Requires: openSUSE-release
%endif
%endif

# Conditionally enable some FSALs, disable others.
#
# 1. rpmbuild accepts these options (gpfs as example):
#    --with gpfs
#    --without gpfs

%define on_off_switch() %%{?with_%1:ON}%%{!?with_%1:OFF}

# A few explanation about %%bcond_with and %%bcond_without
# /!\ be careful: this syntax can be quite messy
# %%bcond_with means you add a "--with" option, default = without this feature
# %%bcond_without adds a"--without" so the feature is enabled by default

%bcond_without nullfs
%global use_fsal_null %{on_off_switch nullfs}

%bcond_without mem
%global use_fsal_mem %{on_off_switch mem}

%bcond_without gpfs
%global use_fsal_gpfs %{on_off_switch gpfs}

%bcond_with xfs
%global use_fsal_xfs %{on_off_switch xfs}

%bcond_with lustre
%global use_fsal_lustre %{on_off_switch lustre}

%ifnarch i686 armv7hl
%bcond_without ceph
%else
%bcond_with ceph
%endif
%global use_fsal_ceph %{on_off_switch ceph}

%ifnarch i686 armv7hl
%bcond_without rgw
%else
%bcond_with rgw
%endif
%global use_fsal_rgw %{on_off_switch rgw}

%bcond_without gluster
%global use_fsal_gluster %{on_off_switch gluster}

%bcond_with panfs
%global use_fsal_panfs %{on_off_switch panfs}

%bcond_with rdma
%global use_rdma %{on_off_switch rdma}

%bcond_with 9P
%global use_9P %{on_off_switch 9P}

%bcond_with jemalloc

%bcond_with lttng
%global use_lttng %{on_off_switch lttng}

%bcond_without utils
%global use_utils %{on_off_switch utils}

%bcond_without gui_utils
%global use_gui_utils %{on_off_switch gui_utils}

%bcond_without system_ntirpc
%global use_system_ntirpc %{on_off_switch system_ntirpc}

%bcond_without man_page
%global use_man_page %{on_off_switch man_page}

%ifnarch i686 armv7hl
%bcond_without rados_recov
%else
%bcond_with rados_recov
%endif
%global use_rados_recov %{on_off_switch rados_recov}

%ifnarch i686 armv7hl
%bcond_without rados_urls
%else
%bcond_with rados_urls
%endif
%global use_rados_urls %{on_off_switch rados_urls}

%bcond_without rpcbind
%global use_rpcbind %{on_off_switch rpcbind}

%bcond_without mspac_support
%global use_mspac_support %{on_off_switch mspac_support}

%bcond_with sanitize_address
%global use_sanitize_address %{on_off_switch sanitize_address}

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%global _rundir %{_localstatedir}/run
%endif

%global dev_version %{lua: s = string.gsub('@GANESHA_EXTRA_VERSION@', '^%-', ''); s2 = string.gsub(s, '%-', '.'); print((s2 ~= nil and s2 ~= '') and s2 or "0.1") }
# %%global	dev rc5

Name:		nfs-ganesha
Version:	3.5
Release:	3%{?dev:%{dev}}%{?dist}
Summary:	NFS-Ganesha is a NFS Server running in user space
License:	LGPLv3+
Url:		https://github.com/nfs-ganesha/nfs-ganesha/wiki

Source0:	https://github.com/%{name}/%{name}/archive/V%{version}%{?dev:-%{dev}}/%{name}-%{version}%{?dev:-%{dev}}.tar.gz

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig
BuildRequires:	userspace-rcu-devel
BuildRequires:	krb5-devel
%if %{with rados_recov} || %{with rados_urls}
BuildRequires: librados-devel >= 0.61
%endif
%if ( 0%{?suse_version} >= 1330 )
BuildRequires:  libnsl-devel
%else
%if ( 0%{?fedora} >= 28 || 0%{?rhel} >= 8 )
BuildRequires:  libnsl2-devel
%endif
%endif
%if ( 0%{?suse_version} )
BuildRequires:	dbus-1-devel
Requires:	dbus-1
BuildRequires:	systemd-rpm-macros
%else
BuildRequires:	dbus-devel
Requires:	dbus
%endif
BuildRequires:	libcap-devel
BuildRequires:	libblkid-devel
BuildRequires:	libuuid-devel
%if ( 0%{?with_mspac_support} )
BuildRequires: libwbclient-devel
%endif
BuildRequires:	gcc-c++
%if ( %{with_system_ntirpc} )
BuildRequires:	libntirpc-devel = 3.4
%else
Requires: libntirpc = @NTIRPC_VERSION_EMBED@
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
# this should effectively be a no-op, as all Red Hat Enterprise Linux installs should have it
# with selinux.
Requires:	policycoreutils-python
%endif
%if ( 0%{?fedora} )
# this should effectively be a no-op, as all Fedora installs should have it
# with selinux.
Requires:	policycoreutils-python-utils
%endif
%if %{with sanitize_address}
BuildRequires: libasan
%endif
Requires:	nfs-utils
%if ( 0%{?with_rpcbind} )
%if ( 0%{?fedora} ) || ( 0%{?rhel} && 0%{?rhel} >= 6 ) || ( 0%{?suse_version} )
Requires:	rpcbind
%else
Requires:	portmap
%endif
%endif

%if ( 0%{?suse_version} )
BuildRequires:	nfsidmap-devel
%else
BuildRequires:	libnfsidmap-devel
%endif

%if %{with rdma}
BuildRequires:	libmooshika-devel >= 0.6-0
%endif
%if %{with jemalloc}
BuildRequires:	jemalloc-devel
%endif
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%if %{with man_page}
%if ( 0%{?rhel} && 0%{?rhel} < 8 )
BuildRequires: python-sphinx
%else
%if ( 0%{?suse_version} )
BuildRequires: python3-Sphinx
%else
BuildRequires: python3-sphinx
%endif
%endif
%endif
Requires(post): psmisc
Requires(pre): /usr/sbin/useradd
Requires(pre): /usr/sbin/groupadd

%if ( 0%{?fedora} >= 30 || 0%{?rhel} >= 8 )
Requires: nfs-ganesha-selinux = %{version}-%{release}
%endif

# Use CMake variables

%description
nfs-ganesha : NFS-GANESHA is a NFS Server running in user space.
It comes with various back-end modules (called FSALs) provided as
shared objects to support different file systems and name-spaces.

%if %{with 9P}
%package mount-9P
Summary: a 9p mount helper

%description mount-9P
This package contains the mount.9P script that clients can use
to simplify mounting to NFS-GANESHA. This is a 9p mount helper.
%endif

%package vfs
Summary: The NFS-GANESHA VFS FSAL
BuildRequires: libattr-devel
Obsoletes: %{name}-xfs <= %{version}
Requires: nfs-ganesha = %{version}-%{release}

%description vfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support VFS based filesystems

%package proxy
Summary: The NFS-GANESHA PROXY FSAL
BuildRequires: libattr-devel
Requires: nfs-ganesha = %{version}-%{release}

%description proxy
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PROXY based filesystems

%if %{with utils}
%package utils
Summary: The NFS-GANESHA util scripts
%if ( 0%{?rhel} && 0%{?rhel} < 8 )
Requires:	dbus-python, pygobject2, pyparsing
BuildRequires:	python-devel
%else
Requires:	python3-gobject, python3-pyparsing
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%if ( 0%{?suse_version} )
Requires:	dbus-1-python
%else
Requires:	python3-dbus
%endif
%endif

%if %{with gui_utils}
%if ( 0%{?suse_version} )
BuildRequires:	python-qt5-devel
%else
%if ( 0%{?fedora} >= 31 || 0%{?rhel} >= 8 )
BuildRequires:	python3-qt5-devel
%else
BuildRequires:	PyQt4-devel
%endif
%endif
%endif

%description utils
This package contains utility scripts for managing the NFS-GANESHA server
%endif

%if %{with lttng}
%package lttng
Summary: The NFS-GANESHA library for use with LTTng
BuildRequires:	lttng-ust-devel >= 2.3
BuildRequires:	lttng-tools-devel >= 2.3
Requires: nfs-ganesha = %{version}-%{release}

%description lttng
This package contains the libganesha_trace.so library. When preloaded
to the ganesha.nfsd server, it makes it possible to trace using LTTng.
%endif

%if %{with rados_recov}
%package rados-grace
Summary: The NFS-GANESHA command for managing the RADOS grace database
Requires: nfs-ganesha = %{version}-%{release}

%description rados-grace
This package contains the ganesha-rados-grace tool for interacting with the
database used by the rados_cluster recovery backend and the
libganesha_rados_grace shared library for using RADOS storage for
recovery state.
%endif

%if %{with rados_urls}
%package rados-urls
Summary: The NFS-GANESHA library for use with RADOS URLs
Group: Applications/System
Requires: nfs-ganesha = %{version}-%{release}

%description rados-urls
This package contains the libganesha_rados_urls library used for
handling RADOS URL configurations.
%endif

# Option packages start here. use "rpmbuild --with gpfs" (or equivalent)
# for activating this part of the spec file

# NULL
%if %{with nullfs}
%package nullfs
Summary: The NFS-GANESHA NULLFS Stackable FSAL
Requires: nfs-ganesha = %{version}-%{release}

%description nullfs
This package contains a Stackable FSAL shared object to
be used with NFS-Ganesha. This is mostly a template for future (more sophisticated) stackable FSALs
%endif

# MEM
%if %{with mem}
%package mem
Summary: The NFS-GANESHA Memory backed testing FSAL
Requires: nfs-ganesha = %{version}-%{release}

%description mem
This package contains a FSAL shared object to be used with NFS-Ganesha. This
is used for speed and latency testing.
%endif

# GPFS
%if %{with gpfs}
%package gpfs
Summary: The NFS-GANESHA GPFS FSAL
Requires: nfs-ganesha = %{version}-%{release}

%description gpfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support GPFS backend
%endif

# CEPH
%if %{with ceph}
%package ceph
Summary: The NFS-GANESHA CephFS FSAL
Requires:	nfs-ganesha = %{version}-%{release}
BuildRequires:	libcephfs2-devel >= 12.2.0
BuildRequires:	libacl-devel

%description ceph
This package contains a FSAL shared object to
be used with NFS-Ganesha to support CephFS
%endif

# RGW
%if %{with rgw}
%package rgw
Summary: The NFS-GANESHA Ceph RGW FSAL
Requires:	nfs-ganesha = %{version}-%{release}
BuildRequires:	librgw2-devel >= 12.2.0

%description rgw
This package contains a FSAL shared object to
be used with NFS-Ganesha to support Ceph RGW
%endif

# XFS
%if %{with xfs}
%package xfs
Summary: The NFS-GANESHA XFS FSAL
Requires:	nfs-ganesha = %{version}-%{release}
BuildRequires:	libattr-devel xfsprogs-devel

%description xfs
This package contains a shared object to be used with FSAL_VFS
to support XFS correctly
%endif

#LUSTRE
%if %{with lustre}
%package lustre
Summary: The NFS-GANESHA LUSTRE FSAL
BuildRequires: libattr-devel
BuildRequires: lustre-client
Requires: nfs-ganesha = %{version}-%{release}
Requires: lustre-client

%description lustre
This package contains a FSAL shared object to
be used with NFS-Ganesha to support LUSTRE based filesystems
%endif

# PANFS
%if %{with panfs}
%package panfs
Summary: The NFS-GANESHA PANFS FSAL
Requires:	nfs-ganesha = %{version}-%{release}

%description panfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PANFS
%endif

# GLUSTER
%if %{with gluster}
%package gluster
Summary: The NFS-GANESHA GLUSTER FSAL
Requires:	nfs-ganesha = %{version}-%{release}
BuildRequires:	glusterfs-api-devel >= 7.0
BuildRequires:	libattr-devel, libacl-devel

%description gluster
This package contains a FSAL shared object to
be used with NFS-Ganesha to support Gluster
%endif

# SELINUX
%if ( 0%{?fedora} >= 29 || 0%{?rhel} >= 8 )
%package selinux
Summary: The NFS-GANESHA SELINUX targeted policy
BuildArch:     noarch
Requires:      nfs-ganesha = %{version}-%{release}
BuildRequires:        selinux-policy-devel
%{?selinux_requires}

%description selinux
This package contains an selinux policy for running ganesha.nfsd

%post selinux
%selinux_modules_install %{_selinux_store_path}/packages/ganesha.pp.bz2

%pre selinux
%selinux_relabel_pre

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall ganesha
fi

%posttrans
%selinux_relabel_post
%endif


# NTIRPC (if built-in)
%if ! %{with system_ntirpc}
%package -n libntirpc
Summary:	New Transport Independent RPC Library
License:	BSD
Version:	@NTIRPC_VERSION_EMBED@
Url:		https://github.com/nfs-ganesha/ntirpc

# libtirpc has /etc/netconfig, most machines probably have it anyway
# for NFS client
Requires:	libtirpc

%description -n libntirpc
This package contains a new implementation of the original libtirpc,
transport-independent RPC (TI-RPC) library for NFS-Ganesha. It has
the following features not found in libtirpc:
 1. Bi-directional operation
 2. Full-duplex operation on the TCP (vc) transport
 3. Thread-safe operating modes
 3.1 new locking primitives and lock callouts (interface change)
 3.2 stateless send/recv on the TCP transport (interface change)
 4. Flexible server integration support
 5. Event channels (remove static arrays of xprt handles, new EPOLL/KEVENT
    integration)

%package -n libntirpc-devel
Summary:	Development headers for libntirpc
Requires:	libntirpc = @NTIRPC_VERSION_EMBED@
License:	BSD
Version:	@NTIRPC_VERSION_EMBED@
Url:		https://github.com/nfs-ganesha/ntirpc

%description -n libntirpc-devel
Development headers and auxiliary files for developing with %{name}.
%endif

%prep
%setup -q -n %{name}-%{version}%{?dev:-%{dev}}

%build
cd src && %cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo	\
	-DBUILD_CONFIG=rpmbuild				\
	-DUSE_FSAL_NULL=%{use_fsal_null}		\
	-DUSE_FSAL_MEM=%{use_fsal_mem}			\
	-DUSE_FSAL_XFS=%{use_fsal_xfs}			\
	-DUSE_FSAL_LUSTRE=%{use_fsal_lustre}		\
	-DUSE_FSAL_CEPH=%{use_fsal_ceph}		\
	-DUSE_FSAL_RGW=%{use_fsal_rgw}			\
	-DUSE_FSAL_GPFS=%{use_fsal_gpfs}		\
	-DUSE_FSAL_PANFS=%{use_fsal_panfs}		\
	-DUSE_FSAL_GLUSTER=%{use_fsal_gluster}		\
	-DUSE_SYSTEM_NTIRPC=%{use_system_ntirpc}	\
	-DUSE_9P_RDMA=%{use_rdma}			\
	-DUSE_LTTNG=%{use_lttng}			\
	-DUSE_ADMIN_TOOLS=%{use_utils}			\
	-DUSE_GUI_ADMIN_TOOLS=%{use_gui_utils}		\
	-DUSE_RADOS_RECOV=%{use_rados_recov}		\
	-DRADOS_URLS=%{use_rados_urls}			\
	-DUSE_FSAL_VFS=ON				\
	-DUSE_FSAL_PROXY=ON				\
	-DUSE_DBUS=ON					\
	-DUSE_9P=%{use_9P}				\
	-DDISTNAME_HAS_GIT_DATA=OFF			\
	-DUSE_MAN_PAGE=%{use_man_page}			\
	-DRPCBIND=%{use_rpcbind}			\
	-D_MSPAC_SUPPORT=%{use_mspac_support}		\
	-DSANITIZE_ADDRESS=%{use_sanitize_address}	\
%if %{with jemalloc}
	-DALLOCATOR=jemalloc
%endif

export VERBOSE=1
%cmake_build

%if ( 0%{?fedora} >= 30 || 0%{?rhel} >= 8 )
make -C selinux -f /usr/share/selinux/devel/Makefile ganesha.pp
pushd selinux && bzip2 -9 ganesha.pp && popd
%endif

%install
mkdir -p %{buildroot}%{_sysconfdir}/ganesha/
mkdir -p %{buildroot}%{_sysconfdir}/dbus-1/system.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}/ganesha
mkdir -p %{buildroot}%{_rundir}/ganesha
mkdir -p %{buildroot}%{_libexecdir}/ganesha
cd src
install -m 644 config_samples/logrotate_ganesha	%{buildroot}%{_sysconfdir}/logrotate.d/ganesha
install -m 644 scripts/ganeshactl/org.ganesha.nfsd.conf	%{buildroot}%{_sysconfdir}/dbus-1/system.d
install -m 755 scripts/nfs-ganesha-config.sh	%{buildroot}%{_libexecdir}/ganesha
%if %{with 9P}
install -m 755 tools/mount.9P	%{buildroot}%{_sbindir}/mount.9P
%endif
install -m 644 config_samples/vfs.conf %{buildroot}%{_sysconfdir}/ganesha
%if %{with rgw}
install -m 644 config_samples/rgw.conf %{buildroot}%{_sysconfdir}/ganesha
%endif

mkdir -p %{buildroot}%{_unitdir}
%if ( 0%{?fedora} ) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/nfs-ganesha-lock.service.d
%endif

install -m 644 scripts/systemd/nfs-ganesha.service.el7	%{buildroot}%{_unitdir}/nfs-ganesha.service
%if ( 0%{?fedora} ) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
install -m 644 scripts/systemd/nfs-ganesha-lock.service.el8    %{buildroot}%{_unitdir}/nfs-ganesha-lock.service
install -m 644 scripts/systemd/rpc-statd.conf.el8      %{buildroot}%{_sysconfdir}/systemd/system/nfs-ganesha-lock.service.d/rpc-statd.conf
%else
install -m 644 scripts/systemd/nfs-ganesha-lock.service.el7	%{buildroot}%{_unitdir}/nfs-ganesha-lock.service
%endif
install -m 644 scripts/systemd/nfs-ganesha-config.service	%{buildroot}%{_unitdir}/nfs-ganesha-config.service
install -m 644 scripts/systemd/sysconfig/nfs-ganesha	%{buildroot}%{_sysconfdir}/sysconfig/ganesha
mkdir -p %{buildroot}%{_localstatedir}/log/ganesha

%if %{with lustre}
install -m 644 config_samples/lustre.conf %{buildroot}%{_sysconfdir}/ganesha
%endif

%if %{with xfs}
install -m 644 config_samples/xfs.conf %{buildroot}%{_sysconfdir}/ganesha
%endif

%if %{with ceph}
install -m 644 config_samples/ceph.conf %{buildroot}%{_sysconfdir}/ganesha
%endif

%if %{with rgw}
install -m 644 config_samples/rgw.conf %{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/rgw_bucket.conf %{buildroot}%{_sysconfdir}/ganesha
%endif

%if %{with gluster}
install -m 644 config_samples/logrotate_fsal_gluster %{buildroot}%{_sysconfdir}/logrotate.d/ganesha-gfapi
%endif

%if %{with gpfs}
install -m 644 config_samples/gpfs.conf	%{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/gpfs.ganesha.nfsd.conf %{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/gpfs.ganesha.main.conf %{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/gpfs.ganesha.log.conf %{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/gpfs.ganesha.exports.conf	%{buildroot}%{_sysconfdir}/ganesha
%endif

%cmake_install

%if ( 0%{?fedora} >= 30 || 0%{?rhel} >= 8 )
install -d %{buildroot}%{_selinux_store_path}/packages
install -d -p %{buildroot}%{_selinux_store_path}/devel/include/contrib
install -p -m 644 selinux/ganesha.if %{buildroot}%{_selinux_store_path}/devel/include/contrib
install -m 0644 selinux/ganesha.pp.bz2 %{buildroot}%{_selinux_store_path}/packages
%endif

%if ( 0%{?rhel} && 0%{?rhel} < 8 )
rm -f %{buildroot}/%{python_sitelib}/gpfs*
rm -f %{buildroot}/%{python_sitelib}/__init__.*
%else
rm -f %{buildroot}/%{python3_sitelib}/gpfs*
rm -f %{buildroot}/%{python3_sitelib}/__init__.*
%endif

%post
%if ( 0%{?suse_version} )
%service_add_post nfs-ganesha.service nfs-ganesha-lock.service nfs-ganesha-config.service
%else
%if ( 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} > 6 ) )
semanage fcontext -a -t ganesha_var_log_t %{_localstatedir}/log/ganesha > /dev/null 2>&1 || :
semanage fcontext -a -t ganesha_var_log_t %{_localstatedir}/log/ganesha/ganesha.log > /dev/null 2>&1 || :
%if %{with gluster}
semanage fcontext -a -t ganesha_var_log_t %{_localstatedir}/log/ganesha/ganesha-gfapi.log > /dev/null 2>&1 || :
%endif
restorecon %{_localstatedir}/log/ganesha
%endif
%systemd_post nfs-ganesha.service
%systemd_post nfs-ganesha-lock.service
%systemd_post nfs-ganesha-config.service
%endif
killall -SIGHUP dbus-daemon >/dev/null 2>&1 || :

%pre
getent group ganesha > /dev/null || groupadd -r ganesha
getent passwd ganesha > /dev/null || useradd -r -g ganesha -d %{_rundir}/ganesha -s /sbin/nologin -c "NFS-Ganesha Daemon" ganesha
exit 0

%preun
%if ( 0%{?suse_version} )
%service_del_preun nfs-ganesha-lock.service
%else
%systemd_preun nfs-ganesha-lock.service
%endif

%postun
%if ( 0%{?suse_version} )
%service_del_postun nfs-ganesha-lock.service
%debug_package
%else
%systemd_postun_with_restart nfs-ganesha-lock.service
%endif

%files
%license src/LICENSE.txt
%{_bindir}/ganesha.nfsd
%{_libdir}/libganesha_nfsd.so*
%config %{_sysconfdir}/dbus-1/system.d/org.ganesha.nfsd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/ganesha
%config(noreplace) %{_sysconfdir}/logrotate.d/ganesha
%dir %{_sysconfdir}/ganesha/
%config(noreplace) %{_sysconfdir}/ganesha/ganesha.conf
%doc src/ChangeLog
%dir %{_rundir}/ganesha
%dir %{_libexecdir}/ganesha/
%{_libexecdir}/ganesha/nfs-ganesha-config.sh
%dir %attr(0755,ganesha,ganesha) %{_localstatedir}/log/ganesha

%{_unitdir}/nfs-ganesha.service
%{_unitdir}/nfs-ganesha-lock.service
%{_unitdir}/nfs-ganesha-config.service
%if ( 0%{?fedora} ) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
%{_sysconfdir}/systemd/system/nfs-ganesha-lock.service.d/rpc-statd.conf
%endif

%if %{with man_page}
%{_mandir}/*/ganesha-config.8.gz
%{_mandir}/*/ganesha-core-config.8.gz
%{_mandir}/*/ganesha-export-config.8.gz
%{_mandir}/*/ganesha-cache-config.8.gz
%{_mandir}/*/ganesha-log-config.8.gz
%endif

%if %{with rados_recov}
%files rados-grace
%{_bindir}/ganesha-rados-grace
%{_libdir}/libganesha_rados_recov.so*
%if %{with man_page}
%{_mandir}/*/ganesha-rados-grace.8.gz
%{_mandir}/*/ganesha-rados-cluster-design.8.gz
%endif
%endif

%if %{with rados_urls}
%files rados-urls
%{_libdir}/libganesha_rados_urls.so*
%endif

%if %{with 9P}
%files mount-9P
%{_sbindir}/mount.9P
%if %{with man_page}
%{_mandir}/*/ganesha-9p-config.8.gz
%endif
%endif

%files vfs
%{_libdir}/ganesha/libfsalvfs*
%config(noreplace) %{_sysconfdir}/ganesha/vfs.conf
%if %{with man_page}
%{_mandir}/*/ganesha-vfs-config.8.gz
%endif

%files proxy
%{_libdir}/ganesha/libfsalproxy*
%if %{with man_page}
%{_mandir}/*/ganesha-proxy-config.8.gz
%endif

# Optional packages
%if %{with lustre}
%files lustre
%{_libdir}/ganesha/libfsallustre*
%config(noreplace) %{_sysconfdir}/ganesha/lustre.conf
%if %{with man_page}
%{_mandir}/*/ganesha-lustre-config.8.gz
%endif
%endif

%if %{with nullfs}
%files nullfs
%{_libdir}/ganesha/libfsalnull*
%endif

%if %{with mem}
%files mem
%{_libdir}/ganesha/libfsalmem*
%endif

%if %{with gpfs}
%files gpfs
%{_libdir}/ganesha/libfsalgpfs*
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.conf
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.ganesha.nfsd.conf
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.ganesha.main.conf
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.ganesha.log.conf
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.ganesha.exports.conf
%{_libexecdir}/ganesha/gpfs-epoch
%if %{with man_page}
%{_mandir}/*/ganesha-gpfs-config.8.gz
%endif
%endif

%if %{with xfs}
%files xfs
%{_libdir}/ganesha/libfsalxfs*
%config(noreplace) %{_sysconfdir}/ganesha/xfs.conf
%if %{with man_page}
%{_mandir}/*/ganesha-xfs-config.8.gz
%endif
%endif

%if %{with ceph}
%files ceph
%{_libdir}/ganesha/libfsalceph*
%config(noreplace) %{_sysconfdir}/ganesha/ceph.conf
%if %{with man_page}
%{_mandir}/*/ganesha-ceph-config.8.gz
%endif
%endif

%if %{with rgw}
%files rgw
%{_libdir}/ganesha/libfsalrgw*
%config(noreplace) %{_sysconfdir}/ganesha/rgw.conf
%config(noreplace) %{_sysconfdir}/ganesha/rgw_bucket.conf
%if %{with man_page}
%{_mandir}/*/ganesha-rgw-config.8.gz
%endif
%endif

%if %{with gluster}
%files gluster
%config(noreplace) %{_sysconfdir}/logrotate.d/ganesha-gfapi
%{_libdir}/ganesha/libfsalgluster*
%if %{with man_page}
%{_mandir}/*/ganesha-gluster-config.8.gz
%endif
%endif

%if ( 0%{?fedora} >= 30 || 0%{?rhel} >= 8 )
%files selinux
%attr(0644,root,root) %{_selinux_store_path}/packages/ganesha.pp.bz2
%attr(0644,root,root) %{_selinux_store_path}/devel/include/contrib/ganesha.if
%endif

%if ! %{with system_ntirpc}
%files -n libntirpc
%{_libdir}/libntirpc.so.@NTIRPC_VERSION_EMBED@
%{_libdir}/libntirpc.so.1.6
%{_libdir}/libntirpc.so
%{!?_licensedir:%global license %%doc}
%license libntirpc/COPYING
%doc libntirpc/NEWS libntirpc/README
%files -n libntirpc-devel
%{_libdir}/pkgconfig/libntirpc.pc
%dir %{_includedir}/ntirpc
%{_includedir}/ntirpc/*
%endif

%if %{with panfs}
%files panfs
%{_libdir}/ganesha/libfsalpanfs*
%endif

%if %{with lttng}
%files lttng
%{_libdir}/ganesha/libganesha_trace*
%endif

%if %{with utils}
%files utils
%if ( 0%{?rhel} && 0%{?rhel} < 8 )
%{python_sitelib}/Ganesha/*
%{python_sitelib}/ganeshactl-*-info
%else
%{python3_sitelib}/Ganesha/*
%{python3_sitelib}/ganeshactl-*-info
%endif
%if %{with gui_utils}
%{_bindir}/ganesha-admin
%{_bindir}/manage_clients
%{_bindir}/manage_exports
%{_bindir}/manage_logger
%{_bindir}/ganeshactl
%if %{with 9P}
%{_bindir}/client_stats_9pOps
%{_bindir}/export_stats_9pOps
%else
%exclude %{_bindir}/client_stats_9pOps
%exclude %{_bindir}/export_stats_9pOps
%endif
%endif
%{_bindir}/fake_recall
%{_bindir}/get_clientids
%{_bindir}/grace_period
%{_bindir}/ganesha_stats
%{_bindir}/sm_notify.ganesha
%{_bindir}/ganesha_mgr
%{_bindir}/ganesha_conf
%{_mandir}/*/ganesha_conf.8.gz
%endif

%changelog
* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 9 2021 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.5-2
- NFS-Ganesha 3.5, rebuild with ceph-16

* Thu Jan 28 2021 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.5-1
- NFS-Ganesha 3.5 GA
- fix for compiling with Ceph-16 (pacific)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.4-1
- NFS-Ganesha 3.4 GA

* Thu Nov 5 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.3-8
- BuildRequires: make

* Tue Sep 8 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.3-7
- selinux

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.3-6
- use cmake_build and %cmake_install

* Mon Jul 20 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.3-5
- use %make_install

* Mon Jul 13 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.3-4
- rpc-statd.conf.el8

* Tue Jun 23 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- explicit BuildRequires: python3-setuptools

* Thu Jun 18 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.3-3
- rhbz#1848208

* Mon Jun 8 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.3-1
- NFS-Ganesha 3.3 GA

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.2-6
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.2-5
- NFS-Ganesha 3.2, NFSv4-compound-op-fails SEGV

* Thu Feb 20 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.2-4
- NFS-Ganesha 3.2, /var/log/ganesha, rhbz#1805493

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.2-2
- NFS-Ganesha 3.2, gcc-10

* Sun Dec 22 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.2-1
- NFS-Ganesha 3.2 GA
- 3.1 was not built

* Mon Nov 11 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.0-1
- NFS-Ganesha 3.0 GA

* Wed Nov 6 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.0-0.3rc5
- nfs-ganesha 3.0 RC5, rebuild w/ libntirpc-3.0 GA

* Tue Nov 5 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.0-0.2rc5
- nfs-ganesha 3.0 RC5, enable fsal_mem (again)

* Sun Nov 3 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 3.0-0.1rc5
- nfs-ganesha 3.0 RC5

* Wed Sep 25 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.2-4
- PyQt4 -> PyQt5

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.8.2-3
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.8.2-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.2-1
- nfs-ganesha 2.8.2 (f32/rawhide)

* Wed Aug 14 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.2-4
- nfs-ganesha 2.8.2, #1741023

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.2-2
- nfs-ganesha 2.8.2 GA

* Tue Jul 2 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.1-1
- nfs-ganesha 2.8.1 GA

* Mon Jul 1 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.0-4
- nfs-ganesha 2.8.0, 2.8.0.3

* Sun Jun 16 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.0-3
- nfs-ganesha 2.8.0, 2.8.0.2

* Tue Jun 11 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.0-2
- nfs-ganesha 2.8.0, 2.8.0.1

* Fri May 31 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.0-1
- nfs-ganesha 2.8.0 GA

* Fri May 31 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.0-0.2rc1
- nfs-ganesha 2.8.0 RC1, utils and gui_utils enabled

* Thu May 30 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.8.0-0.1rc1
- nfs-ganesha 2.8.0 RC1, utils and gui_utils disabled until the python
  byte_compile problems can be resolved

* Fri May 17 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.7.3-4
- Avoid unversioned Python requires

* Thu May 16 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.3-3
- nfs-ganesha 2.7.3, enable utils w/ python2 on f30 and up

* Fri May 10 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.3-2
- nfs-ganesha 2.7.3, selinux bz#1706462

* Fri Apr 5 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.3-1
- nfs-ganesha 2.7.3 GA

* Mon Mar 11 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.2-2
- nfs-ganesha 2.7.2 reenable ceph, rgw, rados from bad merge

* Wed Feb 27 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.2-1
- nfs-ganesha 2.7.2 GA

* Thu Feb 21 2019 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.1-1
- rebuild for f31/rawhide
-  add libnsl2-devel on rhel8
-  eliminate redundant cmake -DDSANITIZE_ADDRESS=OFF

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.1-4
- nfs-ganesha 2.7.1, fix selinux

* Fri Dec 7 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.1-3
- nfs-ganesha 2.7.1, rebuild w/ ceph-14

* Tue Oct 16 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.1-2
- nfs-ganesha 2.7.1, rebuild w/ libntirpc-1.7.1-1

* Fri Oct 12 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.1-1
- nfs-ganesha 2.7.1 GA

* Thu Sep 20 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.0-3
- nfs-ganesha 2.7.0, obsolete xfs, enable lttng

* Thu Sep 20 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.0-2
- nfs-ganesha 2.7.0, obsolete xfs, enable lttng

* Mon Sep 17 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.7.0-1
- nfs-ganesha 2.7.0 GA

* Wed Aug 22 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.3-1
- nfs-ganesha 2.6.3 GA

* Fri Aug 10 2018 Petr Lautrbach <plautrba@redhat.com> - 2.6.2-5
- require the correct package with /usr/sbin/semanage

* Tue Jul 17 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.2-4
- disable utils, python

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 3 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> 
- defattr

* Wed May 16 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.2-2
- nfs-ganesha 2.6.2 w/ ceph and rgw FSALs

* Thu May 10 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.2-1
- nfs-ganesha 2.6.2 GA

* Tue Mar 20 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.1-1
- nfs-ganesha 2.6.1 GA

* Fri Mar 2 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.0-2
- nfs-ganesha 2.6.0 GA, rebuild (relink) with libntirpc-1.6.1

* Tue Feb 20 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.0-1
- nfs-ganesha 2.6.0 GA

* Tue Feb 20 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.0-0.5rc5
- nfs-ganesha 2.6.0 RC5, rebuild with libntirpc-1.6.1

* Fri Feb 9 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.0-0.4rc5
- nfs-ganesha 2.6.0 RC5

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-0.3rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.0-0.1rc3
- nfs-ganesha 2.6.0 RC3

* Wed Jan 17 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.6.0-0.1rc2
- nfs-ganesha 2.6.0 RC2

* Thu Jan 11 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.4-2
- rebuild with libnfsidmap (libnfsidmap.so.1)

* Mon Nov 13 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.4-1
- nfs-ganesha 2.5.4 GA

* Fri Oct 20 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.3-3
- nfs-ganesha 2.5.3, quiet semanage

* Fri Oct 20 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.3-2
- nfs-ganesha 2.5.3, fix semanage in %%post

* Tue Oct 10 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.3-1
- nfs-ganesha 2.5.3 GA

* Wed Sep 27 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.2-6
- /var/log/ganesha -> ganesha_var_log_t
- see https://github.com/nfs-ganesha/nfs-ganesha/issues/212

* Fri Sep 22 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.2-5
- /var/log/ganesha -> ganesha_var_log_t
- see https://github.com/nfs-ganesha/nfs-ganesha/issues/212

* Fri Sep 22 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.2-4
- /var/log/ganesha owner ganesha.ganesha -> ganesha.root 
- see https://github.com/nfs-ganesha/nfs-ganesha/issues/212

* Fri Aug 25 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.2-3
- no rdma on arm(v7hl), FSAL_RGW, FSAL_CEPH; with ceph-12-1.4-5

* Thu Aug 24 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.2-2
- no rdma on arm(v7hl), thus no rgw in ceph, hence no FSAL_RGW

* Thu Aug 24 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.2-1
- nfs-ganesha 2.5.2 GA

* Fri Aug 18 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.1.1-2
- /var/run -> /run

* Wed Aug 2 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.1.1-1
- nfs-ganesha 2.5.1.1 GA
- enable ppc64, enable FSAL_GPFS

* Fri Jul 21 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.1-1
- nfs-ganesha 2.5.1 GA

* Wed Jul 19 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-4
- nfs-ganesha 2.5.0 rebuild with libntirpc-1.5.3

* Tue Jun 27 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-3
- nfs-ganesha 2.5.0 rebuild with ceph

* Sun Jun 25 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-2
- nfs-ganesha 2.5.0 rebuild with userspace-rcu-0.10.0 (liburcu-bp.so.6)

* Mon Jun 12 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-1
- nfs-ganesha 2.5.0 GA

* Wed Jun 7 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.10final
- nfs-ganesha 2.5 final

* Tue Jun 6 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.9rc9
- nfs-ganesha 2.5 rc9

* Tue May 30 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.8rc8
- nfs-ganesha 2.5 rc8, with libntirpc-1.5.2

* Mon May 22 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.7rc7
- nfs-ganesha 2.5 rc7

* Sun May 14 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.6rc6
- nfs-ganesha 2.5 rc6

* Thu May 11 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.5rc5
- nfs-ganesha 2.5 rc5

* Wed May 10 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.4rc4
- rebuild with libntirpc-1.5.1

* Mon May 8 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.3rc4
- nfs-ganesha 2.5 rc4

* Mon May 1 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.2rc3
- nfs-ganesha 2.5 rc3

* Mon Apr 24 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.5.0-0.1rc2
- nfs-ganesha 2.5 rc2

* Wed Apr 19 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.5-2
- nfs-ganesha 2.4.5 GA, w/ RGW again (cephfs-10.2.7)

* Wed Apr 5 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.5-1
- nfs-ganesha 2.4.5 GA

* Tue Mar 21 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.4-1
- nfs-ganesha 2.4.4 GA

* Thu Feb 9 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.3-2
- nfs-ganesha 2.4.3 GA, reenable FSAL_CEPH and FSAL_RGW

* Tue Feb 7 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.3-1
- nfs-ganesha 2.4.3 GA

* Mon Jan 23 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.2-1
- nfs-ganesha 2.4.2 GA

* Wed Jan 18 2017 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- python2 (vs. python3) cleanup

* Fri Dec 23 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.1-2
- nfs-ganesha 2.4.1 w/ FSAL_RGW

* Mon Oct 31 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.1-1
- nfs-ganesha 2.4.1 GA

* Fri Oct 28 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-2
- rebuild with libntirpc-1.4.3

* Thu Sep 22 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-1
- nfs-ganesha 2.4.0 GA

* Wed Sep 21 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.22rc6
- 2.4-rc6

* Fri Sep 16 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.21rc5
- 2.4-rc5

* Sun Sep 11 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.20rc4
- 2.4-rc4

* Wed Sep 7 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.19rc3
- 2.4-rc3

* Tue Sep 6 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.18rc2
- 2.4-rc2

* Mon Aug 29 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.17rc1
- 2.4-rc1

* Tue Aug 16 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.16dev29
- 2.4-dev-29, jemalloc off by default (conflicts with glusterfs-api)

* Mon Aug 15 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.15dev29
- 2.4-dev-29

* Mon Aug 1 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.14dev27
- 2.4-dev-27

* Mon Jul 25 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.13dev26
- 2.4-dev-26

* Wed Jul 20 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.12dev25
- 2.4-dev-25 (revised 32-bit)

* Tue Jul 19 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.11dev25
- 2.4-dev-25

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-0.10dev23
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 5 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.9dev23
- 2.4-dev-23

* Fri Jun 24 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.8dev21
- 2.4-dev-21 w/ FSAL_RGW

* Mon Jun 20 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.7dev21
- 2.4-dev-21

* Mon May 30 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.6dev19
- 2.4-dev-19

* Tue May 10 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.5dev17
- 2.4-dev-17

* Fri Apr 8 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.4dev14
- 2.4-dev-14

* Thu Mar 31 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.3dev12
- 2.4-dev-12

* Mon Feb 29 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.2dev10
- 2.4-dev-10

* Fri Feb 5 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.4.0-0.1dev7
- 2.4-dev-7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-2
- Requires: rpcbind or portmap

* Wed Oct 28 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-1
- 2.3.0 GA

* Tue Oct 27 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.15rc8
- 2.3.0 RC8, rebuild with libntirpc-1.3.1, again

* Mon Oct 26 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.14rc8
- 2.3.0 RC8, rebuild with libntirpc-1.3.1

* Sun Oct 25 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.13rc8
- 2.3.0 RC8

* Thu Oct 22 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.12rc7
- 2.3.0 RC7 (N.B. 2.3.0-0.11rc6 was really rc7)

* Mon Oct 19 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.11rc7
- 2.3.0 RC7

* Mon Oct 12 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.10rc6
- 2.3.0 RC6

* Thu Oct 8 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.9rc5
- 2.3.0 RC5 w/ CMakeLists.txt.patch and config-h.in.cmake.patch

* Wed Oct 7 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.8rc5
- 2.3.0 RC5 mount-9p w/o Requires: nfs-ganesha

* Tue Oct 6 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.7rc5
- 2.3.0 RC5 revised scripts/ganeshactl/CMakeLists.txt.patch

* Mon Oct 5 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.6rc5
- 2.3.0 RC5

* Mon Sep 28 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.5rc4
- 2.3.0 RC4

* Fri Sep 18 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.4rc3
- 2.3.0 RC3

* Fri Sep 11 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.3rc2
- 2.3.0 RC2

* Fri Sep 11 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.2rc1
- 2.3.0 RC1, revised .../SAL/nfs4_state_id.c.patch

* Wed Sep 9 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.3.0-0.1rc1
- 2.3.0 RC1

* Sat Aug 29 2015 Niels de Vos <ndevos@redhat.com> - 2.2.0-6
- Rebuilt for jemalloc SONAME bump

* Fri Jul 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-5
- BuildRequires: libntirprc on base

* Fri Jul 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-4
- link with unbundled, shared libntirpc

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Niels de Vos <ndevos@redhat.com>
- improve readability and allow "rpmbuild --with .." options again

* Fri May 15 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-2
- %%license, build with glusterfs-3.7.0 GA

* Tue Apr 21 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-1
- 2.2.0 GA

* Mon Apr 20 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.13rc-final
- 2.2.0-0.13rc-final

* Mon Apr 13 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.12rc8
- 2.2.0-0.12rc8

* Mon Apr 6 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.11rc7
- 2.2.0-0.11rc7

* Thu Apr 2 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.10rc6
- 2.2.0-0.10rc6, with unbundled libntirpc

* Mon Mar 30 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.9rc6
- 2.2.0-0.9rc6

* Sun Mar 22 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.8rc5
- 2.2.0-0.8rc5

* Tue Mar 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.7rc4
- ntirpc-1.2.1.tar.gz

* Tue Mar 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.6rc4
- updated ntirpc-1.2.0.tar.gz

* Sun Mar 15 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.5rc4
- 2.2.0-0.5rc4

* Mon Feb 23 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.4rc3
- 2.2.0-0.4rc3

* Mon Feb 16 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.3rc2
- subpackage Requires: nfs-ganesha = %%{version}-%%{release}

* Mon Feb 16 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.2rc2
- 2.2.0-0.2rc2

* Fri Feb 13 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.2.0-0.1rc1
- 2.2.0-0.1rc1
- nfs-ganesha.spec based on upstream

* Thu Feb 12 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-14
- Fedora 23/rawhide build fixes
- Ceph restored in EPEL

* Mon Jan 19 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-13
- Ceph retired from EPEL 7

* Thu Nov 6 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-12
- rebuild after libnfsidmap symbol version revert

* Wed Oct 29 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-11
- PyQt -> PyQt4 typo

* Mon Oct 27 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-10
- use upstream init.d script

* Thu Oct 2 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-9
- restore exclusion of gluster gfapi on rhel

* Thu Oct 2 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-8
- install /etc/dbus-1/system.d/org.ganesha.nfsd.conf
- build and install admin tools

* Mon Sep 29 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-7
- install /etc/sysconfig/nfs-ganesha file

* Fri Aug 29 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- Ceph FSAL typo, #1135437

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-5
- use upstream nfs-ganesha.service

* Fri Jul 11 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-4
- keep fsal .so files, implementation now uses them

* Tue Jul 1 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-3
- static libuid2grp

* Tue Jul 1 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-2
- add libuid2grp.so

* Mon Jun 30 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.1.0-1
- nfs-ganesha-2.1.0 GA

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 2 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-9
- Ceph FSAL enabled with ceph-0.80

* Wed May 21 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-8
- getdents()->getdents64(), struct dirent -> struct dirent64

* Sat May 10 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- and exclude libfsalceph

* Sat May 10 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- exclude libfsalgluster correctly

* Fri May 9 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-7
- Ceph FSAL, in a subpackage, (but requires ceph >= 0.78)

* Mon Mar 31 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- GlusterFS FSAL in a subpackage
- EPEL7 has jemalloc as of 2014-02-25

* Tue Jan 21 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- sussed out github archive so as to allow correct Source0

* Fri Jan 17 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-6
- EPEL7 and xfsprogs

* Fri Jan 17 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-5
- EPEL7

* Mon Jan 6 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-4
- with glusterfs-api(-devel) >= 3.4.2

* Sat Jan 4 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-3
- with glusterfs-api

* Thu Jan 2 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-2
- Build on RHEL6. Add sample init.d script

* Wed Dec 11 2013 Jim Lieb <lieb@sea-troll.net> - 2.0.0-1
- Update to V2.0.0 release

* Mon Nov 25 2013 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-0.2.rcfinal
- update to RC-final

* Fri Nov 22 2013 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 2.0.0-0.1.rc5
- Initial commit
