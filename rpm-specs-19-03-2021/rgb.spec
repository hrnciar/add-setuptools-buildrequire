Name:       rgb
Version:    1.0.6
Release:    40%{?dist}
Summary:    X color name database

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils <= 7.7-39

%description
This package includes both the list mapping X color names to RGB values
(rgb.txt) and, if configured to use a database for color lookup, the
rgb program to convert the text file into the binary database format.

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%{_bindir}/showrgb
%{_datadir}/X11/rgb.txt
%{_mandir}/man1/showrgb.1*

%changelog
* Fri Mar 05 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.6-40
- Bump Release to 40 to ensure a working update path. rgb was a separate
  package in xorg-x11-server-utils (not just a Provides) and took the
  Release from that.

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.6-1
- Split rgb out from xorg-x11-server-utils into a separate package (#1934383)

