%{?mingw_package_header}

# This spec file assumes you are building on a Fedora version
# that's still supported by the vendor. It may work on other distros
# or versions, but no effort will be made to ensure that going forward.
%define min_fedora 31

%if 0%{?fedora} && 0%{?fedora} >= %{min_fedora}
    %define supported_platform 1
%else
    %define supported_platform 0
%endif

# Default to skipping autoreconf.  Distros can change just this one line
# (or provide a command-line override) if they backport any patches that
# touch configure.ac or Makefile.am.
%{!?enable_autotools:%define enable_autotools 0}

# The mingw build is client only.  Set up defaults for hypervisor drivers
# that talk via a native remote protocol, and for which prereq mingw
# libraries exist.
%define with_esx           0%{!?_without_esx:1}
# missing libwsman, so can't build hyper-v
%define with_hyperv        0%{!?_without_hyperv:0}
%define with_xenapi        0%{!?_without_xenapi:1}
%define with_vz            0%{!?_without_vz:0}

# RHEL ships ESX but not PowerHypervisor, HyperV, or libxenserver (xenapi)
%if 0%{?rhel}
    %define with_xenapi 0
    %define with_hyperv 0
%endif

Name:           mingw-libvirt
Version:        6.6.0
Release:        3%{?dist}
Summary:        MinGW Windows libvirt virtualization library

License:        LGPLv2+
URL:            https://libvirt.org/

%if %(echo %{version} | grep -q "\.0$"; echo $?) == 1
    %define mainturl stable_updates/
%endif
Source: https://libvirt.org/sources/%{?mainturl}libvirt-%{version}.tar.xz

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-glib2 >= 2.48
BuildRequires:  mingw64-glib2 >= 2.48
BuildRequires:  mingw32-libgpg-error
BuildRequires:  mingw64-libgpg-error
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-portablexdr
BuildRequires:  mingw64-portablexdr
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw64-dlfcn

BuildRequires:  pkgconfig
# Need native version for msgfmt
BuildRequires:  gettext
BuildRequires:  libxslt
BuildRequires:  python3
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
%if 0%{?enable_autotools}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool
%endif
BuildRequires: python3-docutils

BuildRequires: mingw32-libssh2
BuildRequires: mingw64-libssh2
%if %{with_esx}
BuildRequires: mingw32-curl
BuildRequires: mingw64-curl
%endif
BuildRequires: cpp
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: rpcgen
%endif

BuildArch:      noarch

%description
MinGW Windows libvirt virtualization library.

# Mingw32
%package -n mingw32-libvirt
Summary: %{summary}

%description -n mingw32-libvirt
MinGW Windows libvirt virtualization library.

%package -n mingw32-libvirt-static
Summary: %{summary}
Requires: mingw32-libvirt = %{version}-%{release}

%description -n mingw32-libvirt-static
MinGW Windows libvirt virtualization library, static version.

# Mingw64
%package -n mingw64-libvirt
Summary: %{summary}

%description -n mingw64-libvirt
MinGW Windows libvirt virtualization library.

%package -n mingw64-libvirt-static
Summary: %{summary}
Requires: mingw64-libvirt = %{version}-%{release}

%description -n mingw64-libvirt-static
MinGW Windows libvirt virtualization library, static version.

%{?mingw_debug_package}


%prep
%setup -q -n libvirt-%{version}

%build
%if ! %{supported_platform}
echo "This RPM requires Fedora >= %{min_fedora}"
exit 1
%endif

%if ! %{with_esx}
    %define _without_esx --without-esx
%endif

%if ! %{with_hyperv}
    %define _without_hyperv --without-hyperv
%endif

%if ! %{with_xenapi}
    %define _without_xenapi --without-xenapi
%endif

%if ! %{with_vz}
    %define _without_vz --without-vz
%endif

%if 0%{?enable_autotools}
autoreconf -if
%endif

# XXX enable SASL in future
%mingw_configure \
  --enable-static \
  --without-xen \
  --without-qemu \
  --without-openvz \
  --without-lxc \
  --without-vbox \
  %{?_without_xenapi} \
  --without-sasl \
  --without-polkit \
  --without-libvirtd \
  %{?_without_esx} \
  %{?_without_hyperv} \
  --without-vmware \
  --without-parallels \
  --without-netcf \
  --without-audit \
  --without-dtrace \
  --enable-expensive-tests

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

