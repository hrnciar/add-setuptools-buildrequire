Name:           dtkgui
Version:        5.4.0
Release:        1%{?dist}
Summary:        Deepin dtkgui
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/dtkgui

%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{name}_%{version}.orig.tar.xz
%endif
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  dtkcore-devel
BuildRequires:  librsvg2-devel
BuildRequires:  gcc-c++
BuildRequires:  annobin
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%endif
BuildRequires:  make
%description
Dtkgui is the GUI module for DDE look and feel.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcore-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} \
           DTK_VERSION=%{version} \
           LIB_INSTALL_DIR=%{_libdir} \
           BIN_INSTALL_DIR=%{_libexecdir}/dtk5 \
           TOOL_INSTALL_DIR=%{_libexecdir}/dtk5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_libexecdir}/dtk5/deepin-gui-settings
%{_libexecdir}/dtk5/taskbar
%{_sysconfdir}/dbus-1/system.d/com.deepin.dtk.FileDrag.conf

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/dtkgui.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtkgui.pri
%{_libdir}/cmake/DtkGui/
%{_libdir}/lib%{name}.so

%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.4.0-1
- feat: add github action (lxz)
- fix: disable text color hard to read (ck)
- feat: Initial packit setup (Robin Lee)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.2.2.18-2
- rebuild (qt5)

* Sun Nov 08 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.2.2.18-1
- new upstream release: 5.2.2.18

* Wed Sep 23 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.2.2.15-2
- Initial correct changelog
- Re-download upstream tarball
- Fix version value alignment