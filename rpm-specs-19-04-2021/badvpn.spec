Name:           badvpn
Version:        1.999.130
Release:        2%{?dist}
Summary:        Peer-to-peer VPN solution

License:        BSD
URL:            https://github.com/ambrop72/badvpn
Source0:        https://github.com/ambrop72/badvpn/archive/1.999.130/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  openssl-devel

%description
BadVPN is a layer 2 peer-to-peer VPN solution.


%prep
%autosetup -p1


%build
# Use cmake macro but don't override BUILD_SHARED_LIBS as it breaks the build
%define mycmake %(echo '%{cmake}' | sed 's/-DBUILD_SHARED_LIBS:BOOL=ON//')
%mycmake

%cmake_build


%install
%cmake_install


%files
%license COPYING
%{_bindir}/badvpn-client
%{_bindir}/badvpn-flooder
%{_bindir}/badvpn-ncd
%{_bindir}/badvpn-ncd-request
%{_bindir}/badvpn-server
%{_bindir}/badvpn-tun2socks
%{_bindir}/badvpn-tunctl
%{_bindir}/badvpn-udpgw
%{_mandir}/man7/badvpn.7*
%{_mandir}/man8/badvpn-client.8*
%{_mandir}/man8/badvpn-server.8*
%{_mandir}/man8/badvpn-tun2socks.8*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 29 2020 Pete Walter <pwalter@fedoraproject.org> - 1.999.130-1
- Update to 1.999.130
- Switch to new cmake macros
- Switch to autosetup
- Add gcc BuildRequires
- Remove no longer needed buildroot cleaning in install section

* Sat Oct 25 2014 Pete Walter <pwalter@fedoraproject.com> - 1.999.129-1
- First Fedora build
