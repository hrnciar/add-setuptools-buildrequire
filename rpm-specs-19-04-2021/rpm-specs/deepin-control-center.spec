%global repo dde-control-center

%if 0%{?fedora}
%global dde_prefix deepin
Name:           deepin-control-center
%else
%global dde_prefix dde
Name:           %{repo}
%endif
Version:        5.3.0.39
Release:        2%{?fedora:%dist}
Summary:        New control center for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# PATCHES FROM SOURCE GIT:

# systeminfo-deepin-icon
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0001: 0001-systeminfo-deepin-icon.patch

# no user experience
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0002: 0002-no-user-experience.patch

# feat: Initial packit setup
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0003: 0003-feat-Initial-packit-setup.patch

# Arch fixes
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0004: 0004-Arch-fixes.patch


BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  %{dde_prefix}-dock-devel
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  dtkwidget-devel
BuildRequires:  dtkgui-devel dtkcore-devel
BuildRequires:  %{dde_prefix}-qt-dbus-factory-devel
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(geoip)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  libpwquality-devel
%if 0%{?fedora}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qtbase-private-devel
%else
BuildRequires:  qt5-devel
%endif
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xext)
BuildRequires:  kf5-networkmanager-qt-devel
BuildRequires:  udisks2-qt5-devel
BuildRequires:  qt5-linguist
BuildRequires:  cmake
BuildRequires: make
Requires:       %{dde_prefix}-account-faces
Requires:       %{dde_prefix}-api
Requires:       %{dde_prefix}-daemon
Requires:       %{dde_prefix}-qt5integration
Requires:       %{dde_prefix}-network-utils
Requires:       startdde
%if 0%{?fedora} == 0
Requires:       dde-server-industry-config
%endif

%description
New control center for Linux Deepin.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i -E '/add_compile_definitions/d' CMakeLists.txt

sed -i '/%{repo}/ s|/usr/lib|%{_libdir}|' src/frame/modules/update/updatework.cpp \
                                          src/frame/window/mainwindow.cpp \
                                          com.deepin.controlcenter.develop.policy \
                                          README.md

sed -i '/TARGETS/s|lib|%{_lib}|' src/frame/CMakeLists.txt

sed -i '/#include <QPainter>/a #include <QPainterPath>' src/frame/widgets/basiclistdelegate.cpp src/frame/window/modules/update/updatehistorybutton.cpp \
                                                        src/frame/window/modules/commoninfo/commonbackgrounditem.cpp src/frame/modules/accounts/useroptionitem.cpp \
                                                        src/frame/window/modules/sync/pages/avatarwidget.cpp src/frame/window/modules/accounts/avataritemdelegate.cpp \
                                                        src/frame/modules/accounts/avatarwidget.cpp src/frame/window/modules/accounts/accountswidget.cpp \
                                                        src/frame/modules/datetime/timezone_dialog/popup_menu.cpp src/frame/modules/display/recognizedialog.cpp \
                                                        src/frame/window/modules/personalization/roundcolorwidget.cpp src/frame/window/modules/unionid/pages/avatarwidget.cpp
sed -i '/#include <QRect>/a #include <QPainterPath>' src/frame/window/modules/personalization/personalizationgeneral.cpp

sed -i 's|/bin/deepin-recovery-tool|%{_bindir}/deepin-recovery-tool|' src/frame/window/modules/systeminfo/backupandrestoreworker.cpp

# remove after -DDISABLE_SYS_UPDATE=YES working properly
sed -i '/new UpdateModule/d' src/frame/window/mainwindow.cpp

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake %{!?fedora:.} -DDCC_DISABLE_GRUB=YES \
       -DDISABLE_SYS_UPDATE=YES -DDISABLE_ACTIVATOR=YES -DDISABLE_RECOVERY=YES \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%if 0%{?fedora}
%cmake_build
%else
%make_build
%endif

%install
%if 0%{?fedora}
%cmake_install
%else
%make_install INSTALL_ROOT=%{buildroot}
%endif
# place holder plugins dir
mkdir -p %{buildroot}%{_libdir}/%{repo}/plugins

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{repo}
%{_libdir}/%{repo}
%{_libdir}/libdccwidgets.so
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/polkit-1/actions/com.deepin.*.policy
%{_datadir}/%{repo}/
%{_datadir}/dict/MainEnglishDictionary_ProbWL.txt

%files devel
%{_includedir}/%{repo}
%{_libdir}/cmake/DdeControlCenter/

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.39-1
- new upstream release: 5.3.0.39

* Thu Aug  6 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-5
- BR: qt5-qtbase-private-devel
- Applied an upstream patch to fix build with Qt 5.14
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec  1 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-2
- BR pkgconfig(xext)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.9.4-1
- Update to 4.9.4

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 4.9.2.1-1
- Update to 4.9.2.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 4.8.6-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 4.8.6-1
- Update to 4.8.6

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 4.8.2-1
- Update to 4.8.2

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 4.7.7-1
- Update to 4.7.7

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 4.7.6.1-1
- Update to 4.7.6.1

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 4.7.4-1
- Update to 4.7.4

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 4.6.4-1
- Update to 4.6.4

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 4.6.3-1
- Update to 4.6.3

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 4.6.2-1
- Update to 4.6.2

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 4.6.1-1
- Update to 4.6.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 mosquito <sensor.wen@gmail.com> - 4.3.7-3
- Exclude ppc64le, ppc64 and aarch64

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 4.3.7-1
- Update to 4.3.7

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Thu Sep 21 2017 mosquito <sensor.wen@gmail.com> - 4.2.5.10-1
- Update to 4.2.5.10

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 4.2.5.4-1
- Update to 4.2.5.4

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 4.2.5-1
- Update to 4.2.5

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 4.2.4-1.git21d68b6
- Update to 4.2.4

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.2.3-1.git2f420f2
- Update to 4.2.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.1.2-1.git4d3827b
- Update to 4.1.2

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 4.0.7-1.git10c3be2
- Update to 4.0.7

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 3.0.24-1.git481255b
- Downgrade to 3.0.24 for end user

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 4.0.2-2.git8b1a736
- Fix can not start

* Thu Jan 19 2017 mosquito <sensor.wen@gmail.com> - 4.0.2-1.git8b1a736
- Update to 4.0.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.1-1.gitd1c1c9a
- Update to 4.0.1

* Tue Dec 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Bump to newer release because of copr signature

* Fri Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to 3.0.24

* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.21-1
- Initial package build
