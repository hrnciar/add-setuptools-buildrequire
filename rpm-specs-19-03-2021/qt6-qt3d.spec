%global qt_module qt3d

Summary: Qt6 - Qt3D QML bindings and C++ APIs
Name:    qt6-%{qt_module}
Version: 6.0.1
Release: 1%{?dist}

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
# See also http://doc.qt.io/qt-5/licensing.html
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/additional_libraries/%{qt_module}/%{majmin}/%{version}/%{qt_module}-everywhere-src-%{version}.tar.xz
Source1: qt3dcore-config-multilib_p.h

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-static >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtimageformats
# FIXME: enable with newer assimp
# if 0{?fedora}
# BuildRequires: pkgconfig(assimp) >= 3.3.1
# endif
Requires: qt6-qtimageformats%{?_isa} >= %{version}

%description
Qt 3D provides functionality for near-realtime simulation systems with
support for 2D and 3D rendering in both Qt C++ and Qt Quick applications).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

%cmake_qt6
# -DQT_FEATURE_qt3d_system_assimp=ON

%cmake_build


%install
%cmake_install

%ifarch %{multilib_archs}
# multilib: qt3dcore-config_p.h
  mv %{buildroot}%{_qt6_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config_p.h %{buildroot}%{_qt6_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config-%{__isa_bits}_p.h
  install -p -m644 -D %{SOURCE1} %{buildroot}%{_qt6_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config_p.h
%endif

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


%ldconfig_scriptlets

%files
%license LICENSE.GPL* LICENSE.LGPL*
%{_qt6_libdir}/libQt63DAnimation.so.6*
%{_qt6_libdir}/libQt63DCore.so.6*
%{_qt6_libdir}/libQt63DExtras.so.6*
%{_qt6_libdir}/libQt63DInput.so.6*
%{_qt6_libdir}/libQt63DLogic.so.6*
%{_qt6_libdir}/libQt63DQuick.so.6*
%{_qt6_libdir}/libQt63DQuickAnimation.so.6*
%{_qt6_libdir}/libQt63DQuickExtras.so.6*
%{_qt6_libdir}/libQt63DQuickInput.so.6*
%{_qt6_libdir}/libQt63DQuickRender.so.6*
%{_qt6_libdir}/libQt63DQuickScene2D.so.6*
%{_qt6_libdir}/libQt63DRender.so.6*
%{_qt6_plugindir}/geometryloaders/
%{_qt6_plugindir}/renderers/
%{_qt6_plugindir}/renderplugins/
%{_qt6_plugindir}/sceneparsers/
%{_qt6_qmldir}/Qt3D/
%{_qt6_qmldir}/QtQuick/Scene2D/
%{_qt6_qmldir}/QtQuick/Scene3D/

%files devel
%dir %{_qt6_libdir}/cmake/Qt63DAnimation
%dir %{_qt6_libdir}/cmake/Qt63DCore/
%dir %{_qt6_libdir}/cmake/Qt63DExtras
%dir %{_qt6_libdir}/cmake/Qt63DInput
%dir %{_qt6_libdir}/cmake/Qt63DLogic
%dir %{_qt6_libdir}/cmake/Qt63DQuick
%dir %{_qt6_libdir}/cmake/Qt63DQuickAnimation
%dir %{_qt6_libdir}/cmake/Qt63DQuickExtras
%dir %{_qt6_libdir}/cmake/Qt63DQuickInput
%dir %{_qt6_libdir}/cmake/Qt63DQuickRender/
%dir %{_qt6_libdir}/cmake/Qt63DQuickScene2D
%dir %{_qt6_libdir}/cmake/Qt63DRender/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_includedir}/Qt3DAnimation
%{_qt6_includedir}/Qt3DCore/
%{_qt6_includedir}/Qt3DExtras
%{_qt6_includedir}/Qt3DInput/
%{_qt6_includedir}/Qt3DLogic/
%{_qt6_includedir}/Qt3DQuick
%{_qt6_includedir}/Qt3DQuickAnimation
%{_qt6_includedir}/Qt3DQuickExtras
%{_qt6_includedir}/Qt3DQuickInput/
%{_qt6_includedir}/Qt3DQuickRender/
%{_qt6_includedir}/Qt3DQuickScene2D
%{_qt6_includedir}/Qt3DRender/
%{_qt6_libdir}/cmake/Qt6/FindWrapAssimp.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/Qt3DTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt63DAnimation/*.cmake
%{_qt6_libdir}/cmake/Qt63DCore/*.cmake
%{_qt6_libdir}/cmake/Qt63DExtras/*.cmake
%{_qt6_libdir}/cmake/Qt63DInput/*.cmake
%{_qt6_libdir}/cmake/Qt63DLogic/*.cmake
%{_qt6_libdir}/cmake/Qt63DQuick/*.cmake
%{_qt6_libdir}/cmake/Qt63DQuickAnimation/*.cmake
%{_qt6_libdir}/cmake/Qt63DQuickExtras/*.cmake
%{_qt6_libdir}/cmake/Qt63DQuickInput/*.cmake
%{_qt6_libdir}/cmake/Qt63DQuickRender/*.cmake
%{_qt6_libdir}/cmake/Qt63DQuickScene2D/*.cmake
%{_qt6_libdir}/cmake/Qt63DRender/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/libQt63DAnimation.prl
%{_qt6_libdir}/libQt63DAnimation.so
%{_qt6_libdir}/libQt63DCore.prl
%{_qt6_libdir}/libQt63DCore.so
%{_qt6_libdir}/libQt63DExtras.prl
%{_qt6_libdir}/libQt63DExtras.so
%{_qt6_libdir}/libQt63DInput.prl
%{_qt6_libdir}/libQt63DInput.so
%{_qt6_libdir}/libQt63DLogic.prl
%{_qt6_libdir}/libQt63DLogic.so
%{_qt6_libdir}/libQt63DQuick.prl
%{_qt6_libdir}/libQt63DQuick.so
%{_qt6_libdir}/libQt63DQuickAnimation.prl
%{_qt6_libdir}/libQt63DQuickAnimation.so
%{_qt6_libdir}/libQt63DQuickExtras.prl
%{_qt6_libdir}/libQt63DQuickExtras.so
%{_qt6_libdir}/libQt63DQuickInput.prl
%{_qt6_libdir}/libQt63DQuickInput.so
%{_qt6_libdir}/libQt63DQuickRender.prl
%{_qt6_libdir}/libQt63DQuickRender.so
%{_qt6_libdir}/libQt63DQuickScene2D.prl
%{_qt6_libdir}/libQt63DQuickScene2D.so
%{_qt6_libdir}/libQt63DRender.prl
%{_qt6_libdir}/libQt63DRender.so
%{_qt6_libdir}/metatypes/qt6*_metatypes.json


%if 0%{?_qt6_examplesdir:1}
%files examples
%{_qt6_examplesdir}/
%endif


%changelog
* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0-1
- 6.0.0
