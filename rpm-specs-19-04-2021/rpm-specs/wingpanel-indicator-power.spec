%global commit      99343729485afd06780fb5408b3288b346c1b8ca
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210219

%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-power
%global appname io.elementary.wingpanel.power

Name:           wingpanel-indicator-power
Summary:        Power indicator for wingpanel
Version:        2.2.0
Release:        3.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/wingpanel-indicator-power
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A power indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang power-indicator

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f power-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libpower.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.power.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-3.20210219git9934372
- Bump to commit 9934372. Rebuilt for granite 6 soname bump and wingpanel 3.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5-1
- Update to version 2.1.5.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-1
- Update to version 2.1.3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-1
- Update to version 2.1.2.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-8
- Rebuild for granite5 soname bump.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-6
- Add patch to fix undefined symbols.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-5
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 2.1.1-2
- Rebuilt for libgtop2 soname bump

* Tue May 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-1
- Update to version 2.1.1.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Remove explicit BR: pkgconfig.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Clean up spec file.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Spec file cleanups.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.

