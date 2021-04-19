%global pname     streamdev
# If this variable is set the spec file assumes it's building a git snapshot
# Also see info below on generating snapshots
%global gitver    b84b7d858cf4f6f3473ba72d456326c048946cb0
%global gitshort  %(echo %gitver | awk '{print substr($0,1,8)}')
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

%if 0%{?gitver:1}
  # Use vdr-streamdev-snapshot.sh contained in the source of the package to
  # generate new snapshots
  # You can also create snapshots for specific commit hashes
  # Example: sh vdr-streamdev-snapshot.sh b84b7d858cf4f6f3473ba72d456326c048946cb0
  %global srcfile   %{name}-%{gitshort}.tar.xz
  %global setuppath %{name}-%{gitshort}
%else
  # URL for original source file when not using git snapshots
  %global srcfile   http://projects.vdr-developer.org/attachments/download/969/%{name}-%{version}.tgz
  %global setuppath %{pname}-%{version}
%endif

Name:           vdr-%{pname}
Version:        0.6.1
Release:        0.28%{?gitver:.git%{gitshort}}%{?dist}
Summary:        Streaming plug-in for VDR
License:        GPL+ and GPLv2+
URL:            http://projects.vdr-developer.org/projects/plg-streamdev

Source0:        %{srcfile}
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}-server.conf
Source2:        %{name}-client.conf
# Script to generate git snapshots
# listed here so that it's pulled into the SRPM
Source3:        %{name}-snapshot.sh
# https://www.vdr-portal.de/index.php?attachment/41040-0001-fixed-compilation-for-vdr-2-3-7-diff/
Patch0:         0001-Fixed-compilation-for-vdr-2.3.7.diff

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 1.6.0-41

%description
The streamdev plug-in adds streaming capabilities to your VDR.

%package server
Summary:        Streaming server plug-in for VDR
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description server
Lets your VDR act as a streaming server for other clients.
This will let you watch TV or Recordings across the network.

%package client
Summary:        Streaming client plug-in for VDR
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description client
Lets your VDR in conjunction with a streamdev-server act as a streaming client.
VDR will then be able to work even without a DVB device.

%prep
%setup -q -n %{setuppath}
%patch0 -p1
sed -i 's@$(VDRDIR)/device.h@%{_includedir}/vdr/device.h@' Makefile

for f in CONTRIBUTORS HISTORY; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC" CXXFLAGS="-std=c++14 %{optflags} -fPIC"

%install
%make_install
install -dm 755 $RPM_BUILD_ROOT%{vdr_configdir}/plugins/streamdev-server
install -Dpm 644 streamdev-server/streamdevhosts.conf $RPM_BUILD_ROOT%{vdr_configdir}/plugins/streamdev-server/streamdevhosts.conf
install -Dpm 755 streamdev-server/externremux.sh $RPM_BUILD_ROOT%{_libdir}/vdr/bin/externremux.sh 
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-server.conf
install -Dpm 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-client.conf
%find_lang %{name}-server
%find_lang %{name}-client

%files server -f %{name}-server.lang
%doc CONTRIBUTORS COPYING HISTORY PROTOCOL README
%{vdr_plugindir}/libvdr-%{pname}-server.so.%{vdr_apiversion}
%{_libdir}/vdr/bin/externremux.sh
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-server.conf
%dir %{vdr_configdir}/plugins/streamdev-server
%config(noreplace) %{vdr_configdir}/plugins/streamdev-server/streamdevhosts.conf

%files client -f %{name}-client.lang
%doc CONTRIBUTORS COPYING HISTORY PROTOCOL README
%{vdr_plugindir}/libvdr-%{pname}-client.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-client.conf

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.28.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.27.gitb84b7d85
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.26.gitb84b7d85
- Rebuilt for new VDR API version

* Fri Aug 14 2020 Jeff Law <law@redhat.com> - 0.6.1-0.25.gitb84b7d85
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.24.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.23.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.22.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.21.gitb84b7d85
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.20.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.19.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.18.gitb84b7d85
- Rebuild for vdr-2.4.0
- Update to 0.6.1-0.18.gitb84b7d8
- Add 0001-Fixed-compilation-for-vdr-2.3.7.diff

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.17.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.16.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.15.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.14.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.13.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-0.12.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 07 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.6.1-0.11.git84c6f6b6
- fix compile for VDR 2.2 and F22+
- use make install

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-0.10.git10db11ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-0.9.git10db11ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.8.git10db11ac
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.7.git10db11ac
- Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-0.6.git10db11ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.5.git10db11ac
- Rebuild.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.4.git10db11ac
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.3.git10db11ac
- Rebuild.

* Sun Mar 03 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.2.git10db11ac
- Rebuild.

* Thu Feb 21 2013 Felix Kaechele <heffer@fedoraproject.org> - 0.6.1-0.1.git10db11ac
- update to latest git snapshot for VDR 1.7.38 support
- modified spec to easily support git snapshots
- cleanup spec: remove old macros and constructs

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-4
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-3
- Rebuild.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-2
- Make vdr(abi) deps arch qualified.

* Wed Jul 04 2012 Felix Kaechele <heffer@fedoraproject.org> - 0.6.0-1
- update to 0.6.0
- drop all patches as upstream includes them already

* Tue Mar 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-12
- Rebuild.

* Sun Mar 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-11
- Apply upstream VDR 1.7.26+ patches.

* Tue Mar  6 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-10
- Apply upstream VDR 1.7.25+ patches.

* Mon Feb 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-9
- Rebuild.

* Sun Jan 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-8
- Rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-6
- Rebuild.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-5
- Fix build with Liemikuutio patch 1.32.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-4
- Install locale files (#750084).

* Sun Oct 23 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.5.1-3
- own the configuration dir
- add patch to fix the GPL in COPYING and the FSF address in some source files

* Sat Oct 08 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.5.1-2
- move streamdevhosts.conf to the right directory

* Sat Feb 12 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.5.1-1
- update to latest upstream release
- see HISTORY for full changelog

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 25 2010 Felix Kaechele <heffer@fedoraproject.org> - 0.5.0-1
- update to final 0.5.0 release

* Sat Jan 02 2010 Felix Kaechele <heffer@fedoraproject.org> - 0.5.0-0.2.pre20090706
- added missing BuildReq: gettext

* Fri Dec 18 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.5.0-0.1.pre20090706
- update to latest version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Felix Kaechele <felix at fetzig dot org> - 0.3.4-2
- Incorporated fixes suggested in bug #454120
* Fri Jul  4 2008 Felix Kaechele <felix at fetzig dot org> - 0.3.4-1
- Initial Build
