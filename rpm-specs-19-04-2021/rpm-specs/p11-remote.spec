%global enginesdir %(pkg-config --variable=enginesdir libcrypto)

Name:           p11-remote
Version:        0.3
Release:        10%{?dist}
Summary:        Remoting of PKCS#11 modules across sessions

License:        BSD
URL:            https://github.com/NetworkManager/%{name}
Source0:        https://github.com/NetworkManager/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Requires:       openssl-libs
Requires:       p11-kit-server

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(systemd)

%description
This is a PKCS#11 engine for OpenSSL based on p11-kit capable of utilizing the
p11-kit remoting capabilities. It also includes an on-demand activated UNIX
socket based p11-kit server for user sessions.

This is in particular useful to use a GNOME Keyring software HSM with daemons
running outside the user session, such as the NetworkManager managed VPN
daemons or wpa_supplicant.


%prep
%setup -q


%build
%configure
%make_build


%install
%make_install

%post
%systemd_user_post p11-kit-remote.socket

%preun
%systemd_user_preun p11-kit-remote.socket

%triggerun -- %{name} < 0.3-7
# This is for upgrades from previous versions which had a static symlink.
# The %%post scriptlet above only does anything on initial package installation.
# Remove before F33.
systemctl --no-reload preset --global p11-kit-remote.socket >/dev/null 2>&1 || :

%files
%{_userunitdir}/p11-kit-remote.socket
%{_userunitdir}/p11-kit-remote@.service
%exclude %{_userunitdir}/sockets.target.wants
%{_mandir}/man1/libp11-kit-engine.so.1*
%{_mandir}/man5/p11-kit-remote.socket.5*
%{_mandir}/man5/p11-kit-remote@.service.5*
%{enginesdir}/libp11-kit-engine.so
%{_libdir}/libp11-kit-engine.so
%exclude %{enginesdir}/libp11-kit-engine.la


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.3-1
- Update to version 0.3

* Sun Apr 09 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.2-1
- Initial packaging
