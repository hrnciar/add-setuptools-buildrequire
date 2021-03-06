Name:           deepin-calculator
Version:        5.6.0.10
Release:        1%{?dist}
Summary:        An easy to use calculator for ordinary users
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-calculator
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# fix: build failures under Qt 5.15
# Author: Felix Yan <felixonmars@archlinux.org>
Patch0001: 0001-fix-build-failures-under-Qt-5.15.patch


BuildRequires:  qt5-linguist
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -p1
sed -i 's|59 Temple Place, Suite 330|51 Franklin Street, Fifth Floor|;
        s|Boston, MA 02111-1307 USA.|Boston, MA 02110-1335, USA.|' src/math/*.{c,h}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Fri Mar 12 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.6.0.10-1
- fix: fix bug--57861 (jingzhou)
- fix: fix bug--55167 (jingzhou)
- chore: 修改中文下未显示翻译的问题 (jingzhou)
- chore: 修改选中删除和退格键事件 (jingzhou)
- chore: UT test 路径调整 (jingzhou)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.6.0.1-1
- new upstream release: 5.6.0.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Release 5.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 1.0.10-1
- Update to 1.0.10

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 1.0.9-1
- Update to 1.0.9

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 1.0.5-1
- Update to 1.0.5

* Mon Jul 23 2018 mosquito <sensor.wen@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 mosquito <sensor.wen@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Sat Dec  9 2017 mosquito <sensor.wen@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 0.9.0-1
- Initial package build
