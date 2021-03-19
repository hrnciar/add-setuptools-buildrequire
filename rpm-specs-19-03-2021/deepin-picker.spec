Name:           deepin-picker
Version:        5.0.10
Release:        2%{!?openeuler:%dist}
Summary:        A color picker tool for deepin
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# PATCHES FROM SOURCE GIT:

# fix: 修改了Qt5.15编译失败
# Author: wangyu <wangyu@uniontech.com>
Patch0001: 0001-fix-Qt5.15.patch

# fix: 修改了未添加QPainterPath导致Qt5.15编译失败
# Author: wangyu <wangyu@uniontech.com>
Patch0002: 0002-fix-QPainterPath-Qt5.15.patch

# fix: Remove unrecognised category `Picker`
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0003: 0003-fix-Remove-unrecognised-category-Picker.patch


BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
%if 0%{?openeuler}
BuildRequires: qt5-devel
%else
BuildRequires: qt5-linguist
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
Requires:      hicolor-icon-theme
%endif
BuildRequires: libxcb-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel

BuildRequires: pkgconfig(dtkwidget)
BuildRequires: pkgconfig(dtkgui)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: make

%description
%{summary}.

%prep
%autosetup -p1

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 ../
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/com.deepin.Picker.service
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.10-1
- new upstream release: 5.0.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Release 5.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 1.6.4-1
- Update to 1.6.4

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 1.6.3-1
- Update to 1.6.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.1-2
- Remove obsolete scriptlets

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 1.1-1
- Update to 1.1

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 1.0-1
- Update to 1.0

* Fri Oct 13 2017 mosquito <sensor.wen@gmail.com> - 0.4-1
- Initial package
