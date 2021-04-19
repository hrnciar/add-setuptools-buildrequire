Name:       viewres
Version:    1.0.5
Release:    2%{?dist}
Summary:    X11 utility to display the widget hierarchy

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

Obsoletes:  xorg-x11-resutils < 7.7-9

%description
viewres displays a tree showing the widget class hierarchy of the Athena
Widget Set (libXaw).

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
%{_datadir}/X11/app-defaults/Viewres
%{_datadir}/X11/app-defaults/Viewres-color

%changelog
* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.5-2
- Fix Obsoletes line to actually obsolete the -8 resutils

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.5-1
- Split viewres out from xorg-x11-resutils into a separate package (#1933955)
