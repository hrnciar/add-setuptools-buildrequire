%global systemd_units tracker-xdg-portal-3

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           tracker3
Version:        3.1.0~rc
Release:        1%{?dist}
Summary:        Desktop-neutral metadata database and search tool

License:        GPLv2+
URL:            https://gnome.pages.gitlab.gnome.org/tracker/
Source0:        https://download.gnome.org/sources/tracker/3.1/tracker-%{tarball_version}.tar.xz

BuildRequires:  asciidoc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  libstemmer-devel
BuildRequires:  meson
BuildRequires:  systemd
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  /usr/bin/dbus-run-session

Requires: libtracker-sparql3%{?_isa} = %{version}-%{release}

Recommends: tracker-miners3%{?_isa}

%{?systemd_requires}


%description
Tracker is a powerful desktop-neutral first class object database,
tag/metadata database and search tool.

It consists of a common object database that allows entities to have an
almost infinite number of properties, metadata (both embedded/harvested as
well as user definable), a comprehensive database of keywords/tags and
links to other entities.

It provides additional features for file based objects including context
linking and audit trails for a file object.

Metadata indexers are provided by the tracker-miners3 package.


%package -n     libtracker-sparql3
Summary:        Tracker SPARQL library
License:        LGPLv2+
Recommends:     %{name}%{?_isa} = %{version}-%{release}

%description -n libtracker-sparql3
This package contains the libtracker-sparql library.


%package        devel
Summary:        Development files for %{name}
Requires:       libtracker-sparql3%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-devel package contains the documentation for %{name}.


%prep
%autosetup -n tracker-%{tarball_version} -p1


%build
%meson \
  -Dunicode_support=icu \
  -Dsystemd_user_services_dir=%{_userunitdir} \
  %{nil}

%meson_build


%install
%meson_install

%find_lang tracker3


%post
%systemd_user_post %{systemd_units}

%preun
%systemd_user_preun %{systemd_units}

%postun
%systemd_user_postun_with_restart %{systemd_units}


%files -f tracker3.lang
%license COPYING COPYING.GPL
%doc AUTHORS NEWS README.md
%{_bindir}/tracker3
%{_libexecdir}/tracker3/
%{_libexecdir}/tracker-xdg-portal-3
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/tracker3
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_mandir}/man1/tracker*.1*
%{_userunitdir}/tracker-xdg-portal-3.service

%files -n libtracker-sparql3
%license COPYING COPYING.LGPL
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Tracker-3.0.typelib
%{_libdir}/libtracker-sparql-3.0.so.0*
%{_datadir}/tracker3/

%files devel
%{_includedir}/tracker-3.0/
%{_libdir}/libtracker-sparql-3.0.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/tracker-3.0
%{_libdir}/tracker-3.0/trackertestutils/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/tracker-sparql-3.0.*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Tracker-3.0.gir

%files doc
%license docs/reference/COPYING
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libtracker-sparql-3/
%{_datadir}/gtk-doc/html/ontology-3/


%changelog
* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 3.1.0~rc-1
- Update to 3.1.0.rc

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 3.1.0~beta-1
- Update to 3.1.0.beta

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Carlos Garnacho <cgarnach@redhat.com> - 3.1.0~alpha-1
- Update to 3.1.0.alpha

* Mon Jan 04 2021 Felipe Borges <feborges@redhat.com> - 3.0.2-3
- Fix out parameter in VAPI/Vala files

* Thu Dec 24 2020 David King <amigadave@amigadave.com> - 3.0.2-2
- Fix FTS crash with SQLite 3.34.0

* Fri Dec 11 2020 Kalev Lember <klember@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Fri Oct 02 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Sun Sep 20 2020 Kalev Lember <klember@redhat.com> - 3.0.0-2
- Only require the library subpackage from -devel

* Mon Sep 14 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Sep 07 2020 Kalev Lember <klember@redhat.com> - 2.99.5-1
- Initial Fedora packaging, based on earlier tracker 2 package
