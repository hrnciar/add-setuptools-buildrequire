%global commit      4c8668237554bf38b551dd472a4b00f0307523e5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210216

%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-applications

%global plug_type personal
%global plug_name applications
%global plug_rdnn io.elementary.switchboard.%{plug_name}

Name:           switchboard-plug-applications
Summary:        Switchboard Applications plug
Version:        2.1.7
Release:        4.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3+

URL:            http://github.com/elementary/switchboard-plug-applications
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(flatpak) >= 1.1.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.34
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
The applications plug is a section in the Switchboard (System Settings)
that allows the user to manage application settings.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 2.1.7-4.20210216git4c86682
- Bump to commit 4c86682. Rebuilt for granite 6 soname bump.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.7-1
- Update to version 2.1.7.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.6-1
- Update to version 2.1.6.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5-1
- Update to version 2.1.5.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1-1
- Update to version 0.1.3.1.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-2
- Rebuild for granite5 soname bump.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-5
- Clean up .spec file.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-4
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-5
- Clean up spec file.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-4
- Mass rebuild.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Spec file cosmetics.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Add Supplements: switchboard tag.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

