# Review at https://bugzilla.redhat.com/show_bug.cgi?id=722914

Name:           volumeicon
Version:        0.5.1
Release:        8%{?dist}
Summary:        Lightweight volume control for the system tray

License:        GPLv3
URL:            http://www.softwarebakery.com/maato/volumeicon.html
Source0:        http://www.softwarebakery.com/maato/files/volumeicon/volumeicon-%{version}.tar.gz
# Source1 was borrowed from gnome-media package and adjusted for our needs
Source1:        %{name}.desktop

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libnotify-devel >= 0.5.0
BuildRequires:  intltool
BuildRequires:  gettext

Requires:       pavucontrol

# bundling of some functions partly copied from keybinder, currently retired
Provides:       bundled(keybinder) = 0.3.1

%description
Volume Icon aims to be a lightweight volume control that sits in your system
tray.

Features:
* Change volume by scrolling on the systray icon
* Ability to choose which channel to control
* Configurable stepsize
* Several icon themes
* Configurable external mixer
* Volume slider
* Hotkey support

%prep
%setup -q

%build
# Use pavucontrol by default in Fedora
%configure --enable-notify --with-default-mixerapp=pavucontrol
%make_build

%install
%make_install INSTALL='install -p'
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_sysconfdir}/xdg/autostart %{SOURCE1}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Raphael Groner <projects.rg@smart.ms> - 0.5.1-4
- drop useless BR because of bundling

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Raphael Groner <projects.rg@smart.ms> - 0.5.1-1
- new version
- drop upstreamed patches
- update build dependencies
- add runtime dependency pavucontrol, explicitly
- modernize

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6. Uses 'default' ALSA device now

* Sat Jan 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-3
- Temporarily revert "Use default ALSA device rather than hardcoded 'hw:0'"
  for we don't want this in F16

* Sat Jan 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-2
- Fix build error on rawhide

* Sat Jan 14 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-1
- Update ot 0.4.5 (#781649)
- Enable libnotify support (#781642)
- Drop upstreamed DSO fix
- Use default ALSA device rather than hardcoded 'hw:0'

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.1-4
- Rebuild for new libpng

* Thu Aug 11 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-3
- Fix application name in desktop file

* Wed Jul 20 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-2
- Fixes as per package review: Fix license tag, add defattr, drop README, fix
  typo and add some comments (#722914)

* Fri Jul 01 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Inital package
