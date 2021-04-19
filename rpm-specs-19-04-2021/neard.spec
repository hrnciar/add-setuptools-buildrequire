Name:          neard
Version:       0.16
Release:       11%{?dist}
Summary:       Near Field Communication (NFC) manager
License:       GPLv2
URL:           https://01.org/linux-nfc/
Source0:       https://www.kernel.org/pub/linux/network/nfc/%{name}-%{version}.tar.xz

BuildRequires: dbus-devel
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libnl3-devel
BuildRequires: make
BuildRequires: systemd

%description
neard is an NFC (Near Field Communication) daemon for managing NFC operations 
on devices running the Linux operating system. It relies on the Linux kernel NFC 
socket and generic netlink families, and is a fully modular system that can be 
extended through plug-ins.

It supports all 4 NFC tag types reading and writing, along with NFC LLCP 
(peer to peer mode) in both target and initiator modes.

%package tools
Summary: Tools for use with neard

%description tools
These are tools to use neard.

%package devel
Summary: Development package for neard
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with neard.

%prep
%autosetup -p1

%build
%configure --enable-tools
%{make_build} V=1

%install
%{make_install}

rm -f %{buildroot}/usr/include/version.h

%check
make check %{?_smp_mflags} V=1

%ldconfig_scriptlets

%files
%license COPYING
%{_sysconfdir}/dbus-1/system.d/org.neard.conf
%{_unitdir}/neard.service
%{_libexecdir}/nfc/neard
%{_mandir}/man5/neard.conf.5*
%{_mandir}/man8/neard.8*

%files tools
%{_bindir}/nciattach
%{_bindir}/nfctool
%{_mandir}/man1/nfctool.1*

%files devel
%doc doc/*txt
%{_includedir}/near/
%{_libdir}/pkgconfig/neard.pc

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Dave Olsthoorn <daveo@fedoraproject.org> - 0.16-10
- Enable tools

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.16-1
- Initial package
