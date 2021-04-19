%global commit      22b101ea5b7ad2a73f24ddd6b4119c7b769bc0fd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210215

%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-sound

%global plug_type system
%global plug_name sound
%global plug_rdnn io.elementary.switchboard.sound

Name:           switchboard-plug-sound
Summary:        Switchboard Sound Plug
Version:        2.2.6
Release:        3.%{commitdate}git%{shortcommit}%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/switchboard-plug-sound
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
A sound plug for Switchboard.


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
* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 2.2.6-3.20210215git22b101e
- Bump to commit 22b101e. Rebuilt for granite 6 soname bump.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Fabio Valentini <decathorpe@gmail.com> - 2.2.6-1
- Update to version 2.2.6.

* Fri Sep 04 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.5-1
- Update to version 2.2.5.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4-1
- Update to version 2.2.4.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.3-1
- Update to version 2.2.3.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-1
- Update to version 2.2.2.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.2.1-2
- Rebuild with Meson fix for #1699099

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Update to version 2.2.1.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-1
- Update to version 2.1.3.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-1
- Update to version 2.1.2.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Rebuild for granite5 soname bump.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Initial package.

