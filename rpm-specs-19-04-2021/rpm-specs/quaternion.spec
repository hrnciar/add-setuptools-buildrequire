%global appid com.github.quaternion
%global forgeurl    https://github.com/quotient-im/Quaternion
%global tag         0.0.95-beta3

Name:       quaternion
Version:    0.0.95
Release:    0.3%{?dist}

%forgemeta

Summary:    A Qt5-based IM client for Matrix
License:    GPLv3
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Quotient)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Keychain)

Requires:       qt5-qtquickcontrols%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}
Requires:       hicolor-icon-theme

%description
Quaternion is a cross-platform desktop IM client for the Matrix protocol.

%prep
%forgesetup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_INTREE_LIBQMC=NO
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}
%find_lang %{name} --with-qt
cp -p linux/%{appid}.appdata.xml %{buildroot}%{_metainfodir}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_metainfodir}/%{appid}.appdata.xml

%changelog
* Thu Feb 11 2021 Brendan Early <mymindstorm@evermiss.net> - 0.0.95-0.3
- Update to 0.0.95-beta3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9.5-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.5-0.2
- Update to version 0.0.9.5-beta2
- Use forge macro

* Fri Oct 30 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4e-5
- Add explicit requires for qtquickcontrols

* Thu Aug 06 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4e-4
- Fix build failure

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9.4e-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9.4e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4e-1
- Version 0.0.9.4e

* Thu Mar 05 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4c-1
- Version 0.0.9.4c
