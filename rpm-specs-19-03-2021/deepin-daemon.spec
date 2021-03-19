%global _smp_mflags -j1

%if 0%{?fedora} == 0
%global debug_package   %{nil}
%global _unpackaged_files_terminate_build 0
%global _missing_build_ids_terminate_build 0
%define __debug_install_post   \
   %{_rpmconfigdir}/find-debuginfo.sh %{?_find_debuginfo_opts} "%{_builddir}/%{?buildsubdir}"\
%{nil}
%endif

%global sname deepin-daemon
%global repo dde-daemon
%global release_name server-industry

%if 0%{?fedora}
Name:           %{sname}
%else
Name:           %{repo}
%endif
Version:        5.12.52
Release:        1%{?fedora:%dist}
Summary:        Daemon handling the DDE session settings
License:        GPLv3
%if 0%{?fedora}
URL:            https://github.com/linuxdeepin/dde-daemon
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
# upstream default mono font set to 'Noto Mono', which is not yet available in
# Fedora. We change to 'Noto Sans Mono'
Source1:        fontconfig.json
Source2:        %{sname}.sysusers
%else
URL:            http://shuttle.corp.deepin.com/cache/tasks/18802/unstable-amd64/
Source0:        %{repo}-%{version}.orig.tar.xz

# fix build with go 1.16 on Fedora
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0004: 0004-fix-build-with-go-1.16-on-Fedora.patch


# feat(image_effect): run `dde-pixmix` under xvfb-run
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0003: 0003-feat-image_effect-run-dde-pixmix-under-xvfb-run.patch


# fix: rpm fix `deepin-api` path
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0002: 0002-fix-rpm-fix-deepin-api-path.patch


# feat: rpm recomments `lshw`
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0001: 0001-feat-rpm-recomments-lshw.patch

%endif

BuildRequires:  python3
%if 0%{?fedora}
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
BuildRequires:  golang(pkg.deepin.io/dde/api/dxinput) >= 3.1.26
BuildRequires:  golang(github.com/linuxdeepin/go-dbus-factory/org.bluez)
BuildRequires:  golang(github.com/linuxdeepin/go-x11-client)
BuildRequires:  golang(github.com/BurntSushi/xgb)
BuildRequires:  golang(github.com/BurntSushi/xgbutil)
BuildRequires:  golang(github.com/axgle/mahonia)
BuildRequires:  golang(github.com/msteinert/pam)
BuildRequires:  golang(github.com/nfnt/resize)
BuildRequires:  golang(github.com/cryptix/wav)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(github.com/gosexy/gettext)
BuildRequires:  golang(github.com/jinzhu/gorm)
BuildRequires:  golang(github.com/jinzhu/gorm/dialects/sqlite)
BuildRequires:  golang(github.com/kelvins/sunrisesunset)
BuildRequires:  golang(github.com/rickb777/date)
BuildRequires:  golang(github.com/teambition/rrule-go)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/Lofanmi/pinyin-golang/pinyin)
%else
BuildRequires:  gocode
BuildRequires:  ddcutil-devel
BuildRequires:  resize-devel
BuildRequires:  gorm-devel
BuildRequires:  inflection-devel
%endif
BuildRequires:  compiler(go-compiler)
BuildRequires:  deepin-gettext-tools
BuildRequires:  fontpackages-devel
BuildRequires:  librsvg2-tools
BuildRequires:  pam-devel >= 1.3.1
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  systemd-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  libnl3-devel
BuildRequires:  libgudev-devel
BuildRequires:  libinput-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libXcursor-devel
BuildRequires:  pkgconfig(sqlite3)

Requires:       bluez-libs%{?_isa}
Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
%if 0%{?fedora}
Requires:       deepin-session-ui
Requires:       deepin-polkit-agent
%else
Requires:       dde-session-ui
Requires:       dde-polkit-agent
%endif
Requires:       rfkill
Requires:       gvfs
Requires:       iw
Requires:       %{_bindir}/xvfb-run

Recommends:     lshw
Recommends:     iso-codes
Recommends:     imwheel
Recommends:     mobile-broadband-provider-info
Recommends:     google-noto-mono-fonts
Recommends:     google-noto-sans-fonts
%if 0%{?fedora}
Recommends:     google-noto-sans-mono-fonts
%endif

%description
Daemon handling the DDE session settings

%prep
%autosetup -p1 -n %{repo}-%{version}
patch langselector/locale.go < rpm/locale.go.patch

