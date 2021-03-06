Name:		phoc
Version:	0.7.0
Release:	1%{?dist}
Summary:	Display compositor designed for phones

License:	GPLv3+
URL:		https://source.puri.sm/Librem5/phoc
Source0:	https://source.puri.sm/Librem5/phoc/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson

BuildRequires:	pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.15
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wlroots)

BuildRequires:	pkgconfig(gnome-desktop-3.0)

%description
Phoc is a wlroots based Phone compositor as used on the Librem5. Phoc is
pronounced like the English word fog.


%prep
%setup -q -n %{name}-v%{version}

%build
%meson -Dembed-wlroots=disabled
%meson_build


%install
%meson_install


%files
%{_bindir}/phoc
%{_datadir}/glib-2.0/schemas/sm.puri.phoc.gschema.xml
%doc README.md
%license COPYING


%changelog
* Fri Mar 19 2021 Torrey Sorensen <torbuntu@fedpraproject.org> - 0.7.0-1
- Update to 0.7.0

* Tue Jan 05 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Thu Nov 19 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Nov 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Tue Oct 27 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Thu Oct 08 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Thu Aug 06 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.1-2
- Rebuild for new wlroots

* Wed Jul 22 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Tue Jun 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0, note: update version is to align with phosh, thus the jump to 0.4.0

* Tue Jun 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Thu Jun 11 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Thu Mar 26 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.7-1
- Update to 0.1.7 with upstreamed patches

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-2
- Fix build with newer wlroots

* Tue Oct 01 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-1
- Initial packaging
