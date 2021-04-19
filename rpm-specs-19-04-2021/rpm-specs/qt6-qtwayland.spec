%global qt_module qtwayland

Summary: Qt6 - Wayland platform support and QtCompositor module
Name:    qt6-%{qt_module}
Version: 6.0.3
Release: 1%{?dist}

License: LGPLv3
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

# Upstream patches

# Upstreamable patches


# filter qml provides
%global __provides_exclude_from ^%{_qt6_archdatadir}/qml/.*\\.so$

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-static
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libinput)

BuildRequires:  libXext-devel
BuildRequires:  tree

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
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


%ldconfig_scriptlets

%files
%doc README
%license LICENSE.*
%{_qt6_libdir}/libQt6WaylandCompositor.so.6*
%{_qt6_libdir}/libQt6WaylandClient.so.6*
%{_qt6_plugindir}/wayland-decoration-client/
%{_qt6_plugindir}/wayland-graphics-integration-server
%{_qt6_plugindir}/wayland-graphics-integration-client
%{_qt6_plugindir}/wayland-shell-integration
%{_qt6_plugindir}/platforms/libqwayland-egl.so
%{_qt6_plugindir}/platforms/libqwayland-generic.so
%{_qt6_plugindir}/platforms/libqwayland-xcomposite-egl.so
%{_qt6_plugindir}/platforms/libqwayland-xcomposite-glx.so
%{_qt6_qmldir}/QtWayland/

%files devel
%{_qt6_bindir}/qtwaylandscanner
%{_qt6_headerdir}/QtWaylandCompositor/
%{_qt6_headerdir}/QtWaylandClient/
%{_qt6_libdir}/libQt6WaylandCompositor.so
%{_qt6_libdir}/libQt6WaylandClient.so
%{_qt6_libdir}/libQt6WaylandCompositor.prl
%{_qt6_libdir}/libQt6WaylandClient.prl
%{_qt6_libdir}/cmake/Qt6WaylandCompositor/Qt6WaylandCompositorConfig*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWaylandTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6WaylandCompositor/
%{_qt6_libdir}/cmake/Qt6WaylandCompositor/
%dir %{_qt6_libdir}/cmake/Qt6WaylandClient/
%{_qt6_libdir}/cmake/Qt6WaylandClient/
%dir %{_qt6_libdir}/cmake/Qt6WaylandScannerTools/
%{_qt6_libdir}/cmake/Qt6WaylandScannerTools/
%{_qt6_libdir}/metatypes/qt6*_metatypes.json


%files examples
%{_qt6_examplesdir}/wayland/


%changelog
* Mon Apr 05 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.3-1
- 6.0.3

* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0
- 6.0.0
