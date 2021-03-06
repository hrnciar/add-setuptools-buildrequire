%global kf5_version_min 5.78

# Disable ufw for RHEL
%if 0%{?rhel}
%bcond_with ufw
%else
%bcond_without ufw
%endif

Name:    plasma-firewall
Version: 5.21.4
Release: 1%{?dist}
Summary: Control Panel for your system firewall

License: BSD
URL:     https://invent.kde.org/plasma/%{name}

%global verdir %(echo %{version} | cut -d. -f1-3)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global majmin_ver %(echo %{version} | cut -d. -f1,2).50
%global stable unstable
%else
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake

BuildRequires: extra-cmake-modules >= %{kf5_version_min}
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kcmutils-devel >= %{kf5_version_min}
BuildRequires: kf5-kcoreaddons-devel >= %{kf5_version_min}
BuildRequires: kf5-kdeclarative-devel >= %{kf5_version_min}
BuildRequires: kf5-ki18n-devel >= %{kf5_version_min}
BuildRequires: kf5-plasma-devel >= %{kf5_version_min}

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel

# Owns KCM directories
Requires: kf5-kcmutils%{?_isa} >= %{kf5_version_min}

Requires: %{name}-backend = %{version}-%{release}
Suggests: %{name}-firewalld

%description
%{summary}.

%package firewalld
Summary: FirewallD backend for Plasma Firewall
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-backend = %{version}-%{release}
Conflicts: %{name}-backend
Requires: firewalld

%description firewalld
This package provides the backend code for Plasma Firewall
to interface with FirewallD.

%if %{with ufw}
%package ufw
Summary: UFW backend for Plasma Firewall
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-backend = %{version}-%{release}
Conflicts: %{name}-backend
Requires: ufw
# For dbus directories
Requires: dbus-common
# For polkit directories
Requires: polkit

%description ufw
This package provides the backend code for Plasma Firewall
to interface with the Uncomplicated Firewall (UFW).
%endif

%prep
%autosetup -n %{name}-%{version} -p1

%build
%{cmake_kf5}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%if ! %{with ufw}
# Delete ufw stuff when we don't need it
rm -rfv %{buildroot}%{_qt5_plugindir}/kf5/plasma_firewall/ufwbackend.so
rm -rfv %{buildroot}%{_libexecdir}/kde_ufw_plugin_helper.py
rm -rfv %{buildroot}%{_datadir}/dbus-1/system-services/org.kde.ufw.service
rm -rfv %{buildroot}%{_datadir}/dbus-1/system.d/org.kde.ufw.conf
rm -rfv %{buildroot}%{_datadir}/kcm_ufw/defaults
rm -rfv %{buildroot}%{_datadir}/polkit-1/actions/org.kde.ufw.policy
%endif

%files -f %{name}.lang
%license LICENSES/*.txt
%{_libdir}/libkcm_firewall_core.so
%{_qt5_plugindir}/kcms/kcm_firewall.so
%dir %{_qt5_plugindir}/kf5/plasma_firewall
%{_datadir}/kpackage/kcms/kcm_firewall
%{_datadir}/kservices5/kcm_firewall.desktop
%{_metainfodir}/org.kde.plasma.firewall.metainfo.xml

%files firewalld
%{_qt5_plugindir}/kf5/plasma_firewall/firewalldbackend.so

%if %{with ufw}
%files ufw
%{_qt5_plugindir}/kf5/plasma_firewall/ufwbackend.so
%{_libexecdir}/kde_ufw_plugin_helper.py
%{_kf5_libexecdir}/kauth/kde_ufw_plugin_helper
%{_datadir}/dbus-1/system-services/org.kde.ufw.service
%{_datadir}/dbus-1/system.d/org.kde.ufw.conf
%dir %{_datadir}/kcm_ufw
%{_datadir}/kcm_ufw/defaults
%{_datadir}/polkit-1/actions/org.kde.ufw.policy
%endif


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

* Fri Jan 29 2021 Neal Gompa <ngompa13@gmail.com> - 5.20.90-4
- Subpackage firewall backends
- Ensure directory ownership is correct

* Thu Jan 28 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.20.90-3
- Add BuildRequires for gcc-c++, make and cmake

* Wed Jan 27 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.20.90-2
- Fix License

* Wed Jan 27 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.20.90-1
- 5.20.90 (beta)
