# SPDX-License-Identifier: MIT

%global libqat_soversion  0
%global libusdm_soversion 0
Name:             qatlib
Version:          20.10.0
Release:          4%{?dist}
Summary:          Intel QuickAssist user space library
# The entire source code is released under BSD.
# For a breakdown of inbound licenses see the INSTALL file.
License:          BSD and (BSD or GPLv2)
URL:              https://github.com/intel/%{name}
Source0:          https://github.com/intel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:    systemd gcc make autoconf automake libtool systemd-devel openssl-devel zlib-devel
Requires(pre):    shadow-utils
# https://bugzilla.redhat.com/show_bug.cgi?id=1897661
ExcludeArch:      %{arm} aarch64 %{power64} s390x i686

%{?systemd_requires}

%description
Intel QuickAssist Technology (Intel QAT) provides hardware acceleration
for offloading security, authentication and compression services from the
CPU, thus significantly increasing the performance and efficiency of
standard platform solutions.

Its services include symmetric encryption and authentication,
asymmetric encryption, digital signatures, RSA, DH and ECC, and
lossless data compression.

This package provides user space libraries that allow access to
Intel QuickAssist devices and expose the Intel QuickAssist APIs.

%package       devel
Summary:       Headers and libraries to build applications that use qatlib
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
This package contains headers and libraries required to build applications
that use the Intel QuickAssist APIs.

%prep
%autosetup

%build
autoreconf -vif
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install

%pre
getent group qat >/dev/null || groupadd -r qat
exit 0

%post
%systemd_post qat.service

%preun
%systemd_preun qat.service

%postun
%systemd_postun_with_restart qat.service

%files
%license LICENSE*
%{_libdir}/libqat.so.%{libqat_soversion}*
%{_libdir}/libusdm.so.%{libusdm_soversion}*
%{_sbindir}/qatmgr
%{_sbindir}/qat_init.sh
%{_unitdir}/qat.service
%{_mandir}/man8/qat_init.sh.8*
%{_mandir}/man8/qatmgr.8*

%files         devel
%{_libdir}/libqat.so
%{_libdir}/libusdm.so
%{_includedir}/qat
%exclude %{_libdir}/libqat.la
%exclude %{_libdir}/libusdm.la

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20.10.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  14 2020 Giovanni Cabiddu <giovanni.cabiddu@intel.com> - 20.10.0-2
- Add ExcludeArch i686

* Mon Nov  16 2020 Giovanni Cabiddu <giovanni.cabiddu@intel.com> - 20.10.0-1
- Update to qatlib 20.10
- Fixes to spec to address comments from Fedora review

* Mon Aug  10 2020 Mateusz Polrola <mateuszx.potrola@intel.com> - 20.08.0-1
- Initial version of the package