# Fix library exec path
sed -i '/deepin/s|lib|libexec|' Makefile
sed -i '/systemd/s|lib|usr/lib|' Makefile
sed -i 's:/lib/udev/rules.d:%{_udevrulesdir}:' Makefile
sed -i '/${DESTDIR}\/usr\/lib\/deepin-daemon\/service-trigger/s|${DESTDIR}/usr/lib/deepin-daemon/service-trigger|${DESTDIR}/usr/libexec/deepin-daemon/service-trigger|g' Makefile
sed -i '/${DESTDIR}${PREFIX}\/lib\/deepin-daemon/s|${DESTDIR}${PREFIX}/lib/deepin-daemon|${DESTDIR}${PREFIX}/usr/libexec/deepin-daemon|g' Makefile
sed -i 's|lib/NetworkManager|libexec|' network/utils_test.go

for file in $(grep "/usr/lib/deepin-daemon" * -nR |awk -F: '{print $1}')
do
    sed -i 's|/usr/lib/deepin-daemon|%{_libexecdir}/deepin-daemon|g' $file
done
for file in $(grep "/usr/lib/deepin-api" * -nR |awk -F: '{print $1}')
do
    sed -i 's|/usr/lib/deepin-api|%{_libexecdir}/deepin-api|g' $file
done

# Fix grub.cfg path
sed -i 's|boot/grub|boot/grub2|' grub2/{grub2,grub_params,theme}.go

# Fix activate services failed (Permission denied)
# dbus service
pushd misc/system-services/
sed -i '$aSystemdService=deepin-accounts-daemon.service' com.deepin.system.Power.service \
    com.deepin.daemon.{Accounts,Apps,Daemon}.service \
    com.deepin.daemon.{Gesture,SwapSchedHelper,Timedated}.service
sed -i '$aSystemdService=dbus-com.deepin.dde.lockservice.service' com.deepin.dde.LockService.service
popd
# systemd service
cat > misc/systemd/services/dbus-com.deepin.dde.lockservice.service <<EOF
[Unit]
Description=Deepin Lock Service
Wants=user.slice dbus.socket
After=user.slice dbus.socket

[Service]
Type=dbus
BusName=com.deepin.dde.LockService
ExecStart=%{_libexecdir}/%{sname}/dde-lockservice

[Install]
WantedBy=graphical.target
EOF

# Replace reference of google-chrome to chromium-browser
sed -i 's/google-chrome/chromium-browser/g' misc/dde-daemon/mime/data.json

%build
BUILDID="0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
%if 0%{?fedora}
export GOPATH="$(pwd)/build:%{gopath}"
export %{gomodulesmode}
%else
export GOPATH=/usr/share/gocode
%endif
%make_build GO_BUILD_FLAGS=-trimpath GOBUILD="go build -compiler gc -ldflags \"-B $BUILDID\""

%install
BUILDID="0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
%if 0%{?fedora}
export GOPATH="$(pwd)/build:%{gopath}"
export %{gomodulesmode}
%else
export GOPATH=/usr/share/gocode
%endif
%make_install GOBUILD="go build -compiler gc -ldflags \"-B $BUILDID\""

%if 0%{?fedora}
install -Dm644 %{SOURCE2} %{buildroot}/usr/lib/sysusers.d/%{name}.conf
%endif

# fix systemd/logind config
install -d %{buildroot}/usr/lib/systemd/logind.conf.d/
cat > %{buildroot}/usr/lib/systemd/logind.conf.d/10-%{sname}.conf <<EOF
[Login]
HandlePowerKey=ignore
HandleSuspendKey=ignore
EOF

%if 0%{?fedora}
# install default settings
install -Dm644 %{SOURCE1} \
    %{buildroot}%{_datadir}/deepin-default-settings/fontconfig.json
%endif

%find_lang %{repo}

%post
if [ $1 -ge 1 ]; then
  systemd-sysusers %{sname}.conf
  %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
    x-terminal-emulator %{_libexecdir}/%{sname}/default-terminal 30
fi

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove x-terminal-emulator \
    %{_libexecdir}/%{sname}/default-terminal
fi

%postun
if [ $1 -eq 0 ]; then
  rm -f /var/cache/deepin/mark-setup-network-services
  rm -f /var/log/deepin.log 
fi

