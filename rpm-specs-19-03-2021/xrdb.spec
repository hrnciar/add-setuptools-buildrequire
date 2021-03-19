Name:       xrdb
Version:    1.1.1
Release:    1%{?dist}
Summary:    X server resource database utility

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils <= 7.7-39

%description
xrdb is used to get or set the contents of the RESOURCE_MANAGER property on
the root window of screen 0, or the SCREEN_RESOURCES property on the
root window of any or all screens, or everything combined.

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
* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1.1-1
- Split xrdb out from xorg-x11-server-utils into a separate package
  (#1934392)

