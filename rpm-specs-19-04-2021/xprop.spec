Summary:    X property display utility
Name:       xprop
Version:    1.2.3
Release:    2%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils < 7.5-39

%description
The xprop utility is for displaying window and font properties in an X server.

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
%{_bindir}/xprop
%{_mandir}/man1/xprop.1*

%changelog
* Fri Apr 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.3-2
- Add Obsoletes for xorg-x11-utils
- Use the make_build RPM macro

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.2.3-1
- Initial split packaging (#1918038)

