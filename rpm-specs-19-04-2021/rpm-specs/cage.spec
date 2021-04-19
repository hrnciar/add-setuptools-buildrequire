%global forgeurl	https://github.com/Hjdskes/cage

Name:			cage
Version:		0.1.2.1
Release:		4%{?dist}
Summary:		A Wayland kiosk

%forgemeta

License:		MIT
URL:			https://www.hjdskes.nl/projects/cage
Source0:		%{forgesource}
Source1:		https://github.com/Hjdskes/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# http://keys.gnupg.net/pks/lookup?op=get&fingerprint=on&search=0x37C445296EBC43B1
Source2:		gpgkey-6EBC43B1.gpg

Patch0:			%{forgeurl}/pull/174.patch#/unbreak-build-with-wlroots-0.13.0.patch

BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	meson
BuildRequires:	scdoc
BuildRequires:	wlroots-devel >= 0.13

%description
This is Cage, a Wayland kiosk. A kiosk runs a single, maximized application.

This README is only relevant for development resources and instructions. For a
description of Cage and installation instructions for end-users, please see its
project page and the Wiki.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%forgeautosetup -p1


%build
%meson -Dxwayland=true
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Wed Apr 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.1.2.1-4
- Rebuild for wlroots 0.13.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Lyes Saadi <fedora@lyes.eu> - 0.1.2.1-2
- Rebuilding for wlroots 0.12

* Thu Sep 03 2020 Lyes Saadi <fedora@lyes.eu> - 0.1.2.1-1
- Initial package
