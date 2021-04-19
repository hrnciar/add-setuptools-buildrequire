%undefine __cmake_in_source_build

%global base_name    plasma-thunderbolt

Name:    plasma-thunderbolt
Summary: Plasma integration for controlling Thunderbolt devices
Version: 5.21.4
Release: 1%{?dist}

License: GPLv2+ and BSD
URL:     https://cgit.kde.org/%{base_name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

BuildRequires:  gcc-c++

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Notifications)

BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)

Requires:       bolt

%description
Plasma Sytem Settings module and a KDED module to handle authorization of
Thunderbolt devices connected to the computer. There's also a shared library
(libkbolt) that implements common interface between the modules and the
system-wide bolt daemon, which does the actual hard work of talking to the
kernel.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name

%ldconfig_scriptlets


%files -f %{name}.lang
%doc README.md
%license COPYING
%{_kf5_libdir}/libkbolt.so
%{_kf5_qtplugindir}/kcms/kcm_bolt.so
%{_kf5_qtplugindir}/kf5/kded/kded_bolt.so
%{_kf5_datadir}/knotifications5/kded_bolt.notifyrc
%dir %{_kf5_datadir}/kpackage/kcms/kcm_bolt
%{_kf5_datadir}/kpackage/kcms/kcm_bolt/*
%{_kf5_datadir}/kservices5/kcm_bolt.desktop


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

* Tue Jan  5 16:03:33 CET 2021 Jan Grulich <jgrulich@redhat.com> - 5.20.5-1
- 5.20.5

* Tue Dec  1 09:43:01 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.4-1
- 5.20.4

* Wed Nov 11 08:22:43 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.3-1
- 5.20.3

* Tue Oct 27 14:25:14 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.2-1
- 5.20.2

* Tue Oct 20 15:30:59 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.1-1
- 5.20.1

* Sun Oct 11 19:50:05 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.0-1
- 5.20.0

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.90-1
- 5.19.90

* Tue Sep 01 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.5-1
- 5.19.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.4-1
- 5.19.4

* Tue Jul 07 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.3-1
- 5.19.3

* Tue Jun 23 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.2-1
- 5.19.2

* Mon Jun 22 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.1-1
- 5.19.1

* Tue May 05 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.5-1
- 5.18.5

* Tue Mar 31 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.4-1
- 5.18.4

* Tue Mar 10 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.3-1
- 5.18.3

* Mon Mar 09 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.2-1
- 5.18.2 (new package)
