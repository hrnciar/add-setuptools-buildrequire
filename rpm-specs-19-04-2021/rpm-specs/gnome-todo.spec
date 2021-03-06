Name:           gnome-todo
Version:        3.28.1
Release:        12%{?dist}
Summary:        Personal task manager for GNOME

License:        GPLv3+
URL:            https://git.gnome.org/browse/gnome-todo/
Source0:        https://download.gnome.org/sources/%{name}/3.28/%{name}-%{version}.tar.xz
Patch01:        gnome-todo-eds-libecal-2.0.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.2
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  %{_bindir}/desktop-file-validate
BuildRequires:  %{_bindir}/appstream-util

%description
GNOME To Do is a small application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%package devel
Summary:        Development files needed to write plugins for GNOME To Do

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Todo.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Todo.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/gnome-todo
%{_datadir}/applications/org.gnome.Todo.desktop
%{_datadir}/metainfo/org.gnome.Todo.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Todo.png
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Todo-symbolic.svg
%{_libdir}/girepository-1.0/Gtd-1.0.typelib
%{_libdir}/gnome-todo/
%{_datadir}/{%name}/org.gnome.Todo.Autostart.desktop

%files devel
%{_includedir}/gnome-todo/
%{_libdir}/pkgconfig/gnome-todo.pc
%{_datadir}/gir-1.0/Gtd-1.0.gir
%{_datadir}/gtk-doc/

%changelog
* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 3.28.1-12
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 3.28.1-8
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 3.28.1-5
- Add patch to build against newer evolution-data-server (libecal-2.0)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Milan Crha <mcrha@redhat.com> - 3.28.1-3
- Rebuilt for evolution-data-server soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.90-1
- Update to 3.27.90

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 3.26.2-3.1
- Rebuilt for evolution-data-server soname bump

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2.1
- Remove obsolete scriptlets

* Wed Nov 08 2017 Milan Crha <mcrha@redhat.com> - 3.26.2-2
- Rebuild for newer libical

* Wed Nov 01 2017 David King <amigadave@amigadave.com> - 3.26.2-1
- Update to 3.26.2 (#1508187)

* Sun Oct 01 2017 David King <amigadave@amigadave.com> - 3.26.1-1
- Update to 3.26.1 (#1494293)

* Fri Aug 11 2017 David King <amigadave@amigadave.com> - 3.25.90-1
- Update to 3.25.90 (#1480399)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 David King <amigadave@amigadave.com> - 3.25.3-1
- Update to 3.25.3 (#1463023)

* Tue Apr 25 2017 David King <amigadave@amigadave.com> - 3.25.1-1
- Update to 3.25.1 (#1445102)

* Mon Apr 24 2017 David King <amigadave@amigadave.com> - 3.24.0-1
- Update to 3.24.0 (#1444840)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Wed Nov 02 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 3.20.2-3
- Rebuild for newer evolution-data-server

* Wed Jun 22 2016 Milan Crha <mcrha@redhat.com> - 3.20.2-2
- Rebuild for newer evolution-data-server

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Tue Apr 26 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.20.0-2
- rebuild for ICU 57.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 David King <amigadave@amigadave.com> - 3.19.92-1
- Update to 3.19.92 (#1317712)

* Thu Mar 03 2016 David King <amigadave@amigadave.com> - 3.19.91-1
- Update to 3.19.91

* Wed Feb 17 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90 (#1309142)

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 3.19.5-2
- Rebuild for libcamel bump

* Fri Feb 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.19.5-1
- Update to 3.19.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 3.18.1-2
- rebuild for libical 2.0.0

* Wed Oct 14 2015 David King <amigadave@amigadave.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 28 2015 David King <amigadave@amigadave.com> - 3.18.0-3
- Update patch for service file (#1266868)

* Mon Sep 28 2015 David King <amigadave@amigadave.com> - 3.18.0-2
- Fix launching from GNOME Shell (#1266868)

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Wed Sep 02 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Tue Jul 21 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Thu Jun 25 2015 David King <amigadave@amigadave.com> - 3.17.3.1-1
- Update to 3.17.3.1

* Tue Jun 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.17.3-1
- Initial package
