Name:       listres
Version:    1.0.4
Release:    1%{?dist}
Summary:    X11 utility to list application resources

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-resutils <= 7.7-8

%description
The listres program generates a list of X resources for a widget in an X
client written using a toolkit based on libXt.

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules --disable-xprint
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.4-1
- Split listres out from xorg-x11-resutils into a separate package (#1934348)
