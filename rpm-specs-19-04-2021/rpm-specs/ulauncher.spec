Name:           ulauncher
Version:        5.11.0
Release:        1%{?dist}
Summary:        Linux Application Launcher
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/Ulauncher/Ulauncher
Source0:        %{url}/releases/download/%{version}/%{name}_%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=1895572
Source1:        https://raw.githubusercontent.com/Ulauncher/Ulauncher/%{version}/contrib/systemd/%{name}.service

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  keybinder3-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-devel >= 3.30
BuildRequires:  python3-inotify
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-pyxdg
BuildRequires:  python3-websocket-client
BuildRequires:  systemd-rpm-macros

BuildRequires:  python3dist(requests)

BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme
Requires:       keybinder3
Requires:       webkitgtk4
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-inotify
Requires:       python3-Levenshtein
Requires:       python3-pyxdg
Requires:       python3-websocket-client

Recommends:     libappindicator-gtk3

%description
Ulauncher is a fast application launcher for Linux. It's is written in Python,
using GTK+.


%prep
%autosetup -n %{name} -p1
sed -i "s|version='%%VERSION%'|version='%{version}'|g" setup.py


%build
%py3_build


%install

# https://github.com/Ulauncher/Ulauncher/issues/521
install -m 0644 -Dp build/share/applications/ulauncher.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%py3_install

install -Dpm0644 %{SOURCE1} -t \
    %{buildroot}%{_unitdir}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}-toggle
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%dir %{_datadir}/icons/breeze/
%dir %{_datadir}/icons/elementary/
%dir %{_datadir}/icons/gnome/
%dir %{_datadir}/icons/ubuntu-mono-dark/
%dir %{_datadir}/icons/ubuntu-mono-light/
%{_datadir}/icons/breeze/apps/48/%{name}-indicator.svg
%{_datadir}/icons/elementary/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/gnome/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/gnome/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}-indicator.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/icons/ubuntu-mono-*/scalable/apps/%{name}-indicator.svg
%{_unitdir}/%{name}.service
%{python3_sitelib}/%{name}-*-py*.egg-info
%{python3_sitelib}/%{name}/


%changelog
* Sun Apr 18 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 5.11.0-1
- build(update): 5.11.0
- build: libappindicator-gtk3 now optional dep | GH-commit: 87f41b3

* Mon Mar 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 5.10.0-3
- build: libappindicator-gtk3 now hard dep

* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 5.10.0-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 5.10.0-1
- build(update): 5.10.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.9.0-1
- build(update): 5.9.0

* Sun Nov 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.8.2-1
- build(update): 5.8.2

* Sat Nov  7 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.8.1-2
- build: add new systemd unit | rh#1895572

* Wed Oct 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.8.1-1
- build(update): 5.8.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.8.0-1
- Update to 5.8.0

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 5.7.5-2
- Rebuilt for Python 3.9

* Sat Apr 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.7.5-1
- Update to 5.7.5

* Sat Apr 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.7.4-1
- Update to 5.7.4

* Sun Apr 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.7.3-1
- Update to 5.7.3

* Wed Apr 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.7.1-1
- Update to 5.7.1

* Sat Mar 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.7.0-1
- Update to 5.7.0

* Wed Feb 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5.6.1-4
- Initial package
