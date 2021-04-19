%global repo dde-launcher
%global sname deepin-launcher

%if 0%{?fedora}
Name:           %{sname}
%else
Name:           %{repo}
%endif
Version:        5.3.0.45
Release:        1%{?fedora:%dist}
Summary:        Deepin desktop-environment - Launcher module
License:        GPLv3
%if 0%{?fedora}
URL:            https://github.com/linuxdeepin/dde-launcher
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
%else
URL:            http://shuttle.corp.deepin.com/cache/repos/eagle/release-candidate/RERFNS4wLjAuNjU3NQ/pool/main/d/dde-launcher/
Source0:        %{name}_%{version}.orig.tar.xz	
%endif

# fix: fix build on Fedora
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0001: 0001-fix-fix-build-on-Fedora.patch

# fix: fix typo
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0002: 0002-fix-fix-typo.patch

# fix: rpm BuildRequires make
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0003: 0003-fix-rpm-BuildRequires-make.patch

# fix: fix qdbus executable name in Fedora
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0004: 0004-fix-fix-qdbus-executable-name-in-Fedora.patch


BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  dtkwidget-devel
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  gtest-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  make
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-menu
%if 0%{?fedora}
Requires:       deepin-daemon
%else
Requires:       dde-daemon
%endif
Requires:       startdde
Requires:       hicolor-icon-theme

%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i 's/qdbus /qdbus-qt5 /' %{repo}-wrapper

%build
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
%if 0%{?fedora}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DWITHOUT_UNINSTALL_APP=1
%cmake_build
%else
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DWITHOUT_UNINSTALL_APP=1 .
%make_build
%endif

%install
%if 0%{?fedora}
%cmake_install
%else
%make_install INSTALL_ROOT=%{buildroot}
%endif

%files
%license LICENSE
%{_bindir}/%{repo}
%{_bindir}/%{repo}-wrapper
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/scalable/apps/%{sname}.svg

%files devel
%{_includedir}/%{repo}/

%changelog
* Fri Mar 12 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.45-1
- fix: 修复启动器自动化标记错误的问题 (chenwei)
- fix: 窗口模式排序被还原到初始状态 (聂成)
- feat: 规范代码中直接调用系统命令的部分 (聂成)
- fix: 修复启动器全屏模式按键操作的bug (chenwei)
- fix(launcher): 修改了切换为英文后注销，点开启动器，小窗口模式下，应用为中文显示问题 (Li Tao)
- Merge branch 'uos' into maintain/5.2 (聂成)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.27-1
- new upstream release: 5.3.0.27

* Mon Nov 23 07:49:56 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.3.0.22-2
- rebuild (qt5)

* Wed Nov 11 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.22-1
- new upstream release: 5.3.0.22

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.0.0-8
- rebuild (qt5)

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-7
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.0-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.0-2
- rebuild (qt5)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 4.6.6-4
- rebuild (qt5)

* Mon Jun 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.6.6-3
- rebuild (Qt5)

* Sun Mar 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.6.6-2
- rebuild (Qt5)

* Wed Feb 27 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.6.6-1
- Update to 4.6.6

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 4.6.4-1
- Update to 4.6.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 4.5.9-1
- Update to 4.5.9

* Tue Dec 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.5.5.2-2
- BR: qt5-qtbase-private-devel

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 4.5.5.2-1
- Update to 4.5.5.2

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 4.5.2-1
- Update to 4.5.2

* Fri Aug 17 2018 mosquito <sensor.wen@gmail.com> - 4.4.5-1
- Update to 4.4.5

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 4.4.4-1
- Update to 4.4.4

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 4.4.3-1
- Update to 4.4.3

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 4.4.1-1
- Update to 4.4.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3.0-2
- Remove obsolete scriptlets

* Wed Dec 20 2017 mosquito <sensor.wen@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Sat Dec  9 2017 mosquito <sensor.wen@gmail.com> - 4.2.7-1
- Update to 4.2.7

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 4.2.6-1
- Update to 4.2.6

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 4.2.1-1
- Update to 4.2.1

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 4.1.9-1
- Update to 4.1.9

* Sat Aug 26 2017 mosquito <sensor.wen@gmail.com> - 4.1.8-1
- Update to 4.1.8

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 4.1.7-1
- Update to 4.1.7

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 4.1.6-1
- Update to 4.1.6

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 4.1.4-1.gitbe7e408
- Update to 4.1.4

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.1.3-1.git1cc701f
- Update to 4.1.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.0.11-1.git67081d3
- Update to 4.0.11

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 4.0.7-1.gitf2df6ea
- Update to 4.0.7

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.4-1.git8b1a2dd
- Update to 4.0.4

* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.3-1
- Updated to version 4.0.3

* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.2-1
- Initial package build
