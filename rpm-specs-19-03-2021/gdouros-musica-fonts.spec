%global fontname gdouros-musica
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        3.17
Release:        10%{?dist}
Summary:        A font for musical symbols

# https://web.archive.org/web/20150625020428/http://users.teilar.gr/~g1951d/
# "in lieu of a licence:
# Fonts and documents in this site are not pieces of property or merchandise
# items; they carry no trademark, copyright, license or other market tags;
# they are free for any use. George Douros"
License:        Public Domain
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Musica.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Musica is a work-font for Ancient Greek, Byzantine and Western musical symbols.
The font also covers basic Latin, along with a few common symbols. Besides
musical notation glyphs supported by the Unicode Standard 7.0, Musica provides
extra symbols in Plane 15.

It was created by George Douros.

%prep
%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Musica.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
      %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} Musica.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc Musica.pdf

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 3.17-2
- Move metainfo.xml to new location

* Fri Feb 10 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 3.17-1
- 3.17 update

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-0.6.20150430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-0.5.20150430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 3.12-0.4.20150430
- Add license text
- Add appstream validation check

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-0.3.20150430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 3.12-0.2.20150430
- Change naming scheme to cope with upstream's silent updates and internal versions

* Tue Apr 14 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 3.12-2
- Merge the documentation back into the font package

* Fri Apr 03 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 3.12-1
- 3.12 bump
- Add separate source package for documentation
- Add metainfo file to show this font in gnome-software
- Change license to Public Domain

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 20 2009 Robin Sonefors <ozamosi@flukkost.nu> - 2.52-2
- Fix fontconfig priority and category

* Thu Oct 22 2009 Robin Sonefors <ozamosi@flukkost.nu> - 2.52-1
- Initial packaging