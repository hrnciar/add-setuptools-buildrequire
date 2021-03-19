Summary:    X window info utility
Name:       xwininfo
Version:    1.1.5
Release:    1%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/xwininfo-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils <= 7.5-38

%description
xwininfo prints information about an X11 window.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/xwininfo
%{_mandir}/man1/xwininfo.1*

%changelog
* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.1.5-1
- Initial split packaging.

