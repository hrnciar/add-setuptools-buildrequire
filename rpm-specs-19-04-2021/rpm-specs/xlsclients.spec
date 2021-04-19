Summary:    X client list utility
Name:       xlsclients
Version:    1.1.4
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
xlsclients lists the names of the clients currently connected to an X server.

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
%{_bindir}/xlsclients
%{_mandir}/man1/xlsclients.1*

%changelog
* Sat Apr 17 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1.4-2
- Add Obsoletes for xorg-x11-utils
- Use make_build and other rpm macros

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.1.4-1
- Initial split packaging (#1918035)

