Name:           gamescope
Version:        3.7.1
Release:        1%{?dist}
Summary:        Micro-compositor for video games on Wayland

License:        BSD
URL:            https://github.com/Plagman/gamescope
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# wlroots 0.13.0 compatibility patches:
# https://github.com/Plagman/gamescope/commit/fbc6bd0c0882c5c60232fe68e315799566adb476
# https://github.com/Plagman/gamescope/pull/150
Patch0:         gamescope-3.7.1-wlroots-0.13.0-compat.patch

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(wlroots) >= 0.13.0
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
* Wed Apr 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1
- Add patch for wlroots 0.13.0 API changes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.7-2
- Rebuild for wlroots 0.12

* Sun Oct  4 15:56:25 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 3.7-1
- Initial packaging
