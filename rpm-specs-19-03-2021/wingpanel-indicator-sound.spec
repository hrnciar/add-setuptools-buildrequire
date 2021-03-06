%global commit      845e631c420cca84a4807ec08f201be439a9ae88
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210217

%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-sound
%global appname io.elementary.wingpanel.sound

Name:           wingpanel-indicator-sound
Summary:        Sound Indicator for wingpanel
Version:        2.1.8
Release:        3.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
A sound indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang sound-indicator

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f sound-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libsound.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.sound.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 2.1.8-3.20210217git845e631
- Bump to commit 845e631. Rebuilt for granite 6 soname bump and wingpanel 3.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Fabio Valentini <decathorpe@gmail.com> - 2.1.8-1
- Update to version 2.1.8.

* Fri Oct 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.7-1
- Update to version 2.1.7.

* Wed Aug 12 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.6-1
- Update to version 2.1.6.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5-1
- Update to version 2.1.5.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-1
- Update to version 2.1.3.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-1
- Update to version 2.1.2.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-1
- Update to version 2.1.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5-7
- Rebuild for granite5 soname bump.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5-5
- Add patch to fix undefined symbols.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5-4
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5-1
- Update to version 2.0.5.

* Sat Apr 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-1
- Update to version 2.0.4.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-4
- Remove explicit BR: pkgconfig.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-3
- Filter provides.

* Fri Jan 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-2
- Clean up spec file.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Update to version 2.0.3.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Spec file cleanups.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to latest snapshot.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com>
- Weak inverse require wingpanel.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.

