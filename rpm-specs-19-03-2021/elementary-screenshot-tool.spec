%global commit      e33fa59bb42fd4630f8459631771e42533698c71
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210217

%global srcname screenshot
%global appname io.elementary.screenshot

Name:           elementary-screenshot-tool
Summary:        Screenshot tool designed for elementary
Version:        1.7.1
Release:        5.%{commitdate}git%{shortcommit}%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46
BuildRequires:  vala >= 0.24

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0

Requires:       hicolor-icon-theme

%description
Screenshot tool designed for elementary.


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
* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 1.7.1-5.20210217gite33fa59
- Bump to commit e33fa59. Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 1.7.1-1
- Update to version 1.7.1.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.7.0-1
- Update to version 1.7.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.6.2-1
- Update to version 1.6.2.

* Mon Feb 04 2019 Fabio Valentini <decathorpe@gmail.com> - 1.6.1-1
- Update to version 1.6.1.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.0-1
- Update to version 1.6.0.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-2
- Rebuild for granite5 soname bump.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-1
- Initial package renamed from screenshot-tool.

