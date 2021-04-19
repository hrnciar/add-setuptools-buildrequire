%global systemd_unit gnome-remote-desktop.service

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-remote-desktop
Version:        40.0
Release:        2%{?dist}
Summary:        GNOME Remote Desktop screen share service

License:        GPLv2+
URL:            https://gitlab.gnome.org/jadahl/gnome-remote-desktop
Source0:        https://download.gnome.org/sources/gnome-remote-desktop/40/%{name}-%{tarball_version}.tar.xz

# Adds encryption support (requires patched LibVNCServer)
Patch0:         gnutls-anontls.patch

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  meson >= 0.36.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0
BuildRequires:  pkgconfig(libvncserver) >= 0.9.11-7
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(winpr2)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(gnutls)

%{?systemd_requires}
BuildRequires:  systemd

Requires:       pipewire >= 0.3.0

Obsoletes:      vino < 3.22.0-21

%description
GNOME Remote Desktop is a remote desktop and screen sharing service for the
GNOME desktop environment.


%prep
%autosetup -S git -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install


%post
%systemd_user_post %{systemd_unit}


%preun
%systemd_user_preun %{systemd_unit}


%postun
%systemd_user_postun_with_restart %{systemd_unit}


%files
%license COPYING
%doc README
%{_libexecdir}/gnome-remote-desktop-daemon
%{_userunitdir}/gnome-remote-desktop.service
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml


%changelog
* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 40.0-2
- Rebuild for updated FreeRDP.

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Thu Mar 18 2021 Michael Catanzaro <mcatanzaro@redhat.com> - 40.0~rc-2
- Add Obsoletes: vino

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 40.0~rc-1
- Update to 40.rc

* Thu Mar 04 2021 Jonas Ådahl <jadahl@redhat.com> - 40.0~beta-1
- Bump to 40.beta

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.9-2
- Copy using the right destination stride

* Mon Sep 14 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.9-1
- Update to 0.1.9
- Backport race condition crash fix
- Rebase anon-tls patches

* Thu Aug 27 2020 Ray Strode <rstrode@redhat.com> - 0.1.8-3
- Fix crash
  Related: #1844993

* Mon Jun 1 2020 Felipe Borges <feborges@redhat.com> - 0.1.8-2
- Fix black screen issue in remote connections on Wayland

* Wed Mar 11 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 4 2019 Jonas Ådahl <jadahl@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 2 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.6-2
- Don't crash when PipeWire disconnects (rhbz#1632781)

* Tue Aug 7 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.6
- Update to 0.1.6
- Apply ANON-TLS patch
- Depend on pipewire 0.2.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.4-1
- Update to new version

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-3
- Use %%autosetup
- Install licence file

* Tue Aug 22 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-2
- Remove gschema compilation step as that had been deprecated

* Mon Aug 21 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-1
- Update to 0.1.2
- Changed tabs to spaces
- Added systemd user macros
- Install to correct systemd user unit directory
- Compile gsettings schemas after install and uninstall

* Mon Aug 21 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.1-1
- First packaged version
