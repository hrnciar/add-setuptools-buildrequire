Name:       xrandr
Version:    1.5.1
Release:    1%{?dist}
Summary:    Commandline utility to change output properties

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils <= 7.7-39

%description
xrandr is a commandline utility to set the size, orientation and/or
reflection of the outputs for an X screen. It can also set the screen size
and turn outputs on and off..

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

# "needs more nickle bindings" since 2009...
rm -f $RPM_BUILD_ROOT%{_bindir}/xkeystone

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.5.1-1
- Split xrandr out from xorg-x11-server-utils into a separate package
  (#1934391)

