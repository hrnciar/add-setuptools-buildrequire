%global commit 65e34726da66cef7bedf05e46505fb9773838ea0

%if 0%{?fedora} > 33 || 0%{?rhel} > 8
%global link_bin nc
%global link_man nc-man
%else
%global link_bin nmap
%global link_man ncman
%endif

Summary:         OpenBSD netcat to read and write data across connections using TCP or UDP
Name:            netcat
# Version from CVS revision of OpenBSD netcat.c
Version:         1.217
Release:         3%{?dist}
License:         BSD
URL:             https://man.openbsd.org/nc.1
Source0:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/netcat.c
Source1:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/nc.1
Source2:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/atomicio.c
Source3:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/atomicio.h
Source4:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/socks.c
Source5:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/Makefile
# Port peculiarities from OpenBSD to Linux
Patch0:          https://salsa.debian.org/debian/netcat-openbsd/-/raw/841c8ab8a3020e43390358069b15475b923b27bc/debian/patches/port-to-linux-with-libsd.patch
BuildRequires:   make
BuildRequires:   gcc
BuildRequires:   libbsd-devel
BuildRequires:   libretls-devel
%if 0%{?fedora} >= 33 || 0%{?rhel}
Requires(post):  %{_sbindir}/alternatives
Requires(preun): %{_sbindir}/alternatives
Obsoletes:       nc < 1.109.20120711-2
Obsoletes:       nc6 < 1.00-22
Provides:        nc = %{version}-%{release}
Provides:        nc6 = %{version}-%{release}
%endif

%description
The OpenBSD nc (or netcat) utility can be used for just about anything involving
TCP, UDP, or UNIX-domain sockets. It can open TCP connections, send UDP packets,
listen on arbitrary TCP and UDP ports, do port scanning, and deal with both IPv4
and IPv6. Unlike telnet(1), nc scripts nicely, and separates error messages onto
standard error instead of sending them to standard output, as telnet(1) might do
with some.

%prep
%setup -q -T -c
cp -pf %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .
%patch0 -p1 -b .port-to-linux-with-libsd
sed -e '1i #define unveil(path, permissions) 0' \
    -e '1i #define pledge(request, paths) 0' \
    -i netcat.c
sed -e 's/^\(LIBS=.*\)/\1 -ltls/' -i Makefile

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
install -D -p -m 0755 nc $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 nc.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%if 0%{?fedora} > 33 || 0%{?rhel}
touch $RPM_BUILD_ROOT%{_bindir}/nc
touch $RPM_BUILD_ROOT%{_mandir}/man1/nc.1.gz

%post
%{_sbindir}/alternatives --install %{_bindir}/nc %{link_bin} %{_bindir}/%{name} 10 \
  --slave %{_mandir}/man1/nc.1.gz %{link_man} %{_mandir}/man1/%{name}.1.gz

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove %{link_bin} %{_bindir}/%{name}
fi
%endif

%files
%if 0%{?fedora} > 33 || 0%{?rhel}
%ghost %{_bindir}/nc
%ghost %{_mandir}/man1/nc.1.gz
%endif
%{_bindir}/netcat
%{_mandir}/man1/netcat.1*

%changelog
* Wed Mar 17 2021 Robert Scheck <robert@fedoraproject.org> 1.217-3
- Changes to match the Fedora Packaging Guidelines (#1939769 #c1)

* Wed Mar 17 2021 Robert Scheck <robert@fedoraproject.org> 1.217-2
- Changes to match the Fedora Packaging Guidelines (#1939769)

* Sun Mar 07 2021 Robert Scheck <robert@fedoraproject.org> 1.217-1
- Upgrade to 1.217
- Initial spec file for Fedora and Red Hat Enterprise Linux
