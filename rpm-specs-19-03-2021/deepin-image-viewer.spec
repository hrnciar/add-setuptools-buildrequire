Name:           deepin-image-viewer
Version:        5.6.3.73
Release:        1%{?dist}
Summary:        Deepin Image Viewer
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-image-viewer
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-appdata.xml

# fix: build failures under Qt 5.15
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0001: 0001-fix-build-failures-under-Qt-5.15.patch

# feat: Initial packit setup
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0002: 0002-feat-Initial-packit-setup.patch

# fix: use Q_GLOBAL_STATIC to initialize `effectcs` in slideeffect.cpp
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0003: 0003-fix-use-Q_GLOBAL_STATIC-to-initialize-effectcs-in-sl.patch




BuildRequires:  gcc-c++
BuildRequires:  freeimage-devel
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  udisks2-qt5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  make
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -p1
# Fedora freeimage 3.19.0-0.1.svn1859 does not support FAXG3
sed -i '/FIF_FAXG3/d' viewer/utils/unionimage.cpp

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dm644 %SOURCE1 %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_qt5_plugindir}/imageformats/*.so
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{name}/
%{_datadir}/dman/%{name}/
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Fri Mar 12 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.6.3.73-1
- fix: 设置ttb的延时定时器只执行一次 (liuminghang)
- fix: 修改bug55109 (liuminghang)
- fix: 修改bug54962 (liuminghang)
- fix: 修复幻灯片退出异常的问题 (shuwenzhi)
- fix: 最新镜像不支持deepin-turbo，删除turbo代码 (shuwenzhi)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.6.3.27-2
- Fix crash at startup

* Thu Nov 12 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.6.3.27-1
- new upstream release: 5.6.3.27

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 5.0.0-4
- Rebuild for new LibRaw

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-2
- BR pkgconfig(xext)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 1.3.8-1
- Update to 1.3.8

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 1.3.6-1
- Update to 1.3.6

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 1.2.23-1
- Update to 1.2.23

* Thu Jul 19 2018 Adam Williamson <awilliam@redhat.com> - 1.2.16.8-3
- Rebuild for new libraw

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 mosquito <sensor.wen@gmail.com> - 1.2.16.8-1
- Update to 1.2.16.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.16.7-2
- Remove obsolete scriptlets

* Thu Dec 28 2017 mosquito <sensor.wen@gmail.com> - 1.2.16.7-1
- Update to 1.2.16.7

* Sat Dec  9 2017 mosquito <sensor.wen@gmail.com> - 1.2.16.5-1
- Update to 1.2.16.5

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 1.2.16.4-1
- Update to 1.2.16.4

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 1.2.16.1-1
- Update to 1.2.16.1

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 1.2.15-1
- Update to 1.2.15

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.2.14-1.gite77fde5
- Update to 1.2.14

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.2.13-1.gita6ac784
- Update to 1.2.13

* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 1.2.4-1.gitfad9c98
- Update to 1.2.4

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 1.2.1-1.git8378500
- Update to 1.2.1

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.2.0-1.git933325f
- Update to 1.2.0

* Fri Jan 06 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.3-2
- Fixed build dependecies

* Sat Dec 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.3-1
- Initial package build
