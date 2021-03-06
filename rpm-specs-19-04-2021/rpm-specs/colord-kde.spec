
Name:           colord-kde
Version:        0.5.0
Release:        14%{?dist}
Summary:        Colord support for KDE

License:        GPLv2+
URL:            https://cgit.kde.org/%{name}.git
Source0:        http://download.kde.org/stable/colord-kde/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches (lookaside cache)
Patch1: 0001-Remove-unused-dependencies.patch
Patch3: 0003-Add-categorized-logging.patch
Patch4: 0004-Avoid-crash-on-exit-on-wayland.patch
Patch5: 0005-Fix-colord-helper-DBus-annotations.patch

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel

BuildRequires:  lcms2-devel
BuildRequires:  libXrandr-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

# colord is a dbus daemon
Requires:       colord
Requires:       plasma-systemsettings

%description
KDE support for colord including KDE Daemon module and System Settings module.


%prep
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install

%find_lang colord-kde


%files -f colord-kde.lang
%license COPYING
%doc MAINTAINERS TODO
%{_kf5_bindir}/colord-kde-icc-importer
%{_kf5_qtplugindir}/kcm_colord.so
%{_kf5_qtplugindir}/kded_colord.so
%{_kf5_datadir}/applications/colordkdeiccimporter.desktop
%{_kf5_datadir}/kservices5/kcm_colord.desktop
%{_kf5_datadir}/kservices5/kded/colord.desktop


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.5.0-4
- pull in upstream fixes, update URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.5.0-2
- pull in upstream fixes, use %%{?dist}

* Fri Oct 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.5.0-1
- 0.5.0 release (+translations)

* Mon Feb 22 2016 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-4.20150519git
- .spec cosmetics

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3.20150519git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2.20150519git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Jan Grulich <jgrulich@redhat.com> - 0.4.0-1.20150519git
- Update to a git snapshot based on KF5

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 06 2015 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-5
- update URL:, +%%{?kde4_runtime_requires}

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Luk???? Tinkl <ltinkl@redhat.com> - 0.3.0-1
- New upstream version 0.3.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.2.0-1
- update to version 0.2.0

* Thu Mar 22 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.1.0-2
- fix kcmshell4 visibility by setting X-KDE-ParentApp

* Wed Mar 21 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.1.0-1
- initial try
