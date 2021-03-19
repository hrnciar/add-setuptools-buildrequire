Version:        3.15
Release:        1%{?dist}
URL:            https://rsms.me/inter/

%global foundry rsms
%global fontlicense OFL
%global fontlicenses LICENSE.txt
%global fontdocsex %{fontlicenses}

%global fontfamily Inter
%global fontsummary The Inter font family
%global fonts "Inter Desktop"/*.otf
%global fontconfs %{SOURCE10}
%global fontdescription %{expand:Inter is a typeface specially designed for user interfaces with focus on high
legibility of small-to-medium sized text on computer screens.

The family features a tall x-height to aid in readability of mixed-case and
lower-case text. Several OpenType features are provided as well, like contextual
alternates that adjusts punctuation depending on the shape of surrounding
glyphs, slashed zero for when you need to disambiguate "0" from "o", tabular
numbers, etc.}

Source0:        https://github.com/rsms/inter/releases/download/v%{version}/inter-%{version}.zip
Source10:       63-%{fontpkgname}.conf

%fontpkg


%prep
%autosetup -c


%build
%fontbuild


%install
%fontinstall


%check
%fontcheck


%fontfiles


%changelog
* Thu Dec 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.15-1
- Initial RPM release
