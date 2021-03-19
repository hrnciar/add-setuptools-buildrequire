Summary:    X11 display information utility
Name:       xdpyinfo
Version:    1.3.2
Release:    1%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/xdpyinfo-%{version}.tar.bz2

BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(dmx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xrandr) >= 1.2
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86dga)
BuildRequires:  pkgconfig(xxf86vm)

Obsoletes: xorg-x11-utils <= 7.5-38

%description
xdpyinfo prints basic diagnostic information about a given X server.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/xdpyinfo
%{_mandir}/man1/xdpyinfo.1*

%changelog
* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.3.2-1
- Initial split packaging.

