# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/rubik
%global commit      2e360a2044e6d1d4e3a6ddd992144a9a0b5446af
%forgemeta

Version: 2.100
Release: 4%{?dist}
URL:     %{forgeurl}

%global foundry           google
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Rubik
%global fontsummary       Rubik, a sans serif font family with slightly rounded corners
%global fonts             fonts/ttf/*ttf fonts/variable*fonts/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Rubik is a sans serif font family with slightly rounded corners designed by
Philipp Hubert and Sebastian Fischer at Hubert & Fischer as part of the Chrome
Cube Lab project.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.100-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.100-1.20191208git2e360a2
✅ Initial packaging
