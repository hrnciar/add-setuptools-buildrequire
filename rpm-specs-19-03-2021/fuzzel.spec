Name:           fuzzel
Version:        1.5.1
Release:        2%{?dist}
Summary:        Application launcher for wlroots based Wayland compositors

License:        MIT
URL:            https://codeberg.org/dnkl/fuzzel
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.53
BuildRequires:  tllist-static
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fcft) >= 2.0.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
Fuzzel is a Wayland-native application launcher, similar to rofi's drun mode.

Features:
- Wayland native
- Rofi drun-like mode of operation
- dmenu mode where newline separated entries are read from stdin
- Emacs key bindings
- Icons!
- Remembers frequently launched applications


%prep
%autosetup -n %{name} -p1


%build
%meson
%meson_build


%install
%meson_install
# Will be installed to correct location with rpm macros
rm %{buildroot}%{_docdir}/%{name}/LICENSE


%check
%meson_test


%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Mon Mar 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.1-2
- style: Trivial changes for pushing into official repo

* Tue Feb 02 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.1-0.1
- Update to 1.5.1

* Fri Jan 29 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.0-0.1
- Update to 1.5.0

* Sat Jan 09 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.4.2-0.1
- Initial package
