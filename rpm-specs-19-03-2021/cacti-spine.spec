Name: cacti-spine
Version: 1.2.16
Release: 2%{?dist}
Summary: Threaded poller for Cacti written in C
License: LGPLv2+
URL: https://cacti.net
Source0: https://www.cacti.net/downloads/spine/%{name}-%{version}.tar.gz

BuildRequires: gcc
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: mariadb-connector-c-devel
%else
BuildRequires: mysql-devel
%endif
BuildRequires: net-snmp-devel
BuildRequires: help2man
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: pkgconfig
BuildRequires: make

Requires: cacti = %{version}
Requires: rrdtool

%description
Spine is a supplemental poller for Cacti that makes use of pthreads to achieve
excellent performance.

%prep
%autosetup

%build
autoreconf -fiv

%configure
%make_build

%install
%make_install
%{__mv} %{buildroot}/%{_sysconfdir}/spine.conf.dist %{buildroot}/%{_sysconfdir}/spine.conf

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/spine
%config(noreplace) %{_sysconfdir}/spine.conf
%{_mandir}/man1/spine.1.*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Morten Stevens <mstevens@fedoraproject.org> - 1.2.16-1
- Update to 1.2.16

* Tue Nov 03 2020 Morten Stevens <mstevens@fedoraproject.org> - 1.2.15-1
- Update to 1.2.15

* Thu Aug 27 2020 Josef Řídký <jridky@redhat.com> - 1.2.14-2
- Rebuilt for new net-snmp release

* Thu Aug 06 2020 Morten Stevens <mstevens@fedoraproject.org> - 1.2.14-1
- Update to 1.2.14

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Morten Stevens <mstevens@fedoraproject.org> - 1.2.13-1
- Update to 1.2.13

* Wed May 27 2020 Morten Stevens <mstevens@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12

* Tue Apr 07 2020 Morten Stevens <mstevens@fedoraproject.org> - 1.2.11-1
- Update to 1.2.11

* Mon Mar 02 2020 Morten Stevens <mstevens@fedoraproject.org> - 1.2.10-1
- Update to 1.2.10

* Mon Feb 10 2020 Morten Stevens <mstevens@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8

* Sat Nov 30 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7

* Tue Sep 03 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6

* Sat Aug 03 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.5-3
- Fix building on RHEL8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Sat Jun 08 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Sun Mar 31 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Mon Feb 25 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sun Jan 06 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.0-2
- Use spine.conf as default

* Thu Jan 03 2019 Morten Stevens <mstevens@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Fri Nov 09 2018 Morten Stevens <mstevens@fedoraproject.org> - 1.1.38-2
- Added RPM macro to fix building on RHEL

* Tue Nov 06 2018 Morten Stevens <mstevens@fedoraproject.org> - 1.1.38-1
- Initial cacti-spine release for Fedora
