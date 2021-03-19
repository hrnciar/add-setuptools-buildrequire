%global qt_module qtquick3d

Summary: Qt6 - Quick3D Libraries and utilities
Name:    qt6-%{qt_module}
Version: 6.0.1
Release: 1%{?dist}

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
# See also http://doc.qt.io/qt-5/licensing.html
License: GPLv3 with exceptions
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-static >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtshadertools-devel
#if 0{?fedora}
# BuildRequires: pkgconfig(assimp) >= 5.0.0
#endif

%description
The Qt 6 Quick3D library.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%ifnarch s390x
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

%cmake_qt6 \
%ifarch s390x
  -DQT_BUILD_EXAMPLES=OFF
%endif
#   -DQT_FEATURE_system_assimp=ON

%cmake_build


%install
%cmake_install

# hardlink files to %{_bindir}, add -qt6 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    balsam|meshdebug|shadergen)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt6
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

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
%license LICENSE.GPL*
%{_qt6_libdir}/libQt6Quick3D.so.6*
%{_qt6_libdir}/libQt6Quick3DAssetImport.so.6*
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so.6*
%{_qt6_libdir}/libQt6Quick3DUtils.so.6*
%dir %{_qt6_qmldir}/QtQuick3D/
%{_qt6_qmldir}/QtQuick3D/
%{_qt6_plugindir}/assetimporters/*.so

%files devel
%{_bindir}/balsam-qt6
%{_bindir}/meshdebug-qt6
%{_bindir}/shadergen-qt6
%{_qt6_bindir}/balsam
%{_qt6_bindir}/meshdebug
%{_qt6_bindir}/shadergen
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_includedir}/QtQuick3D/
%{_qt6_includedir}/QtQuick3DAssetImport/
%{_qt6_includedir}/QtQuick3DRuntimeRender/
%{_qt6_includedir}/QtQuick3DUtils/
%{_qt6_libdir}/cmake/Qt6/FindWrapQuick3DAssimp.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtQuick3DTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3D/
%{_qt6_libdir}/cmake/Qt6Quick3D/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DAssetImport/
%{_qt6_libdir}/cmake/Qt6Quick3DAssetImport/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DRuntimeRender/
%{_qt6_libdir}/cmake/Qt6Quick3DRuntimeRender/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DTools/
%{_qt6_libdir}/cmake/Qt6Quick3DTools/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DUtils/
%{_qt6_libdir}/cmake/Qt6Quick3DUtils/*.cmake
%{_qt6_libdir}/libQt6Quick3D.prl
%{_qt6_libdir}/libQt6Quick3D.so
%{_qt6_libdir}/libQt6Quick3DAssetImport.prl
%{_qt6_libdir}/libQt6Quick3DAssetImport.so
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.prl
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so
%{_qt6_libdir}/libQt6Quick3DUtils.prl
%{_qt6_libdir}/libQt6Quick3DUtils.so
%{_qt6_libdir}/metatypes/qt6*_metatypes.json

%ifnarch s390x
%if 0%{?_qt6_examplesdir:1}
%files examples
%{_qt6_examplesdir}/
%endif
%endif

%changelog
* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0-1
- 6.0.0
