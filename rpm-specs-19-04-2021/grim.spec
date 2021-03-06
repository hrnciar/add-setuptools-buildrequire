Name:		grim
Version:	1.3.2
Release:	1%{?dist}
Summary:	Screenshot tool for Sway

License:	MIT
URL:		https://github.com/emersion/grim
Source0:	%{url}/releases/download/v%{version}/grim-%{version}.tar.gz
Source1:	%{url}/releases/download/v%{version}/grim-%{version}.tar.gz.sig
Source2:	dj3498u4hyyarh35rkjfnghbjxug6b19

BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	scdoc
BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	gnupg2

%description
Grim is a command-line tool to grab images from Sway.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_bindir}/grim
%{_mandir}/man1/grim.1*

%changelog
* Sun Apr 18 2021 Benjamin Lowry <ben@ben.gmbh> - 1.3.2-1
- Grim 1.3.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Benjamin Lowry <ben@ben.gmbh> 1.3.1-1
- Grim 1.3.1

* Sun Mar 8 2020 Benjamin Lowry <ben@ben.gmbh> 1.3.0-3
- Clarify package description (RHBZ#1811403)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Benjamin Lowry <ben@ben.gmbh> 1.3.0-1
- Grim 1.3.0

* Fri Jan 10 2020 Benjamin Lowry <ben@ben.gmbh> 1.2.0-2
- Use PGP key from author's website instead of keyserver

* Sun Dec 29 2019 Benjamin Lowry <ben@ben.gmbh> 1.2.0-1
- Initial Fedora package
