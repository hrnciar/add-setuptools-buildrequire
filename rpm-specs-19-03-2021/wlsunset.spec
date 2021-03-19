Name:           wlsunset
Version:        0.1.0
Release:        2%{?dist}
Summary:        Day/night gamma adjustments for Sway

License:        MIT
URL:            https://sr.ht/~kennylevinsen/%{name}
Source0:        https://git.sr.ht/~kennylevinsen/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Upstream patch after removing unsupported options
# https://git.sr.ht/~kennylevinsen/wlsunset/commit/fa2bd44253148ae8dc0e7145ffd2d0f04bfac1ab
Patch0:         wlsunset-0.1.0-add-manpage.patch

BuildRequires:  gcc
BuildRequires:  meson >= 0.53
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

%description
Day/night gamma adjustments for Sway and other Wayland compositors
supporting wlr-gamma-control-unstable-v1.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.1.0-1
- Initial import (#1891163)
