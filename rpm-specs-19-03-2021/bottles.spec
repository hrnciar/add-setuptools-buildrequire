%global uuid pm.mirko.%{name}

Name: bottles
Version: 3.0.9
Release: 1%{?dist}

License: GPLv3+
Summary: Easily manage Wine prefix in a new way
URL: https://github.com/bottlesdevs/Bottles
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: python3
BuildRequires: python3-gobject
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)

Requires: gtk3
Requires: hicolor-icon-theme
Requires: libhandy1
Requires: python3-gobject

%description
Easily manage Wine prefix in a new way! (Run Windows software and games on
Linux).

Features:

- Create bottles based on environments (a set of rule and dependencies for
  better software compatibility)
- Access to a customizable environment for all your experiments
- Run every executable (.exe/.msi) in your bottles, using the context menu in
  your file manager
- Integrated management and storage for executable file arguments
- Support for custom environment variables
- Simplified DLL overrides
- On-the-fly runner change for any Bottle
- Various optimizations for better gaming performance (esync, fsync, dxvk,
  cache, shader compiler, offload .. and much more.)
- Tweak different wine prefix settings, without leaving Bottles
- Automated dxvk installation
- Automatic installation and management of Wine and Proton runners
- System for checking runner updates for the bottle and automatic repair in
  case of breakage
- Integrated Dependencies installer with compatibility check based on a
  community-driver repository
- Detection of installed programs
- Integrated Task manager for wine processes
- Easy access to ProtonDB and WineHQ for support
- Configurations update system across Bottles versions
- Backup bottles as configuration file or full archive
- Import backup archive
- Importer from Bottles v1 (and other wineprefix manager)
- Bottles versioning (experimental)
- .. and much more that you can find by installing Bottles!


%prep
%autosetup -n Bottles-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml


%changelog
* Sat Mar 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.9-1
- build(update): 3.0.9

* Mon Mar 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.8-1
- build(update): 3.0.8

* Sun Mar 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.6-1
- build(update): 3.0.6

* Wed Mar 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.5-1
- build(update): 3.0.5

* Fri Feb 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.2-1
- build(update): 3.0.2

* Fri Feb 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.1.1-2
- build: Add libhandy1 dep

* Fri Feb 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.1.1-1
- build(update): 3.0.1.1

* Mon Feb 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.2-1
- build(update): 2.1.2

* Fri Feb 19 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.1-1
- build(update): 2.1.1

* Thu Feb 18 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0.7-1
- build(update): 2.1.0.7

* Thu Feb 04 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0.6-1
- build(update): 2.1.0.6

* Tue Jan 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0.5-1
- build(update): 2.1.0.5

* Wed Jan 20 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0.4-1
- build(update): 2.1.0.4

* Mon Jan 18 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0.2-1
- build(update): 2.1.0.2

* Tue Jan 12 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0-1
- build(update): 2.1.0

* Sun Jan 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.9.9-1
- build(update): 2.0.9.9

* Sat Jan  9 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.9.8-1
- build(update): 2.0.9.8

* Thu Jan  7 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.9.7-1
- Initial package
