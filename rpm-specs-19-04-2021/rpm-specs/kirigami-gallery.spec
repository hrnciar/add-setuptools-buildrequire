Name:    kirigami-gallery
Version: 21.03.90
Release: 3%{?dist}
Summary: Gallery application built using Kirigami
License: LGPLv2+
URL:     https://apps.kde.org/en/kirigami2.gallery

%global majmin %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

Source:  https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)

Requires:   kf5-kirigami2
Requires:   kf5-kitemmodels
Requires:   qt5-qtquickcontrols2
Requires:   qt5-qtgraphicaleffects
Requires:   breeze-icon-theme

%description
Example application which uses all features from kirigami,
including links to the source code, tips on how to use the
components and links to the corresponding HIG pages and
code examples on invent.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang kirigamigallery --with-qt
install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 org.kde.kirigami2.gallery.appdata.xml %{buildroot}%{_datadir}/metainfo/org.kde.kirigami2.gallery.appdata.xml

%check
# https://github.com/hughsie/appstream-glib/issues/360
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.kirigami2.gallery.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kirigami2.gallery.desktop

%files -f kirigamigallery.lang
%doc README.md
%license LICENSE.LGPL-2
%{_kf5_metainfodir}/org.kde.kirigami2.gallery.appdata.xml
%{_kf5_datadir}/applications/org.kde.kirigami2.gallery.desktop
%{_kf5_bindir}/kirigami2gallery

%changelog
* Mon Apr 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org>  21.03.90-3
- requirement : breeze-icon-theme added.

* Mon Apr 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org>  21.03.90-2
- F35FailsToInstall fix (#1948402)

* Sat Apr 10 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org>  21.03.90-1
- 21.03.90 (#1943793)

* Thu Mar 25 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org>  20.12.3-1
- Initial version of the package