rm -rf $RPM_BUILD_ROOT%{mingw32_sysconfdir}/libvirt/nwfilter
rm -rf $RPM_BUILD_ROOT%{mingw64_sysconfdir}/libvirt/nwfilter
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/doc/*
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/doc/*
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc/*
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc/*

rm -rf $RPM_BUILD_ROOT%{mingw32_libexecdir}/libvirt_iohelper.exe
rm -rf $RPM_BUILD_ROOT%{mingw64_libexecdir}/libvirt_iohelper.exe
rm -rf $RPM_BUILD_ROOT%{mingw32_libexecdir}/libvirt-guests.sh
rm -rf $RPM_BUILD_ROOT%{mingw64_libexecdir}/libvirt-guests.sh


# Mingw32
%files -n mingw32-libvirt
%dir %{mingw32_sysconfdir}/libvirt/
%config(noreplace) %{mingw32_sysconfdir}/libvirt/libvirt.conf
%config(noreplace) %{mingw32_sysconfdir}/libvirt/libvirt-admin.conf

%{mingw32_bindir}/libvirt-0.dll
%{mingw32_bindir}/virsh.exe
%{mingw32_bindir}/virt-admin.exe
%{mingw32_bindir}/virt-xml-validate
%{mingw32_bindir}/virt-pki-validate
%{mingw32_bindir}/libvirt-lxc-0.dll
%{mingw32_bindir}/libvirt-qemu-0.dll
%{mingw32_bindir}/libvirt-admin-0.dll

%{mingw32_libdir}/libvirt.dll.a
%{mingw32_libdir}/pkgconfig/libvirt.pc
%{mingw32_libdir}/pkgconfig/libvirt-qemu.pc
%{mingw32_libdir}/pkgconfig/libvirt-lxc.pc
%{mingw32_libdir}/pkgconfig/libvirt-admin.pc
%{mingw32_libdir}/libvirt-lxc.dll.a
%{mingw32_libdir}/libvirt-qemu.dll.a
%{mingw32_libdir}/libvirt-admin.dll.a

%dir %{mingw32_datadir}/libvirt/
%dir %{mingw32_datadir}/libvirt/schemas/
%{mingw32_datadir}/libvirt/schemas/basictypes.rng
%{mingw32_datadir}/libvirt/schemas/capability.rng
%{mingw32_datadir}/libvirt/schemas/cputypes.rng
%{mingw32_datadir}/libvirt/schemas/domain.rng
%{mingw32_datadir}/libvirt/schemas/domainbackup.rng
%{mingw32_datadir}/libvirt/schemas/domaincaps.rng
%{mingw32_datadir}/libvirt/schemas/domaincheckpoint.rng
%{mingw32_datadir}/libvirt/schemas/domaincommon.rng
%{mingw32_datadir}/libvirt/schemas/domainsnapshot.rng
%{mingw32_datadir}/libvirt/schemas/interface.rng
%{mingw32_datadir}/libvirt/schemas/network.rng
%{mingw32_datadir}/libvirt/schemas/networkcommon.rng
%{mingw32_datadir}/libvirt/schemas/networkport.rng
%{mingw32_datadir}/libvirt/schemas/nodedev.rng
%{mingw32_datadir}/libvirt/schemas/nwfilter.rng
%{mingw32_datadir}/libvirt/schemas/nwfilter_params.rng
%{mingw32_datadir}/libvirt/schemas/nwfilterbinding.rng
%{mingw32_datadir}/libvirt/schemas/secret.rng
%{mingw32_datadir}/libvirt/schemas/storagecommon.rng
%{mingw32_datadir}/libvirt/schemas/storagepool.rng
%{mingw32_datadir}/libvirt/schemas/storagepoolcaps.rng
%{mingw32_datadir}/libvirt/schemas/storagevol.rng
%dir %{mingw32_datadir}/libvirt/api/
%{mingw32_datadir}/libvirt/api/libvirt-api.xml
%{mingw32_datadir}/libvirt/api/libvirt-lxc-api.xml
%{mingw32_datadir}/libvirt/api/libvirt-qemu-api.xml
%{mingw32_datadir}/libvirt/api/libvirt-admin-api.xml

%{mingw32_datadir}/libvirt/cpu_map/*.xml

%{mingw32_datadir}/libvirt/test-screenshot.png

%{mingw32_datadir}/locale/*/LC_MESSAGES/libvirt.mo

