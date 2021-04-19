%global commit      aae52175d99799cf4a3810c5ae818e40e00195bc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210218

%global srcname sideload
%global appname io.elementary.sideload

Name:           elementary-sideload
Summary:        Sideload flatpaks on Pantheon
Version:        1.1.1
Release:        4.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/sideload
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       hicolor-icon-theme

%description
Sideload is a simple application that lets users install flatpaks on
Pantheon without needing to use a command line application.


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
%license LICENSE
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-4.20210218gitaae5217
- Bump to commit aae5217. Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-1
- Update to version 1.1.1.

* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Wed Feb 26 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Initial packaging.

