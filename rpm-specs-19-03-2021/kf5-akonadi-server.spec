
%global framework akonadi-server

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

%global mysql mysql
%if 0%{?rhel} > 6
# el7 mariadb pkgs don't have compat Provides: mysql (apparently?)
%global mysql mariadb
%endif

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
# skip slow(er) archs, for now -- rex
%ifnarch %{arm} s390x
%global tests 0
%endif
%endif

Name:    kf5-%{framework}
Summary: PIM Storage Service
Version: 20.12.3
Release: 1%{?dist}

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/akonadi-%{version}.tar.xz

## mysql config
Source10:       akonadiserverrc.mysql
Source11:       akonadiserverrc.sqlite

## upstreamable patches

## upstream patches (lookaside cache)

## downstream patches

%define mysql_conf_timestamp 20170512

BuildRequires:  extra-cmake-modules >= 5.60
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtxmlpatterns-devel

BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Config) >= 5.71
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Crash)

BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sqlite3) >= 3.6.23

%global majmin_ver %(echo %{version} | cut -d. -f1,2)

## (some) optional deps
%if ! 0%{?bootstrap}
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  cmake(KF5DesignerPlugin)
BuildRequires:  cmake(AccountsQt5)
BuildRequires:  cmake(KAccounts)
BuildRequires:  kaccounts-integration-devel
%endif

# ^^ sqlite3 driver plugin needs versioned qt5 dep
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

# backends, used at buildtime to query known locations of server binaries
# FIXME/TODO: set these via cmake directives, avoids needless buildroot items
BuildRequires:  mariadb-server
BuildRequires:  postgresql-server

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

Recommends:     %{name}-mysql = %{version}-%{release}

Conflicts:      akonadi < 1.13.0-100

# translations moved here
Conflicts: kde-l10n < 17.03

# when kf5-akonadi was split, -socialutils was dropped
Obsoletes: kf5-akonadi-socialutils < 16.07

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Obsoletes:      kf5-akonadi-devel < 16.03
## see if we can get away with droping this in 16.08 -- rex
#Provides:      kf5-akonadi-devel = %{version}-%{release}
# when kf5-akonadi was split, -socialutils was dropped
Obsoletes: kf5-akonadi-socialutils-devel < 16.07
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       kf5-kcompletion-devel
Requires:       kf5-kjobwidgets-devel
Requires:       kf5-kservice-devel
Requires:       kf5-solid-devel
Requires:       kf5-kxmlgui-devel
Requires:       kf5-kitemmodels-devel
Requires:       qt5-qtbase-devel
# at least dbus-1/interfaces conflict, maybe more -- rex
Conflicts:      akonadi-devel
%description devel
%{summary}.

%package mysql
Summary:        Akonadi MySQL backend support
# upgrade path
Obsoletes:      akonadi < 1.7.90-2
Obsoletes:      akonadi-mysql < 15.08.0
Provides:       akonadi-mysql = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{mysql}-server
%if "%{?mysql}" != "mariadb" && 0%{?fedora} > 20
Recommends:     mariadb-server
%endif
Requires:       qt5-qtbase-mysql%{?_isa}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%description mysql
Configures akonadi to use mysql backend by default.

Requires an available instance of mysql server at runtime.
Akonadi can spawn a per-user one automatically if the mysql-server
package is installed on the machine.
See also: %{_sysconfdir}/akonadi/mysql-global.conf


%prep
%autosetup -n akonadi-%{version} -p1


%build
%cmake_kf5 \
  %{?database_backend:-DDATABASE_BACKEND=%{database_backend}} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DINSTALL_APPARMOR:BOOL=OFF

%cmake_build


%install
%cmake_install

%find_lang libakonadi5
%find_lang akonadi_knut_resource
cat akonadi_knut_resource.lang >> libakonadi5.lang

install -p -m644 -D %{SOURCE10} %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
install -p -m644 -D %{SOURCE11} %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite

mkdir -p %{buildroot}%{_datadir}/akonadi/agents

touch -d %{mysql_conf_timestamp} \
  %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-global*.conf \
  %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-local.conf

# create/own these dirs
mkdir -p %{buildroot}%{_kf5_datadir}/akonadi/plugins
mkdir -p %{buildroot}%{_kf5_libdir}/akonadi

