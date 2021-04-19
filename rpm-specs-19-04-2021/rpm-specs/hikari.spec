Name:           hikari
Version:        2.3.0
Release:        1%{?dist}
Summary:        Stacking Wayland compositor with tiling capabilities

License:        BSD
URL:            https://hikari.acmelabs.space/
Source0:        %{url}/releases/%{name}-%{version}.tar.gz

BuildRequires: bmake
BuildRequires: mk-files
BuildRequires: gcc
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(libucl)
BuildRequires: pkgconfig(wlroots)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libevdev)
BuildRequires: glib-devel
BuildRequires: pixman-devel
BuildRequires: pam-devel
Recommends: xorg-x11-server-Xwayland

%description
Hikari is a stacking Wayland compositor with additional tiling capabilities, it
is heavily inspired by the Calm Window manager (cwm(1)). Its core concepts are
views, groups, sheets and the workspace.

%prep
%autosetup

%build
%set_build_flags
bmake WITH_POSIX_C_SOURCE=YES \
      WITH_XWAYLAND=YES \
      WITH_SCREENCOPY=YES \
      WITH_GAMMACONTOL=YES \
      WITH_LAYERSHELL=YES

%install
bmake DESTDIR=%{buildroot} \
      PREFIX=%{_prefix} \
      ETC_PREFIX="" \
      WITHOUT_SUID=YES \
      install

%files
%license LICENSE
%doc README.md
%config %{_sysconfdir}/pam.d/%{name}-unlocker
%config %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0755, root, root) %{_bindir}/%{name}
%attr(0755, root, root) %{_bindir}/%{name}-unlocker
%{_mandir}/man1/hikari.1*
%{_datadir}/backgrounds/%{name}/
%{_datadir}/backgrounds/%{name}/hikari_wallpaper.png
%{_datadir}/wayland-sessions/%{name}.desktop

%changelog
* Mon Apr 12 2021 Timothée Floure <fnux@fedoraproject.org> - 2.3.0-1
- New upstream release.

* Sat Mar 20 2021 Timothée Floure <fnux@fedoraproject.org> - 2.2.2-3
- Remove useless setuid
- Properly set fedora build flags

* Sat Mar 06 2021 Timothée Floure <fnux@fedoraproject.org> - 2.2.2-2
- Fix various permission and rpmlint issues.

* Thu Dec 24 2020 Timothée Floure <fnux@fedoraproject.org> - 2.2.2-1
- New upstream release

* Wed Sep 09 2020 Timothée Floure <fnux@fedoraproject.org> - 2.2.0-1
- New upstream release

* Wed Jul 22 2020 Timothée Floure <fnux@fedoraproject.org> - 2.1.1-1
- New upstream release

* Wed Jul 22 2020 Timothée Floure <fnux@fedoraproject.org> - 2.1.0-1
- New upstream release

* Wed Jun 03 2020 Timothée Floure <fnux@fedoraproject.org> - 2.0.0-1
- New upstream release

* Sun May 24 2020 Timothée Floure <fnux@fedoraproject.org> - 1.2.1-1
- New upstream release

* Wed May 20 2020 Timothée Floure <fnux@fedoraproject.org> - 1.2.0-1
- New upstream release

* Tue May 12 2020 Timothée Floure <fnux@fedoraproject.org> - 1.1.1-1
- New upstream release

* Fri May 01 2020 Timothée Floure <fnux@fedoraproject.org> - 1.1.0-1
- New upstream release

* Sat Apr 25 2020 Timothée Floure <fnux@fedoraproject.org> - 1.0.4-1
- New upstream release

* Mon Apr 20 2020 Timothée Floure <fnux@fedoraproject.org> - 1.0.3-2
- Enable XWayland, Screencopy, Gammacontrol and Layer-shell support

* Mon Apr 20 2020 Timothée Floure <fnux@fedoraproject.org> - 1.0.3-2
- Fix pam configuration installation, remove useless recommends, make use of pkgconfig.

* Sun Apr 19 2020 Timothée Floure <fnux@fedoraproject.org> - 1.0.3-1
- Let there be package.
