Name:       xgamma
Version:    1.0.6
Release:    2%{?dist}
Summary:    X utility to query and alter the gamma correction of a monitor

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
xgamma allows X users to query and alter the gamma correction of a
monitor via the X video mode extension (XFree86-VidModeExtension).

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
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.6-2
- Fix Obsoletes line to actually obsolete the -39 server-utils (#1932754)

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.6-1
- Split xgamma out from xorg-x11-server-utils into a separate package
  (#1934385)