%dir %{mingw32_includedir}/libvirt
%{mingw32_includedir}/libvirt/libvirt.h
%{mingw32_includedir}/libvirt/libvirt-common.h
%{mingw32_includedir}/libvirt/libvirt-domain.h
%{mingw32_includedir}/libvirt/libvirt-domain-checkpoint.h
%{mingw32_includedir}/libvirt/libvirt-domain-snapshot.h
%{mingw32_includedir}/libvirt/libvirt-event.h
%{mingw32_includedir}/libvirt/libvirt-host.h
%{mingw32_includedir}/libvirt/libvirt-interface.h
%{mingw32_includedir}/libvirt/libvirt-network.h
%{mingw32_includedir}/libvirt/libvirt-nodedev.h
%{mingw32_includedir}/libvirt/libvirt-nwfilter.h
%{mingw32_includedir}/libvirt/libvirt-secret.h
%{mingw32_includedir}/libvirt/libvirt-storage.h
%{mingw32_includedir}/libvirt/libvirt-stream.h
%{mingw32_includedir}/libvirt/virterror.h
%{mingw32_includedir}/libvirt/libvirt-lxc.h
%{mingw32_includedir}/libvirt/libvirt-qemu.h
%{mingw32_includedir}/libvirt/libvirt-admin.h

%{mingw32_mandir}/man1/virsh.1*
%{mingw32_mandir}/man1/virt-admin.1*
%{mingw32_mandir}/man1/virt-xml-validate.1*
%{mingw32_mandir}/man1/virt-pki-validate.1*
%{mingw32_mandir}/man7/virkey*.7*

%files -n mingw32-libvirt-static
%{mingw32_libdir}/libvirt.a
%{mingw32_libdir}/libvirt-lxc.a
%{mingw32_libdir}/libvirt-qemu.a
%{mingw32_libdir}/libvirt-admin.a

# Mingw64
%files -n mingw64-libvirt
%dir %{mingw64_sysconfdir}/libvirt/
%config(noreplace) %{mingw64_sysconfdir}/libvirt/libvirt.conf
%config(noreplace) %{mingw64_sysconfdir}/libvirt/libvirt-admin.conf

%{mingw64_bindir}/libvirt-0.dll
%{mingw64_bindir}/virsh.exe
%{mingw64_bindir}/virt-admin.exe
%{mingw64_bindir}/virt-xml-validate
%{mingw64_bindir}/virt-pki-validate
%{mingw64_bindir}/libvirt-lxc-0.dll
%{mingw64_bindir}/libvirt-qemu-0.dll
%{mingw64_bindir}/libvirt-admin-0.dll

%{mingw64_libdir}/libvirt.dll.a
%{mingw64_libdir}/pkgconfig/libvirt.pc
%{mingw64_libdir}/pkgconfig/libvirt-qemu.pc
%{mingw64_libdir}/pkgconfig/libvirt-lxc.pc
%{mingw64_libdir}/pkgconfig/libvirt-admin.pc
%{mingw64_libdir}/libvirt-lxc.dll.a
%{mingw64_libdir}/libvirt-qemu.dll.a
%{mingw64_libdir}/libvirt-admin.dll.a

