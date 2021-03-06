%global commit      c8e462150911c8701d3f22e10bd67a1d349e8ab7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210218

%global srcname videos
%global appname io.elementary.videos

Name:           elementary-videos
Summary:        Video player and library app from elementary
Version:        2.7.2
Release:        4.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22

Requires:       hicolor-icon-theme

%description
A modern video player that brings the lessons learned from the web home
to the desktop.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 2.7.2-4.20210218gitc8e4621
- Bump to commit c8e4621. Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.7.2-1
- Update to version 2.7.2.

* Thu Apr 16 2020 Fabio Valentini <decathorpe@gmail.com> - 2.7.1-1
- Update to version 2.7.1.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.7.0-1
- Update to version 2.7.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3-1
- Update to version 2.6.3.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2-1
- Update to version 2.6.2.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1-2
- Fix FTBFS issue with vala 0.42.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1-1
- Update to version 2.6.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6-1
- Initial package renamed from audience.

