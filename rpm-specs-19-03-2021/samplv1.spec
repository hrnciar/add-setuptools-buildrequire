Summary:       A polyphonic sampler synthesizer with stereo fx
Name:          samplv1
Version:       0.9.20
Release:       1%{?dist}
License:       GPLv2+
URL:           https://%{name}.sourceforge.io/
Source0:       https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:        %{name}-nostrip.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: lv2-devel >= 1.8.1
BuildRequires: desktop-file-utils
BuildRequires: libsndfile-devel
BuildRequires: liblo-devel
BuildRequires: libappstream-glib
Requires:      hicolor-icon-theme

%description
%{name} is a polyphonic sampler synthesizer with stereo fx.

%package -n lv2-%{name}
Summary:       An LV2 port of %{name}
Requires:      lv2 >= 1.8.1

%description -n lv2-%{name}
An LV2 plugin of the %{name} synth

%prep
%autosetup -p1

# Remove cruft from appdata file
pushd src/appdata
iconv -f utf-8 -t ascii//IGNORE -o tmpfile %{name}.appdata.xml 2>/dev/null || :
mv -f tmpfile %{name}.appdata.xml
popd

%build
%configure
%make_build

%install
%make_install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%doc AUTHORS README
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_bindir}/%{name}_jack
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_metainfodir}/%{name}.appdata.xml

%files -n lv2-%{name}
%doc AUTHORS README
%license COPYING
%{_libdir}/lv2/%{name}.lv2/

%changelog
* Mon Feb 15 2021 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.20-1
- Update to 0.9.20

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 11:11:11 CET 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.19-1
- Update to 0.9.19

* Mon Sep 14 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.17-1
- Update to 0.9.17

* Fri Aug 28 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.16-1
- Update to 0.9.16

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.14-1
- Update to 0.9.14

* Mon Apr 20 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.13-2
- Validate AppData
- Add missing BR for g++

* Sat Apr 18 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.13-1
- Update to 0.9.13
- Enable OSC support
- Some spec cleanup

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.10-1
- Update to 0.9.10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.6-2
- Remove obsolete scriptlets

* Sun Dec 24 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.8.3-3
- Update to 0.8.6

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.8.3-1
- Update to 0.8.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Brendan Jones <brendan.jones.it@gmail.com> - 0.7.6-3
- Install desktop file

* Tue Sep 20 2016 Brendan Jones <brendan.jones.it@gmail.com> - 0.7.6-2
- Add missing libsndfile

* Tue Sep 20 2016 Brendan Jones <brendan.jones.it@gmail.com> - 0.7.6-1
- Update to 0.7.6

* Sat Apr 23 2016 Brendan Jones <brendan.jones.it@gmail.com> 0.7.4-1
- Update to 0.7.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.7.1-2
- Add missing dep

* Sat Nov 21 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.7.1-1
- Update to 0.7.1
- enable Qt5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.2-1
- Update to 0.6.2

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 22 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.0-1
- Update to 0.6.1

* Tue Feb 03 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.0-1
- Update to 0.6.0

* Thu Sep 25 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.5.1-1
- Update to 0.5.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 08 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.0-2
- Fix FTBFS on secondary 64bit arches

* Tue Jul 08 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.5.0-1
- Update to 0.5.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 12 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.4.1-1
- Update to 0.4.1

* Sat Jan 11 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.3.6-1
- Update to 0.3.6

* Wed Oct 16 2013 Karsten Hopp <karsten@redhat.com> 0.3.5-2
- update 64bitarchs.patch

* Tue Oct 01 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.3.5-1
- Update to 0.3.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.3.4-1
- Update to 0.3.4

* Fri Mar 08 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.3.2-1
- Update to 0.3.2

* Fri Feb 22 2013 Karsten Hopp <karsten@redhat.com> 0.3.0-3
- add s390x and ppc64 to archs using lib64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.3.0-1
- New upstream release

* Sat Sep 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-1
- Update to 0.1.0

* Wed Aug 29 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.9-0.1.svn769
- UPdate to 0.0.9svn769

* Wed Jul 18 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.8-0.1.svn759
- new upstream 0.0.8

* Fri Jun 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-0.2.svn671
- Correct URL

* Wed May 16 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-0.1.svn671
- initial build
