Name:       xfontsel
Version:    1.0.6
Release:    1%{?dist}
Summary:    Tool to list X11 core protocol fonts

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps <= 7.7-30

%description
xfontsel provides a simple way to display the X11 core protocol fonts known
to your X server, examine samples of each, and retrieve the X Logical Font
Description ("XLFD") full name for a font.

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
%{_bindir}/xfontsel
%{_mandir}/man1/xfontsel.1*
%{_datadir}/X11/app-defaults/XFontSel

%changelog
* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.6-1
- Split xfontsel out from xorg-x11-apps into a separate package (#1933945)
