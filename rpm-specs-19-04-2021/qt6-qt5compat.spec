%global qt_module qt5compat

Summary: Qt6 - Qt 5 Compatibility Libraries
Name:    qt6-%{qt_module}
Version: 6.0.3
Release: 1%{?dist}

License: LGPLv3
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

# Upstream patches

# Upstreamable patches

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: libicu-devel

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
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
%license LICENSE.*
%{_qt6_libdir}/libQt6Core5Compat.so.6*

%files devel
%{_qt6_headerdir}/QtCore5Compat/
%{_qt6_libdir}/libQt6Core5Compat.prl
%{_qt6_libdir}/libQt6Core5Compat.so
%{_qt6_libdir}/cmake/Qt6/FindWrapIconv.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/Qt5CompatTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6Core5Compat/
%{_qt6_libdir}/cmake/Qt6Core5Compat/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_datadir}/modules/*.json

%changelog
* Mon Apr 05 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.3-1
- 6.0.3

* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0
- 6.0.0
