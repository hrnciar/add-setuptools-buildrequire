Name:    lxqt-session
Summary: Main session for LXQt desktop suite
Version: 0.16.0
Release: 2%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:  0001-Configure-Fedora-theme.patch
BuildRequires: make
BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires: pkgconfig(lxqt) >= 0.15.0
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libudev)
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(glib-2.0)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

Requires:      dbus-x11
Requires:      openbox-theme-mistral-thin
Requires:      lxqt-themes-fedora

%if 0%{?fedora}
# use pcmanfm-qt for default desktop
Recommends:    pcmanfm-qt
%endif

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-session
Requires:       lxqt-session
%description l10n
This package provides translations for the lxqt-session package.

%prep
%setup -q
%patch1 -p1

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

mkdir -p %{_target_platform}
pushd %{_target_platform}
	%{cmake_lxqt} -DBUNDLE_XDG_UTILS=NO -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
for name in config-session hibernate lockscreen logout reboot shutdown suspend; do 
	desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
		--remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-${name}.desktop
done
mkdir %{buildroot}%{_sysconfdir}/lxqt/
cp %{buildroot}%{_datadir}/lxqt/lxqt.conf %{buildroot}%{_datadir}/lxqt/session.conf %{buildroot}%{_sysconfdir}/lxqt/
%if 0%{?fedora}
sed -i 's/theme=frost/theme=fedora-lxqt/g;s/icon_theme=oxygen/icon_theme=breeze/g' %{buildroot}%{_sysconfdir}/lxqt/lxqt.conf
sed -i 's/cursor_theme=whiteglass/cursor_theme=breeze_cursors/g;/General/a window_manager=openbox' %{buildroot}%{_sysconfdir}/lxqt/session.conf
%endif
%if 0%{?el7}
sed -i 's/theme=frost/theme=fedora-lxqt/g;s/icon_theme=oxygen/icon_theme=breeze/g' %{buildroot}%{_sysconfdir}/lxqt/lxqt.conf
sed -i 's/cursor_theme=whiteglass/cursor_theme=Adwaita/g;/General/a window_manager=openbox' %{buildroot}%{_sysconfdir}/lxqt/session.conf
%endif


%find_lang lxqt-session --with-qt
%find_lang lxqt-config-session --with-qt
%find_lang lxqt-leave --with-qt

%files
%{_bindir}/lxqt-session
%{_bindir}/lxqt-config-session
%{_bindir}/lxqt-leave
%{_bindir}/startlxqt
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/autostart/lxqt-xscreensaver-autostart.desktop
%{_sysconfdir}/xdg/openbox/lxqt-rc.xml
%{_sysconfdir}/lxqt/
%{_datadir}/kdm/sessions/lxqt.desktop
%{_datadir}/lxqt/lxqt.conf
%{_datadir}/lxqt/session.conf
%{_datadir}/lxqt/windowmanagers.conf
%{_datadir}/xsessions/lxqt.desktop
%{_mandir}/man1/startlxqt.1.gz
%{_mandir}/man1/lxqt-config-session*
%{_mandir}/man1/lxqt-leave*
%{_mandir}/man1/lxqt-session*

%files l10n -f lxqt-session.lang -f lxqt-leave.lang -f lxqt-config-session.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/%{name}
%dir %{_datadir}/lxqt/translations/lxqt-config-session
%dir %{_datadir}/lxqt/translations/lxqt-leave
%dir %{_datadir}/lxqt/translations/lxqt-session
%{_datadir}/lxqt/translations/lxqt-config-session/lxqt-config-session_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-session/lxqt-config-session_arn.qm
%{_datadir}/lxqt/translations/lxqt-leave/lxqt-leave_ast.qm
%{_datadir}/lxqt/translations/lxqt-leave/lxqt-leave_arn.qm
%{_datadir}/lxqt/translations/lxqt-session/lxqt-session_ast.qm
%{_datadir}/lxqt/translations/lxqt-session/lxqt-session_arn.qm

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Tue Aug 25 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-4
- Fix default Qt theme
- Fixes RHBZ#1872163

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-2
- Fix default theme name

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-3
- Update to use newer Fedora lxqt theme

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-1
- Update to version 0.14.1

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.13.0-5
- Requires: dbus-x11 (#1652431)

* Sat Sep 01 2018 Raphael Groner <projects.rg@smart.ms> - 0.13.0-4
- add weak dependency for pcmanfm-qt for functional default desktop

* Mon Aug 27 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-3
- Change to Requires: lxqt-themes-fedora

* Sun Aug 26 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-2
- Configure Fedora theme

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> -  0.11.0-1
- New upstream release 0.11.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Another razorqt obsoletes

* Sat Dec 12 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Prepare to epel7 with new cmake3

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-session and razorqt-desktop as migrated to lxqt

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Proper add locale for Qt tm files

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Prepare 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-6
- Rebuild against new Qt 5.4.0

* Sat Dec 20 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Unify naming as discussed on Fedora IRC

* Thu Nov 20 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-4
- omit Obsoletes: razorqt-session (for now)

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update for review issues on https://bugzilla.redhat.com/show_bug.cgi?id=1158999

* Thu Oct 30 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Obsoletes razorqt session. Disable internal XDG_UTILS

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
