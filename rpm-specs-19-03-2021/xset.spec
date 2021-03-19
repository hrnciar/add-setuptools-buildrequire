Name:       xset
Version:    1.2.4
Release:    1%{?dist}
Summary:    User preference utility for X

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils <= 7.7-39

%description
This program is used to set various user preference options of the X server,
including bell volume, dpms features, font paths and some settings related
to the pointer.

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
* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.2.4-1
- Split xset out from xorg-x11-server-utils into a separate package
  (#1934394)

