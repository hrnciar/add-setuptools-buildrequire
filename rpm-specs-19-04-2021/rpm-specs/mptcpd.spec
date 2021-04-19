Summary: Multipath TCP daemon
Name: mptcpd
Version: 0.6
Release: 1%{?dist}
License: BSD
URL: https://multipath-tcp.org
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: libell-devel
BuildRequires: systemd-units
BuildRequires: systemd-rpm-macros

Source0: https://github.com/intel/mptcpd/archive/v%{version}/%{name}-%{version}.tar.gz

%description
The Multipath TCP Daemon is a daemon for Linux based operating systems that
performs multipath TCP path management related operations in user space. It
interacts with the Linux kernel through a generic netlink connection to track
per-connection information (e.g. available remote addresses), available network
interfaces, request new MPTCP subflows, handle requests for subflows, etc.

%package devel
Summary: MPTCP path manager header files
Group: Development/Libraries
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}
License: BSD

%description devel
Header files for adding MPTCP path manager support to applications

%prep
%autosetup -p1

%build
autoreconf --install --symlink --force
%configure --enable-debug=info
%make_build V=1

%install
install -d %{buildroot}/%{_libexecdir}
install -d %{buildroot}/%{_mandir}/man8
install -d %{buildroot}/%{_sysconfdir}/%{name}
install -d %{buildroot}/%{_unitdir}
install -d %{buildroot}/%{_libdir}/%{name}
install -d %{buildroot}/%{_includedir}/%{name}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%systemd_postun mptcp.service

%files
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%dir %{_sysconfdir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/libmptcpd.so.*
%{_libdir}/%{name}/*.so
%{_libexecdir}/%{name}
%{_unitdir}/mptcp.service
%{_mandir}/man8/%{name}.8.gz
# todo add %doc
%license COPYING

%files devel
%doc COPYING
%dir %{_includedir}/%{name}
%{_libdir}/*.so
%{_includedir}/mptcpd/*.h
%{_libdir}/pkgconfig/mptcpd.pc

%changelog
* Tue Feb 23 2021 Davide Caratti <dcaratti@redhat.com> - 0.6-1
- update to version 0.6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Davide Caratti <dcaratti@redhat.com> - 0.5.1-1
- initial build
