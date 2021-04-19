Summary:    X font list utility
Name:       xlsfonts
Version:    1.0.6
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
xlsfonts lists the fonts available on an X server.

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
%{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1*

%changelog
* Fri Apr 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.6-2
- Add Obsoletes for xorg-x11-utils
- Use the make_build rpm macro

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.0.6-1
- Initial split packaging (#1918037)

