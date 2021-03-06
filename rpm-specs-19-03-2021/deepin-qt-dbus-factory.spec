%global soname dframeworkdbus
%global repo   dde-qt-dbus-factory

%if 0%{?fedora}
Name:           deepin-qt-dbus-factory
%else
Name:           dde-qt-dbus-factory
%endif
Version:        5.3.35
Release:        1%{?fedora:%dist}
Summary:        A repository stores auto-generated Qt5 dbus code
# The entire source code is GPLv3+ except
# libdframeworkdbus/qtdbusextended/ which is LGPLv2+
License:        GPLv3+ and LGPLv2+
%if 0%{?fedora}
URL:            https://github.com/linuxdeepin/dde-qt-dbus-factory
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
%else
URL:            http://shuttle.corp.deepin.com/cache/repos/eagle/release-candidate/56qX566h6IGU6LCD5rWL6K-V6aqM6K-BMDUyMTQ5Mg/pool/main/d/dde-qt-dbus-factory/
Source0:        %{name}_%{version}.orig.tar.xz
%endif

BuildRequires:  python3
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-private-devel
%endif
BuildRequires:  make

%description
A repository stores auto-generated Qt5 dbus code.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i "s/env python$/env python3/g" libdframeworkdbus/generate_code.py
sed -i "s/python/python3/g" libdframeworkdbus/libdframeworkdbus.pro

%build
%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md CHANGELOG.md technology-overview.md
%license LICENSE
%{_libdir}/lib%{soname}.so.2*

%files devel
%{_includedir}/lib%{soname}-2.0/
%{_libdir}/pkgconfig/%{soname}.pc
%{_libdir}/lib%{soname}.so
%{_libdir}/cmake/DFrameworkdbus/

%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.3.35-1
- fix: 统一xml格式 (聂成)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.3.0.20-2
- drop hard-coded Qt5 runtime dependency

* Thu Nov 26 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.20-1
- new upstream release: 5.3.0.20

* Mon Nov 23 07:51:26 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.3.0.19-2
- rebuild (qt5)

* Mon Sep 28 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.19-1
- new upstream release: 5.3.0.19

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.0.1-7
- rebuild (qt5)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.1-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.1-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.1-2
- rebuild (qt5)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Release 5.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-4
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-3
- rebuild (qt5)

* Thu May 16 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.1.0-2
- Requires Qt private headers

* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Feb 25 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.0.6-2
- use %%ldconfig_scriptlets
- drop explicit Requires: cmake-filesystem (handled automatically now)
- -devel: own %%{_libdir}/cmake/DFrameworkdbus

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 1.0.5-1
- Update to 1.0.5

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Wed Jul 25 2018 Zamir SUN <zsun@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Sat Aug  5 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1
- Fix license

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1.gitbecf852
- Update to 0.2.1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 0.2.0-1.git98d9901
- Update to 0.2.0

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 0.1.0-1.git9adc304
- Update to 0.1.0

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 0.0.4-1.gitefa4f7f
- Update to 0.0.4

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.0.3-1.gitffda1af
- Initial build
