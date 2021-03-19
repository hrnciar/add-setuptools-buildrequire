
%global pkgname   dirsrv
%global srcname   389-ds-base

# Exclude i686 bit arches
ExcludeArch: i686 

# for a pre-release, define the prerel field e.g. .a1 .rc2 - comment out for official release
# also remove the space between % and global - this space is needed because
# fedpkg verrel stupidly ignores comment lines
#% global prerel .rc3
# also need the relprefix field for a pre-release e.g. .0 - also comment out for official release
#% global relprefix 0.

# If perl-Socket-2.000 or newer is available, set 0 to use_Socket6.
%global use_Socket6 0

%global use_asan 0
%global use_rust 1
%global bundle_jemalloc 1
%if %{use_asan}
%global bundle_jemalloc 0
%endif

%if %{bundle_jemalloc}
%global jemalloc_name jemalloc
%global jemalloc_ver 5.2.1
%global __provides_exclude ^libjemalloc\\.so.*$
%endif

# Use Clang instead of GCC
%global use_clang 0

# Build cockpit plugin
%global use_cockpit 1

# fedora 15 and later uses tmpfiles.d
# otherwise, comment this out
%{!?with_tmpfiles_d: %global with_tmpfiles_d %{_sysconfdir}/tmpfiles.d}

# systemd support
%global groupname %{pkgname}.target

# set PIE flag
%global _hardened_build 1

Summary:          389 Directory Server (base)
Name:             389-ds-base
Version:          2.0.3
Release:          %{?relprefix}3%{?prerel}%{?dist}.1
License:          GPLv3+
URL:              https://www.port389.org
Conflicts:        selinux-policy-base < 3.9.8
Conflicts:        freeipa-server < 4.0.3
Obsoletes:        %{name} <= 1.4.0.9
Obsoletes:        %{name}-legacy-tools < 1.4.4.6
Obsoletes:        %{name}-legacy-tools-debuginfo < 1.4.4.6
Provides:         ldif2ldbm >= 0

BuildRequires:    nspr-devel
BuildRequires:    nss-devel >= 3.34
BuildRequires:    openldap-devel
BuildRequires:    libdb-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    icu
BuildRequires:    libicu-devel
BuildRequires:    pcre-devel
BuildRequires:    cracklib-devel
%if %{use_clang}
BuildRequires:    libatomic
BuildRequires:    clang
%else
BuildRequires:    gcc
BuildRequires:    gcc-c++
%endif
# The following are needed to build the snmp ldap-agent
BuildRequires:    net-snmp-devel
BuildRequires:    lm_sensors-devel
BuildRequires:    bzip2-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
# the following is for the pam passthru auth plug-in
BuildRequires:    pam-devel
BuildRequires:    systemd-units
BuildRequires:    systemd-devel
%if %{use_asan}
BuildRequires:    libasan
%endif
# If rust is enabled
%if %{use_rust}
BuildRequires: cargo
BuildRequires: rust
%endif
BuildRequires:    pkgconfig
BuildRequires:    pkgconfig(systemd)
BuildRequires:    pkgconfig(krb5)

# Needed to support regeneration of the autotool artifacts.
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
# For our documentation
BuildRequires:    doxygen
# For tests!
BuildRequires:    libcmocka-devel
BuildRequires:    libevent-devel
# For lib389 and related components
BuildRequires:    python%{python3_pkgversion}-devel
BuildRequires:    python%{python3_pkgversion}-setuptools
BuildRequires:    python%{python3_pkgversion}-ldap
BuildRequires:    python%{python3_pkgversion}-six
BuildRequires:    python%{python3_pkgversion}-pyasn1
BuildRequires:    python%{python3_pkgversion}-pyasn1-modules
BuildRequires:    python%{python3_pkgversion}-dateutil
BuildRequires:    python%{python3_pkgversion}-argcomplete
BuildRequires:    python%{python3_pkgversion}-argparse-manpage
BuildRequires:    python%{python3_pkgversion}-libselinux
BuildRequires:    python%{python3_pkgversion}-policycoreutils

# For cockpit
%if %{use_cockpit}
BuildRequires:    rsync
%endif

Requires:         %{name}-libs = %{version}-%{release}
Requires:         python%{python3_pkgversion}-lib389 = %{version}-%{release}

