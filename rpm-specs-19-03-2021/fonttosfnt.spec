Name:       fonttosfnt
Version:    1.2.1
Release:    1%{?dist}
Summary:    Tool to wrap bdf or pcf bitmap fonts in an sfnt wrapper

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  gcc make libtool
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Conflicts:  xorg-x11-font-utils <= 7.5-50

%description
fonttosfnt wraps a set of bdf or pcf bitmap fonts in a sfnt (TrueType or
OpenType) wrapper.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt.1*

%changelog
* Thu Feb 25 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.2.1-1
- Split fonttosfnt out from xorg-x11-font-utils into its own
  package (#1932737)
