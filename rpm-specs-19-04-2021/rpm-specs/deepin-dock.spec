%global sname deepin-dock
%global repo dde-dock
%global __provides_exclude_from ^%{_libdir}/%{repo}/.*\\.so$

%if 0%{?fedora}
%global start_logo start-here
Name:           %{sname}
%else
Name:           %{repo}
%endif
Version:        5.3.64
Release:        2%{?fedora:%dist}
Summary:        Deepin desktop-environment - Dock module
License:        GPLv3
%if 0%{?fedora}
URL:            https://github.com/linuxdeepin/dde-dock
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
%else
URL:            http://shuttle.corp.deepin.com/cache/repos/eagle/release-candidate/RERFNS4wLjAuNjU3NQ/pool/main/d/dde-dock/
Source0:        %{name}_%{version}.orig.tar.xz
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  dtkwidget-devel >= 5.1
BuildRequires:  dtkgui-devel >= 5.2.2.16
BuildRequires:  dtkcore-devel >= 5.1
BuildRequires:  pkgconfig(dframeworkdbus) >= 2.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  qt5-linguist
BuildRequires:  gtest-devel
Requires:       dbusmenu-qt5
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  make
Requires:       deepin-network-utils
Requires:       deepin-qt-dbus-factory
%else
Requires:       dde-network-utils
Requires:       dde-qt-dbus-factory
%endif
Requires:       xcb-util-wm
Requires:       xcb-util-image
Recommends:     %{name}-onboard-plugin

%description
Deepin desktop-environment - Dock module.

%package devel
Summary:        Development package for %{sname}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{sname}.

%package onboard-plugin
Summary:        deepin desktop-environment - dock plugin
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       onboard

