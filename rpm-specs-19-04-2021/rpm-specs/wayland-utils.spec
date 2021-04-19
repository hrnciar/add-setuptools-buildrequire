Name:           wayland-utils
Version:        1.0.0
Release:        2%{?dist}
Summary:        Wayland utilities

License:        MIT
URL:            https://wayland.freedesktop.org/
Source0:        https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-scanner)


%description
wayland-utils contains wayland-info, a standalone version of weston-info,
a utility for displaying information about the Wayland protocols supported
by the Wayland compositor.
wayland-info also provides additional information for a subset of Wayland
protocols it knows about, namely Linux DMABUF, presentation time, tablet and
XDG output protocols.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wayland-info
%{_mandir}/man1/wayland-info.1*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug  3 2020 Olivier Fourdan <ofourdan@redhat.com> - 1.0.0-1
- Initial package
