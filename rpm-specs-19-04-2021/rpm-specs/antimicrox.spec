# Force out of source build
%undefine __cmake_in_source_build

# % global snap       20200911
# % global gitcommit  9b383805b7967884a8b602c5a43be415c3427fe4
# % global shortcommit % (c=% {gitcommit}; echo $ {c:0:5})

%global appname io.github.antimicrox.antimicrox
%global libname libantilib

# Last released version: antimicroX-3.0-2.20200617gitc6d79
# antimicroX was abandoned by upstream, no new versions
%global obsname antimicroX
%global obsver 3.0-3
# libantilib and libantilib-devel has been removed as of 3.1.4
%global obslibver 3.1.4-1

Name:         antimicrox
Version:      3.1.4
Release:      2%{?snap:.%{snap}git%{shortcommit}}%{?dist}
Summary:      Graphical program used to map keyboard buttons and mouse controls to a gamepad

License:  GPLv3+
URL:      https://github.com/AntiMicroX/%{name}

%if 0%{?snap}
%global archivename %{name}-%{gitcommit}
%else
%global archivename %{name}-%{version}
%endif

%if 0%{?snap}
Source0:        %{url}/archive/%{gitcommit}/%{archivename}.tar.gz
%else
Source0:        %{url}/archive/%{version}/%{archivename}.tar.gz
%endif

Provides: %{obsname} = %{obsver}
Obsoletes: %{obsname} < %{obsver}

Obsoletes: %{obsname}-%{libname} < %{obsver}
Obsoletes: %{name}-%{libname} < %{obslibver}
Obsoletes: %{name}-%{libname}-devel < %{obslibver}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  SDL2-devel
BuildRequires:  itstool
BuildRequires:  gettext
# For desktop file & AppData
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

%description
%{name} is a graphical program used to map keyboard keys and mouse controls
to a gamepad. This program is useful for playing PC games using a gamepad that
do not have any form of built-in gamepad support. %{name} is a fork of
AntiMicro which was inspired by QJoyPad but has additional features.

%prep
%setup -n %{archivename} -q

%build
%cmake3
%cmake3_build

%install
%cmake3_install

%find_lang %{name} --with-qt

%files -f %{name}.lang
# Redundant
%exclude %{_datadir}/%{name}/CHANGELOG.md
%exclude %dir %{_datadir}/%{name}/translations
%exclude %{_datadir}/%{name}/translations/*
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/*/*/apps/*
%{_metainfodir}/%{appname}.appdata.xml
%{_datadir}/mime/packages/%{appname}.xml
%{_mandir}/man1/%{name}.1*
# Ignore header files, there is no reusable library any more
%exclude %dir %{_includedir}/%{name}
%exclude %{_includedir}/%{name}/*

%check
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appname}.desktop
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Gergely Gombos <gombosg@disroot.org> - 3.1.4-1
- 3.1.4, remove libantilib subpackage

* Sun Nov 15 2020 Gergely Gombos <gombosg@disroot.org> - 3.1.3-1
- 3.1.3, remove icons dependency, add % {arm} arch

* Fri Oct 2 2020 Gergely Gombos <gombosg@disroot.org> - 3.1.2-1
- 3.1.2

* Fri Sep 11 2020 Gergely Gombos <gombosg@disroot.org> - 3.1-1.20200911git9b383
- Initial package
