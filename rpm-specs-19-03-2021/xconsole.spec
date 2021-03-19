Name:       xconsole
Version:    1.0.7
Release:    1%{?dist}
Summary:    Display messages in an X11 window

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
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps <= 7.7-30

%description
xconsole displays in a X11 window the messages which are usually sent
to /dev/console

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
%{_bindir}/xconsole
%{_mandir}/man1/xconsole.1*
%{_datadir}/X11/app-defaults/XConsole

%changelog
* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.7-1
- Split xconsole out from xorg-x11-apps into a separate package (#1933941)
