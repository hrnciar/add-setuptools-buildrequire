Name:           nsca-ng
Version:        1.6
Release:        3%{?dist}
Summary:        Add-on for transferring check results (and other commands) to Nagios or Icinga

License:        BSD
URL:            https://nsca-ng.org
Source:         https://github.com/weiss/nsca-ng/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
# Common
BuildRequires:  openssl-devel
BuildRequires:  libev-devel
BuildRequires:  libbsd-devel

%description
%{summary}.

%package client
Summary:        %{SUMMARY} (client)
Conflicts:      nsca-client

%description client
%{summary}.

%package server
Summary:        %{SUMMARY} (server)
BuildRequires:  libconfuse-devel
BuildRequires:  systemd-devel
Requires:       user(nagios)

%description server
%{summary}.

%prep
%autosetup
# Bundled stuff
sed -i -e "/lib\/ev\/libev.m4/d" m4/ev.m4
sed -r -i -e "/lib\/(ev|pidfile)\/Makefile/d" configure.ac
sed -r -i -e "/^MAYBE_(EV|PIDFILE)/d" lib/Makefile.am
rm -vr lib/{pidfile,ev}

%build
autoreconf -vfi
%configure \
  --enable-client \
  --enable-server \
  --with-ev=external \
  %{nil}
%make_build

%install
%make_install
install -Dpm0644 -t %{buildroot}%{_unitdir} etc/nsca-ng.{service,socket}

%check
%make_build check

%files client
%license COPYING
%doc README NEWS PROTOCOL
%{_sbindir}/send_nsca
%{_mandir}/man8/send_nsca.8*
%config(noreplace) %{_sysconfdir}/send_nsca.cfg
%{_mandir}/man5/send_nsca.cfg.5*

%files server
%license COPYING
%doc README NEWS PROTOCOL
%{_unitdir}/nsca-ng.{socket,service}
%{_sbindir}/nsca-ng
%{_mandir}/man8/nsca-ng.8*
%attr(0640,nagios,nagios) %config(noreplace) %{_sysconfdir}/nsca-ng.cfg
%{_mandir}/man5/nsca-ng.cfg.5*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.6-2
- Make sure that nsca-ng.cfg is owned by appropriate user

* Wed Dec 16 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.6-1
- Initial package
