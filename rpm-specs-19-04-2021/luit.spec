Name:       luit
Version:    1.1.1
Release:    2%{?dist}
Summary:    Locale to UTF-8 encoding filter

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

# Upstream but not in any release
Patch01:    0001-config-Add-missing-AC_CONFIG_SRCDIR.patch
Patch02:    0001-Replace-hardcoded-_XOPEN_SOURCE-500-with-AC_USE_SYST.patch

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

# luit requires the encodings from xorg-x11-fonts-misc (rhbz#1046341)
Requires:   xorg-x11-fonts-misc

Obsoletes:  xorg-x11-apps < 7.7-31

%description
luit is a filter that can be run between an arbitrary application and
a UTF-8 terminal emulator such as xterm.  It will convert application
output from the locale's encoding into UTF-8, and convert terminal
input from UTF-8 into the locale's encoding.

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
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.1-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1.1-1
- Split luit out from xorg-x11-apps into a separate package (#1933934)
