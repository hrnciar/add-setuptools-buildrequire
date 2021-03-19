Name:       xclipboard
Version:    1.1.3
Release:    1%{?dist}
Summary:    Utility to collect and display text selections

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps <= 7.7-30

%description
xclipboard is used to collect and display text selections that are
sent to the CLIPBOARD by other clients.  It is typically used to save
CLIPBOARD selections for later use.  It stores each CLIPBOARD
selection as a separate string, each of which can be selected.

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
%{_bindir}/xclipboard
%{_bindir}/xcutsel
%{_mandir}/man1/xclipboard.1*
%{_mandir}/man1/xcutsel.1*
%{_datadir}/X11/app-defaults/XClipboard

%changelog
* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1.3-1
- Split xclipboard out from xorg-x11-apps into a separate package
  (#1933939)
