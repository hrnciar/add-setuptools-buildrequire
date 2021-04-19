%global qt_module qtdeclarative

# definition borrowed from qtbase
%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9

Summary: Qt6 - QtDeclarative component
Name:    qt6-%{qt_module}
Version: 6.0.3
Release: 1%{?dist}

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

# header file to workaround multilib issue
# https://bugzilla.redhat.com/show_bug.cgi?id=1441343
Source5: qv4global_p-multilib.h

## upstream patches

## upstreamable patches

# filter qml provides
%global __provides_exclude_from ^%{_qt6_archdatadir}/qml/.*\\.so$

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: python%{python3_pkgversion}
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: mesa-dri-drivers
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Provides:  %{name}-private-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package static
Summary: Static library files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build

# HACK so calls to "python" get what we want
ln -s %{__python3} python
export PATH=`pwd`:$PATH

%cmake_qt6

%cmake_build


%install
%cmake_install

%ifarch %{multilib_archs}
# multilib: qv4global_p.h
  mv %{buildroot}%{_qt6_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p.h \
     %{buildroot}%{_qt6_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p-%{__isa_bits}.h
  install -p -m644 -D %{SOURCE5} %{buildroot}%{_qt6_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p.h
%endif

# hardlink files to %{_bindir}, add -qt6 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    qmlcachegen|qmlleasing|qmlformat|qmleasing|qmlimportscanner|qmllint| \
    qmlpreview|qmlscene|qmltestrunner|qmltyperegistrar|qmlplugindump| \
    qmlprofiler|qml|qmlbundle|qmlmin|qmlscene)
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
  rm -fv "$(basename ${prl_file} .prl).la"
  sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
done
popd


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
export PATH=%{buildroot}%{_qt6_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt6_libdir}
make sub-tests-all %{?_smp_mflags}
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make check -k -C tests ||:
%endif


%ldconfig_scriptlets

%files
%license LICENSE.LGPL*
%{_qt6_libdir}/libQt6Qml.so.6*
%{_qt6_libdir}/libQt6QmlModels.so.6*
%{_qt6_libdir}/libQt6QmlWorkerScript.so.6*
%{_qt6_libdir}/libQt6Quick.so.6*
%{_qt6_libdir}/libQt6QuickWidgets.so.6*
%{_qt6_libdir}/libQt6QuickParticles.so.6*
%{_qt6_libdir}/libQt6QuickShapes.so.6*
%{_qt6_libdir}/libQt6QuickTest.so.6*
%{_qt6_plugindir}/qmltooling/
%{_qt6_archdatadir}/qml/

%files devel
%dir %{_qt6_libdir}/cmake/Qt6PacketProtocol/
%dir %{_qt6_libdir}/cmake/Qt6Qml/
%dir %{_qt6_libdir}/cmake/Qt6QmlCompiler/
%dir %{_qt6_libdir}/cmake/Qt6QmlDebug/
%dir %{_qt6_libdir}/cmake/Qt6QmlDevTools/
%dir %{_qt6_libdir}/cmake/Qt6QmlImportScanner/
%dir %{_qt6_libdir}/cmake/Qt6QmlModels/
%dir %{_qt6_libdir}/cmake/Qt6QmlTools/
%dir %{_qt6_libdir}/cmake/Qt6QmlWorkerScript/
%dir %{_qt6_libdir}/cmake/Qt6Quick/
%dir %{_qt6_libdir}/cmake/Qt6QuickParticles/
%dir %{_qt6_libdir}/cmake/Qt6QuickShapes/
%dir %{_qt6_libdir}/cmake/Qt6QuickTest/
%{_bindir}/qml*
%{_qt6_bindir}/qml*
%{_qt6_headerdir}/Qt*/
%{_qt6_libdir}/libQt6Qml.so
%{_qt6_libdir}/libQt6Qml.prl
%{_qt6_libdir}/libQt6QmlModels.so
%{_qt6_libdir}/libQt6QmlModels.prl
%{_qt6_libdir}/libQt6QmlWorkerScript.so
%{_qt6_libdir}/libQt6QmlWorkerScript.prl
%{_qt6_libdir}/libQt6Quick*.so
%{_qt6_libdir}/libQt6Quick*.prl
%{_qt6_libdir}/metatypes/qt6*_metatypes.json
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_archdatadir}/mkspecs/features/*.prf
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtDeclarativeTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6PacketProtocol/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/*.cmake*
%{_qt6_libdir}/cmake/Qt6Qml/*.cpp.in
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6QmlCompiler/*.cmake
%{_qt6_libdir}/cmake/Qt6QmlDebug/*.cmake
%{_qt6_libdir}/cmake/Qt6QmlDevTools/*.cmake
%{_qt6_libdir}/cmake/Qt6QmlImportScanner/*.cmake
%{_qt6_libdir}/cmake/Qt6QmlModels/*.cmake
%{_qt6_libdir}/cmake/Qt6QmlTools/*.cmake
%{_qt6_libdir}/cmake/Qt6QmlWorkerScript/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick/*.cmake
%{_qt6_libdir}/cmake/Qt6QuickParticles/*.cmake
%{_qt6_libdir}/cmake/Qt6QuickShapes/*.cmake
%{_qt6_libdir}/cmake/Qt6QuickTest/*.cmake
%{_qt6_libdir}/cmake/Qt6QuickWidgets/*.cmake
%{_qt6_datadir}/modules/*.json

%files static
%{_qt6_libdir}/libQt6QmlCompiler.a
%{_qt6_libdir}/libQt6QmlCompiler.prl
%{_qt6_libdir}/libQt6QmlDevTools.prl
%{_qt6_libdir}/libQt6QmlDevTools.a
%{_qt6_libdir}/libQt6PacketProtocol.a
%{_qt6_libdir}/libQt6PacketProtocol.prl
%{_qt6_libdir}/libQt6QmlDebug.a
%{_qt6_libdir}/libQt6QmlDebug.prl

%files examples
%{_qt6_examplesdir}/


%changelog
* Mon Apr 05 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.3-1
- 6.0.3

* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0-1
- 6.0.0
