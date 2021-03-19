%global extdir		%{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global giturl		https://github.com/micheleg/dash-to-dock
#%%global commit 71abe800b2bc0bca60c63c8e646db2a8a9827ddf
#%%global commit_short 71abe80
#%%global commit_date 20201004


Name:		gnome-shell-extension-dash-to-dock
Version:	69
Release:	4%{?dist}
#Release:	2.%%{commit_date}git%%{commit_short}%%{?dist}
Summary:	Dock for the Gnome Shell by micxgx@gmail.com

License:	GPLv2+
URL:		https://micheleg.github.io/dash-to-dock
%if 0%{?commit:1}
Source0:	%{giturl}/archive/%{commit}.tar.gz
%else
Source0:	%{giturl}/archive/extensions.gnome.org-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	%{_bindir}/glib-compile-schemas
BuildRequires: make

Requires:	gnome-shell-extension-common
# libdbusmenu won't be part of RHEL 9, thus disable the dependency.
%if 0%{?fedora}
Requires:	libdbusmenu-gtk3
%endif

%description
This extension enhances the dash moving it out of the overview and
transforming it in a dock for an easier launching of applications
and a faster switching between windows and desktops without having
to leave the desktop view.


%prep
%if 0%{?commit:1}
%autosetup -n dash-to-dock-%{commit} -p 1
%else
%autosetup -n dash-to-dock-extensions.gnome.org-v%{version} -p 1
%endif


%build
%make_build


%install
%make_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Create manifest for i18n.
%find_lang %{name} --all-name


# Fedora handles this using triggers.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
	%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi


%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Tomas Popela <tpopela@redhat.com> - 69-3
- Disable the libdbusmenu-gtk3 dependency on ELN/RHEL 9 as it won't contain
  libdbusmenu

* Thu Nov 19 2020 Mike DePaulo <mikedep333@gmail.com> - 69-2
- Merge PR from topherisswell (Christopher Morrow) to depend on libdbusmenu-gtk3
- Either this or the previous change (or both) should resolve enabling the
  extension on recent / all installations of F33 (rhbz: #1884795)

* Thu Nov 19 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 69-1.20201004git71abe80
- Upgrade to version 69, fixing GNOME 3.38 compatibility issues

* Mon Sep 14 2020 Mike DePaulo <mikedep333@gmail.com> - 68-3.20200911gite2cc441
- Upgrade to PR/branch for GNOME 3.38 compatibility, latest as of 2020-09-11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Mike DePaulo <mikedep333@gmail.com> - 68-1
- Update from nightlies (called v67, of v68) to v68 release (2020-04-19)

* Thu Apr 16 2020 Mike DePaulo <mikedep333@gmail.com> - 67-8.20200408git3ca96a2
- Rebase to master branch as of 2020-04-15
  ("Use new convenience function to open settings")
- Use latest proposed patches (37 total) for GNOME 3.36 compatibility
  as of 2020-04-16
  ("DnD shoud work properly also in horizontal mode")

* Thu Apr 09 2020 Mike DePaulo <mikedep333@gmail.com> - 67-7.20200408git77bc707
- Rebase to master branch as of 2020-04-08
- Use latest proposed patches (36 total) for GNOME 3.36 compatibility
  as of 2020-04-08
  https://github.com/micheleg/dash-to-dock/pull/1097#event-3216150535

* Mon Apr 06 2020 Mike DePaulo <mikedep333@gmail.com> - 67-6.20200323git70f1db8
- Rebase to master branch as of 2020-03-23
- Use latest proposed patches (36 total) for GNOME 3.36 compatibility
  (rhbz: #1794889)

* Tue Mar 03 2020 Mike DePaulo <mikedep333@gmail.com> - 67-5.20200224git5658b5c
- Add 7 new addtl proposed patches for GNOME 3.36 compatibility (rhbz: #1794889)

* Thu Feb 27 2020 Mike DePaulo <mikedep333@gmail.com> - 67-4.20200224git5658b5c
- Add new addtl proposed patch for GNOME 3.36 compatibility (rhbz: #1794889)

* Tue Feb 25 2020 Mike DePaulo <mikedep333@gmail.com> - 67-3
- Upgrade to latest master branch
- Add proposed PR/patches for GNOME 3.36 compatibility

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Mike DePaulo <mikedep333@gmail.com> - 67-1
- Upgrade to 67 for GNOME 3.34 (f31) compatibility (rhbz#1753665)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Björn Esser <besser82@fedoraproject.org> - 66-1
- Upgrade to 66 for GNOME 3.32 (f30) compatibility (rhbz#1700690)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Mike DePaulo <mikedep333@gmail.com> - 64-1
- Upgrade to 64 for GNOME 3.30 (f29) compatibility as well as formal
  GNOME 3.28 (f28 & EPEL 7.6) compatibility. (resolves #1634447)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 61-1
- Initial import (rhbz#1520149)

* Fri Dec 01 2017 Björn Esser <besser82@fedoraproject.org> - 61-0.1
- Initial rpm release (rhbz#1520149)
