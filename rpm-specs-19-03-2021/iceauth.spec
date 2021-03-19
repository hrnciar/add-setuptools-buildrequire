Name:       iceauth
Version:    1.0.8
Release:    1%{?dist}
Summary:    Display the authorization information used in connecting with ICE

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils <= 7.7-39

%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE. It operates very much
like the xauth program for X11 connection authentication records.

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.8-1
- Split iceauth out from xorg-x11-server-utils into a separate package
  (#1934382)

