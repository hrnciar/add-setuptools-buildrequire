Name:           dtkwidget
Version:        5.4.1
Release:        1%{?dist}
Summary:        Deepin tool kit widget modules
License:        LGPLv3+
%if 0%{?fedora}
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        %{name}_%{version}.orig.tar.xz
%endif

BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  dtkgui-devel
BuildRequires:  dtkcore-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)

# libQt5Gui.so.5(Qt_5.10.1_PRIVATE_API)(64bit) needed by dtkwidget-2.0.6.1-1.fc29.x86_64
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  make
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcore-devel%{?_isa}
Requires:       dtkgui-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir} DBUS_VERSION_0_4_2=YES
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_libdir}/libdtk-*/
%{_datadir}/libdtk-*/

%files devel
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/DtkWidget/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.4.1-1
- refactor: ???????????????DApplication??????????????????????????? (zccrs)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0-1
- new upstream release: 5.3.0

* Mon Nov 23 07:51:54 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.2.2.16-2
- rebuild (qt5)

* Sun Sep 27 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.2.2.16-1
- new upstream release: 5.2.2.16

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 2.1.1-7
- rebuild (qt5)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.1.1-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 2.1.1-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 2.1.1-2
- rebuild (qt5)

* Fri Aug  9 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.1.1-1
- Release 2.1.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.16.1-1
- Update to 2.0.16.1

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 2.0.9.17-4
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 2.0.9.17-3
- rebuild (qt5)

* Sun Mar 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.9.17-2
- rebuild (Qt5)

* Tue Feb 26 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.9.17-1
- Update to 2.0.9.17

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 2.0.9.16-1
- Update to 2.0.9.16

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.0.9.11-3
- use %%ldconfig_scriptlets
- own %%_libdir/cmake/DtkWidget

* Tue Dec 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.9.11-2
- rebuild (Qt5)

* Thu Dec 13 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.11-1
- Update to 2.0.9.11

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.9.9-3
- rebuild (qt5)

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.9-2
- Remove obsoletes statement (BZ#1537224)

* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.9-1
- Update to 2.0.9.9

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 2.0.9.3-2
- rebuild (qt5)

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.3-1
- Update to 2.0.9.3

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.2-1
- Update to 2.0.9.2

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.1-1
- Update to 2.0.9.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.6.1-3
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.6.1-2
- BR: qt5-qtbase-private-devel

* Tue Feb 20 2018 mosquito <sensor.wen@gmail.com> - 2.0.6.1-1
- Update to 2.0.6.1

* Mon Feb 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.5.3-3
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 28 2017 mosquito <sensor.wen@gmail.com> - 2.0.5.3-1
- Update to 2.0.5.3

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 2.0.5.2-1
- Update to 2.0.5.2

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 2.0.4.1-1
- Update to 2.0.4.1

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 2.0.1-2
- Fix DAboutDialog icon not supporting hidpi

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Thu Aug 24 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-2
- Dont depend a specific version of Qt

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 29 2017 mosquito <sensor.wen@gmail.com> - 0.3.3-1
- Initial package build
