%global fontname oflb-goudy-bookletter-1911
%global fontconf 61-%{fontname}.conf

Name:		%{fontname}-fonts
Summary:	Clean serif font based on Kennerly Old Style
Version:	20080206
Release:	21%{?dist}
License:	Public Domain
# Source was originally downloaded from here:
# http://openfontlibrary.org/people/chemoelectric/chemoelectric_-_Goudy_Bookletter_1.zip
# It is no longer available. The main website has this zip for download:
# http://home.comcast.net/%7Ecrudfactory/cf3/fonts/GoudyBookletter1911--2008.02.06.zip
# But, it doesn't have the source, just an otf.
Source0:	chemoelectric_-_Goudy_Bookletter_1.zip
Source1:	%{name}-fontconfig.conf
Source2:	GoudyBookletter1911.otf
Source3:        %{fontname}.metainfo.xml

URL:		http://home.comcast.net/~crudfactory/cf3/gb1911.html
BuildRequires:	fontpackages-devel, fontforge
Requires:	fontpackages-filesystem
BuildArch:	noarch

%description
Based on the roman of Frederic Goudy's Kennerley Old Style (designed and cut in
1911 for a limited edition of "The Door in the Wall and Other Stories" by H G
Wells, published by Mitchell Kennerley). The letters, though not condensed, may
seem to fit together like pieces of a jigsaw puzzle, giving text an unusually
solid appearance.

%prep
%setup -q -c -n %{name}
sed -i 's|/home/trashman/bin/fontforge|/usr/bin/fontforge|g' make-otf.py

%build
# Fontforge's python support is broken, so we can't build this from source, sadly.
# ./generate-it.sh
# The otf file was generated by converting it with Fontforge manually.
cp %{SOURCE2} .

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20080206-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080206-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 20080206-10
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080206-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080206-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080206-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080206-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080206-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080206-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug  5 2010 Tom "spot" Callaway <tcallawa@redhat.com> 20080206-4
- source building no longer sane, use pre-generated otf

* Mon Jun 28 2010 Tom "spot" Callaway <tcallawa@redhat.com> 20080206-3
- fix upstream URL and source

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080206-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20080206-2
- rename package to oflb-goudy-bookletter-1911-fonts
- drop common_desc (unnecessary)
- fix fontconfig file
- use %%global rather than %%define
- continue to annoy people diffing spec files

* Sun Mar 29 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20080206-1
- Initial package for Fedora