# %%ghost'd global akonadiserverrc
touch akonadiserverrc
install -p -m644 -D akonadiserverrc %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc

## unpackaged files
# omit mysql-global-mobile.conf
rm -fv %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-global-mobile.conf
# part of omitting exceptions header hack, drop the custom (no-longer-used) header itself
rm -fv %{buildroot}%{_kf5_includedir}/AkonadiCore/std_exception.h


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif


%post
%{?ldconfig}
%{_sbindir}/update-alternatives \
  --install %{_sysconfdir}/xdg/akonadi/akonadiserverrc \
  akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite \
  8

%postun
%{?ldconfig}
if [ $1 -eq 0 ] ; then
%{_sbindir}/update-alternatives \
  --remove akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite
fi


%files -f libakonadi5.lang
%doc AUTHORS
%doc README*
%license LICENSES/*
%dir %{_sysconfdir}/xdg/akonadi/
%ghost %config(missingok,noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc
%config(noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite
%{_kf5_datadir}/qlogging-categories5/akonadi.*
%{_kf5_bindir}/akonadi_agent_launcher
%{_kf5_bindir}/akonadi_agent_server
%{_kf5_bindir}/akonadi_control
%{_kf5_bindir}/akonadi_rds
%{_kf5_bindir}/akonadictl
%{_kf5_bindir}/akonadiserver
%{_kf5_libdir}/akonadi/
%{_kf5_datadir}/dbus-1/services/org.freedesktop.Akonadi.*.service
%{_kf5_datadir}/mime/packages/akonadi-mime.xml
%{_kf5_datadir}/akonadi/
%{_kf5_datadir}/config.kcfg/resourcebase.kcfg
%{_kf5_datadir}/kf5/akonadi/
%{_kf5_qtplugindir}/akonadi/
%if ! 0%{?bootstrap}
%{_kf5_qtplugindir}/designer/akonadiwidgets.so
%endif
%{_kf5_qtplugindir}/sqldrivers/libqsqlite3.so
%{_kf5_libdir}/libKF5AkonadiAgentBase.so.5*
%{_kf5_libdir}/libKF5AkonadiCore.so.5*
%{_kf5_libdir}/libKF5AkonadiPrivate.so.5*
%{_kf5_libdir}/libKF5AkonadiWidgets.so.5*
%{_kf5_libdir}/libKF5AkonadiXml.so.5*
# let newer %%trigger-based scriptlets catch this -- rex
%{_kf5_datadir}/icons/hicolor/*/apps/akonadi.*

# akonadi_knut_resource
%{_kf5_bindir}/akonadi_knut_resource
%{_kf5_datadir}/kf5/akonadi_knut_resource/

%files devel
%{_kf5_bindir}/akonadi2xml
%{_kf5_bindir}/akonadiselftest
%{_kf5_bindir}/akonaditest
%{_kf5_bindir}/asapcat

