Summary:    X video extension query utility
Name:       xvinfo
Version:    1.1.3
Release:    2%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xv)

Obsoletes: xorg-x11-utils < 7.5-39

%description
xvinfo displays information about the XVideo extension on an X server.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc README
%license COPYING
%{_bindir}/xvinfo
%{_mandir}/man1/xvinfo.1*

%changelog
* Fri Apr 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.3-2
- Add Obsoletes for xorg-x11-utils
- Use the make_build RPM macro

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.1.3-1
- Initial split packaging (#1918040)