%dir %{mingw64_datadir}/libvirt/
%dir %{mingw64_datadir}/libvirt/schemas/
%{mingw64_datadir}/libvirt/schemas/basictypes.rng
%{mingw64_datadir}/libvirt/schemas/capability.rng
%{mingw64_datadir}/libvirt/schemas/cputypes.rng
%{mingw64_datadir}/libvirt/schemas/domain.rng
%{mingw64_datadir}/libvirt/schemas/domainbackup.rng
%{mingw64_datadir}/libvirt/schemas/domaincaps.rng
%{mingw64_datadir}/libvirt/schemas/domaincheckpoint.rng
%{mingw64_datadir}/libvirt/schemas/domaincommon.rng
%{mingw64_datadir}/libvirt/schemas/domainsnapshot.rng
%{mingw64_datadir}/libvirt/schemas/interface.rng
%{mingw64_datadir}/libvirt/schemas/network.rng
%{mingw64_datadir}/libvirt/schemas/networkcommon.rng
%{mingw64_datadir}/libvirt/schemas/networkport.rng
%{mingw64_datadir}/libvirt/schemas/nodedev.rng
%{mingw64_datadir}/libvirt/schemas/nwfilter.rng
%{mingw64_datadir}/libvirt/schemas/nwfilter_params.rng
%{mingw64_datadir}/libvirt/schemas/nwfilterbinding.rng
%{mingw64_datadir}/libvirt/schemas/secret.rng
%{mingw64_datadir}/libvirt/schemas/storagecommon.rng
%{mingw64_datadir}/libvirt/schemas/storagepool.rng
%{mingw64_datadir}/libvirt/schemas/storagepoolcaps.rng
%{mingw64_datadir}/libvirt/schemas/storagevol.rng
%dir %{mingw64_datadir}/libvirt/api/
%{mingw64_datadir}/libvirt/api/libvirt-api.xml
%{mingw64_datadir}/libvirt/api/libvirt-lxc-api.xml
%{mingw64_datadir}/libvirt/api/libvirt-qemu-api.xml
%{mingw64_datadir}/libvirt/api/libvirt-admin-api.xml

%{mingw64_datadir}/libvirt/cpu_map/*.xml

%{mingw64_datadir}/libvirt/test-screenshot.png

%{mingw64_datadir}/locale/*/LC_MESSAGES/libvirt.mo

%dir %{mingw64_includedir}/libvirt
%{mingw64_includedir}/libvirt/libvirt.h
%{mingw64_includedir}/libvirt/libvirt-common.h
%{mingw64_includedir}/libvirt/libvirt-domain.h
%{mingw64_includedir}/libvirt/libvirt-domain-checkpoint.h
%{mingw64_includedir}/libvirt/libvirt-domain-snapshot.h
%{mingw64_includedir}/libvirt/libvirt-event.h
%{mingw64_includedir}/libvirt/libvirt-host.h
%{mingw64_includedir}/libvirt/libvirt-interface.h
%{mingw64_includedir}/libvirt/libvirt-network.h
%{mingw64_includedir}/libvirt/libvirt-nodedev.h
%{mingw64_includedir}/libvirt/libvirt-nwfilter.h
%{mingw64_includedir}/libvirt/libvirt-secret.h
%{mingw64_includedir}/libvirt/libvirt-storage.h
%{mingw64_includedir}/libvirt/libvirt-stream.h
%{mingw64_includedir}/libvirt/virterror.h
%{mingw64_includedir}/libvirt/libvirt-lxc.h
%{mingw64_includedir}/libvirt/libvirt-qemu.h
%{mingw64_includedir}/libvirt/libvirt-admin.h

%{mingw64_mandir}/man1/virsh.1*
%{mingw64_mandir}/man1/virt-admin.1*
%{mingw64_mandir}/man1/virt-xml-validate.1*
%{mingw64_mandir}/man1/virt-pki-validate.1*
%{mingw64_mandir}/man7/virkey*.7*

%files -n mingw64-libvirt-static
%{mingw64_libdir}/libvirt.a
%{mingw64_libdir}/libvirt-lxc.a
%{mingw64_libdir}/libvirt-qemu.a
%{mingw64_libdir}/libvirt-admin.a


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:43:38 GMT 2020 Sandro Mani <manisandro@gmail.com> - 6.6.0-2
- Rebuild (mingw-gettext)

* Tue Aug 04 2020 Cole Robinson <crobinso@redhat.com> - 6.6.0-1
- Update to version 6.6.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Cole Robinson <crobinso@redhat.com> - 6.5.0-1
- Update to version 6.5.0

* Tue Jun 02 2020 Cole Robinson <crobinso@redhat.com> - 6.4.0-1
- Update to version 6.4.0

* Tue May 05 2020 Cole Robinson <crobinso@redhat.com> - 6.3.0-1
- Update to version 6.3.0

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 6.2.0-2
- Rebuild (gettext)

* Thu Apr 02 2020 Cole Robinson <crobinso@redhat.com> - 6.2.0-1
- Update to version 6.2.0

* Wed Mar 04 2020 Cole Robinson <crobinso@redhat.com> - 6.1.0-1
- Update to version 6.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Cole Robinson <crobinso@redhat.com> - 6.0.0-1
- Update to version 6.0.0
