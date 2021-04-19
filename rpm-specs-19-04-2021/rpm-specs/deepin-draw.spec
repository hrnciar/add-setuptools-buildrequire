Name:           deepin-draw
Version:        5.8.0.20
Release:        2%{?dist}
Summary:        A lightweight drawing tool for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-draw
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# PATCHES FROM SOURCE GIT:

# dwidget include
# Author: Robin Lee <cheeselee@fedoraproject.org>
Patch0001: 0001-dwidget-include.patch


BuildRequires:  gcc-c++
BuildRequires:  freeimage-devel
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
BuildRequires:  desktop-file-utils
BuildRequires: make
Requires:       deepin-notifications
Requires:       deepin-qt5integration

%description
A lightweight drawing tool for Linux Deepin.

%prep
%autosetup -p1
sed -i '/include <DGraphicsView>/i #include <QFileDevice>' frame/cgraphicsview.h
sed -i '/include <QPainter>/a #include <QMouseEvent>' widgets/ciconbutton.cpp

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.8.0.20-1
- new upstream release: 5.8.0.20

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 mosquito <sensor.wen@gmail.com> - 1.0.0-1
- Initial package build
