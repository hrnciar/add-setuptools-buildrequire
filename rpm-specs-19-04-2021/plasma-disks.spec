%undefine __cmake_in_source_build

Name:    plasma-disks
Summary: Hard disk health monitoring for KDE Plasma
Version: 5.21.4
Release: 1%{?dist}

License: GPLv2+ and LGPLv3+ and BSD and CC0
URL:     https://invent.kde.org/plasma/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kauth-devel
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Solid)

BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Core)

BuildRequires:  smartmontools
Requires:       smartmontools

%description
Plasma Disks monitors S.M.A.R.T. data of disks and alerts the user when
signs of imminent failure appear.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%files -f %{name}.lang
%license LICENSES/*.txt
%{_libexecdir}/kf5/kauth/kded-smart-helper
%{_qt5_plugindir}/kcms/smart.so
%{_kf5_plugindir}/kded/smart.so
%{_kf5_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_kf5_datadir}/dbus-1/system.d/org.kde.kded.smart.conf
%{_kf5_datadir}/knotifications5/org.kde.kded.smart.notifyrc
%{_kf5_datadir}/kpackage/kcms/plasma_disks/*
%{_kf5_datadir}/kservices5/smart.desktop
%{_kf5_datadir}/metainfo/org.kde.plasma.disks.metainfo.xml
%{_kf5_datadir}/polkit-1/actions/org.kde.kded.smart.policy

%changelog
* Tue Apr 06 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.4-1
- 5.21.4

* Tue Mar 16 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.3-1
- 5.21.3

* Tue Mar 02 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.2-1
- 5.21.2

* Tue Feb 23 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.1-1
- 5.21.1

* Thu Feb 11 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.0-1
- 5.21.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Jan Grulich <jgrulich@redhat.com> - 5.20.90-1
- 5.20.90 (beta)

* Tue Jan  5 16:03:32 CET 2021 Jan Grulich <jgrulich@redhat.com> - 5.20.5-1
- 5.20.5

* Mon Dec  7 08:11:21 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.4-1
- 5.20.4

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.90-1
- 5.19.90 (new package)
