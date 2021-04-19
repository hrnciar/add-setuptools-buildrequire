%global extension   pop-shell
%global uuid        %{extension}@system76.com
%global forgeurl    https://github.com/pop-os/shell
%global tag         %{version}

%forgemeta

Name:           gnome-shell-extension-%{extension}
Version:        1.2.0
Release:        3%{?dist}
Summary:        GNOME Shell extension for advanced tiling window management
# main license - GPLv3
# src/plugins/calc/math.js - ASL 2.0
# src/levenshtein.ts - MIT
License:        GPLv3 and ASL 2.0 and MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_org.gnome.shell.%{extension}.gschema.override
# downstream-only patch
Patch0:         0001-Remove-schemas-from-compile-target.patch

BuildArch:      noarch
BuildRequires:  npm(typescript) >= 3.8
BuildRequires:  make

Requires:       gnome-shell-extension-common

Provides:       %{extension}
Provides:       bundled(npm(mathjs)) = 8.1.0
Provides:       bundled(npm(js-levenshtein))

Recommends:     %{name}-shortcut-overrides = %{version}-%{release}
Recommends:     gnome-extensions-app
Recommends:     gnome-shell-extension-native-window-placement


%description
Pop Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Pop Shell
is the addition of advanced tiling window management - a feature that has been
highly-sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.


%package shortcut-overrides
Summary:        Shortcut overrides for %{name}


%description shortcut-overrides
Shortcut overrides for %{name}.


%prep
%forgeautosetup -p 1

# remove launcher plugin developer guide
rm src/plugins/README.md


%build
%make_build compile


%install
%make_install

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml

# install the gnome-control-center keybindings
install -d -m 0755 %{buildroot}%{_datadir}/gnome-control-center/keybindings
install -p -m 0644 keybindings/*.xml %{buildroot}%{_datadir}/gnome-control-center/keybindings/

# install the schema override files
install -d -m 0755 %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m 0644 %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{buildroot}%{_datadir}/glib-2.0/schemas/


%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_prefix}/lib/pop-shell


%files shortcut-overrides
%{_datadir}/glib-2.0/schemas/*.%{extension}.gschema.override


%changelog
* Mon Feb 15 2021 Carl George <carl@george.computer> - 1.2.0-3
- Fix org.gnome.mutter override

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Carl George <carl@george.computer> - 1.2.0-1
- Latest upstream

* Sun Jan 10 2021 Carl George <carl@george.computer> - 1.1.0-1
- Latest upstream

* Thu Dec 03 2020 Carl George <carl@george.computer> - 1.0.0-3.20201130gitee943b8
- Latest upstream

* Wed Nov 18 2020 Carl George <carl@george.computer> - 1.0.0-2.20201118git5137d52
- Latest upstream
- Include gnome-control-center keybindings

* Mon Nov 09 2020 Carl George <carl@george.computer> - 1.0.0-1.20201109git04eaf4f
- Latest upstream
- Provide pop-shell

* Thu Oct 29 2020 Carl George <carl@george.computer> - 1.0.0-1
- Latest upstream

* Thu Oct 22 2020 Carl George <carl@george.computer> - 0.1.0-1.20201016gita11d3c3
- Split gschema overrides to seperate files

* Tue Oct 20 2020 Carl George <carl@george.computer> - 0.1.0-0.9.20201016gita11d3c3
- Latest upstream commit
- Sync shortcut overrides with pop-session
- Move shortcut overrides to a subpackage
- Open shortcuts website if pop-shell-shortcuts is not installed

* Fri Oct 02 2020 Carl George <carl@george.computer> - 0.1.0-0.8.20201001gitff702bc
- Latest upstream commit
- Include new color-dialog file

* Fri Oct 02 2020 Drew DeVore <drew@devorcula.com> - 0.1.0-0.7.20200929gitb9f8d96
- Added override for stacking conflict

* Thu Oct 01 2020 Carl George <carl@george.computer> - 0.1.0-0.6.20200929gitb9f8d96
- Latest upstream commit

* Mon Sep 21 2020 Carl George <carl@george.computer> - 0.1.0-0.5.20200920git8791171
- Latest upstream commit

* Tue Sep 15 2020 Carl George <carl@george.computer> - 0.1.0-0.4.20200915gite5a80ea
- Latest upstream commit

* Thu Sep 10 2020 Carl George <carl@george.computer> - 0.1.0-0.3.20200908git017c92e
- Latest upstream commit
- Add primary-super-h/l versions of toggle-tiled-left/right keybindings

* Fri Aug 28 2020 Carl George <carl@george.computer> - 0.1.0-0.2.20200821git8416328
- Add keyboard shortcut overrides

* Thu Aug 27 2020 Carl George <carl@george.computer> - 0.1.0-0.1.20200821git8416328
- Initial package