# this is needed for using semanage from our setup scripts
Requires:         policycoreutils-python-utils
Requires:         /usr/sbin/semanage
Requires:         libsemanage-python%{python3_pkgversion}

Requires:         selinux-policy >= 3.14.1-29

# the following are needed for some of our scripts
Requires:         openldap-clients
Requires:         /usr/bin/c_rehash
Requires:         python%{python3_pkgversion}-ldap

# this is needed to setup SSL if you are not using the
# administration server package
Requires:         nss-tools
Requires:         nss >= 3.34

# these are not found by the auto-dependency method
# they are required to support the mandatory LDAP SASL mechs
Requires:         cyrus-sasl-gssapi
Requires:         cyrus-sasl-md5
Requires:         cyrus-sasl-plain

# this is needed for verify-db.pl
Requires:         libdb-utils

# Needed for password dictionary checks
Requires:         cracklib-dicts

# Needed by logconv.pl
Requires:         perl-DB_File
Requires:         perl-Archive-Tar

# Picks up our systemd deps.
%{?systemd_requires}

Obsoletes:        %{name} <= 1.3.5.4

Source0:          https://releases.pagure.org/389-ds-base/%{name}-%{version}%{?prerel}.tar.bz2
# 389-ds-git.sh should be used to generate the source tarball from git
Source1:          %{name}-git.sh
Source2:          %{name}-devel.README
%if %{bundle_jemalloc}
Source3:          https://github.com/jemalloc/%{jemalloc_name}/releases/download/%{jemalloc_ver}/%{jemalloc_name}-%{jemalloc_ver}.tar.bz2
%endif

%description
389 Directory Server is an LDAPv3 compliant server.  The base package includes
the LDAP server and command line utilities for server administration.
%if %{use_asan}
WARNING! This build is linked to Address Sanitisation libraries. This probably
isn't what you want. Please contact support immediately.
Please see http://seclists.org/oss-sec/2016/q1/363 for more information.
%endif

%package          libs
Summary:          Core libraries for 389 Directory Server
BuildRequires:    nspr-devel
BuildRequires:    nss-devel >= 3.34
BuildRequires:    openldap-devel
BuildRequires:    libdb-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    libicu-devel
BuildRequires:    pcre-devel
BuildRequires:    libtalloc-devel
BuildRequires:    libevent-devel
BuildRequires:    libtevent-devel
Requires:         krb5-libs
Requires:         libevent
BuildRequires:    systemd-devel
BuildRequires:    make
Provides:         svrcore = 4.1.4
Conflicts:        svrcore
Obsoletes:        svrcore <= 4.1.3

%description      libs
Core libraries for the 389 Directory Server base package.  These libraries
are used by the main package and the -devel package.  This allows the -devel
package to be installed with just the -libs package and without the main package.

%package          devel
Summary:          Development libraries for 389 Directory Server
Requires:         %{name}-libs = %{version}-%{release}
Requires:         pkgconfig
Requires:         nspr-devel
Requires:         nss-devel >= 3.34
Requires:         openldap-devel
Requires:         libtalloc
Requires:         libevent
Requires:         libtevent
Requires:         systemd-libs
Provides:         svrcore-devel = 4.1.4
Conflicts:        svrcore-devel
Obsoletes:        svrcore-devel <= 4.1.3

%description      devel
Development Libraries and headers for the 389 Directory Server base package.

%package          snmp
Summary:          SNMP Agent for 389 Directory Server
Requires:         %{name} = %{version}-%{release}

Obsoletes:        %{name} <= 1.4.0.0

%description      snmp
SNMP Agent for the 389 Directory Server base package.

%package -n python%{python3_pkgversion}-lib389
Summary:  A library for accessing, testing, and configuring the 389 Directory Server
BuildArch:        noarch
Requires: openssl
Requires: iproute
Recommends: bash-completion
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-distro
Requires: python%{python3_pkgversion}-ldap
Requires: python%{python3_pkgversion}-six
Requires: python%{python3_pkgversion}-pyasn1
Requires: python%{python3_pkgversion}-pyasn1-modules
Requires: python%{python3_pkgversion}-dateutil
Requires: python%{python3_pkgversion}-argcomplete
Requires: python%{python3_pkgversion}-libselinux
Requires: python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-lib389}

