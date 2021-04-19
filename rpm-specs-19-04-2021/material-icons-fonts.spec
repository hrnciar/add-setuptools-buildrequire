Version:        4.0.0
Release:        3%{?dist}
URL:            https://google.github.io/material-design-icons/

%global fontlicense     ASL 2.0
%global fontlicenses    LICENSE
%global fontdocs        README.md
%global fontfamily      Material Icons
%global fontsummary     Google material design system icons
%global fonts           font/*.otf font/*.ttf
%global fontconfs       %{SOURCE1}

%global fontdescription %{expand:
Material design icons is the official icon set from Google.  The icons
are designed under the material design guidelines.}

Source0:        https://github.com/google/material-design-icons/archive/%{version}/material-design-icons-%{version}.tar.gz
Source1:        65-%{fontpkgname}.conf

BuildRequires:  libappstream-glib

%fontpkg

%prep
%autosetup -n material-design-icons-%{version}

%build
%fontbuild

%install
%fontinstall
metainfo=%{buildroot}%{_metainfodir}/org.fedoraproject.%{name}.metainfo.xml

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,ASL 2\.0,Apache-2.0,' \
    -e 's,updatecontact,update_contact,g' \
    -e 's,<!\[CDATA\[\(.*\)\]\]>,\1,' \
    -e 's,<font></font>,<font>Material Icons Outlined Regular</font>\n    <font>Material Icons Round Regular</font>\n    <font>Material Icons Sharp Regular</font>\n    <font>Material Icons Two Tone Regular</font>,' \
    -i $metainfo

appstream-util validate-relax --nonet $metainfo

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%fontfiles

%changelog
* Mon Mar 29 2021 Jerry James <loganjerry@gmail.com> - 4.0.0-3
- Fix problems in the generated metainfo (bz 1943727)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Jerry James <loganjerry@gmail.com> - 4.0.0-1
- Initial RPM
