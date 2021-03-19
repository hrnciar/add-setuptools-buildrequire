Name:       xstdcmap
Version:    1.0.4
Release:    1%{?dist}
Summary:    Utility to define standard colormap properties

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils <= 7.7-39

%description
The xstdcmap utility can be used to selectively define standard colormap
properties.  It is intended to be run from a user's X startup script to
create standard colormap definitions in order to facilitate sharing of
scarce colormap resources among clients using PseudoColor visuals.

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
* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.4-1
- Split xstdcmap out from xorg-x11-server-utils into a separate package
  (#1934396)

