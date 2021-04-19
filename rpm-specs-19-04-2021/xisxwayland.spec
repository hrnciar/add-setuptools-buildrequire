Name:       xisxwayland
Version:    1
Release:    1%{?dist}
Summary:    Tool to check if the X server is XWayland

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  meson gcc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
xisxwayland is a tool to be used within shell scripts to determine whether
the X server in use is Xwayland. It exits with status 0 if the server is an
Xwayland server and 1 otherwise.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/xisxwayland
%{_mandir}/man1/xisxwayland.1*

%changelog
* Thu Feb 25 2021 Peter Hutterer <peter.hutterer@redhat.com> 1-1
- Split xisxwayland out from xorg-x11-server-utils into its own package
  (#1932760)
