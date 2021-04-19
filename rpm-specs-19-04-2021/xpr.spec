Name:       xpr
Version:    1.0.5
Release:    2%{?dist}
Summary:    Convert xwd window dumps to printer formats

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xpr takes as input a window dump file produced by xwd
and formats it for output on various types of printers.

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
%{_bindir}/xdpr
%{_bindir}/xpr
%{_mandir}/man1/xdpr.1*
%{_mandir}/man1/xpr.1*

%changelog
* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.5-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.5-1
- Split xpr out from xorg-x11-apps into a separate package (#1933952)
