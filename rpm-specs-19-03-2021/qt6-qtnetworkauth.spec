%global qt_module qtnetworkauth

Summary: Qt6 - NetworkAuth component
Name:    qt6-%{qt_module}
Version: 6.0.1
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/additional_libraries/%{qt_module}/%{majmin}/%{version}/%{qt_module}-everywhere-src-%{version}.tar.xz

# filter plugin/qml provides
%global __provides_exclude_from ^(%{_qt6_archdatadir}/qml/.*\\.so|%{_qt6_plugindir}/.*\\.so)$

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1

%description
%{summary}

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
%license LICENSE.GPL*
%{_qt6_libdir}/libQt6NetworkAuth.so.6*

%files devel
%{_qt6_headerdir}/QtNetworkAuth/
%{_qt6_libdir}/libQt6NetworkAuth.so
%{_qt6_libdir}/libQt6NetworkAuth.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtNetworkAuthTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6NetworkAuth/
%{_qt6_libdir}/cmake/Qt6NetworkAuth/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_networkauth*.pri
%{_qt6_datadir}/modules/*.json

%files examples
%{_qt6_examplesdir}/


%changelog
* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0-1
- 6.0.0
