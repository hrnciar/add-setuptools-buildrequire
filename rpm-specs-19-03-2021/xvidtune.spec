Name:       xvidtune
Version:    1.0.3
Release:    1%{?dist}
Summary:    Video mode tuner for Xorg

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps <= 7.7-30

%description
xvidtune is a client interface to the X server video mode extension
(XFree86-VidModeExtension).

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
%{_bindir}/xvidtune
%{_mandir}/man1/xvidtune.1*
%{_datadir}/X11/app-defaults/Xvidtune

%changelog
* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.3-1
- Split xvidtune out from xorg-x11-apps into a separate package (#1933954)
