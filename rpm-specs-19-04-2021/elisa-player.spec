
Name:       elisa-player
Version:    20.12.3
Release:    1%{?dist}
Summary:    Elisa music player

# Main program LGPLv3+
# Background image CC-BY-SA
License:    LGPLv3+ and CC-BY-SA
URL:        https://community.kde.org/Elisa

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/elisa-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickTest)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Kirigami2)
Requires:       hicolor-icon-theme
Requires:       qt5-qtquickcontrols%{?_isa}
Requires:       kf5-kirigami2


%description
Elisa is a simple music player aiming to provide a nice experience for its
users.

%prep
%autosetup -n elisa-%{version} -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang elisa --all-name --with-kde --with-html

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.elisa.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.elisa.appdata.xml

%files -f elisa.lang
%license COPYING
%{_kf5_bindir}/elisa
%{_kf5_datadir}/applications/org.kde.elisa.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/elisa*
%{_kf5_datadir}/qlogging-categories5/elisa.categories
%{_kf5_metainfodir}/org.kde.elisa.appdata.xml
%{_kf5_libdir}/elisa/
%{_kf5_libdir}/qt5/qml/org/kde/elisa/

%changelog
* Fri Mar  5 08:47:17 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 20.12.3-1
- Update to 20.12.3
- Close: rhbz#1935395

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.2-1
- Update to 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 14:18:41 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 20.12.1-1
- Update to 20.12.1
- Close: rhbz#1913967

* Fri Dec 11 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.0-1
- Update to 20.12.0

* Sat Nov 07 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.3-1
- Update to 20.08.3

* Wed Oct 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.2-1
- Update to 20.08.2

* Wed Sep 23 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.1-1
- Update to 20.08.1

* Wed Aug 19 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.0-1
- Update to 20.08.0

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-4
- drop unused dep on qt5-qtbase-private-devel
- tighten qt5-qtquickcontrols runtime dep
- drop kde-filesystem dep (not needed, pulled in elsewhere)
- drop __cmake_in_source_build reference, enforced by %%cmake_kf5 now

* Tue Jul 28 16:05:29 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20.04.3-3
- Fix FTBFS

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.3-1
- Update to 20.04.3

* Fri Jun 12 2020 Marie Loise Nolden <loise@kde.org> - 20.04.2-1
- Update to 20.04.2

* Sun May 24 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.1-1
- Update to 20.04.1

* Fri Apr 24 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.0-1
- Update to 20.04.0

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.03.90-2
- rebuild (qt5)

* Sat Apr 04 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.03.90-1
- Update to 20.03.90

* Thu Apr 02 19:31:23 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20.03.80-1
- Update to 20.03.80 (#1800330)
- Update translations (#1820139)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 15:32:31 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 19.12.1-1
- Update to 19.12.1 (#1789485)
- Fix desktop file (#1790040)

* Sat Dec 14 05:41:09 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 19.12.0-1
- Release 19.12.0 (#1773785)

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.4.2-4
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.4.2-3
- rebuild (qt5)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 00:24:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.2-1
- Release 0.4.2 (#1722265)

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.4.0-2
- rebuild (qt5)

* Mon May 20 23:45:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Release 0.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-2
- Add qt5-qtquickcontrols

* Sun Sep 30 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Release 0.3.0

* Mon Jul 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Release 0.2.0

* Tue Apr 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- Release 0.1.1

* Sat Apr 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1-1
- Release 0.1

* Fri Feb 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.81-0.2.alpha2
- Rebuild with missing translations

* Thu Feb 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.81-0.1.alpha2
- Release 0.0.81

* Fri Dec 08 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.80-0.1.alpha1
- First RPM release
