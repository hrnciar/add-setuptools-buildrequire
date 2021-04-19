Name:    kquickimageeditor
Version: 0.1.2
Release: 2%{?dist}
Summary: QtQuick components providing basic image editing capabilities
License: GPLv2+
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://invent.kde.org/libraries/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel        >= 5.12.0
BuildRequires: qt5-qtdeclarative-devel >= 5.12.0

%description
%{summary}

%package devel
Summary: Development files for %{name}

%description devel
The %{name}-devel package contains cmake and mkspecs for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-v%{version}

%build
%{cmake_kf5}
%{cmake_build}

%install
%{cmake_install}

%files
%{_libdir}/qt5/qml/org/kde/kquickimageeditor

%files devel
%{_libdir}/cmake/KQuickImageEditor
%{_libdir}/qt5/mkspecs/modules/qt_KQuickImageEditor.pri

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Marc Deop <marcdeop@fedoraproject.org> - 0.1.2-1
- Initial package.

