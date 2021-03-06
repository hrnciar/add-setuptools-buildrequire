%{!?configure_options: %global configure_options %{nil}}

Name: libvma
Version: 9.2.2
Release: 3%{?dist}
Summary: A library for boosting TCP and UDP traffic (over RDMA hardware)

License: GPLv2 or BSD
Url: https://github.com/Mellanox/libvma
Source0: https://github.com/Mellanox/libvma/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: 0002-Update-systemctl-files.patch
Patch1: 0003-Remove-30-libvma-limits.patch
Patch2: 0004-Use-vmad-for-systemd.patch
Patch3: 0005-Fix-issues-for-gcc-11.patch

# libvma currently supports only the following architectures
ExclusiveArch: x86_64 ppc64le ppc64 aarch64

BuildRequires: pkgconfig
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: rdma-core-devel
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libnl-route-3.0)
BuildRequires: make

%description
libvma is a LD_PRELOAD-able library that boosts performance of TCP and
UDP traffic. It allows application written over standard socket API to
handle fast path data traffic from user space over Ethernet and/or
Infiniband with full network stack bypass and get better throughput,
latency and packets/sec rate.

No application binary change is required for that.
libvma is supported by RDMA capable devices that support "verbs"
IBV_QPT_RAW_PACKET QP for Ethernet and/or IBV_QPT_UD QP for IPoIB.

%package devel
Summary: Header files required to develop with libvma
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes headers for building programs with libvma's
interfaces.

%package utils
Summary: Utilities used with libvma
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
This package contains the tool for collecting and analyzing libvma statistic.

%prep
%setup -q
%autosetup -p1

%build
export revision=1
if [ ! -e configure ] && [ -e autogen.sh ]; then
    VMA_RELEASE=1 ./autogen.sh
fi

%configure %{?configure_options}
%{make_build}

%install
%{make_install}

find $RPM_BUILD_ROOT%{_libdir} -name '*.la' -delete
install -D -m 644 contrib/scripts/vma.service $RPM_BUILD_ROOT/%{_prefix}/lib/systemd/system/vma.service

%post
%systemd_post vma.service

%preun
%systemd_preun vma.service

%postun
%systemd_postun_with_restart vma.service

%files
%{_libdir}/%{name}.so*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.txt
%doc %{_pkgdocdir}/journal.txt
%doc %{_pkgdocdir}/VMA_VERSION
%config(noreplace) %{_sysconfdir}/libvma.conf
%{_sbindir}/vmad
%{_prefix}/lib/systemd/system/vma.service
%license COPYING LICENSE
%{_mandir}/man7/vma.*
%{_mandir}/man8/vmad.*

%files devel
%dir %{_includedir}/mellanox
%{_includedir}/mellanox/vma_extra.h

%files utils
%{_bindir}/vma_stats
%{_mandir}/man8/vma_stats.*

%changelog
* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 9.2.2-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Igor Ivanov <igor.ivanov.va@gmail.com> 9.2.2-1
- Bump version to 9.2.2
- Fix issues for gcc-11

* Thu Dec 10 2020 Jeff Law <law@redhat.com> 9.1.1-2
- Don't use "register" in C++17.  Still FTBFS though.

* Sun Nov 15 2020 Igor Ivanov <igor.ivanov.va@gmail.com> 9.1.1-1
- Bump version to 9.1.1

* Fri Apr 17 2020 Igor Ivanov <igor.ivanov.va@gmail.com> 9.0.2-1
- Align with Fedora guidelines
- Bump version to 9.0.2

* Thu Feb 7 2019 Igor Ivanov <igor.ivanov.va@gmail.com> 8.8.2-1
- Improve package update processing

* Tue Dec 19 2017 Igor Ivanov <igor.ivanov.va@gmail.com> 8.5.1-1
- Add systemd support

* Tue May 9 2017 Ophir Munk <ophirmu@mellanox.com> 8.3.4-1
- Add libvma-debug.so installation

* Mon Nov 28 2016 Igor Ivanov <igor.ivanov.va@gmail.com> 8.2.2-1
- Add daemon

* Mon Jan  4 2016 Avner BenHanoch <avnerb@mellanox.com> 7.0.12-1
- Initial Packaging
