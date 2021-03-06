%global commit      162d11f8ee73b3859ad42b5f69cdd355d033b8a7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210218

%global srcname files
%global appname io.elementary.files

%global __provides_exclude_from ^%{_libdir}/(gtk-3.0)|(%{appname})/.*\\.so$

Name:           elementary-files
Summary:        File manager from elementary
Version:        4.5.0
Release:        3.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

# Install contracts for compressing/uncompressing files with file-roller
Source1:        file-roller-compress.contract
Source2:        file-roller-extract-here.contract

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.47.0
BuildRequires:  vala >= 0.48.2

BuildRequires:  pkgconfig(cloudproviders) >= 0.3.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0) >= 2.40
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.25
BuildRequires:  pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0
BuildRequires:  pkgconfig(libnotify) >= 0.7.2
BuildRequires:  pkgconfig(pango) >= 1.1.2
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(sqlite3)

Requires:       contractor
Requires:       file-roller

%description
The simple, powerful, and sexy file manager from elementary.


%package        portal
Summary:        File manager from elementary (flatpak file chooser portal)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xdg-desktop-portal
%description    portal
The simple, powerful, and sexy file manager from elementary.

This package contains a file chooser portal implementation for flatpak.


%package        devel
Summary:        File manager from elementary (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The simple, powerful, and sexy file manager from elementary.

This package contains the development headers.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson -Dwith-zeitgeist=disabled
%meson_build


%install
%meson_install

%find_lang %{appname}

# remove unused pixmaps
rm -r %{buildroot}/%{_datadir}/pixmaps

# install file-roller contracts
mkdir -p %{buildroot}/%{_datadir}/contractor
cp -pav %{SOURCE1} %{buildroot}/%{_datadir}/contractor/
cp -pav %{SOURCE2} %{buildroot}/%{_datadir}/contractor/


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%post portal
%systemd_user_post %{appname}.xdg-desktop-portal.service

%preun portal
%systemd_user_preun %{appname}.xdg-desktop-portal.service


%files -f %{appname}.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{appname}
%{_bindir}/%{appname}-daemon
%{_bindir}/%{appname}-pkexec

%{_libdir}/%{appname}/
%{_libdir}/libpantheon-files-core.so.4*
%{_libdir}/libpantheon-files-widgets.so.4*

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/contractor/*.contract
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/dbus-1/services/%{appname}.Filemanager1.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/polkit-1/actions/%{appname}.policy

%files portal
%{_libexecdir}/%{appname}.xdg-desktop-portal
%{_userunitdir}/%{appname}.xdg-desktop-portal.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.elementary.files.service
%{_datadir}/xdg-desktop-portal/portals/io.elementary.files.portal

%files devel
%{_includedir}/pantheon-files-core/
%{_includedir}/pantheon-files-widgets.h

%{_libdir}/libpantheon-files-core.so
%{_libdir}/libpantheon-files-widgets.so

%{_libdir}/pkgconfig/pantheon-files-core.pc
%{_libdir}/pkgconfig/pantheon-files-widgets.pc

%{_datadir}/vala/vapi/pantheon-files-core.vapi
%{_datadir}/vala/vapi/pantheon-files-widgets.vapi


%changelog
* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 4.5.0-3.20210218git162d11f
- Bump to commit 162d11f. Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Fabio Valentini <decathorpe@gmail.com> - 4.5.0-1
- Update to version 4.5.0.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Fabio Valentini <decathorpe@gmail.com> - 4.4.4-1
- Update to version 4.4.4.

* Tue Jun 02 2020 Fabio Valentini <decathorpe@gmail.com> - 4.4.3-1
- Update to version 4.4.3.
- Disable useless libunity / zeitgeist integrations.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 4.4.2-1
- Update to version 4.4.2.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 4.4.1-1
- Update to version 4.4.1.

* Fri Feb 14 2020 Fabio Valentini <decathorpe@gmail.com> - 4.4.0-1
- Update to version 4.4.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0-1
- Update to version 4.3.0.

* Sat Nov 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0-2
- Include upstream patch to fix compilation with newer versions of vala.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0-1
- Update to version 4.2.0.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9-1
- Update to version 4.1.9.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8-1
- Update to version 4.1.8.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 4.1.7-2
- Rebuild with Meson fix for #1699099

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.7-1
- Update to version 4.1.7.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6-1
- Update to version 4.1.6.

* Thu Feb 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5-1
- Update to version 4.1.5.

* Thu Jan 31 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.4-1
- Update to version 4.1.4.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0-1
- Update to version 4.0.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5-9.20180826.git39b673c
- Initial package renamed from pantheon-files.

