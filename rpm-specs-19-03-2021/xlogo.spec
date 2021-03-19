Name:       xlogo
Version:    1.0.4
Release:    1%{?dist}
Summary:    Display the X11 logo

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps <= 7.7-30

%description
xlogo displays a magnified snapshot of a portion of an X11 screen.

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
%{_bindir}/xlogo
%{_mandir}/man1/xlogo.1*
%{_datadir}/X11/app-defaults/XLogo
%{_datadir}/X11/app-defaults/XLogo-color

%changelog
* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.4-1
- Split xlogo out from xorg-x11-apps into a separate package (#1933949)
