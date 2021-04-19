%bcond_without check

Name:           gplugin
Version:        0.30.0
Release:        2%{?dist}
Summary:        GObject based library that implements a reusable plugin system

License:        LGPLv2+
URL:            https://keep.imfreedom.org/gplugin/gplugin
Source0:        https://dl.bintray.com/pidgin/releases/%{name}-%{version}.tar.xz
Source1:        https://dl.bintray.com/pidgin/releases/%{name}-%{version}.tar.xz.asc
Source2:        https://keybase.io/grim/pgp_keys.asc

BuildRequires:  gnupg2
BuildRequires:  meson >= 0.42.0
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  /usr/bin/help2man
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  gettext
%if %{with check}
BuildRequires:  /usr/bin/gtester
BuildRequires:  /usr/bin/xsltproc
%endif
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
GPlugin is a GObject based library that implements a reusable plugin system
which supports loading plugins in other languages via loaders.
It relies heavily on GObject Introspection to expose its API to the other
languages.

It has a very simple API which makes it very simple to use in your application.

%package        libs
Summary:        Library for %{name}

%description    libs
%{summary}.

%package        gtk
Summary:        GTK applications for %{name}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
Requires:       %{name}-gtk-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    gtk
%{summary}.

%package        gtk-libs
Summary:        GTK libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    gtk-libs
%{summary}.

%package        loader-lua
Summary:        Lua loader for %{name}
BuildRequires:  pkgconfig(lua) >= 5.1.0
BuildRequires:  lua-lgi
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    loader-lua
%{summary}.

%package        loader-perl
Summary:        Perl loader for %{name}
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Glib::Object::Introspection)
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    loader-perl
%{summary}.

%package        loader-python
Summary:        Python loader for %{name}
BuildRequires:  (pkgconfig(python3-embed) if python3 >= 3.8.0 else pkgconfig(python3))
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    loader-python
%{summary}.

%package        devel
Summary:        Development libraries and header files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
%{summary}.

%package        gtk-devel
Summary:        Development libraries and header files for %{name}-gtk-libs
Requires:       %{name}-gtk-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    gtk-devel
%{summary}.

%package        vala
Summary:        Vala bindings for %{name}-libs
BuildRequires:  vala
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    vala
%{summary}.

%package        gtk-vala
Summary:        Vala bindings for %{name}-gtk-libs
Requires:       %{name}-vala%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    gtk-vala
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# We install docs ourselves
sed -i -e '/install_data/,+1 d' meson.build
sed -i -e '/install_data/,+1 d' gplugin/share/valgrind/meson.build

%build
%meson
%meson_build

%install
%meson_install

%if %{with check}
%check
# Everything is tested during build process...
%meson_test
%endif

%files
%{_bindir}/gplugin-query
%{_mandir}/man1/gplugin-query.1*

%files libs
%license COPYING
%doc ChangeLog README.md
%{_libdir}/libgplugin.so.*
%dir %{_libdir}/gplugin/
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GPlugin-1.0.typelib

%files gtk
%{_bindir}/gplugin-gtk-viewer
%{_mandir}/man1/gplugin-gtk-viewer.1*

%files gtk-libs
%{_libdir}/libgplugin-gtk.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GPluginGtk-1.0.typelib

%files loader-lua
%{_libdir}/gplugin/gplugin-lua.so

%files loader-perl
%{_libdir}/gplugin/gplugin-perl5.so

%files loader-python
%{_libdir}/gplugin/gplugin-python3.so

%files devel
%doc gplugin/share/valgrind/gplugin.supp
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/gplugin/
%{_libdir}/libgplugin.so
%dir %{_includedir}/gplugin-1.0/
%{_includedir}/gplugin-1.0/gplugin/
%{_includedir}/gplugin-1.0/gplugin.h
%{_includedir}/gplugin-1.0/gplugin-native.h
%{_libdir}/pkgconfig/gplugin.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GPlugin-1.0.gir

%files gtk-devel
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/gplugin-gtk/
%{_libdir}/libgplugin-gtk.so
%{_includedir}/gplugin-1.0/gplugin-gtk/
%{_includedir}/gplugin-1.0/gplugin-gtk.h
%{_libdir}/pkgconfig/gplugin-gtk.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GPluginGtk-1.0.gir
%dir %{_datadir}/glade
%dir %{_datadir}/glade/catalogs
%{_datadir}/glade/catalogs/gplugin-gtk.xml

%files vala
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gplugin.deps
%{_datadir}/vala/vapi/gplugin.vapi

%files gtk-vala
%{_datadir}/vala/vapi/gplugin-gtk.deps
%{_datadir}/vala/vapi/gplugin-gtk.vapi

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.30.0-1
- Update to latest version
- Add Perl and Vala subpackages
- Add development documentation
- Update URLs to new upstream location
- Check source tarball GPG signature

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.29.0-4
- Rebuilt for Python 3.9

* Mon Apr 06 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.29.0-3
- Fix build with GCC 10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.29.0-1
- Update to 0.29.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.28.0-2
- Rebuilt for Python 3.8

* Sun Jul 28 17:04:09 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.28.0-1
- Update to 0.28.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.27.0-7
- Switch to %%ldconfig_scriptlets

* Fri Aug 11 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.27.0-6
- Remove extraneous pkgconfig library path.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.27.0-2
- Add missing ldconfig scriptlets

* Mon Jan 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.27.0-1
- Initial package
