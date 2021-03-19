Name:       megapixels
Version:    0.15.0
Release:    1%{?dist}
Summary:    A GTK3 camera application that knows how to deal with the media request api

License:    GPLv3+
URL:        https://git.sr.ht/~martijnbraam/megapixels
Source0:    https://git.sr.ht/~martijnbraam/megapixels/archive/%{version}.tar.gz

ExclusiveArch:  aarch64 armv7hl

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  inih-devel
BuildRequires:	zbar-devel
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	/usr/bin/xauth
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

Requires: hicolor-icon-theme
# for postprocess.sh
Requires: dcraw


%description
A GTK3 camera application that knows how to deal with the media request api

%prep
%setup -q -n %{name}-%{version}

%build 
%meson
%meson_build

%install
%meson_install


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.postmarketos.Megapixels.metainfo.xml

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.postmarketos.Megapixels.desktop

LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test
SH


%files
%dir %{_datadir}/megapixels
%dir %{_datadir}/megapixels/config

%{_bindir}/megapixels
%{_bindir}/megapixels-camera-test
%{_bindir}/megapixels-list-devices
%{_datadir}/applications/org.postmarketos.Megapixels.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.postmarketos.Megapixels.svg
%{_datadir}/megapixels/config/pine64,pinephone-1.0.ini
%{_datadir}/megapixels/config/pine64,pinephone-1.1.ini
%{_datadir}/megapixels/config/pine64,pinephone-1.2.ini
%{_datadir}/megapixels/config/pine64,pinetab.ini
%{_datadir}/megapixels/postprocess.sh
%{_datadir}/metainfo/org.postmarketos.Megapixels.metainfo.xml

%doc README.md
%license LICENSE


%changelog
* Sun Feb 21 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0

* Mon Jan 11 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0

* Fri Jan 01 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.2-1
- Update to 0.13.2

* Tue Dec 15 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.1-2
- Adding license and README

* Thu Dec 10 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Thu Dec 03 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.12.0-2
- Adding dependencies for postprocess.sh

* Sat Nov 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.12.0-1
- Initial packaging

