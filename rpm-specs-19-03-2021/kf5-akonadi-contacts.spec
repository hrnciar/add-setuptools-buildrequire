%global framework akonadi-contacts

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 20.12.3
Release: 1%{?dist}
Summary: The Akonadi Contacts Library

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
%global kf5_ver 5.39
BuildRequires:  kf5-kdbusaddons-devel >= %{kf5_ver}
BuildRequires:  kf5-kio-devel >= %{kf5_ver}
BuildRequires:  kf5-kconfig-devel >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  kf5-kitemmodels-devel >= %{kf5_ver}
BuildRequires:  kf5-prison-devel >= %{kf5_ver}

BuildRequires:  cmake(Grantlee5) >= 5.1
BuildRequires:  qt5-qtwebengine-devel
BuildRequires:  cmake(Qt5Widgets) >= 5.8

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-grantleetheme-devel >= %{majmin_ver}
%if !(0%{?rhel} == 8 && ( "%{_arch}" == "aarch64" || "%{_arch}" == "s390x" ))
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
%endif
BuildRequires:  kf5-kcontacts-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-libkleo-devel >= %{majmin_ver}

%if 0%{?tests}
BuildRequires: kf5-akonadi-server >= %{majmin_ver}
BuildRequires: kf5-akonadi-server-mysql
BuildRequires: xorg-x11-server-Xvfb
%endif

# split from kf5-akonadi/kdepimlibs in 16.07
Obsoletes: kf5-akonadi < 16.07
Obsoletes: kf5-akonadi-contact < 16.07
Provides:  kf5-akonadi-contact = %{version}-%{release}

# kdepim-apps-libs deprecated, some content moved here
Obsoletes: kdepim-apps-libs < 20.11.90

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
# split from kf5-akonadi/kdepimlibs in 16.07
Obsoletes: kf5-akonadi-devel < 16.07
Obsoletes: kf5-akonadi-contact-devel < 16.07
Provides:  kf5-akonadi-contact-devel = %{version}-%{release}
Obsoletes: kdepim-apps-libs-devel < 20.11.90
Requires:  cmake(KF5Akonadi)
Requires:  cmake(KF5Contacts)
Requires:  cmake(KF5GrantleeTheme)
Recommends:  cmake(KF5CalendarCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
%make_build test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKF5AkonadiContact.so.*
%{_kf5_libdir}/libKF5ContactEditor.so.*
%{_kf5_qtplugindir}/kcm_akonadicontact_actions.so
%{_kf5_qtplugindir}/akonadi/contacts/
%{_kf5_qtplugindir}/akonadi_serializer_*.so
%{_kf5_datadir}/akonadi/plugins/serializer/
%{_kf5_datadir}/kservices5/akonadicontact_actions.desktop
%dir %{_kf5_datadir}/kf5/akonadi/
%{_kf5_datadir}/kf5/akonadi/contact/

%files devel
%{_kf5_libdir}/cmake/KF5AkonadiContact/
%{_kf5_libdir}/cmake/KF5ContactEditor/
%{_kf5_libdir}/libKF5AkonadiContact.so
%{_kf5_libdir}/libKF5ContactEditor.so
%{_kf5_archdatadir}/mkspecs/modules/qt_AkonadiContact.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_ContactEditor.pri
%{_kf5_includedir}/Akonadi/Contact/
%{_kf5_includedir}/akonadi/contact/
%{_kf5_includedir}/ContactEditor/
%{_kf5_includedir}/contacteditor/


%changelog
* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Fri Feb 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-3
- -devel: Requires: cmake(KF5GrantleeTheme)

* Fri Feb 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-2
- Obsoletes: kdepim-apps-libs(-devel)

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 15:36:45 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Thu Apr 02 2020 Bj??rn Esser <besser82@fedoraproject.org> - 19.12.3-2
- Fix string quoting for rpm >= 4.16

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Fri Oct 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.90-1
- 17.11.90

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-1
- 17.11.80

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Sat May 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Thu Sep 15 2016 Than Ngo <than@redhat.com> - - 16.08.1-3
- use %%{qt5_qtwebengine_arches}

* Tue Sep 13 2016 Than Ngo <than@redhat.com> - - 16.08.1-2
- dont build on ppc64/s390x as qtwebengine is not supported yet

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Sun Sep 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-4
- -devel: Requires:  KF5Akonadi,KF5Contacts,KF5CalendarCore
- drop some bootstrapping hacks

* Sun Sep 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-3
- de-bootstrap

* Sat Sep 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-2
- bump bootstrap versioning

* Sat Sep 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- -devel: fix Obsoletes/Provides: kf5-akonadi-contact-devel
- 16.08.0

* Sun Jul 31 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- kf5-akonadi-contacts-16.07.80
