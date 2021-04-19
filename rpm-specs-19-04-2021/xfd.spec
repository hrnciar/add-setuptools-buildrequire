Name:       xfd
Version:    1.1.2
Release:    2%{?dist}
Summary:    Display characters of a font

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
Display all the characters in a font using either the X11 core protocol or
libXft2.

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
%{_bindir}/xfd
%{_mandir}/man1/xfd.1*
%{_datadir}/X11/app-defaults/Xfd

%changelog
* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.2-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-1
- Split xfd out from xorg-x11-apps into a separate package (#1933944)
