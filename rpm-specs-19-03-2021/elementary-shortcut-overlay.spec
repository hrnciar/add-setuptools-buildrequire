%global commit      8e3ba1fd91e576990045fc8084105220211adcce
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210120

%global srcname shortcut-overlay
%global appname io.elementary.shortcut-overlay

Name:           elementary-%{srcname}
Summary:        Native, OS-wide shortcut overlay
Version:        1.1.2
Release:        4.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.80.0

%description
This GTK+ applet reads window manager and OS keyboard shortcuts from
dconf and exposes them to the user when launched. Inspired by the
similar feature of Ubuntu Unity introduced in Ubuntu 12.04.

The shortcut window opens centered on the primary display. The gear in
the titlebar opens the system keyboard settings.


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
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.2-4.20210120git8e3ba1f
- Bump to commit 8e3ba1f. Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.2-1
- Update to version 1.1.2.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-1
- Update to version 1.1.1.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0-2
- Rebuild for granite5 soname bump.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0-1
- Initial package.