%description -n python%{python3_pkgversion}-lib389
This module contains tools and libraries for accessing, testing,
 and configuring the 389 Directory Server.

%if %{use_cockpit}
%package -n cockpit-389-ds
Summary:          Cockpit UI Plugin for configuring and administering the 389 Directory Server
BuildArch:        noarch
Requires:         cockpit
Requires:         389-ds-base
Requires:         python%{python3_pkgversion}
Requires:         python%{python3_pkgversion}-lib389

%description -n cockpit-389-ds
A cockpit UI Plugin for configuring and administering the 389 Directory Server
%endif

%prep
%autosetup -p1 -v -n %{name}-%{version}%{?prerel}
%setup -q -n %{name}-%{version}%{?prerel}

%if %{bundle_jemalloc}
%setup -q -n %{name}-%{version}%{?prerel} -T -D -b 3
%endif

cp %{SOURCE2} README.devel

%build

OPENLDAP_FLAG="--with-openldap"
%{?with_tmpfiles_d: TMPFILES_FLAG="--with-tmpfiles-d=%{with_tmpfiles_d}"}
# hack hack hack https://bugzilla.redhat.com/show_bug.cgi?id=833529
NSSARGS="--with-nss-lib=%{_libdir} --with-nss-inc=%{_includedir}/nss3"

%if %{use_asan}
ASAN_FLAGS="--enable-asan --enable-debug"
%endif

%if %{use_rust}
RUST_FLAGS="--enable-rust --enable-rust-offline"
%endif

%if !%{use_cockpit}
COCKPIT_FLAGS="--disable-cockpit"
%endif 

%if %{use_clang}
export CC=clang
export CXX=clang++
CLANG_FLAGS="--enable-clang"
%endif

%if %{bundle_jemalloc}
# Override page size, bz #1545539
# 4K
%ifarch %ix86 %arm x86_64 s390x
%define lg_page --with-lg-page=12
%endif

# 64K
%ifarch ppc64 ppc64le aarch64
%define lg_page --with-lg-page=16
%endif

# Override huge page size on aarch64
# 2M instead of 512M
%ifarch aarch64
%define lg_hugepage --with-lg-hugepage=21
%endif

# Build jemalloc
pushd ../%{jemalloc_name}-%{jemalloc_ver}
%configure \
        --libdir=%{_libdir}/%{pkgname}/lib \
        --bindir=%{_libdir}/%{pkgname}/bin \
        --enable-prof
make %{?_smp_mflags}
popd
%endif

# Enforce strict linking
%define _ld_strict_symbol_defs 1

# Rebuild the autotool artifacts now.
autoreconf -fiv

%configure --enable-autobind --with-selinux $TMPFILES_FLAG \
           --with-systemd \
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-systemdsystemconfdir=%{_sysconfdir}/systemd/system \
           --with-systemdgroupname=%{groupname}  \
           --libexecdir=%{_libexecdir}/%{pkgname} \
           $NSSARGS $ASAN_FLAGS $RUST_FLAGS $CLANG_FLAGS $COCKPIT_FLAGS \
           --enable-cmocka \
           --enable-perl


# lib389
pushd ./src/lib389
%py3_build
popd
# argparse-manpage dynamic man pages have hardcoded man v1 in header,
# need to change it to v8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}%{?prerel}/src/lib389/man/dsconf.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}%{?prerel}/src/lib389/man/dsctl.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}%{?prerel}/src/lib389/man/dsidm.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}%{?prerel}/src/lib389/man/dscreate.8

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

#make %{?_smp_mflags}
make

%install

mkdir -p %{buildroot}%{_datadir}/gdb/auto-load%{_sbindir}
%if %{use_cockpit}
mkdir -p %{buildroot}%{_datadir}/cockpit
%endif
make DESTDIR="$RPM_BUILD_ROOT" install

%if %{use_cockpit}
find %{buildroot}%{_datadir}/cockpit/389-console -type d | sed -e "s@%{buildroot}@@" | sed -e 's/^/\%dir /' > cockpit.list
find %{buildroot}%{_datadir}/cockpit/389-console -type f | sed -e "s@%{buildroot}@@" >> cockpit.list
%endif