%description onboard-plugin
deepin desktop-environment - dock plugin.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i '/TARGETS/s|lib|%{_lib}|' plugins/*/CMakeLists.txt \
                                 plugins/plugin-guide/plugins-developer-guide.md

sed -i 's|/lib|/%{_lib}|' frame/controller/dockpluginscontroller.cpp \
                          frame/panel/mainpanelcontrol.cpp \
                          plugins/tray/system-trays/systemtrayscontroller.cpp


sed -i 's|/lib|/libexec|g' plugins/show-desktop/showdesktopplugin.cpp \
                           frame/panel/mainpanelcontrol.cpp

sed -i 's:libdir.*:libdir=%{_libdir}:' dde-dock.pc.in

sed -i 's|/usr/lib/dde-dock/plugins|%{_libdir}/dde-dock/plugins|' plugins/plugin-guide/plugins-developer-guide.md
sed -i 's|local/lib/dde-dock/plugins|local/%{_lib}/dde-dock/plugins|' plugins/plugin-guide/plugins-developer-guide.md

%if 0%{?fedora}
# set icon to Fedora logo
sed -i 's|deepin-launcher|%{start_logo}|' frame/item/launcheritem.cpp
%endif

%build
export PATH=%{_qt5_bindir}:$PATH
%if 0%{?fedora}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DARCHITECTURE=%{_arch}
%cmake_build
%else
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DARCHITECTURE=%{_arch} .
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
%{_sysconfdir}/%{repo}/
%{_bindir}/%{repo}
%{_libdir}/%{repo}/
%{_datadir}/%{repo}/
%{_datarootdir}/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml
%{_datarootdir}/polkit-1/actions/com.deepin.dde.dock.overlay.policy

%files devel
%doc plugins/plugin-guide
%{_includedir}/%{repo}/
%{_libdir}/pkgconfig/%{repo}.pc
%{_libdir}/cmake/DdeDock/DdeDockConfig.cmake

%files onboard-plugin
%{_libdir}/dde-dock/plugins/libonboard.so


%changelog
* Wed Apr  7 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.3.64-2
- onboard fixes

* Fri Mar 12 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.3.64-1
- fix: 关闭窗口特效模式，已打开的的应用在任务栏上tooltip窗口没有根据文案长度自适应 (yangyuyin)
- feat: 更新任务栏翻译文件 (chenwei)
- fix: 修改蓝牙插件界面相关bug (chenwei)
- fix: 时间插件显示异常 (Zhang Qipeng)
- fix: 桌面和多任务视图移除后重新添加没有按照添加顺序显示 (dongrui)
- fix: 旋转屏幕任务栏高度异常 (Zhang Qipeng)
- fix(network): displayed the wrong AP signal strength (zsien)
- fix: 任务栏图标动画重叠 (Zhang Qipeng)
- fix: 应用图标tips位置错误 (Zhang Qipeng)
- fix: 任务栏切换位置后模糊特效异常 (Zhang Qipeng)
- fix: 任务栏插件参数缺失 (Zhang Qipeng)
- fix: 时间日期格式问题 (dongrui)
- fix: 蓝牙列表排序问题 (Zhang Qipeng)
- fix: 蓝牙列表排序问题 (Zhang Qipeng)
- fix: 任务栏蓝牙插件设备列表无法刷新 (Zhang Qipeng)
- fix: fix dde-dock windowRadius bug (xmuli)
- fix: 修复任务栏时间显示不完整的bug (chenwei)
- fix: 蓝牙图标未及时刷新 (Zhang Qipeng)
- fix: 时间插件返回大小错误 (Zhang Qipeng)
- fix: 插件区域图标显示不全 (Zhang Qipeng)
- fix: 蓝牙tips未及时更新 (Zhang Qipeng)
- fix: 分割线不居中 (Zhang Qipeng)
- fix: 任务栏显示区域异常 (Zhang Qipeng)
- fix: 修复左键任务栏上的声音插件tips不完整的bug (chenwei)
- fix(sound): 修改了音量设备标题字太小问题 (chenyunxiong)
- feat: 整理打印输出级别 (Fanpengcheng)
- fix: 修复有快捷键打开终端，窗口收回特效异常的问题 (Fanpengcheng)
- fix: 蓝牙设备连接成功后，移动端作为蓝牙客户端，连接成功后会必现图标异常及偶现文字异常 (yangyuyin)
- fix(blutetooth): 蓝牙插件弹框界面问题 (Li Tao)
- feat: 添加运行库依赖 (liuxing)
- fix(bluet): 修改了蓝牙界面问题 (Li Tao)
- fix: 智能隐藏时，窗口最大化并不能隐藏任务栏 (liuxing)
- feat: 任务栏gtest单元测试框架添加 (liuxing)
- fix(bluetooth): 当蓝牙适配器id相同时，为了防止内存泄露，不应该替换map的元素。 (chenyunxiong)
- feat: 避免反复设置窗口工作位置 (Fanpengcheng)
- fix: 重启进入桌面，任务栏消失 (Xie Chuan)
- feat: Initial packit setup (Robin Lee)
- feat: 任务栏插件显示大小新增支持自定义宽度(或高度) (苏义航)
- fix: 调用com.deepin.daemon.PowerManager接口来判断系统是否支持待机和休眠 (chenjun)
- feat: fix lintian error (Fanpengcheng)
- Revert "feat: 任务栏插件显示大小新增支持自定义宽度(或高度)" (Fanpengcheng)
- feat: 任务栏插件显示大小新增支持自定义宽度(或高度) (suyihang)
- fix: 使用root用户登陆时，dock右键没有切换用户选项 (dongrui)
- fix: 任务栏网络图标的tooltips显示空白 (Zhang Qipeng)
- fix(network): 修改了控制中心网络下网卡状态是“已连接”，任务栏单击网络图标​对应网卡后面的“对勾标识”不显示​ (Litao)
- fix: 任务栏音量拖到最右边概率性显示不是100% (xuyanghe)
- fix: 任务栏开机几率无法显示 (liuxing)
- fix: 任务栏授权管理图标在托盘区域的插件收缩键头两边来回驻留 (xiaoyaobing)
- fix: 任务栏位置调整左边，摩灯窗口还是从底部出来 (chengbo)
- fix: 紧急修复任务栏无法置顶的问题 (Fanpengcheng)
- fix :多次向右旋转屏幕导致任务栏消失 (Xie Chuan)
- fix: remove dbus service file (lxz)
- fix: cannot min/restore window (lxz)
- Revert "fix: show slow" (lxz)
- feat: Optimize code structure (Zhang Qipeng)
- fix: 调节任务栏音量与控制中心输出音量不同步 (xuyanghe)
- fix: qt找不到应用图标 (聂成)
- fix: 打开多个窗口在桌面，在任务栏预览窗口点击窗口关闭按钮，窗口被关闭，其它窗口被隐藏 (xiaoyaobing)
- feat: 自动化代码限制一下检测到未标记的新控件类，debug模式编译不通过 (Fanpengcheng)
- fix: Fix dde-dock incorrectly set to right angle (xmuli)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.21-1
- new upstream release: 5.3.0.21

* Tue Nov 10 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.13-1
- new upstream release: 5.3.0.13

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-4
- BR: qt5-qtbase-private-devel
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug  5 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.9.0-3
- Filter private library provides

* Thu Mar  7 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.9.0-2
- Change launcher icon to Fedora logo, Requires deepin-icon-theme and fedora-logos
- Requires onboard, required by a plugin
- Own %%{_sysconfdir}/%%{repo}/

* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 4.9.0-1
- Update to 4.9.0

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 4.8.9-1
- Update to 4.8.9

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 4.8.4.1-1
- Update to 4.8.4.1

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 4.8.4-1
- Update to 4.8.4

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 4.8.1-1
- Update to 4.8.1

* Mon Nov 12 2018 mosquito <sensor.wen@gmail.com> - 4.8.0-1
- Update to 4.8.0

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 4.7.2-1
- Update to 4.7.2

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 4.7.1.1-1
- Update to 4.7.1.1

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 4.6.9-1
- Update to 4.6.9

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 4.6.7-1
- Update to 4.6.7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 4.5.12-1
- Update to 4.5.12

* Sat Feb 10 2018 mosquito <sensor.wen@gmail.com> - 4.5.9.1-1
- Update to 4.5.9.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 mosquito <sensor.wen@gmail.com> - 4.5.9-1
- Update to 4.5.9

* Sat Dec  9 2017 mosquito <sensor.wen@gmail.com> - 4.5.7.1-1
- Update to 4.5.7.1

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 4.5.7-1
- Update to 4.5.7

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 4.5.1-1
- Update to 4.5.1

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 4.4.1-1
- Update to 4.4.1

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 4.3.4-1
- Update to 4.3.4

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.3.3-1.gitbf79f1c
- Update to 4.3.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.2.1-1.git42610ae
- Update to 4.2.1

* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 4.1.4-1.gitd772fe2
- Update to 4.1.4

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 4.1.3-1.git26f189d
- Update to 4.1.3

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.8-1.gita882590
- Update to 4.0.8

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.7-1
- Update to version 4.0.7 and renamed to deepin-dock

* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.6-1
- Update to version 4.0.6

* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-2
- Rebuild with newer deepin-tool-kit

* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-1
- Initial package build
