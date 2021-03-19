%global commit 53f07e90b7f1da6977143a488dd5cb73a33b233b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20210224
%global _hardened_build 1

Name: odhcp6c
Version: 0
Release: 0.11.%{date}git%{shortcommit}%{?dist}
Summary: Embedded DHCPv6 and RA client
# License is GPLv2 except:
# ./src/md5.c: ISC
# ./src/md5.h: ISC
License: GPLv2 and ISC
URL: https://git.openwrt.org/?p=project/odhcp6c.git
# Source fetched from git:
# git clone https://git.openwrt.org/project/odhcp6c.git
# cd odhcp6c
# git archive --format=tar.gz --prefix=odhcp6c-53f07e90b7f1da6977143a488dd5cb73a33b233b/ 53f07e90b7f1da6977143a488dd5cb73a33b233b > ../odhcp6c-53f07e90b7f1da6977143a488dd5cb73a33b233b.tar.gz
Source0: %{name}-%{commit}.tar.gz
Source1: odhcp6c@.service
BuildRequires: cmake
BuildRequires: gcc
%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
odhcp6c is a minimal DHCPv6 and Router Advertisement client for use in embedded
Linux systems, especially routers. It compiles to only about 35 KB.

%prep
%autosetup -n %{name}-%{commit}

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}
install -D -p -m 0755 odhcp6c-example-script.sh %{buildroot}%{_sysconfdir}/odhcp6c/odhcp6c-example-script.sh
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/odhcp6c@.service

%files
%doc README
%license COPYING
%{_sbindir}/odhcp6c
%dir %{_sysconfdir}/odhcp6c
%{_sysconfdir}/odhcp6c/odhcp6c-example-script.sh
%{_unitdir}/odhcp6c@.service

%changelog
* Wed Feb 24 2021 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.11.20210224git53f07e9
- Update to commit 53f07e9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20201203gita7b2221
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.9.20201203gita7b2221
- Update to commit a7b2221

* Tue Aug 04 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.8.20200416gitf575351
- Use cmake_build and cmake_install macros. Fix RHBZ#1865137

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20200416gitf575351
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200416gitf575351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.5.20200416gitf575351
- Install preserving time stamps
- Own /etc/odhcp6c dir

* Tue Apr 21 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.4.20200416gitf575351
- Install in multi-user.target
- Update description

* Sat Apr 18 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.3.20200416gitf575351
- Harden service

* Sat Apr 18 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.2.20200416gitf575351
- Order service unit after network-pre.target
- Fix build in epel

* Thu Apr 16 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.1.20200416gitf575351
- Initial release
