%define specrelease 1%{?dist}
%if 0%{?openeuler}
%define specrelease 1
%global _missing_build_ids_terminate_build 0
%global debug_package   %{nil}
%global dde_prefix dde
%else
%global dde_prefix deepin
%endif

Name:           startdde
Version:        5.6.0.35.1
Release:        %{specrelease}
Summary:        Starter of deepin desktop environment
License:        GPLv3
URL:            https://github.com/linuxdeepin/startdde
%if 0%{?openeuler}
Source0:        %{name}_%{version}.orig.tar.xz

BuildRequires:  gocode
Requires:       gocode
Requires:       libXfixes
Requires:       libXcursor
%else
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}

BuildRequires:  compiler(go-compiler)
BuildRequires:  golang(pkg.deepin.io/dde/api/dxinput)
BuildRequires:  golang(pkg.deepin.io/lib)
BuildRequires:  golang(github.com/godbus/dbus)
BuildRequires:  golang(github.com/linuxdeepin/go-x11-client)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(golang.org/x/xerrors)
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
%endif

BuildRequires:  golang
BuildRequires:  jq
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  libXcursor-devel
BuildRequires:  libXfixes-devel
BuildRequires:  gtk3-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(gudev-1.0)

Provides:       x-session-manager
Requires:       %{dde_prefix}-daemon
Requires:       procps
Requires:       deepin-desktop-schemas
Requires:       %{dde_prefix}-kwin
Recommends:     %{dde_prefix}-qt5integration

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}
## Scripts in /etc/X11/Xsession.d are not executed after xorg start
sed -i 's|X11/Xsession.d|X11/xinit/xinitrc.d|g' Makefile
# fix deepin-daemon executables path
find * -type f -not -path "rpm/*" -print0 | xargs -0 sed -i 's:/lib/deepin-daemon/:/libexec/deepin-daemon/:'
# fix dde-polkit-agent path
sed -i '/polkit/s|lib|libexec|' watchdog/dde_polkit_agent.go

%build
%if 0%{?openeuler}
export GOPATH=/usr/share/gocode
%make_build GO_BUILD_FLAGS=-trimpath
%else
export GOPATH="%{gopath}"
%make_build GO_BUILD_FLAGS="%{gobuildflags}"
# rebuild other executables with different build-ids
for cmd in fix-xauthority-perm greeter-display-daemon; do
    rm $cmd
    %make_build $cmd GO_BUILD_FLAGS="%{gobuildflags}"
done
%endif

%install
%make_install

%post
xsOptsFile=/etc/X11/Xsession.options
update-alternatives --install /usr/bin/x-session-manager x-session-manager \
    /usr/bin/startdde 90 || true
if [ -f $xsOptsFile ];then
	sed -i '/^use-ssh-agent/d' $xsOptsFile
	if ! grep '^no-use-ssh-agent' $xsOptsFile >/dev/null; then
		echo no-use-ssh-agent >> $xsOptsFile
	fi
fi

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/X11/xinit/xinitrc.d/00deepin-dde-env
%{_sysconfdir}/X11/xinit/xinitrc.d/01deepin-profile
%{_sysconfdir}/profile.d/deepin-xdg-dir.sh
%{_bindir}/%{name}
%{_sbindir}/deepin-fix-xauthority-perm
%{_datadir}/xsessions/deepin.desktop
%{_datadir}/lightdm/lightdm.conf.d/60-deepin.conf
%{_datadir}/%{name}/
%{_libexecdir}/deepin-daemon/greeter-display-daemon

%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.6.0.35.1-1
- fix(session): ???????????????????????????????????????????????????????????? (chenyunxiong)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.6.0.10-1
- new upstream release: 5.6.0.10

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Release 5.0.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.12.1-3
- Add a patch to fix RHBZ#1711001

* Thu May 16 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.12.1-2
- Fix fallback session script path (RHBZ#1706281)

* Wed Feb 27 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.12.1-1
- Update to 3.12.1

* Tue Feb 19 2019 mosquito <sensor.wen@gmail.com> - 3.11.0-1
- Update to 3.11.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Mon Aug 20 2018 mosquito <sensor.wen@gmail.com> - 3.1.33-1
- Update to 3.1.33

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.1.24-3
- Rebuild with fixed binutils

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 3.1.24-1
- Update to 3.1.24

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 mosquito <sensor.wen@gmail.com> - 3.1.23-1
- Update to 3.1.23

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 3.1.22-1
- Update to 3.1.22

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 3.1.17-1
- Update to 3.1.17

* Fri Oct 13 2017 mosquito <sensor.wen@gmail.com> - 3.1.16-1
- Update to 3.1.16

* Sat Aug 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.15-1
- Update to 3.1.15

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 3.1.14-1
- Update to 3.1.14

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.13-1.git08de5b9
- Update to 3.1.13

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.1.8-1.gita9130d0
- Update to 3.1.8

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.2-1.gitd7c1216
- Update to 3.1.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.14.1-1.gitd3ba123
- Update to 3.0.14.1

* Wed Dec 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-2
- Updated GO dependencies
- Fixed wrong system path for dde-readahead

* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-1
- Update to package 3.0.13

* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.12-1
- Update to package 3.0.12

* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.11-1
- Initial package build
