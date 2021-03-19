
%global kf5_version_min 5.78

Name:    qqc2-breeze-style
Version: 5.21.3
Release: 1%{?dist}
Summary: QtQuickControls2 breeze style

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

Source0: http://download.kde.org/%{stable}/plasma/%{verdir}/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules >= %{kf5_version_min}
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kirigami2-devel >= %{kf5_version_min}
Requires: kf5-kirigami2%{?_isa} >= %{kf5_version_min}
BuildRequires: kf5-kconfig-devel >= %{kf5_version_min}
BuildRequires: kf5-kguiaddons-devel >= %{kf5_version_min}
BuildRequires: kf5-kiconthemes-devel >= %{kf5_version_min}
BuildRequires: kf5-kconfigwidgets-devel >= %{kf5_version_min}
BuildRequires: qt5-qtquickcontrols2-devel
Requires: qt5-qtquickcontrols2%{?_isa}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel


%description
This is a pure Qt Quick/Kirigami Qt Quick Controls style.

%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install


%files 
%doc README.md
%license LICENSES/*.txt
%{_kf5_plugindir}/kirigami/org.kde.breeze.so
%{_qt5_qmldir}/QtQuick/Controls.2/org.kde.breeze
%{_qt5_qmldir}/org/kde/breeze/
%{_qt5_qmldir}/org/kde/kirigami.2/styles/org.kde.breeze/
%{_kf5_libdir}/cmake/KF5QQC2BreezeStyle/

%changelog
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

* Fri Jan 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.20.90-1
- 5.20.90 (beta)
