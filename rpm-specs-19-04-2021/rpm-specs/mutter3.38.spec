%global gtk3_version 3.19.8
%global glib_version 2.53.2
%global gsettings_desktop_schemas_version 40~alpha
%global json_glib_version 0.12.0
%global libinput_version 1.4
%global pipewire_version 0.3.0
%global mutter_api_version 7

Name:           mutter3.38
Version:        3.38.4
Release:        1%{?dist}
Summary:        Window and compositing manager based on Clutter
License:        GPLv2+

URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/mutter/3.38/mutter-%{version}.tar.xz

# downstream patch to make s390x build pass
Patch0:         0000-Revert-build-Do-not-provide-built-sources-as-libmutt.patch

# downstream work-around for OpenJDK's compliance test
Patch1:         0001-window-actor-Special-case-shaped-Java-windows.patch

# downstream patch to make mutter 3.38 work on GNOME 40:
# backport MR 1416 for gsettings-desktop-schemas >= 40.alpha support
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1416
Patch2:         0002-Adapt-to-settings-moving-to-gsettings-desktop-schema.patch

# downstream patch to fix window shadow rendering glitches since mutter 3.28.4
Patch3:         0003-Fix-glitches-in-gala.patch

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  xorg-x11-server-Xorg
BuildRequires:  xorg-x11-server-Xwayland
BuildRequires:  zenity

BuildRequires:  glib2-devel >= %{glib_version}
BuildRequires:  gnome-desktop3-devel
BuildRequires:  gnome-settings-daemon-devel
BuildRequires:  gobject-introspection-devel >= 1.41.0
BuildRequires:  gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_version}
BuildRequires:  gtk3-devel >= %{gtk3_version}
BuildRequires:  json-glib-devel >= %{json_glib_version}
BuildRequires:  libcanberra-devel
BuildRequires:  libgudev1-devel
BuildRequires:  libinput-devel >= %{libinput_version}
BuildRequires:  libSM-devel
BuildRequires:  libwacom-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXi-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXtst-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  pam-devel
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
BuildRequires:  sysprof-devel
BuildRequires:  systemd-devel
BuildRequires:  upower-devel
BuildRequires:  xkeyboard-config-devel

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3) >= %{pipewire_version}
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-server)

# make conflict with non-compat mutter package explicit
Conflicts:      mutter

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       control-center-filesystem
Requires:       dbus
Requires:       gnome-settings-daemon
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires:       startup-notification
Requires:       zenity

%description
Mutter is a window and compositing manager that displays and manages
your desktop via OpenGL. Mutter combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Mutter can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as GNOME Shell. For
this reason, Mutter is very extensible via plugins, which are used both
to add fancy visual effects and to rework the window management
behaviors to meet the needs of the environment.


%package libs
Summary:        Shared pibraries provided by %{name}

Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       libinput%{?_isa} >= %{libinput_version}
Requires:       pipewire%{?_isa} >= %{pipewire_version}

%description libs
Shared libraries provided by mutter.


%package devel
Summary:        Development package for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# make conflict with non-compat mutter-devel package explicit
Conflicts:      mutter-devel

%description devel
Header files and libraries for developing Mutter plugins. Also includes
utilities for testing Metacity/Mutter themes.


%package  tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}
# make conflict with non-compat mutter-tests package explicit
Conflicts:      mutter-tests

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.


%prep
%autosetup -S git -n mutter-%{version}


%build
%meson -Degl_device=true -Dwayland_eglstream=true -Dxwayland_initfd=disabled
%meson_build


%install
%meson_install

%find_lang mutter


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/mutter.desktop


%ldconfig_scriptlets libs


%files -f mutter.lang
%{_bindir}/mutter
%{_datadir}/applications/mutter.desktop
%{_libexecdir}/mutter-restart-helper
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-*.xml
%{_mandir}/man1/mutter.1*
%{_udevrulesdir}/61-mutter.rules

%files libs
%license COPYING
%doc README.md NEWS

%{_libdir}/libmutter-%{mutter_api_version}.so.*
%dir %{_libdir}/mutter-%{mutter_api_version}
%{_libdir}/mutter-%{mutter_api_version}/libmutter-*.so.*
%{_libdir}/mutter-%{mutter_api_version}/*-%{mutter_api_version}.typelib
%{_libdir}/mutter-%{mutter_api_version}/plugins/

%files devel
%{_includedir}/mutter-%{mutter_api_version}/
%{_libdir}/libmutter-%{mutter_api_version}.so
%{_libdir}/mutter-%{mutter_api_version}/libmutter-*.so
%{_libdir}/mutter-%{mutter_api_version}/*-%{mutter_api_version}.gir
%{_libdir}/pkgconfig/libmutter-%{mutter_api_version}.pc
%{_libdir}/pkgconfig/mutter-{clutter,clutter-x11,cogl,cogl-pango}-%{mutter_api_version}.pc

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/mutter-%{mutter_api_version}/
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/mutter-%{mutter_api_version}/
%dir %{_datadir}/mutter-%{mutter_api_version}
%{_datadir}/mutter-%{mutter_api_version}/tests/


%changelog
* Sat Mar 27 2021 Fabio Valentini <decathorpe@gmail.com> - 3.38.4-1
- Update to version 3.38.4.

* Thu Mar 11 2021 Fabio Valentini <decathorpe@gmail.com> - 3.38.3-4
- Apply patches from gnome-3-38 branch and a fix for shadow rendering glitches.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Fabio Valentini <decathorpe@gmail.com> - 3.38.3-2
- Backport MR 1416 for gsettings-desktop-schemas >= 40.alpha support.

* Sun Jan 17 2021 Fabio Valentini <decathorpe@gmail.com> - 3.38.3-1
- Update to version 3.38.3.

* Thu Jan 07 2021 Fabio Valentini <decathorpe@gmail.com> - 3.38.2-1
- Initial compat package for mutter 3.38.

