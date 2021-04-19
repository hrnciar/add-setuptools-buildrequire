%global rname   vdr-plugin-graphlcd
%global sname   graphlcd

Name:           vdr-graphlcd
Version:        1.0.6
Release:        1%{?dist}
Summary:        VDR plugin: Output to graphic LCD
License:        GPLv2+
URL:            https://projects.vdr-developer.org/projects/graphlcd/
Source0:        https://projects.vdr-developer.org/git/%{rname}.git/snapshot/%{rname}-%{version}.tar.bz2
Source1:        %{name}.conf
Source2:        %{name}.conf.sample
Source3:        %{name}-fonts.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  vdr-devel >= 1.6.0
BuildRequires:  graphlcd-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       dejavu-sans-fonts
Requires:       bitstream-vera-sans-fonts

%description
graphlcd is a plugin for the Video Disc Recorder and shows information
about the current state of VDR on displays supported by the GraphLCD
driver library.

%prep
%autosetup -p1 -n %{rname}-%{version}

# W: file-not-utf8
iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build
%make_build

%install
%make_install SKIP_INSTALL_DOC=1

# remove bundling fonts
rm -rf %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/{DejaVuSans-Bold,DejaVuSansCondensed}.ttf
ln -s %{_datadir}/fonts/dejavu/{DejaVuSans-Bold,DejaVuSansCondensed}.ttf \
  %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/

rm -rf %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/{Vera,VeraBd}.ttf
ln -s %{_datadir}/fonts/bitstream-vera/{Vera,VeraBd}.ttf \
  %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/

install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf

install -Dpm 644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf.sample

install -Dpm 644 %{SOURCE3} \
    %{buildroot}%{vdr_resdir}/plugins/%{sname}/fonts.conf

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%dir %{vdr_resdir}/plugins/%{sname}
%{vdr_resdir}/plugins/%{sname}/fonts
%{vdr_resdir}/plugins/%{sname}/logos
%{vdr_resdir}/plugins/%{sname}/skins
%config(noreplace) %{vdr_resdir}/plugins/%{sname}/*.alias
%config(noreplace) %{vdr_resdir}/plugins/%{sname}/fonts.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf.sample

%changelog
* Thu Mar 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6

* Wed Feb 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Mon Feb 08 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- Renamed config file (sample) included in RPM are not used and has to be renamed
  fixes (BZ#1926073)

* Thu Jan 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-5
- Add ShowReplayLogo.patch fix (BZ #1917097)

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-4
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-3
- Rebuilt for new VDR API version

* Wed Aug 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-2
- Update 1.0.2

* Mon Aug 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-9
- Rebuilt for new version of graphlcd-base-2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-5
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-3
- Rebuilt

* Mon Nov 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-2
- Add BR gcc-c++
- Add BR pkgconfig(freetype2)
- License is GPLv2+ not GPL+
- Convert HISTORY file to utf-8

* Mon Nov 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Nov 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-2
- Add %%{name}-Improved-trim-function.patch

* Tue Nov 06 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1
- Initial package
