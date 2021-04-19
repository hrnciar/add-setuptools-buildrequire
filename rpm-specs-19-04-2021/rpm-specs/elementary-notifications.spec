%global commit      eec89e611b3ea3976b377c700faa77f16f433e87
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210311

%global srcname notifications
%global appname io.elementary.notifications

Name:           elementary-notifications
Version:        0
Release:        0.11.%{commitdate}.git%{shortcommit}%{?dist}
Summary:        GTK Notifications Server
License:        GPLv3+

URL:            https://github.com/elementary/notifications
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libhandy-1)

%description
elementary Notifications is a GTK notification server for Pantheon.


%package demo
Summary:        Demo application for the elementary GTK Notifications Server
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description demo
elementary Notifications is a GTK notification server for Pantheon.

This package contains a demo application.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.demo.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml

%files demo
%{_bindir}/%{appname}.demo

%{_datadir}/applications/%{appname}.demo.desktop


%changelog
* Tue Mar 16 2021 Fabio Valentini <decathorpe@gmail.com> - 0-0.11.20210311.giteec89e6
- Bump to commit eec89e6.

* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 0-0.10.20210119.git749e28b
- Bump to commit 749e28b. Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20201020.git739268b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 24 2020 Fabio Valentini <decathorpe@gmail.com> - 0-0.8.20201020.git739268b
- Bump to commit 739268b.

* Fri Oct 09 2020 Fabio Valentini <decathorpe@gmail.com> - 0-0.7.20200512.git5867ed0
- Bump to commit 5867ed0.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200512.gita16377d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.20200512.gita16377d
- Bump to commit a16377d.

* Sat May 09 2020 Fabio Valentini <decathorpe@gmail.com> - 0-0.4.20200429.git6eeaf3e
- Bump to commit 6eeaf3e.

* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 0-0.3.20200331.gitdb552b0
- Bump to commit db552b0.

* Sat Mar 21 2020 Fabio Valentini <decathorpe@gmail.com> - 0-0.2.20200318.gitba4310b
- Bump to commit ba4310b.

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20200224.git676c175
- Initial packaging for fedora.

