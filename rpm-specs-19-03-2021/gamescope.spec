Name:           gamescope
Version:        3.7
Release:        3%{?dist}
Summary:        Micro-compositor for video games on Wayland

License:        BSD
URL:            https://github.com/Plagman/gamescope
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Fedora specific fixes
Patch1001:      1001-meson-Switch-to-using-external-wlroots.patch
Patch1002:      1002-meson-Switch-to-using-external-libliftoff.patch

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(wlroots) >= 0.11.0
BuildRequires:  pkgconfig(liftoff)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  /usr/bin/glslangValidator

Requires:       xorg-x11-server-Xwayland
Recommends:     mesa-dri-drivers
Recommends:     mesa-vulkan-drivers

%description
%{name} is the micro-compositor optimized for running video games on Wayland.

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
%{_bindir}/gamescope


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.7-2
- Rebuild for wlroots 0.12

* Sun Oct  4 15:56:25 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 3.7-1
- Initial packaging
