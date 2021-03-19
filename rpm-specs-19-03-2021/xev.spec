Summary:    X Event utility
Name:       xev
Version:    1.2.4
Release:    1%{?dist}
License:    MIT
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/xev-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr) >= 1.2

Obsoletes: xorg-x11-utils <= 7.5-38

%description
xev displays the X11 protocol events sent to a given window.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/xev
%{_mandir}/man1/xev.1*

%changelog
* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.2.4-1
- Initial split packaging

