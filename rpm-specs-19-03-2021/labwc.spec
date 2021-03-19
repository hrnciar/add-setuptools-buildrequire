Name: labwc
Version: 0.1.0
Release: 1%{?dist}
Summary: Openbox alternative for Wayland

License: GPLv2
URL: https://github.com/johanmalm/labwc
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson >= 0.53.0
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libinput) >= 1.14
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wlroots) >= 0.11.0
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)

# Upstream recommendations
# https://github.com/johanmalm/labwc#5-integrate
Recommends: bemenu%{?_isa}  %dnl # Launcher
Recommends: grim%{?_isa}    %dnl # Screenshoter
Recommends: swaybg%{?_isa}  %dnl # Background image
Recommends: waybar%{?_isa}  %dnl # Panel
Suggests: wofi%{?_isa}      %dnl # Launcher

Recommends: wdisplays%{?_isa}   %dnl # GUI display configurator for wlroots
                                %dnl # compositors
  

%description
Labwc is a wlroots-based stacking compositor for Wayland.

It has the following aims:

- Be light-weight, small and fast
- Have the look and feel of openbox albeit with a smaller feature set
- Where practicable, use clients to show wall-paper, take screenshots, and so
  on
- Stay in keeping with wlroots and sway in terms of approach and coding style


%prep
%autosetup -p1


%build
%meson \
    -Dxwayland=enabled
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md NEWS.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1.*
%{_mandir}/man5/*.5.*


%changelog
* Sun Mar 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1
- Initial package
