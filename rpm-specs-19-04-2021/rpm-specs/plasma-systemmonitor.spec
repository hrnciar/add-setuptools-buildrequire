
%global kf5_version_min 5.78

Name:    plasma-systemmonitor
Version: 5.21.4
Release: 1%{?dist}
Summary: An application for monitoring system resources

License: GPLv2+ and LGPLv2+
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

## upstream patches

BuildRequires: extra-cmake-modules >= %{kf5_version_min}
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kirigami2-devel >= %{kf5_version_min}
Requires: kf5-kirigami2%{?_isa} >= %{kf5_version_min}
BuildRequires: kf5-kconfig-devel >= %{kf5_version_min}
BuildRequires: kf5-kdeclarative-devel >= %{kf5_version_min}
BuildRequires: kf5-ki18n-devel >= %{kf5_version_min}
BuildRequires: kf5-kiconthemes-devel >= %{kf5_version_min}
BuildRequires: kf5-kitemmodels-devel >= %{kf5_version_min}
BuildRequires: kf5-kservice-devel >= %{kf5_version_min}
BuildRequires: kf5-kglobalaccel-devel >= %{kf5_version_min}
BuildRequires: kf5-kio-devel >= %{kf5_version_min}
BuildRequires: kf5-kdbusaddons-devel >= %{kf5_version_min}
BuildRequires: kf5-knewstuff-devel >= %{kf5_version_min}

BuildRequires: qt5-qtquickcontrols2-devel
Requires: qt5-qtquickcontrols2%{?_isa}

BuildRequires: libksysguard-devel >= %{version}

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel

# We need ksystemstats from ksysguard (rhbz#1930514)
Requires: ksystemstats >= %{version}

%description
An interface for monitoring system sensors, process information and other system
resources.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%{cmake_kf5}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%license LICENSES/*.txt
%{_bindir}/plasma-systemmonitor
%{_datadir}/applications/org.kde.plasma-systemmonitor.desktop
%{_datadir}/config.kcfg/systemmonitor.kcfg
%{_kf5_datadir}/knsrcfiles/
%{_kf5_datadir}/ksysguard/sensorfaces/
%{_kf5_datadir}/plasma-systemmonitor/
%{_kf5_qmldir}/org/kde/ksysguard/

%changelog
* Tue Apr 06 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.4-1
- 5.21.4

* Tue Mar 16 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.3-1
- 5.21.3

* Tue Mar 02 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.2-1
- 5.21.2

* Sun Feb 28 2021 Neal Gompa <ngompa13@gmail.com> - 5.21.1-2
- Require ksystemstats from ksysguard (rhbz#1930514)

* Tue Feb 23 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.1-1
- 5.21.1

* Thu Feb 11 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.0-1
- 5.21.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.20.90-1
- 5.20.90 (beta)