%files -f %{repo}.lang
%doc README.md
%license LICENSE
%{_sysconfdir}/pam.d/deepin-auth-keyboard
%{_sysconfdir}/NetworkManager/conf.d/deepin.dde.daemon.conf
%{_sysconfdir}/modules-load.d/i2c_dev.conf
%{_libexecdir}/%{sname}/
%{_prefix}/lib/systemd/logind.conf.d/10-%{sname}.conf
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/status/*
%{_datadir}/%{repo}/
%{_datadir}/dde/
%{_datadir}/polkit-1/actions/*.policy
%{_var}/cache/appearance/
%{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Accounts.pkla
%{_sysconfdir}/acpi/actions/deepin_lid.sh
%{_sysconfdir}/acpi/events/deepin_lid
# This directory is not provided by any other package.
%dir %{_sysconfdir}/pulse/daemon.conf.d
%{_sysconfdir}/pulse/daemon.conf.d/10-deepin.conf
%{_udevrulesdir}/80-deepin-fprintd.rules
%{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Fprintd.pkla
%{_unitdir}/dbus-com.deepin.dde.lockservice.service
%{_unitdir}/deepin-accounts-daemon.service
%{_unitdir}/hwclock_stop.service
%if 0%{?fedora}
%{_sysusersdir}/%{name}.conf
%{_datadir}/deepin-default-settings/
%exclude %{_sysconfdir}/default/grub.d/10_deepin.cfg
%exclude %{_sysconfdir}/grub.d/35_deepin_gfxmode
%exclude %{_libexecdir}/%{name}/grub2
%exclude %{_datadir}/dbus-1/system-services/com.deepin.daemon.Grub2.service
%exclude %{_datadir}/dbus-1/system.d/com.deepin.daemon.Grub2.conf
%exclude %{_datadir}/polkit-1/actions/com.deepin.daemon.Grub2.policy
%exclude %{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Grub2.pkla
%else
%{_sysconfdir}/default/grub.d/10_deepin.cfg
%{_sysconfdir}/grub.d/35_deepin_gfxmode
%{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Grub2.pkla
%endif

%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.12.52-1
- feat(network): GetActiveConnectionInfo adds the SpecificObject property (zsien)
- feat: activeConnection adds the SpecificPath property (zsien)
- chore(timedate): 修改zone测试用例 (lichangze)
- chore(audio): 修改pulseaudio的错误拼写 (lichangze)
- fix(grub2): 更新grub配置时没有语言环境变量 (electricface)
- fix(power): 修复待机时电量变化，唤醒后低电量屏保不更新的问题 (xiejiabo)
- fix(launcher): 搜索支持多音字 (xiejiabo)
- fix(portal): 根据PORTAL_ENABLE环境变量判断当前是否启动portal认证 (chenyunxiong)
- fix(bluetooth): 修复蓝牙连接导致session-daemon崩溃的问题 (lichangze)
- fix(network): 修复连接无线网络时候不弹出正在连接弹窗的问题 (lichangze)
- fix(accounts): 新增身份认证失败对应的翻译。 (聂成)
- fix(accounts): 修复认证弹框时，点取消和输入错误密码时，产生的错误信息一致，需要区分。 (聂成)
- fix(network): 修复每次注销或重启无线网卡状态从“已断开”变成“已禁用”问题 (lichangze)
- fix(audio): 修复不同端口音量增强开关状态会互相影响的问题 (lichangze)
- fix(network): reboot系统之后，未插网线的网口，网卡状态从“已断开”变成“已禁用”问题 (Li Tao)
- fix(network): 修复NetworkManager实际状态与保存的配置信息不符导致的状态问题。 (chenyunxiong)
- fix(accounts): 导出root用户的DBus服务，供其他应用调用 (chenyunxiong)
- fix(launcher): 修复拼音简拼搜索精确度问题 (xiejiabo)
- fix: 修复从桌面打开应用时,新装应用标记不消失的问题 (lichangze)
- fix: 标准用户显示在授权列表中 (Zhang Qipeng)
- chore(coverage): test coverage statistics (hubenchang0515)
- fix(display): Clear tty print data (wubowen)
- feat(launcher): 依产品要求,去除对generic name的搜索 (xiejiabo)
- fix(inputdevices): 修复只有触摸板时默认双击间隔时间太短问题 (luokai)
- chore(appearance): 更新翻译文件 (lichangze)
- chore(plymouth): 恢复同步设置plymouth的接口 (lichangze)
- feat(appearance): 完成修改屏幕缩放比例后通知显示的修改 (lichangze)
- feat: 蓝牙传输文件横幅停留时间改为15s (yangyuyin)
- fix(appearance): 修复版本升级后壁纸库出现代码路径 (weizhixiang)
- fix: 系统无待机功能 (BigShuaiGe)
- fix(audio): 输入音量显示不正常 (chengbo)
- fix(network): 笔记本开盖待机唤醒后网络连接多次 (chengbo)
- fix(bluetooth): 修复蓝牙设备被忽略后重新回到我的设备列表的问题 (weizhixiang)
- feat(launcher): 搜索优化新需求 (xiejiabo)
- fix(accounts): 初始化保存的多任务视图当前所在工作区 (weizhixiang)
- fix: 声卡没切换成功时，无法获取相应sink信息 (BigShuaiGe)
- fix: 设置壁纸后，壁纸预览展示的壁纸顺序不正确 (BigShuaiGe)
- fix(keybinding): use new module to display TouchpadToggle (hubenchang0515)
- fix: register fullscreen will not emit motion signal (longqi)
- fix(keyevent): add module keyevent (hubenchang0515)
- fix: ScalePlymouth timeout (longqi)
- feat: add signal CursorShowAgain for XEventMonitor (longqi)
- fix(network): WiFi strength not being refreshed (zsien)
- fix: Disable grub-related functions on Fedora (Robin Lee)
- fix(network): 修复开关VPN按钮和重启时，VPN的回连不上的问题 (chenyunxiong)
- fix(appearance): 修复添加工作区后登录桌面过程中背景图片显示错误的问题 (weizhixiang)
- chore(power_manager): 给 canSuspend 补充一个待办 (electricface)
- fix(power_manager): 判断能否待机的条件 (electricface)
- fix: include sysuser config file for Fedora (Robin Lee)
- fix: 多声道输出端口启用按钮关闭后切换其他端口，再次切回多声道失败 (BigShuaiGe)
- chore: debian 目录增加 abi.json 文件 (wubowen)
- fix: 控制中心声音模块启用按钮关闭后再打开，无音效输出 (BigShuaiGe)
- fix(bluetooth): 修复蓝牙其他设备列表静置三分钟后，点击允许蓝牙设备可被发现开关，设备列表会消失的问题 (weizhixiang)
- fix(Audio): 切换新用户发现声音输入设备端口显示为空 (chengbo)
- feat: 社区版订制需求，保存窗口圆角值 (chengbo)
- fix(dde-greeter-setter): use xsettingsd to config scale (hubenchang0515)
- feat(grub2): 配合grub的名称修改过滤条件 (hubenchang0515)
- feat: remove pam module (zsien)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.11.0.36-3
- run dde-pixmix under xvfb-run

* Tue Dec 01 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.11.0.36-2
- Recommends lshw
- Fix path for deepin-api

* Tue Nov 10 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.11.0.36-1
- new upstream release: 5.11.0.36

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0
- Disable grub-related functions

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.23.0-2
- Replace reference of google-chrome to chromium-browser

* Tue Feb 26 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.23.0-1
- Update to 3.23.0
- default-settings update to 2019.1.30
- Disable parallel building by now

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 3.22.0-1
- Update to 3.22.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.0-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 3.7.0-3
- acpid is unavailable in ppc64le

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 3.7.0-2
- Build test for ppc64le and aarch64

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 3.2.20-1
- Update to 3.2.20

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 mosquito <sensor.wen@gmail.com> - 3.2.9-2
- Nothing providers grub2 in s390x and armv7hl.

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 3.2.9-1
- Update to 3.2.9

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.2.8-2
- Rebuilt for switch to libxcrypt

* Fri Dec 22 2017 mosquito <sensor.wen@gmail.com> - 3.2.8-1
- Update to 3.2.8

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 3.2.7-1
- Update to 3.2.7

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Sat Oct 14 2017 mosquito <sensor.wen@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Wed Aug 30 2017 mosquito <sensor.wen@gmail.com> - 3.1.19-2
- Add fontconfig settings

* Sat Aug 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.19-1
- Update to 3.1.19

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 3.1.18-1
- Update to 3.1.18

* Wed Aug  2 2017 mosquito <sensor.wen@gmail.com> - 3.1.17-1
- Update to 3.1.17

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 3.1.16.1-1
- Update to 3.1.16.1

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 3.1.14-1.git0f8418a
- Update to 3.1.14

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.13-1.git03541ad
- Update to 3.1.13

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.1.9-1.git82313d2
- Update to 3.1.9

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.3-1.git87df955
- Update to 3.1.3

* Fri Jan 20 2017 mosquito <sensor.wen@gmail.com> - 3.0.25.2-1.gitcfbe9c8
- Update to 3.0.25.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.25.1-1.gitde04735
- Update to 3.0.25.1

* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Changed GOLANG dependencies

* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to version 3.0.24

* Mon Oct 31 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.23-1
- Upgrade to version 3.0.23

* Sun Sep 25 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.22-1
- Initial package build
