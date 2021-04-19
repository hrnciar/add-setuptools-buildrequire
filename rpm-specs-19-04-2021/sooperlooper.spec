Summary: Realtime software looping sampler
Name: sooperlooper
Version: 1.7.3
Release: 17%{?dist}
License: GPLv2+
URL: http://essej.net/sooperlooper/
Source0: http://essej.net/sooperlooper/sooperlooper-%{version}.tar.gz
Source1: sooperlooper.png
Source2: sooperlooper.desktop
Source3: sooperlooper.appdata.xml
Patch0:  sooperlooper-sigc++-inc.patch
# Upstream fix for std::bind vs sigc::bind conflict:
# https://github.com/essej/sooperlooper/commit/0cb1e65166
Patch1: sooperlooper-sigc_bind.diff
# Patch for wxWidgets 3.0 support from Debian:
# https://salsa.debian.org/multimedia-team/sooperlooper/blob/master/debian/patches/04-build_with_wx_30.patch
Patch2: sooperlooper-wxwidgets3.0.patch
Requires: hicolor-icon-theme

BuildRequires: make
BuildRequires: gettext-devel ncurses-devel wxGTK3-devel rubberband-devel
BuildRequires: desktop-file-utils jack-audio-connection-kit-devel
BuildRequires: libsigc++20-devel libsndfile-devel liblo-devel fftw-devel
BuildRequires: libsamplerate-devel alsa-lib-devel libxml2-devel
BuildRequires: libappstream-glib gcc-c++

%description
SooperLooper is a realtime software looping sampler in the spirit of
Gibson's Echoplex Digital Pro. If used with a low-latency kernel and
the proper audio buffer configuration it is capable of truly realtime
live looping performance.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# kill the stubborn overriding of CXXFLAGS
sed -i 's|OPT_FLAGS="$OPT_FLAGS -pipe"|OPT_FLAGS=""|g' configure
sed -i 's|OPT_FLAGS="$OPT_FLAGS -pipe"|OPT_FLAGS="%{optflags}"|g' \
  libs/pbd/configure libs/midi++/configure


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}


%install
%make_install

# install icon in the proper freedesktop location
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README OSC
%license COPYING
%{_bindir}/*
%{_datadir}/sooperlooper
%{_datadir}/appdata/sooperlooper.appdata.xml
%{_datadir}/applications/sooperlooper.desktop
%{_datadir}/icons/hicolor/64x64/apps/sooperlooper.png


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 14 2020 Jeff Law <law@redhat.com> - 1.7.3-16
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Scott Talbert <swt@techie.net> - 1.7.3-11
- Rebuild with wxWidgets 3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.3-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.7.3-5
- Backported upstream fix for bind conflict

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 21 2016 Hans de Goede <hdegoede@redhat.com> - 1.7.3-3
- Fix FTBFS (rhbz#1308142)
- Add appdata

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Hans de Goede <hdegoede@redhat.com> - 1.7.3-1
- New upstream release 1.7.3
- Fix FTBFS

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.7.0-1
- Update to 1.7.0

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.18-4
- Remove --vendor from desktop-file-install for F19+. https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 02 2012 Brendan Jones <brendan.jones.it@gmail.com> - 1.6.18-1
- Update to upstream 1.6.18, remove consts patch
- Remove obsolete BuildRoot tags and clean section

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.6.13-6
- Rebuild against new liblo
- Update scriptlets to the latest guidelines

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.6.13-5
- rebuilt against wxGTK-2.8.11-2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 1.6.13-3
- constify ret of strchr(const char*)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Anthony Green <green@redhat.com> 1.6.13-1
- New upstream release 1.6.13

* Tue Apr 15 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.6.2-1
- New upstream release 1.6.2

* Mon Oct  1 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0-2
- updated the desktop categories to conform to desktop standard
  (added midi)

* Wed Sep 26 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0-1
- updated to 1.2.0, dropped patch0 and patch1, no need for extra
  perl one liners, etc

* Wed Jun  6 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.1.0-1
- updated to 1.1.0
- patch automake version comparison in autogen.sh, it is compared as
  a number in perl and it fails for automake > 1.9 (1.10 in fc7)
- fix #if to #ifdef and failed include in libs/pbd/mountpoint.cc (patch1)

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.8-0.4.c
- added long int patch for x86_64

* Sat Sep  9 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.8-0.3.c
- fixed typo in desktop file (SooperLooper instead of Sooperlooper, 
  thanks to Anthony Green)

* Wed Aug  2 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.8-0.2.c
- added auto* build dependencies, call ./autogen.sh to redo the autotools
  configuration to match newer autotools versions, added missing
  gettext-devel build requirement
- added COPYING license file

* Tue Aug  1 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.8-0.1.c
- specfile tweaks for Extras submission, change version/release to 
  match naming guidelines

* Sun May  7 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.8c
- update to 1.0.8c, add Planet CCRMA categories to desktop file,
  add icon

* Fri Mar 31 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.3
- same for fc5

* Tue May 31 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.3
- remove compiler option not recognized by gcc4.0

* Wed May  4 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.3
- updated to 1.0.3, added menu entry

* Wed Feb 16 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0dev28-1
- updated to 1.0.0dev28

* Mon Dec 27 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0dev25-1
- spec file cleanup

* Tue Dec  7 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0dev25-1
- initial build.