# Copy in our docs from doxygen.
cp -r %{_builddir}/%{name}-%{version}%{?prerel}/man/man3 $RPM_BUILD_ROOT/%{_mandir}/man3

# lib389
pushd src/lib389
%py3_install
popd

mkdir -p $RPM_BUILD_ROOT/var/log/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lib/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lock/%{pkgname}

# for systemd
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/%{groupname}.wants

# remove libtool archives and static libs
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/plugins/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libsvrcore.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libsvrcore.la

%if %{bundle_jemalloc}
pushd ../%{jemalloc_name}-%{jemalloc_ver}
make DESTDIR="$RPM_BUILD_ROOT" install_lib install_bin
cp -pa COPYING ../%{name}-%{version}%{?prerel}/COPYING.jemalloc
cp -pa README ../%{name}-%{version}%{?prerel}/README.jemalloc
popd
%endif

%check
# This checks the code, if it fails it prints why, then re-raises the fail to shortcircuit the rpm build.
if ! make DESTDIR="$RPM_BUILD_ROOT" check; then cat ./test-suite.log && false; fi

%post
if [ -n "$DEBUGPOSTTRANS" ] ; then
    output=$DEBUGPOSTTRANS
    output2=${DEBUGPOSTTRANS}.upgrade
else
    output=/dev/null
    output2=/dev/null
fi
# reload to pick up any changes to systemd files
/bin/systemctl daemon-reload >$output 2>&1 || :

# https://fedoraproject.org/wiki/Packaging:UsersAndGroups#Soft_static_allocation
# Soft static allocation for UID and GID
USERNAME="dirsrv"
ALLOCATED_UID=389
GROUPNAME="dirsrv"
ALLOCATED_GID=389
HOMEDIR="/usr/share/dirsrv"

getent group $GROUPNAME >/dev/null || /usr/sbin/groupadd -f -g $ALLOCATED_GID -r $GROUPNAME
if ! getent passwd $USERNAME >/dev/null ; then
    if ! getent passwd $ALLOCATED_UID >/dev/null ; then
      /usr/sbin/useradd -r -u $ALLOCATED_UID -g $GROUPNAME -d $HOMEDIR -s /sbin/nologin -c "user for 389-ds-base" $USERNAME
    else
      /usr/sbin/useradd -r -g $GROUPNAME -d $HOMEDIR -s /sbin/nologin -c "user for 389-ds-base" $USERNAME
    fi
fi

# Reload our sysctl before we restart (if we can)
sysctl --system &> $output; true

# Gather the running instances so we can restart them
instbase="%{_sysconfdir}/%{pkgname}"
ninst=0
for dir in $instbase/slapd-* ; do
    echo dir = $dir >> $output 2>&1 || :
    if [ ! -d "$dir" ] ; then continue ; fi
    case "$dir" in *.removed) continue ;; esac
    basename=`basename $dir`
    inst="%{pkgname}@`echo $basename | sed -e 's/slapd-//g'`"
    echo found instance $inst - getting status  >> $output 2>&1 || :
    if /bin/systemctl -q is-active $inst ; then
       echo instance $inst is running >> $output 2>&1 || :
       instances="$instances $inst"
    else
       echo instance $inst is not running >> $output 2>&1 || :
    fi
    ninst=`expr $ninst + 1`
done
if [ $ninst -eq 0 ] ; then
    echo no instances to upgrade >> $output 2>&1 || :
    exit 0 # have no instances to upgrade - just skip the rest
else
    # restart running instances
    echo shutting down all instances . . . >> $output 2>&1 || :
    for inst in $instances ; do
        echo stopping instance $inst >> $output 2>&1 || :
        /bin/systemctl stop $inst >> $output 2>&1 || :
    done
    for inst in $instances ; do
        echo starting instance $inst >> $output 2>&1 || :
        /bin/systemctl start $inst >> $output 2>&1 || :
    done
fi


