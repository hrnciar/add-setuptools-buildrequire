%global shortname adwaita-qt

%{?mingw_package_header}

Name:           mingw-adwaita-qt
Version:        1.2.1
Release:        1%{?dist}
Summary:        Adwaita theme for Qt-based applications

License:        GPLv2+ and MIT
Url:            https://github.com/FedoraQt/adwaita-qt
Source0:        https://github.com/FedoraQt/adwaita-qt/archive/%{version}/adwaita-qt-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase

%description
Theme to let Qt applications fit nicely into Fedora Workstation

# Win32
%package -n mingw32-adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       mingw32-libadwaita-qt5 = %{version}-%{release}

%description -n mingw32-adwaita-qt5
Adwaita theme variant for applications utilizing Qt5.

%package -n mingw32-libadwaita-qt5
Summary:        Adwaita Qt5 library

%description -n mingw32-libadwaita-qt5
%{summary}.

%package -n mingw32-libadwaita-qt5-static
Summary:        Development files for mingw32-libadwaita-qt5
Requires:       mingw32-libadwaita-qt5 = %{version}-%{release}

%description -n mingw32-libadwaita-qt5-static
Static version of the mingw32-libadwaita-qt5 library.

# Win64
%package -n mingw64-adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       mingw64-libadwaita-qt5 = %{version}-%{release}
BuildArch:      noarch

%description -n mingw64-adwaita-qt5
Adwaita theme variant for applications utilizing Qt5.

%package -n mingw64-libadwaita-qt5
Summary:        Adwaita Qt5 library

%description -n mingw64-libadwaita-qt5
%{summary}.

%package -n mingw64-libadwaita-qt5-static
Summary:        Development files for mingw64-libadwaita-qt5
Requires:       mingw64-libadwaita-qt5 = %{version}-%{release}

%description -n mingw64-libadwaita-qt5-static
Static version of the mingw64-libadwaita-qt5 library.


%{?mingw_debug_package}

%prep
%autosetup -p1 -n adwaita-qt-%{version}

%build
%mingw_cmake

%mingw_make_build

%install
%mingw_make_install


# Win32
%files -n mingw32-adwaita-qt5
%{mingw32_libdir}/qt5/plugins/styles/libadwaita-qt.dll

%files -n mingw32-libadwaita-qt5
%{mingw32_bindir}/libadwaitaqt-1.dll
%{mingw32_bindir}/libadwaitaqtpriv-1.dll
%{mingw32_includedir}/AdwaitaQt/
%{mingw32_libdir}/cmake/AdwaitaQt/
%{mingw32_libdir}/pkgconfig/adwaita-qt.pc

%files -n mingw32-libadwaita-qt5-static
%{mingw32_libdir}/libadwaitaqt.dll.a
%{mingw32_libdir}/libadwaitaqtpriv.dll.a

# Win64
%files -n mingw64-adwaita-qt5
%{mingw64_libdir}/qt5/plugins/styles/libadwaita-qt.dll

%files -n mingw64-libadwaita-qt5
%{mingw64_bindir}/libadwaitaqt-1.dll
%{mingw64_bindir}/libadwaitaqtpriv-1.dll
%{mingw64_includedir}/AdwaitaQt/
%{mingw64_libdir}/cmake/AdwaitaQt/
%{mingw64_libdir}/pkgconfig/adwaita-qt.pc

%files -n mingw64-libadwaita-qt5-static
%{mingw64_libdir}/libadwaitaqt.dll.a
%{mingw64_libdir}/libadwaitaqtpriv.dll.a


%changelog
* Mon Mar 22 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.1-1
- 1.2.1

* Tue Mar 09 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.0-3
- Fix adwaita-qt library to be properly linked using CMake

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Jan Grulich <jgrulich@redhat.com> - 1.2.0-1
- 1.2.0

* Mon Nov 09 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.91-1
- Initial release
