Name:       xinput
Version:    1.6.3
Release:    1%{?dist}
Summary:    Utility to query X Input devices

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils <= 7.7-39

%description
xinput is a commandline utility to query and configure X11 X Input Extension
devices. It is commonly used to change driver properties at runtime.

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
* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.6.3-1
- Split xinput out from xorg-x11-server-utils into a separate package
  (#1934387)