%preun
if [ $1 -eq 0 ]; then # Final removal
    # remove instance specific service files/links
    rm -rf %{_sysconfdir}/systemd/system/%{groupname}.wants/* > /dev/null 2>&1 || :
fi

%postun
if [ $1 = 0 ]; then # Final removal
    rm -rf /var/run/%{pkgname}
fi

%post snmp
%systemd_post %{pkgname}-snmp.service

%preun snmp
%systemd_preun %{pkgname}-snmp.service %{groupname}

%postun snmp
%systemd_postun_with_restart %{pkgname}-snmp.service

exit 0

%files
%if %{bundle_jemalloc}
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.jemalloc
%license COPYING.jemalloc
%else
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl
%endif
%dir %{_sysconfdir}/%{pkgname}
%dir %{_sysconfdir}/%{pkgname}/schema
%config(noreplace)%{_sysconfdir}/%{pkgname}/schema/*.ldif
%dir %{_sysconfdir}/%{pkgname}/config
%dir %{_sysconfdir}/systemd/system/%{groupname}.wants
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/slapd-collations.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/certmap.conf
%{_datadir}/%{pkgname}
%{_datadir}/gdb/auto-load/*
%{_unitdir}
%{_bindir}/dbscan
%{_mandir}/man1/dbscan.1.gz
%{_bindir}/ds-replcheck
%{_mandir}/man1/ds-replcheck.1.gz
%{_bindir}/ds-logpipe.py
%{_mandir}/man1/ds-logpipe.py.1.gz
%{_bindir}/ldclt
%{_mandir}/man1/ldclt.1.gz
%{_bindir}/logconv.pl
%{_mandir}/man1/logconv.pl.1.gz
%{_bindir}/pwdhash
%{_mandir}/man1/pwdhash.1.gz
#%caps(CAP_NET_BIND_SERVICE=pe) {_sbindir}/ns-slapd
%{_sbindir}/ns-slapd
%{_mandir}/man8/ns-slapd.8.gz
%{_sbindir}/openldap_to_ds
%{_mandir}/man8/openldap_to_ds.8.gz
%{_libexecdir}/%{pkgname}/ds_systemd_ask_password_acl
%{_mandir}/man5/99user.ldif.5.gz
%{_mandir}/man5/certmap.conf.5.gz
%{_mandir}/man5/slapd-collations.conf.5.gz
%{_mandir}/man5/dirsrv.5.gz
%{_mandir}/man5/dirsrv.systemd.5.gz
%{_libdir}/%{pkgname}/python
%dir %{_libdir}/%{pkgname}/plugins
%{_libdir}/%{pkgname}/plugins/*.so
# This has to be hardcoded to /lib - $libdir changes between lib/lib64, but
# sysctl.d is always in /lib.
%{_prefix}/lib/sysctl.d/*
%dir %{_localstatedir}/lib/%{pkgname}
%dir %{_localstatedir}/log/%{pkgname}
%ghost %dir %{_localstatedir}/lock/%{pkgname}
%exclude %{_sbindir}/ldap-agent*
%exclude %{_mandir}/man1/ldap-agent.1.gz
%exclude %{_unitdir}/%{pkgname}-snmp.service
%if %{bundle_jemalloc}
%{_libdir}/%{pkgname}/lib/
%{_libdir}/%{pkgname}/bin/
%exclude %{_libdir}/%{pkgname}/bin/jemalloc-config
%exclude %{_libdir}/%{pkgname}/bin/jemalloc.sh
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc.a
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc.so
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc_pic.a
%exclude %{_libdir}/%{pkgname}/lib/pkgconfig
%endif

%files devel
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%{_mandir}/man3/*
%{_includedir}/svrcore.h
%{_includedir}/%{pkgname}
%{_libdir}/libsvrcore.so
%{_libdir}/%{pkgname}/libslapd.so
%{_libdir}/%{pkgname}/libns-dshttpd.so
%{_libdir}/%{pkgname}/libldaputil.so
%{_libdir}/pkgconfig/svrcore.pc
%{_libdir}/pkgconfig/dirsrv.pc

%files libs
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%dir %{_libdir}/%{pkgname}
%{_libdir}/libsvrcore.so.*
%{_libdir}/%{pkgname}/libslapd.so.*
%{_libdir}/%{pkgname}/libns-dshttpd-*.so
%{_libdir}/%{pkgname}/libldaputil.so.*
%{_libdir}/%{pkgname}/librewriters.so*
%if %{bundle_jemalloc}
%{_libdir}/%{pkgname}/lib/libjemalloc.so.2
%endif

%files snmp
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/ldap-agent.conf
%{_sbindir}/ldap-agent*
%{_mandir}/man1/ldap-agent.1.gz
%{_unitdir}/%{pkgname}-snmp.service

%files -n python%{python3_pkgversion}-lib389
%doc LICENSE LICENSE.GPLv3+
%{python3_sitelib}/lib389*
%{_sbindir}/dsconf
%{_mandir}/man8/dsconf.8.gz
%{_sbindir}/dscreate
%{_mandir}/man8/dscreate.8.gz
%{_sbindir}/dsctl
%{_mandir}/man8/dsctl.8.gz
%{_sbindir}/dsidm
%{_mandir}/man8/dsidm.8.gz
%{_libexecdir}/%{pkgname}/dscontainer

%if %{use_cockpit}
%files -n cockpit-389-ds -f cockpit.list
%{_datarootdir}/metainfo/389-console/org.port389.cockpit_console.metainfo.xml
%doc README.md
%endif

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.3-3.1
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Fri Feb 26 2021 Alexander Bokovoy <abokovoy@redhat.com> - 2.0.3-3
- Remove a revert of the fix for Issue 4609 - CVE - info disclosure when authenticating(breaks Dogtag)
- Dogtag has fixed own code that failed in the presence of the fix for Issue 4609

* Fri Feb 19 2021 Mark Reynolds <mreynolds@redhat.com> - 2.0.3-2
- Bump version to 2.0.3-2
- Revert Issue 4609 - CVE - info disclosure when authenticating(breaks DogTag)

* Fri Feb 12 2021 Mark Reynolds <mreynolds@redhat.com> - 2.0.3-1
- Bump version to 2.0.3
- Issue 4619 - remove pytest requirement from lib389
- Issue 4615 - log message when psearch first exceeds max threads per conn
- Issue 4469 - Backend redesing phase 3a - implement dbimpl API and use it in back-ldbm (#4618)
- Issue 4324 - Some architectures the cache line size file does not exist
- Issue 4593 - RFE - Print help when nsSSLPersonalitySSL is not found (#4614)
- Issue 4469 - Backend redesign phase 3a - bdb dependency removal from back-ldbm
- PR 4564 - Update dscontainer
- Issue 4149 - UI - port TreeView and opther components to PF4
- Issue 4577 - Add GitHub actions
- Issue 4591 - RFE - improve openldap_to_ds help and features (#4607)
- issue 4612 - Fix pytest fourwaymmr_test for non root user (#4613)
- Issue 4609 - CVE - info disclosure when authenticating
- Issue 4348 - Add tests for dsidm
- Issue 4571 - Stale libdb-utils dependency
- Issue 4600 - performance modify rate: reduce lock contention on the object extension factory (#4601)
- Issue 4577 - Add GitHub actions
- Issue 4588 - BUG - unable to compile without xcrypt (#4589)
- Issue 4579 - libasan detects heap-use-after-free in URP test (#4584)
- Issue 4581 - A failed re-indexing leaves the database in broken state (#4582)
- Issue 4348 - Add tests for dsidm
- Issue 4577 - Add GitHub actions
- Issue 4563 - Failure on s390x: 'Fails to split RDN "o=pki-tomcat-CA" into components' (#4573)
- Issue 4093 - fix compiler warnings and update doxygen
- Issue 4575 - Update test docstrings metadata
- Issue 4526 - sync_repl: when completing an operation in the pending list, it can select the wrong operation (#4553)
- Issue 4324 - Performance search rate: change entry cache monitor to recursive pthread mutex (#4569)
- Issue 4513 - Add DS version check to SSL version test (#4570)
- Issue 5442 - Search results are different between RHDS10 and RHDS11
- Issue 4396 - Minor memory leak in backend (#4558)
- Issue 4513 - Fix replication CI test failures (#4557)
- Issue 4513 - Fix replication CI test failures (#4557)
- Issue 4153 - Added a CI test (#4556)
- Issue 4506 - BUG - fix oob alloc for fds (#4555)
- Issue 4548 - CLI - dsconf needs better root DN access control plugin validation
- Issue 4506 - Temporary fix for io issues (#4516)
- Issue 4535 - lib389 - Fix log function in backends.py
- Issue 4534 - libasan read buffer overflow in filtercmp (#4541)
- Issue 4544 - Compiler warnings on krb5 functions (#4545)
- Update rpm.mk for RUST tarballs

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Mark Reynolds <mreynolds@redhat.com> - 2.0.2-1
- Bump version to 2.0.2
- Issue 4539 - BUG - no such file if no overlays in openldap during migration (#4540)
- Issue 4528 - Fix cn=monitor SCOPE_ONE search (#4529)
- Issue 4535 - lib389 - healthcheck throws exception if backend is not replicated
- Issue 4537 - Use KRB5_CLIENT_KTNAME for client keytabs (#4523)
- Issue 4513 - CI Tests - fix test failures
- Issue 4504 - insure that repl_monitor_test use ldapi (for RHEL) - fix merge issue (#4533)
- Issue 4315 - performance search rate: nagle triggers high rate of setsocketopt
- Issue 4504 - pytest test_dsconf_replication_monitor fails on RHEL - Fix merging issue (#4530)
- Issue 4504 - Insure ldapi is enabled in repl_monitor_test.py (Needed on RHEL) (#4527)
- Issue 4506 - BUG - Fix bounds on fd table population (#4520)
- Issue 4521 - DS crash in deref plugin if dereferenced entry exists but is not returned by internal search (#4525)
- Issue 4219 - Log internal unindexed searches (notes=A)
- Issue 4384 - Separate eventq into REALTIME and MONOTONIC
- Issue 4381 - RFE - LDAPI authentication DN rewritter
- Issue 4513 - Fix schema test and lib389 task module (#4514)
- Issue 4414 - disk monitoring - prevent division by zero crash
- Issue 4517 - BUG: Multiple systemd pin warnings (#4518)
- Issue 4507 - Improve csngen testing task (#4508)
- Issue 4498 - BUG - entryuuid replication may not work (#4503)
- Issue 4480 - Unexpected info returned to ldap request (#4491)
- Issue 4504 - Fix pytest test_dsconf_replication_monitor (#4505)
- Issue 4373 - BUG - one line cleanup, free results in mt if ent 0 (#4502)
- Issue 4500 - Add cockpit enabling to dsctl
- Issue 4272 - RFE - add support for gost-yescrypt for hashing passwords (#4497)
- Issue 1795 - RFE - Enable logging for libldap and libber in error log (#4481)
- Issue 3522 - Remove DES to AES conversion code
- Issue 4492 - Changelog cache can upload updates from a wrong starting point (CSN) (#4493)
- Issue 4373 - BUG - calloc of size 0 in MT build (#4496)
- Issue 4483 - heap-use-after-free in slapi_be_getsuffix
- Issue 4486 - Remove random ldif file generation from import test (#4487)
- Issue 4224 - cleanup specfile after libsds removal
- Issue 4421 - Unable to build with Rust enabled in closed environment
- Issue 4489 - Remove return statement from a void function (#4490)
- Issue 4229 - RFE - Improve rust linking and build performance (#4474)
- Issue 4224 - openldap can become confused with entryuuid
- Issue 4313 - improve tests and improve readme re refdel
- Issue 4313 - fix potential syncrepl data corruption
- Issue 4419 - Warn users of skipped entries during ldif2db online import (#4476)
- Issue 4243 - Fix test (4th): SyncRepl plugin provides a wrong (#4475)
- Issue 4315 - performance search rate: nagle triggers high rate of setsocketopt (#4437)
- Issue 4460 - BUG - add machine name to subject alt names in SSCA (#4472)
- Issue 4446 - RFE - openldap password hashers
- Issue 4284 - dsidm fails to delete an organizationalUnit entry
- Issue 4243 - Fix test: SyncRepl plugin provides a wrong cookie (#4466) (#4466)
- Issue 4464 - RFE - clang with ds+asan+rust
- Issue 4105 - Remove python.six (fix regression)
- Issue 4384 - Use MONOTONIC clock for all timing events and conditions
- Issue 4418 - ldif2db - offline. Warn the user of skipped entries
- Issue 4243 - Fix test: SyncRepl plugin provides a wrong cookie (#4467)
- Issue 4460 - BUG  - lib389 should use system tls policy
- Issue 3657 - Add options to dsctl for dsrc file
- Issue 4454 - RFE - fix version numbers to allow object caching
- Issue 3986 - UI - Handle objectclasses that do not have X-ORIGIN set
- Issue 4297 - 2nd fix for on ADD replication URP issue internal searches with filter containing unescaped chars (#4439)
- Issue 4112 - Added a CI test (#4441)
- Issue 4449 - dsconf replication monitor fails to retrieve database RUV - consumer (Unavailable) (#4451)
- Issue 4105 - Remove python.six from lib389 (#4456)
- Issue 4440 - BUG - ldifgen with --start-idx option fails with unsupported operand (#4444)
- Issue 4410 - RFE - ndn cache with arc in rust
- Issue 4373 - BUG - Mapping Tree nodes can be created that are invalid
- Issue 4428 - BUG Paged Results with critical false causes sigsegv in chaining
- Issue 4428 - Paged Results with Chaining Test Case
- Issue 2054 - do not add referrals for masters with different data generation
- Issue 4383 - Do not normalize escaped spaces in a DN
- Issue 4432 - After a failed online import the next imports are very slow
- Issue 4316 - performance search rate: useless poll on network send callback (#4424)
- Issue 4281 - dsidm user status fails with Error: 'nsUserAccount' object has no attribute 'is_locked'
- Issue 4429 - NULL dereference in revert_cache()
- Issue 4412 - Fix CLI repl-agmt requirement for parameters (#4422)
- Issue 4407 - RFE - remove http client and presence plugin (#4409)
- Issue 4398 - build problems at alpine linux
- Issue 4415 - unable to query schema if there are extra parenthesis

* Thu Oct 29 2020 Mark Reynolds <mreynolds@redhat.com> - 2.0.1-1
- Bump version to 2.0.1
- Issue 4420 - change NVR to use X.X.X instead of X.X.X.X
- Issue 4391 - DSE config modify does not call be_postop (#4394)
- Issue 4218 - Verify the new wtime and optime access log keywords (#4397)
- Issue 4176 - CL trimming causes high CPU
- Issue 2058 - Add keep alive entry after on-line initialization - second version (#4399)
- Issue 4403 - RFE - OpenLDAP pw hash migration tests (#4408)

* Wed Oct 28 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.5.0-1
- Bump version to 1.4.5.0
- Issue 4262 - more perl removal cleanup
- Issue 2526 - retrocl backend created out of order

* Mon Oct 26 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.4.6-1
- Bump version to 1.4.4.6
- Issue 4262 - Remove legacy tools subpackage (final cleanup)
- Issue 4262 - Remove legacy tools subpackage (restart instances after rpm install)
- Issue 4262 - Remove legacy tools subpackage
- Issue 2526 - revert API change in slapi_be_getsuffix()
- Issue 4363 - Sync repl: per thread structure was incorrectly initialized (#4395)
- Issue 4392 - Update create_test.py
- Issue 2820 - Fix CI tests (#4365)
- Issue 2526 - suffix management in backends incorrect
- Issue 4389 - errors log with incorrectly formatted message parent_update_on_childchange
- Issue 4295 - Fix a closing quote issue (#4386)
- Issue 1199 - Misleading message in access log for idle timeout (#4385)
- Issue 3600 - RFE - openldap migration tooling (#4318)
- Issue 4176 - import ldif2cl task should not close all changelogs
- Issue 4159 - Healthcheck code DSBLE0002 not returned on disabled suffix
- Issue 4379 - allow more than 1 empty AttributeDescription for ldapsearch, without the risk of denial of service (#4380)
- Issue 4329 - Sync repl - if a serie of updates target the same entry then the cookie get wrong changenumber (#4356)
- Issue 3555 - Fix npm audit issues (#4370)
- Issue 4372 - BUG - Chaining DB did not validate bind mech parameters (#4374)
- Issue 4334 - RFE - Task timeout may cause larger dataset imports to fail (#4359)
- Issue 4361 - RFE - add - dscreate --advanced flag to avoid user confusion
- Issue 4368 - ds-replcheck crashes when processing glue entries
- Issue 4366 - lib389 - Fix account status inactivity checks
- Issue 4265 - UI - Make the secondary plugins read-only (#4364)
- Issue 4360 - password policy max sequence sets is not working as expected
- Issue 4348 - Add tests for dsidm
- Issue 4350 - One line, fix invalid type error in tls_cacertdir check (#4358)

