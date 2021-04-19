Name:       appres
Version:    1.0.5
Release:    2%{?dist}
Summary:    X11 utility to print application resources

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes: xorg-x11-resutils < 7.7-9

%description
The appres program prints the resources seen by an application (or
sub-hierarchy of an application) with the specified class and instance
names. It can be used to determine which resources a particular
program will load.

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
* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.5-2
- Fix Obsoletes line to actually obsolete the -8 resutils

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.5-1
- Split appres out from xorg-x11-resutils into a separate package (#1934344)
