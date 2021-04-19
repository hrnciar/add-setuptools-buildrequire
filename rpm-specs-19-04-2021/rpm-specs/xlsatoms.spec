Summary:    X11 atom list utility
Name:       xlsatoms
Version:    1.1.2
Release:    2%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils < 7.5-39

%description
xlsatoms prints the atom database from an X server.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xlsatoms
%{_mandir}/man1/xlsatoms.1*

%changelog
* Fri Apr 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.2-2
- Add Obsoletes for xorg-x11-utils
- Use make_build and other rpm macros

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.1.2-1
- Initial split packaging (#1918034)
