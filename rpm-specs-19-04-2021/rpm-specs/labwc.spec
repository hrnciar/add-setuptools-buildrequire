Name: labwc
Version: 0.1.0
Release: 3%{?dist}
Summary: Openbox alternative for Wayland

License: GPLv2
URL: https://github.com/johanmalm/labwc
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop

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
# https://github.com/johanmalm/labwc#6-integrate
Recommends: bemenu%{?_isa}      %dnl # Launchers
Suggests: fuzzel%{?_isa}        %dnl # Launchers
Suggests: grim%{?_isa}          %dnl # Screen-shooter
Suggests: kanshi%{?_isa}        %dnl # Output managers
Suggests: swaybg%{?_isa}        %dnl # Background image
Suggests: waybar%{?_isa}        %dnl # Panel
Suggests: wlr-randr%{?_isa}     %dnl # Output managers
Suggests: wofi%{?_isa}          %dnl # Launchers

Suggests: wdisplays%{?_isa}     %dnl # GUI display configurator for wlroots compositors
  

%description
Labwc is a wlroots-based stacking compositor for Wayland.

It has the following aims:

  * Be light-weight, small and fast.
  * Use openbox-3.4 specification for configuration and themes.
  * Keep feature set small (ca 40% of openbox).
  * Where practicable, use clients for wall-paper, panel, screenshots, and so
    on.
  * Stay in keeping with wlroots and sway in terms of approach and coding
    style.


%prep
%autosetup -p1


%build
%meson \
    -Dxwayland=enabled
%meson_build


%install
%meson_install
install -Dpm0644 %{SOURCE1} -t %{buildroot}%{_datadir}/wayland-sessions/


%files
%license LICENSE
%doc README.md NEWS.md
%{_bindir}/%{name}
%{_datadir}/wayland-sessions/%{name}.desktop
%{_mandir}/man{1,5}/*.{1,5}*


%changelog
* Wed Mar 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-3
- build: Convert Recommends deps into Suggests

* Wed Mar 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-2
- feat: Add session file for DM

* Sun Mar 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1
- Initial package
