Name:           power-profiles-daemon
Version:        0.1
Release:        4%{?dist}
Summary:        Makes power profiles handling available over D-Bus

License:        GPLv3+
URL:            https://gitlab.freedesktop.org/hadess/power-profiles-daemon
Source0:        https://gitlab.freedesktop.org/hadess/power-profiles-daemon/uploads/5efc7a766d5a50ed811e085035c7b967/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  systemd
BuildRequires:  umockdev
BuildRequires:  python3-dbusmock
BuildRequires:  systemd-rpm-macros

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%autosetup

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%triggerun -- power-profiles-daemon < 0.1-2

# This is for upgrades from previous versions before power-profiles-daemon became part
# of the system daemons.
systemctl --no-reload preset power-profiles-daemon.service &>/dev/null || :

%files
%license COPYING
%doc README.md
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_sysconfdir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Bastien Nocera <bnocera@redhat.com> - 0.1-2
+ power-profiles-daemon-0.1-2
- Reload presets when updating from an older version

* Fri Aug 07 2020 Bastien Nocera <bnocera@redhat.com> - 0.1-1
- Initial package
