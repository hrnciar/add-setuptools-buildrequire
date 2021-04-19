%global qt_module qtquickcontrols2

Name:    qt6-%{qt_module}
Summary: Qt6 - module with set of QtQuick controls for embedded
Version: 6.0.3
Release: 1%{?dist}

License: GPLv2+ or LGPLv3 and GFDL
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

# filter qml provides
%global __provides_exclude_from ^%{_qt6_archdatadir}/qml/.*\\.so$

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel

Requires: qt6-qtdeclarative%{?_isa} >= %{version}

%description
The Qt Labs Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

Unlike Qt Quick Controls, these controls are optimized for embedded systems
and so are preferred for hardware with limited resources.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary:        Examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%cmake_qt6

%cmake_build


%install
%cmake_install

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# Remove .la leftovers
rm -f %{buildroot}%{_qt6_libdir}/libQt6*.la


%ldconfig_scriptlets

%files
%license LICENSE.LGPLv3 LICENSE.GPLv3
%{_qt6_libdir}/libQt6QuickTemplates2.so.6*
%{_qt6_libdir}/libQt6QuickControls2.so.6*
%{_qt6_libdir}/libQt6QuickControls2Impl.so.6*
%{_qt6_qmldir}/Qt/labs/platform
%{_qt6_archdatadir}/qml/QtQuick/Controls/
%{_qt6_archdatadir}/qml/QtQuick/NativeStyle/
%{_qt6_archdatadir}/qml/QtQuick/Templates/

%files examples
%{_qt6_examplesdir}/quickcontrols2/

%files devel
%{_qt6_headerdir}/
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/metatypes/*.json
%{_qt6_libdir}/libQt6QuickTemplates2.so
%{_qt6_libdir}/libQt6QuickControls2.so
%{_qt6_libdir}/libQt6QuickTemplates2.prl
%{_qt6_libdir}/libQt6QuickControls2.prl
%{_qt6_libdir}/libQt6QuickControls2Impl.prl
%{_qt6_libdir}/libQt6QuickControls2Impl.so
%{_qt6_libdir}/qt6/mkspecs/modules/*
%{_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtQuickControls2TestsConfig.cmake
%dir %{_libdir}/cmake/Qt6QuickControls2/
%{_libdir}/cmake/Qt6QuickControls2/*.cmake
%dir %{_libdir}/cmake/Qt6QuickTemplates2/
%{_libdir}/cmake/Qt6QuickTemplates2/*.cmake
%{_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_libdir}/cmake/Qt6QuickControls2Impl/
%{_libdir}/cmake/Qt6QuickControls2Impl/*.cmake

%changelog
* Mon Apr 05 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.3-1
- 6.0.3

* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0
- 6.0.0
