%global commit      f1d517f6091c8d545fad46f632baf0eb52410464
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210217

%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-bluetooth
%global appname io.elementary.wingpanel.bluetooth

Name:           wingpanel-indicator-bluetooth
Summary:        Bluetooth Indicator for wingpanel
Version:        2.1.6
Release:        3.%{commitdate}git%{shortcommit}%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       bluez
Requires:       wingpanel%{?_isa}

Supplements:    (wingpanel%{?_isa} and bluez)


%description
A bluetooth indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang bluetooth-indicator

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f bluetooth-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libbluetooth.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.bluetooth.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 2.1.6-3.20210217gitf1d517f
- Bump to commit f1d517f. Rebuilt for granite 6 soname bump and wingpanel 3.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Fabio Valentini <decathorpe@gmail.com> - 2.1.6-1
- Update to version 2.1.6.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5-1
- Update to version 2.1.5.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-1
- Update to version 2.1.3.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-1
- Update to version 2.1.2.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-1
- Update to version 2.1.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Rebuild for granite5 soname bump.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-3
- Rebuild for granite soname bump.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-2
- Fix a copy-paste-error.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Update to version 2.0.3.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Add upstream patch to fix compilation with vala 0.35+.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.
- Make dependency on /usr/bin/pkg-config explicit.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0-4
- Clean up spec file.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Spec file cleanups.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.

