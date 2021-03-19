%global commit      b90e59ae351b5aa099a3f5982752d76f9c5c039e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210217

%global srcname applications-menu
%global appname io.elementary.wingpanel.applications-menu

%global __provides_exclude_from ^%{_libdir}/(wingpanel|%{appname})/.*\\.so$

Name:           wingpanel-applications-menu
Summary:        Lightweight and stylish app launcher
Version:        2.7.1
Release:        4.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.32.1

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       redhat-menus

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
The lightweight and stylish app launcher from elementary.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson -Dwith-zeitgeist=false
%meson_build


%install
%meson_install

%find_lang slingshot


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f slingshot.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/menus/pantheon-applications.menu

%{_libdir}/%{appname}/
%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.applications-menu.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 2.7.1-4.20210217gitb90e59a
- Bump to commit b90e59a. Rebuilt for granite 6 soname bump and wingpanel 3.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Fabio Valentini <decathorpe@gmail.com> - 2.7.1-1
- Update to version 2.7.1.
- Drop useless unity and zeitgeist dependencies.

* Sat May 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.7.0-1
- Update to version 2.7.0.

* Sat Apr 18 2020 Fabio Valentini <decathorpe@gmail.com> - 2.6.0-1
- Update to version 2.6.0.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0-1
- Update to version 2.5.0.
- Switch to meson build system.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4-1
- Update to version 2.4.4.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3-1
- Update to version 2.4.3.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.2-1
- Update to version 2.4.2.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1-1
- Update to version 2.4.1.
- Drop explicit dependency on zeitgeist.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-1
- Update to version 2.4.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Initial package renamed from slingshot-launcher.

