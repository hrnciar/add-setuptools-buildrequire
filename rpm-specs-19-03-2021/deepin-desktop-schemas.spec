Name:           deepin-desktop-schemas
Version:        5.8.44
Release:        1%{?dist}
Summary:        GSettings deepin desktop-wide schemas
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{name}_%{version}.orig.tar.xz
%endif

BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  glib2
#add jzy
BuildRequires:  compiler(go-compiler)
BuildRequires:  golang(pkg.deepin.io/lib/keyfile)
BuildRequires:  make
ExclusiveArch:  %{go_arches}

Requires:       dconf
Requires:       deepin-gtk-theme
Requires:       deepin-icon-theme
Requires:       deepin-sound-theme
Obsoletes:      deepin-artwork-themes <= 15.12.4

%description
%{summary}.

%prep
%autosetup -p1

# fix default background url
sed -i '/picture-uri/s|default_background.jpg|default.png|' \
    overrides/common/com.deepin.wrap.gnome.desktop.override
sed -i 's|python|python3|' Makefile tools/overrides.py

%build
export GOPATH=%{gopath}
%make_build ARCH=x86

%install
%make_install PREFIX=%{_prefix}
cp %{buildroot}/usr/share/deepin-desktop-schemas/server-override %{buildroot}/usr/share/glib-2.0/schemas/91_deepin_product.gschema.override

%check
make test

%files
%doc README.md
%license LICENSE
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/deepin-appstore/
%{_datadir}/deepin-app-store/
%{_datadir}/%{name}/


%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.8.44-1
- fix: 更新社区版应用预装列表 (chenwei)
- feat: 更新个人版应用预装列表 (chenwei)
- feat: 更新应用预装列表 (chenwei)
- feat: 更新应用预装列表 (chenwei)
- feat: 添加通知相关的配置文件 (chenwei)
- feat(launcher): add option to enable search package name (xiejiabo)
- feat: 更新启动器不可卸载应用的列表中的输入法项 (Fanpengcheng)
- feat: 更新启动器不可卸载应用的列表 (Fanpengcheng)
- feat(startdde): quick black screen is default true (hubenchang0515)
- fix: 关闭turbo加速功能 (Fanpengcheng)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.8.0.20-1
- new upstream release: 5.8.0.20

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug  9 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.13.9-1
- Release 3.13.9

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.12.0-2
- Obsoletes deepin-artwork-themes

* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 3.11.0-1
- Update to 3.11.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Mon Aug 06 2018 Zamir SUN <zsun@fedoraproject.org> - 3.2.18-2
- In Rawhide (f29) python command do not exist now.

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 3.2.18-1
- Update to 3.2.18

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 3.2.15-1
- Update to 3.2.15

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2.6-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 3.2.6-1
- Update to 3.2.6

* Sat Feb 10 2018 mosquito <sensor.wen@gmail.com> - 3.2.5-1
- Update to 3.2.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 mosquito <sensor.wen@gmail.com> - 3.2.4-1
- Update to 3.2.4

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 3.2.3-1
- Update to 3.2.3

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 3.1.19-1
- Update to 3.1.19

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 3.1.18-1
- Update to 3.1.18

* Fri Oct 13 2017 mosquito <sensor.wen@gmail.com> - 3.1.17-1
- Update to 3.1.17

* Sat Aug 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.16-1
- Update to 3.1.16

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 3.1.15-1
- Update to 3.1.15

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 3.1.14-1.giteeea1d4
- Update to 3.1.14

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.13-1.git95af7cd
- Update to 3.1.13

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.1.6-1.gita41ca06
- Update to 3.1.6

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.1-1.gitf6ffe70
- Update to 3.1.1

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.13-1.git10efc5e
- Update to 3.0.13

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-1
- Update to version 3.0.13

* Sat Dec 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.12-1
- Update to version 3.0.12

* Thu Oct 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.11-1
- Update to version 3.0.11

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.10-1
- Initial package build
