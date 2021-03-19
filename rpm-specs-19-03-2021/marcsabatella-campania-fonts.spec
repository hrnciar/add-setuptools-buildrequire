Version:        2.009
Release:        2%{?dist}
URL:            https://github.com/MarcSabatella/Campania

%global foundry           MarcSabatella
%global fontlicense       OFL
%global fontlicenses      LICENSE
%global fontdocs          README.md
%global fontfamily        Campania
%global fontsummary       Font for Roman numeral analysis (music theory)
%global fonts             *.otf
%global fontconfs         %{SOURCE1}

%global fontdescription   %{expand:
This font is inspired by the work of Florian Kretlow and the impressive
Figurato font he developed for figured bass, as well as the work of
Ronald Caltabiano and his pioneering Sicilian Numerals font.  This
version of Campania is not directly based on either of these, however.
Instead, it uses the glyphs from Doulos and adds some relatively
straightforward contextual substitutions and positioning rules to allow
you to enter the most common symbols just by typing naturally.}

Source0:        https://github.com/MarcSabatella/Campania/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        65-%{fontpkgname}.conf

BuildRequires:  fontforge

%fontpkg

%prep
%autosetup -n Campania-%{version}

%build
%fontbuild
fontforge -lang=ff -c 'Open($1); Generate($2)' Campania.sfd Campania.otf

%install
%fontinstall

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%fontfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Jerry James <loganjerry@gmail.com> - 2.009-1
- Initial RPM
