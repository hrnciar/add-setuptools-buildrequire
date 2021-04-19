%global repo dde-session-ui
%global __provides_exclude_from ^%{_libdir}/dde-dock/.*\\.so$

%if 0%{?fedora}
Name:           deepin-session-ui
%else
Name:           %{repo}
%endif
Version:        5.3.35
Release:        2%{?fedora:%dist}
Summary:        Deepin desktop-environment - Session UI module
License:        GPLv3
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  deepin-gettext-tools
BuildRequires:  pkgconfig(dtkwidget) >= 5.1
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xext)
BuildRequires:  golang-github-msteinert-pam-devel
BuildRequires:  dtkcore-devel >= 5.1
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  make
BuildRequires:  gio-qt-devel
BuildRequires:  gtest-devel
%if 0%{?fedora}
Requires:       deepin-daemon
Requires:       deepin-session-shell
%else
Requires:       dde-daemon
%endif
Requires:       startdde

Provides:       deepin-notifications = %{version}-%{release}
Obsoletes:      deepin-notifications <= 3.3.4

%description
This project include those sub-project:

- dde-shutdown: User interface of shutdown.
- dde-lock: User interface of lock screen.
- dde-lockservice: The back-end service of locking screen.
- lightdm-deepin-greeter: The user interface when you login in.
- dde-switchtogreeter: The tools to switch the user to login in.
- dde-lowpower: The user interface of reminding low power.
- dde-osd: User interface of on-screen display.
- dde-hotzone: User interface of setting hot zone.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i 's|lib|libexec|' \
    misc/applications/deepin-toggle-desktop.desktop* \
    dde-osd/dde-osd_autostart.desktop \
    dde-osd/com.deepin.dde.osd.service \
    dde-osd/notification/files/com.deepin.dde.*.service* \
    dde-osd/dde-osd.pro \
    dde-welcome/com.deepin.dde.welcome.service \
    dde-welcome/dde-welcome.pro \
    dde-bluetooth-dialog/dde-bluetooth-dialog.pro \
    dde-touchscreen-dialog/dde-touchscreen-dialog.pro \
    dde-warning-dialog/com.deepin.dde.WarningDialog.service \
    dde-warning-dialog/dde-warning-dialog.pro \
    dde-offline-upgrader/dde-offline-upgrader.pro \
    dde-suspend-dialog/dde-suspend-dialog.pro \
    dnetwork-secret-dialog/dnetwork-secret-dialog.pro \
    dde-lowpower/dde-lowpower.pro
sed -i 's|/usr/lib/dde-dock|%{_libdir}/dde-dock|' dde-notification-plugin/notifications/notifications.pro

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} PKGTYPE=rpm
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/dde-*
%{_bindir}/dmemory-warning-dialog
%{_libexecdir}/deepin-daemon/*
%{_datadir}/%{repo}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/dbus-1/services/*.service
%{_libdir}/dde-dock/plugins/libnotifications.so
%{_prefix}/share/glib-2.0/schemas/com.deepin.dde.dock.module.notifications.gschema.xml

%changelog
* Tue Apr 06 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.3.35-2
- Requires deepin-session-shell

* Fri Mar 12 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.3.35-1
- fix: 小键盘enter键按下快捷键操作无效 (chenwei)
- fix: 修复无线网络连接提示框在任务栏有图标的bug (chenwei)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.18-1
- new upstream release: 5.3.0.18

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.8.11-3
- Fix Obsoletes for RPM 4.15

* Fri Mar  8 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.8.11-2
- Provides lightdm-greeter

* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 4.8.11-1
- Update to 4.8.11

* Tue Feb 19 2019 mosquito <sensor.wen@gmail.com> - 4.8.9-1
- Update to 4.8.9

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 4.8.7-1
- Update to 4.8.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Thu Nov 22 2018 mosquito <sensor.wen@gmail.com> - 4.6.2-2
- Provide deepin-notifications

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 4.6.2-1
- Update to 4.6.2

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 4.4.5-1
- Update to 4.4.5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.2.0-2
- Remove obsolete scriptlets

* Wed Dec 20 2017 mosquito <sensor.wen@gmail.com> - 4.2.0-1
- Update to 4.2.0

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 4.1.7-1
- Update to 4.1.7

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 4.0.17-1
- Update to 4.0.17

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 4.0.15-1
- Update to 4.0.15

* Thu Sep 21 2017 mosquito <sensor.wen@gmail.com> - 4.0.14-1
- Update to 4.0.14

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 4.0.13.1-1
- Update to 4.0.13.1

* Sun Aug  6 2017 mosquito <sensor.wen@gmail.com> - 4.0.13-1
- Rebuild

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.0.13-1.git4cadab1
- Update to 4.0.13

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.0.6-1.git1511ccf
- Update to 4.0.6

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.0.27-1.git6a09cb4
- Update to 3.0.27

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.23-1.git9db2f1d
- Update to 3.0.23

* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.22-1
- Initial package build
