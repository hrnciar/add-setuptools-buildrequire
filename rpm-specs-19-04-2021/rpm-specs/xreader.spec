# Filter provides from plugins.
%global __provides_exclude_from ^%{_libdir}/%{name}/.*$

Name:		xreader
Version:	2.8.3
Release:	3%{?dist}
Summary:	Simple document viewer

License:	GPLv2+
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake3
BuildRequires:	gcc-c++
BuildRequires:	meson
BuildRequires:	mathjax
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(gail-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(kpathsea)
BuildRequires:	pkgconfig(libgxps)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xapp) >= 1.4.0
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	texlive
BuildRequires:	t1lib-devel
BuildRequires:	yelp-tools

Requires:	shared-mime-info%{?_isa}
Requires:	gsettings-desktop-schemas%{?_isa}
Requires:	xapps%{?_isa}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

Recommends:	yelp%{?_isa}

%description
X-Apps Document Reader is a document viewer capable of displaying
multiple and single page document formats like PDF and PostScript.

%package libs
Summary:    xreader document viewer libraries
Requires:	%{name}-data = %{version}-%{release}

%description libs
This package contains the shared library files for %{name}.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files for %{name}.


%package doc
Summary:	Documentation files for %{name}
BuildArch:	noarch

%description doc
This package contains the documentation files for %{name}.

%package data
Summary: Support files for the %{name} document viewer
BuildArch: noarch

%description data
This package contains icons and other support files used by the
%{name} application and libraries.

%package thumbnailer
Summary: System thumbnailer using %{name} libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description thumbnailer
This package adds configuration to use %{name} as a thumbnailer.


%prep
%autosetup -p1

%build
%meson	\
 -Ddeprecated_warnings=false \
 -Ddjvu=true \
 -Ddvi=true \
 -Dt1lib=true \
 -Dpixbuf=true \
 -Dcomics=true \
 -Dintrospection=true \
 -Dhelp_files=true \
 -Dtests=false

%meson_build

%install
%meson_install
%{_bindir}/find %{buildroot} -type f -name '*.a' -print -delete
%{_bindir}/find %{buildroot} -type f -name '*.la' -print -delete
%{__sed} -i -e '/.*<project_group>.*/d' \
	%{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%find_lang %{name}

%check
# Validate desktop-files.
%{_bindir}/desktop-file-validate    \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Validate AppData-files.
%{_bindir}/appstream-util validate-relax --nonet    \
	%{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%ldconfig_scriptlets

%files -f %{name}.lang
%license AUTHORS COPYING debian/copyright
%doc ChangeLog README debian/changelog
%{_bindir}/%{name}
%{_bindir}/%{name}-previewer
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/help/*/%{name}/
%{_datadir}/icons/hicolor/*/*/*
%{_libexecdir}/xreaderd
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-previewer.1*

%files libs
%{_libdir}/girepository-1.0/*
%{_libdir}/*.so.*
%{_libdir}/%{name}/

%files data
%{_datadir}/%{name}/

%files thumbnailer
%{_bindir}/%{name}-thumbnailer
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_mandir}/man1/%{name}-thumbnailer.1*

%files devel
%{_datadir}/gir-1.0/*
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/xreader-document-1.5.pc
%{_libdir}/pkgconfig/xreader-view-1.5.pc

%files doc
%license %{_datadir}/licenses/%{name}*
%doc %{_datadir}/doc/%{name}*

%changelog
* Sun Feb 28 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.8.3-3
- Create subpackages for libs, data, and thumbnailer (rhbz#1933895)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Leigh Scott <leigh123linux@gmail.com> - 2.8.3-1
- Update to 2.8.3 release

* Sat Jan  2 2021 Leigh Scott <leigh123linux@gmail.com> - 2.8.2-1
- Update to 2.8.2 release

* Thu Dec 10 2020 Leigh Scott <leigh123linux@gmail.com> - 2.8.1-1
- Update to 2.8.1 release

* Wed Dec  2 2020 Leigh Scott <leigh123linux@gmail.com> - 2.8.0-1
- Update to 2.8.0 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Leigh Scott <leigh123linux@gmail.com> - 2.6.4-1
- Update to 2.6.4 release

* Sat Jun 06 2020 Leigh Scott <leigh123linux@gmail.com> - 2.6.2-1
- Update to 2.6.2 release

* Sat May 23 2020 Leigh Scott <leigh123linux@gmail.com> - 2.6.1-1
- Update to 2.6.1 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 2.6.0-1
- Update to 2.6.0 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 2.4.4-3
- Rebuild for poppler-0.84.0

* Fri Jan 10 2020 Leigh Scott <leigh123linux@gmail.com> - 2.4.4-2
- Add build requires t1lib-devel

* Fri Jan 10 2020 Leigh Scott <leigh123linux@googlemail.com> - 2.4.4-1
- Update to 2.4.4 release

* Wed Dec 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.4.3-1
- Update to 2.4.3 release

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.4.2-1
- Update to 2.4.2 release

* Tue Nov 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-1
- Update to 2.4.1 release

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- Update to 2.4.0 release

* Tue Sep 10 2019 Florian Weimer <fweimer@redhat.com> - 2.2.3-2
- Fix building in C99 mode

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.2.3-1
- Update to 2.2.3 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.2.2-1
- Update to 2.2.2 release

* Sun Jun 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.2.1-1
- Update to 2.2.1 release

* Sat Jun 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-1
- Update to 2.2.0 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.2-1
- Update to 2.0.2 release

* Wed Nov 28 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-1
- Update to 2.0.1 release

* Mon Nov 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-1
- Update to 2.0.0 release

* Wed Aug 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.8.5-1
- Update to 1.8.5 release

* Mon Jul 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.8.4-1
- Update to 1.8.4 release
- Add BuildRequires gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.8.1-1
- Update to 1.8.1 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.6.2-1
- New upstream release

* Tue Dec 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.6.1-1
- New upstream release
- Fix typelib version

* Thu Nov 16 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.6.0-3
- Redistributable build on EPEL7

* Thu Nov 16 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.6.0-2
- Bootstrapping on EPEL7

* Sat Nov 04 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.6.0-1
- Update to 1.6.0 release

* Fri Sep 01 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.4-6
- Some more fixes for EPEL

* Fri Sep 01 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.4-5
- Some more fixes for EPEL

* Fri Sep 01 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.4-4
- Adjustments for EPEL

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.4-1
- New upstream release (rhbz#1462726)

* Wed May 24 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.2-1
- New upstream release (rhbz#1454986)

* Mon May 08 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.1-2
- Add patch to fix build without Caja-extension

* Mon May 08 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.1-1
- New upstream release (rhbz#1448921)

* Mon May 08 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.0-2
- Disable Caja-extension for Fedora <= 25

* Mon May 08 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.0-1
- Initial import (rhbz#1424832)

* Sat May 06 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4.0-0.1
- Initial rpm-release (rhbz#1424832)
