# SPDX-License-Identifier: GPL-2.0-only
# Copyright (C) 2019 Mellanox Technologies. All Rights Reserved.
#

Name: rshim
Version: 2.0.4
Release: 5%{?dist}
Summary: User-space driver for Mellanox BlueField SoC

License: GPLv2

URL: https://github.com/mellanox/rshim-user-space
Source0: https://github.com/Mellanox/rshim-user-space/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc, autoconf, automake, make
BuildRequires: pkgconfig(libpci), pkgconfig(libusb-1.0), pkgconfig(fuse)
BuildRequires: systemd
BuildRequires: systemd-rpm-macros

Requires: kmod(cuse.ko)
Suggests: kernel-modules-extra

%description
This is the user-space driver to access the BlueField SoC via the rshim
interface. It provides ways to push boot stream, debug the target or login
via the virtual console or network interface.

%prep
%setup -q -n %{name}-%{version}

%build
./bootstrap.sh
%configure
%make_build

%install
%make_install

%post
%systemd_post rshim.service

%preun
%systemd_preun rshim.service

%postun
%systemd_postun_with_restart rshim.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/rshim
%{_unitdir}/rshim.service
%{_mandir}/man8/rshim.8.gz

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.4-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Liming Sun <lsun@mellanox.com> - 2.0.4-1
- Update .spec file according to review comments
- Fix the 'KillMode' in rshim.service
- Support process termination by SIGTERM
- Fix some compiling warnings and configure issue for FreeBSD
- Fix a read()/write() issue in rshim_pcie.c caused by optimization

* Tue Apr 14 2020 Liming Sun <lsun@mellanox.com> - 2.0.3-1
- Enable pci device during probing
- Map the pci resource0 file instead of /dev/mem
- Add copyright header in bootstrap.sh
- Add 'Requires' tag check in the rpm .spec for kernel-modules-extra
- Fix the 'rshim --version' output

* Thu Apr 09 2020 Liming Sun <lsun@mellanox.com> - 2.0.2-1
- Remove unnecessary dependency in .spec and use make_build
- Add package build for debian/ubuntu
- Fix some format in the man page
- Add check for syslog headers

* Mon Mar 23 2020 Liming Sun <lsun@mellanox.com> - 2.0.1-1
- Rename bfrshim to rshim
- Remove rshim.spec since it's auto-generated from rshim.spec.in
- Fix warnings reported by coverity
- Add rhel/rshim.spec.in for fedora
- Move rshim to sbin and move man page to man8

* Fri Mar 13 2020 Liming Sun <lsun@mellanox.com> - 2.0-1
- Update the spec file according to fedora packaging-guidelines

* Mon Dec 16 2019 Liming Sun <lsun@mellanox.com>
- Initial packaging
