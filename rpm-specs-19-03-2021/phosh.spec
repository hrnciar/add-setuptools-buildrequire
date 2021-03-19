%global gvc_commit ae1a34aafce7026b8c0f65a43c9192d756fe1057

Name:		phosh
Version:	0.9.0
Release:	1%{?dist}
Summary:	Graphical shell for mobile devices

License:	GPLv3+
URL:		https://source.puri.sm/Librem5/phosh
Source0:	https://source.puri.sm/Librem5/phosh/-/archive/v%{version}/%{name}-v%{version}.tar.gz

# This library doesn't compile into a DSO or ever has had any releases.
# Other projects, such as gnome-shell use it this way.
Source1:	https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/%{gvc_commit}/libgnome-volume-control-%{gvc_commit}.tar.gz

Source2:	phosh

Patch0:		0001-patch-home-for-wlroots12.patch

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	pam-devel
BuildRequires:	dbus-daemon
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gcr-3) >= 3.7.5
BuildRequires:	pkgconfig(gio-2.0) >= 2.58
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.58
BuildRequires:	pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:	pkgconfig(gnome-desktop-3.0) >= 3.26
BuildRequires:	pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:	pkgconfig(gtk+-wayland-3.0) >= 3.22
BuildRequires:	pkgconfig(libhandy-1) >= 1.1.90
BuildRequires:	pkgconfig(libnm) >= 1.14
BuildRequires:	pkgconfig(libpulse) >= 2.0
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libsystemd) >= 241
BuildRequires:	pkgconfig(polkit-agent-1) >= 0.105
BuildRequires:	pkgconfig(upower-glib) >= 0.99.1
BuildRequires:	pkgconfig(wayland-client) >= 1.14
BuildRequires:	pkgconfig(wayland-protocols) >= 1.12
BuildRequires:	pkgconfig(libfeedback-0.0)
BuildRequires:	feedbackd-devel
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	at-spi2-core
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	/usr/bin/xauth
BuildRequires:	desktop-file-utils
BuildRequires:	git-core
BuildRequires:	systemd-rpm-macros

Requires:	phoc
Requires:	iio-sensor-proxy
Requires:	gnome-session
Requires:	lato-fonts
Requires:	hicolor-icon-theme


%description
Phosh is a simple shell for Wayland compositors speaking the layer-surface
protocol. It currently supports

* a lockscreen
* brightness control and nighlight
* the gcr system-prompter interface
* acting as a polkit auth agent
* enough of org.gnome.Mutter.DisplayConfig to make gnome-settings-daemon happy
* a homebutton that toggles a simple favorites menu
* status icons for battery, wwan and wifi


%prep
%setup -a1 -q -n %{name}-v%{version}
%patch0 -p1

rmdir subprojects/gvc
ln -s ../libgnome-volume-control-%{gvc_commit} subprojects/gvc


%build
%meson -Dphoc_tests=disabled
%meson_build


%install
mkdir -p $RPM_BUILD_ROOT/etc/pam.d/
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/
%meson_install
%find_lang %{name}


%{__install} -Dpm 0644 data/phosh.service %{buildroot}%{_unitdir}/phosh.service


%check
desktop-file-validate \
%{buildroot}/%{_datadir}/applications/sm.puri.Phosh.desktop
LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test
SH


%files -f %{name}.lang
%{_bindir}/phosh
%{_bindir}/phosh-osk-stub
%{_libexecdir}/phosh
%{_datadir}/applications/sm.puri.Phosh.desktop
%{_datadir}/glib-2.0/schemas/sm.puri.phosh.gschema.xml
%{_datadir}/glib-2.0/schemas/sm.puri.phosh.enums.xml
%{_datadir}/glib-2.0/schemas/00_sm.puri.Phosh.gschema.override
%{_datadir}/gnome-session/sessions/phosh.session
%{_datadir}/applications/sm.puri.OSK0.desktop
%{_datadir}/wayland-sessions/phosh.desktop
%{_datadir}/phosh
%{_sysconfdir}/pam.d/phosh
%{_unitdir}/phosh.service
%doc README.md
%license COPYING


%changelog
* Wed Mar 03 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0
- Revert GVC to downstream subproject version

* Wed Feb 17 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.1-2
- Patch for glib2 > 2.67.1

* Fri Feb 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.1-1
- Update to phosh 0.8.1
- Update gvc to latest.

* Wed Feb 03 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.0-3
- Update phosh pam file to fix gnome keyring

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.0-1
- Update to phosh 0.8.0

* Fri Dec 18 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.7.1-1
- Update to phosh 0.7.1

* Thu Dec 10 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.7.0-1
- Update to phosh 0.7.0

* Fri Nov 20 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0-2
- Patch for wlroots 0.12

* Sun Nov 15 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0-1
- Update to phosh 0.6.0

* Wed Nov 04 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.1-1
- Update to phosh 0.5.1

* Tue Nov 03 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0-2
- Requires git-core instead of git

* Wed Oct 28 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0-1
- Update to phosh 0.5.0

* Sun Oct 11 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.5-1
- Update to phosh 0.4.5

* Mon Sep 21 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.4-1
- Update to phosh 0.4.4

* Tue Aug 18 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.3-3
- Require hicolor icon theme

* Fri Aug 07 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.3-2
- Patch for 32 bit builds

* Mon Aug 03 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.3-1
- Update to phosh 0.4.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.2-1
- Update to phosh 0.4.2

* Tue Jul 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.1-1
- Update to phosh 0.4.1

* Wed Jul 01 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0-1
- Update to phosh 0.4.0
- Now depends on phoc

* Mon Jun 29 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-3
- Revert libgnome-volume-control to align with phosh source dependency version
- Move phosh.service to systemd unitdir

* Fri Jun 26 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-2
- Update libgnome-volume-control to latest commit

* Tue Jun 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-1
- Update to phosh 0.3.1
- Adding dbus-daemon

* Tue May 19 2020 Nikhil Jha <hi@nikhiljha.com> - 0.3.0-1
- Update to phosh 0.3.0

* Thu Mar 05 2020 Nikhil Jha <hi@nikhiljha.com> - 0.2.1-1
- Update to phosh 0.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 0.1.0-3
- Rebuilt for libgnome-desktop soname bump

* Wed Oct 02 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-2
- Fixes from review (thanks Robert-André Mauchin):
- Corrected the License tag
- Validate the Desktop Entry file

* Tue Oct 01 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-1
- Initial packaging

