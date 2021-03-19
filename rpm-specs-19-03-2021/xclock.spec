Name:       xclock
Version:    1.0.9
Release:    1%{?dist}
Summary:    The classic X Window System clock utility

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps <= 7.7-30

%description
xclock is the classic X Window System clock utility. It displays
the time in analog or digital form, continuously updated at a
frequency which may be specified by the user.

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
%{_bindir}/xclock
%{_mandir}/man1/xclock.1*
%{_datadir}/X11/app-defaults/XClock
%{_datadir}/X11/app-defaults/XClock-color

%changelog
* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.9-1
- Split xclock out from xorg-x11-apps into a separate package (#1933940)
