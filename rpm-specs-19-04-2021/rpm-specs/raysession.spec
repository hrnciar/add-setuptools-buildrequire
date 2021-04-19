Name:               raysession
Version:            0.9.1
Release:            3%{?dist}
Summary:            Session manager for audio software
BuildArch:          noarch


# The entire source code is GPLv2

License:            GPLv2
URL:                https://github.com/Houston4444/RaySession
Source0:            %{url}/archive/v%{version}/RaySession-%{version}.tar.gz
# https://github.com/Houston4444/RaySession/issues/44
Source1:            README-wayland

BuildRequires: make
BuildRequires:      python3-qt5
BuildRequires:      qt5-linguist
BuildRequires:      desktop-file-utils
Requires:           python3 
Requires:           python3-qt5
Requires:           python3-pyliblo
Requires:           hicolor-icon-theme
Requires:           shared-mime-info
Recommends:         wmctrl
Recommends:         git
Recommends:         jack-audio-connection-kit

%description
Ray Session is a GNU/Linux session manager for audio programs as Ardour,
Carla, QTractor, Non-Timeline, etc...

It uses the same API as Non Session Manager, so programs compatible with NSM
are also compatible with Ray Session. As Non Session Manager, the principle
is to load together audio programs, then be able to save or close all
documents together.

Ray Session offers a little more:

 - Factory templates for NSM and LASH compatible applications
 - Possibility to save any client as template
 - Save session as template
 - Name files with a prettier way
 - remember if client was started or not
 - Abort session almost anytime
 - Change Main Folder of sessions on GUI
 - Possibility to KILL client if clean exit is too long
 - Open Session Folder button (open default file manager)

 Ray Session is being developed by houston4444, using Python3 and Qt5.

%prep
%autosetup -p 1 -n RaySession-%{version}
/usr/bin/cp %{SOURCE1} ./

%build
%{set_build_flags}
make LRELEASE=lrelease-qt5 %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}
# Build processs creates absolute symbolic links, they need to be replaced
# https://github.com/Houston4444/RaySession/issues/91
rm %{buildroot}%{_bindir}/ray-jack_checker_daemon
ln -s %{_datadir}/%{name}/ray-jack_checker_daemon %{buildroot}%{_bindir}/ray-jack_checker_daemon
rm %{buildroot}%{_bindir}/ray-jack_config_script
ln -s %{_datadir}/%{name}/ray-jack_config_script %{buildroot}%{_bindir}/ray-jack_config_script
rm %{buildroot}%{_bindir}/ray-pulse2jack
ln -s %{_datadir}/%{name}/ray-pulse2jack %{buildroot}%{_bindir}/ray-pulse2jack
rm %{buildroot}%{_bindir}/ray_git
ln -s %{_datadir}/%{name}/ray_git %{buildroot}%{_bindir}/ray_git

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%doc TODO
%doc TRANSLATORS
%doc snapshots_explain
%doc README-wayland
%license COPYING
%{_bindir}/ray-daemon
%{_bindir}/ray-jack_checker_daemon
%{_bindir}/ray-jack_config_script
%{_bindir}/ray-proxy
%{_bindir}/ray-pulse2jack
%{_bindir}/ray_git
%{_bindir}/ray_control
%{_bindir}/raysession
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/ray-jack_checker.desktop
%{_datadir}/applications/ray-jackpatch.desktop
%{_datadir}/applications/ray-network.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_sysconfdir}/xdg/raysession/*
# No manpages, developer is aware https://github.com/Houston4444/RaySession/issues/40

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.9.1-1
- Removed patches, issues were fixed upstream
- CLI: Control almost all GUI actions and more with the CLI ray_control.
- Session scripts: allow user to edit shell scripts at session load, save and
  close.
- JACK config session script: script that saves and recalls the JACK
  configuration for the session.
- Add this from session templates in "New Session" window.
- RayHack: New client protocol which is an alternative to ray-proxy.
- This allows to launch directly the process and to edit its properties even if
  process is stopped.
- Obviously NSM protocol is highly preferred, this protocol is a workaround
  only, nothing more.
- Factory client templates are installed in /etc/xdg/raysession to allow
  packagers to add some templates.
- Always prefer NSM template if NSM compatibility is found in executable binary
- Get client label, icon and description from their .desktop file
- Subfolder combobox removed in New Session Dialog
- Daemon option "Save from client" has been removed. Please affect a global
  keyboard shortcut (Meta+Ctrl+S) to ray_control save instead.

* Sat Feb 8 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.8.3-1
- Initial release for Fedora
