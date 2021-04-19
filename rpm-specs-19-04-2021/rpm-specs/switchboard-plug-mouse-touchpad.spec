%global commit      f2d22e1457ea7f4ee3a113bbda4e494d9a54941e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210218

%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-mouse-touchpad

%global plug_type hardware
%global plug_name mouse-touchpad
%global plug_rdnn io.elementary.switchboard.mouse-touchpad

Name:           switchboard-plug-mouse-touchpad
Summary:        Switchboard Mouse and Touchpad plug
Version:        2.4.2
Release:        5.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/switchboard-plug-mouse-touchpad
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

# patch to add support for GNOME 40 GSettings schema locations
Patch0:         %{url}/pull/167.patch

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
A switchboard plug to configure the behavior of mice and touchpads.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson -Dgnome_40=true
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Sun Mar 28 2021 Fabio Valentini <decathorpe@gmail.com> - 2.4.2-5.20210218gitf2d22e1
- Include patch to add support for GNOME 40 GSettings schema locations.

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 2.4.2-4.20210218gitf2d22e1
- Bump to commit f2d22e1. Rebuilt for granite 6 soname bump.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.2-1
- Update to version 2.4.2.

* Wed Apr 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.1-1
- Update to version 2.4.1.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-1
- Update to version 2.4.0.

* Tue Dec 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-1
- Update to version 2.3.1.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Update to version 2.3.0.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.2.0-2
- Rebuild with Meson fix for #1699099

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2-2
- Clean up spec file.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2-1
- Update to version 0.1.1.2.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-1
- Update to version 0.1.1.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Mass rebuild.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

