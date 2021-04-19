Summary:    X window info utility
Name:       xwininfo
Version:    1.1.5
Release:    2%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils < 7.5-39

%description
xwininfo prints information about an X11 window.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/xwininfo
%{_mandir}/man1/xwininfo.1*

%changelog
* Fri Apr 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.5-2
- Bump Obsoletes for xorg-x11-utils
- Use the make_build rpm macro

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.1.5-1
- Initial split packaging.

