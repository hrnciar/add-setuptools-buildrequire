%global repo qt5platform-plugins
%global __provides_exclude_from ^%{_qt5_plugindir}/platforms/.*\\.so$

Name:           deepin-%{repo}
Version:        5.0.21
Release:        5%{?dist}
Summary:        Qt platform integration plugins for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(mtdev)
# for libQt5EdidSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
BuildRequires: make
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Provides:       deepin-qt5dxcb-plugin = %{version}-%{release}
Provides:       deepin-qt5dxcb-plugin%{?_isa} = %{version}-%{release}
Obsoletes:      deepin-qt5dxcb-plugin < 5.0.21

%description
%{repo} is the
%{summary}.

%prep
%autosetup -p1 -n %{repo}-%{version}
rm -r xcb/libqt5xcbqpa-dev wayland/qtwayland-dev

# Disable wayland for now: https://github.com/linuxdeepin/qt5platform-plugins/issues/47
sed -i '/wayland/d' qt5platform-plugins.pro

sed -i 's|error(Not support Qt Version: .*)|INCLUDEPATH += %{_qt5_includedir}/QtXcb|' xcb/linux.pri

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_qt5_plugindir}/platforms/libdxcb.so

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.21-4
- rebuild (qt5)

* Thu Nov 19 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.21-3
- Provides deepin-qt5dxcb-plugin%%{?_isa}

* Sat Nov 14 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.21-2
- Filter private so from Provides

* Fri Nov 13 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.21-1
- Review request for rename from deepin-qt5dxcb-plugin