%{_kf5_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml
%{_kf5_includedir}/akonadi_version.h
%{_kf5_includedir}/akonadi/
%{_kf5_includedir}/AkonadiAgentBase/
%{_kf5_includedir}/AkonadiCore/
%{_kf5_includedir}/AkonadiWidgets/
%{_kf5_includedir}/AkonadiXml/
%{_kf5_libdir}/libKF5AkonadiAgentBase.so
%{_kf5_libdir}/libKF5AkonadiCore.so
%{_kf5_libdir}/libKF5AkonadiPrivate.so
%{_kf5_libdir}/libKF5AkonadiWidgets.so
%{_kf5_libdir}/libKF5AkonadiXml.so
%{_kf5_libdir}/cmake/KF5Akonadi/
%{_kf5_archdatadir}/mkspecs/modules/qt_Akonadi*.pri
#
%dir %{_kf5_datadir}/kdevappwizard/
%dir %{_kf5_datadir}/kdevappwizard/templates/
%{_kf5_datadir}/kdevappwizard/templates/akonadi*

%post mysql
%{_sbindir}/update-alternatives \
  --install %{_sysconfdir}/xdg/akonadi/akonadiserverrc \
  akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql \
  10

%postun mysql
if [ $1 -eq 0 ]; then
%{_sbindir}/update-alternatives \
  --remove akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
fi

%files mysql
%config(noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
%config(noreplace) %{_sysconfdir}/xdg/akonadi/mysql-global.conf
%config(noreplace) %{_sysconfdir}/xdg/akonadi/mysql-local.conf


%changelog
* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:52:37 CET 2020 Jan Grulich <jgrulich@redhat.com> - 20.08.3-2
- rebuild (qt5)

* Fri Nov  6 15:38:03 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Fri Oct 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-2
- rebuild

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 20.08.0-2
- rebuild (qt5)

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-2
- rebuild (kaccounts)

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-2
- rebuild (qt5)

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 19.08.3-2
- rebuild (qt5)

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Fri Oct 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 19.04.3-3
- rebuild (qt5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 19.04.2-2
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-3
- rebuild (qt5)

* Fri Apr 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-2
- pull in upstream fixes

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-2
- rebuild (qt5)

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Tue Dec 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-2
- rebuild

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Dec 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-2
- rebuild (Qt5)

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Sun Oct 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-2
- move akonadi_knut_resource to main (from -devel)
- use %%make_build

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 18.04.3-3
- rebuild (qt5)

* Wed Aug 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-2
- rebuild (qt5)

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-2
- rebuild (qt5)

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-3
- bootstrap off

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-2
- rebuild (qt5)
- bootstrap mode (avoids broken qtwebkit for now)
- drop Requires: kf5-filesystem (tier 1 frameworks handle that)
- devel: drop R: kf5-kdelibs4support

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Sat Apr 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-2
- own /usr/share/akonadi/plugins, update scriptlets, cleanup

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 17.12.2-2
- rebuild (qt5)

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-2
- rebuild (qt5)

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 17.12.0-2
- rebuild (qt5)

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.90-1
- 17.11.90

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-2
- rebuild (qt5)

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-1
- 17.11.80

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Mon Oct 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-3
- rebuild (qt5)

* Tue Sep 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-2
- backport mariadb workaround (#1491316)

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-3
- rebuild (qt5)

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 17.04.2-2
- Rebuilt for Boost 1.64

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Mon May 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-3
- rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.04.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu May 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-3
- rebuild (qt5)

* Thu Mar 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-2
- rebuild, update URL

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Thu Dec 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-2
- rebuild (qt5)

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-2
- release++

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1.2
- branch rebuild (qt5)

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-3
- Obsoletes: kf5-akonadi-socialutils(-devel) (#1384477)

* Sun Sep 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-2
- drop hack to workaround issue(s) with case-insensitive filesystems (#1379080)

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Sat Sep 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sat Sep 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-4
- rebuild (gcc)

* Sun Jul 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-3
- backport FTBFS fix
- make build use mysql backend as default (so tests use that)
- add alternatives support for sqlite backend to main pkg

* Wed Jul 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-2
- BR: qt5-qtbase-private-devel (sqlite3 driver plugin)

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Tue Jun 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Tue May 24 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-2
- backport Fix-MySQL-5.7-support.patch

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Sun May 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-2
- -devel: Obsoletes: kf5-akonadi-devel, add Requires: inherited from kf5-aknoadi-devel

* Sat Apr 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0, update URL, support bootstrap, add %%check

* Mon Mar 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-3
- -mysql: Provides: akonadi-mysql

* Thu Mar 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-2
- Recommends: kf5-akonadi-mysql

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.2-1
- 15.12.2

* Sat Feb 06 2016 Rex Dieter <rdieter@fedoraproject.org> 15.12.1-1
- 15.12.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Rex Dieter <rdieter@fedoraproject.org> 15.12.0-2
- move dbus-1/interfaces to -devel, (unversioned) Conflicts: akonadi-devel

* Tue Dec 15 2015 Jan Grulich <jgrulich@redhat.com> - 15.12-0-1
- Update to 15.12.0

* Fri Dec 11 2015 Rex Dieter <rdieter@fedoraproject.org> 15.11.90-2
- Conflicts: akonadi < 1.13.0-100 (#1289646)

* Mon Dec 07 2015 Jan Grulich <jgrulich@redhat.com> - 15.11.90-1
- Update to 15.11.90

* Thu Dec 03 2015 Jan Grulich <jgrulich@redhat.com> - 15.11.80-1
- Update to 15.11.80

* Mon Aug 24 2015 Daniel Vr??til <dvratil@redhat.com> - 15.08.0-1
- Initial version, based on akonadi.spec
