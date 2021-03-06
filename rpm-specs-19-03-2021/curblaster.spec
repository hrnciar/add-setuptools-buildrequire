Name: curblaster
Version:  1.13
Release:  9%{?dist}
Summary: Sidescrolling shooter, carry the pods through the gate

License: GPLv3+
URL: http://curblaster.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires: ncurses-devel, desktop-file-utils, SDL2_mixer-devel, cppcheck
BuildRequires: make
Requires: hicolor-icon-theme

%description
Grab pods and drop them in the gate, while fighting enemies in your way.
Multiple weapons available.

%prep
%setup -q

%build

make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 curblaster %{buildroot}%{_bindir}/curblaster
mkdir -p %{buildroot}%{_mandir}/man6
install -p -m644 curblaster.6 %{buildroot}%{_mandir}/man6/curblaster.6
mkdir -p %{buildroot}%{_datadir}/curblaster/data
install -p -m644 data/* %{buildroot}%{_datadir}/curblaster/data
mkdir -p %{buildroot}%{_datadir}/appdata
install -m 644 curblaster.appdata.xml %{buildroot}%{_datadir}/appdata/

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
  curblaster.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 curblaster-logo.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%check
make check



%files
%{_bindir}/curblaster
%doc CHANGELOG COPYING
%{_datadir}/applications/curblaster.desktop
%{_datadir}/icons/hicolor/32x32/apps/curblaster-logo.png
%{_datadir}/curblaster/
%{_mandir}/man6/curblaster.6.gz
%{_datadir}/appdata/curblaster.appdata.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.13-2
- Remove obsolete scriptlets

* Thu Aug 24 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.13-1
- 1.13 minor bugfixes.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jon Ciesla <limburgher@gmail.com> - 1.12-1
- 1.12

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.11-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Sep 24 2014 Jon Ciesla <limburgher@gmail.com> - 1.11-1
- Migrated to SDL2.
- Included AppData.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 Jon Ciesla <limburgher@gmail.com> - 1.10-1
- Improved in-game documentation.

* Mon Aug 06 2012 Jon Ciesla <limburgher@gmail.com> - 1.09-1
- Fix for crash, BZ 845930.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Jon Ciesla <limburgher@gmail.com> - 1.08-1
- Fixed gcc 4.7.0 errors.

* Sun Dec 04 2011 Jon Ciesla <limb@jcomserv.net> - 1.07-1
- Upstream relocated.

* Thu Jun 16 2011 Jon Ciesla <limb@jcomserv.net> - 1.06-1
- Silenced remaining compiler warnings.

* Fri Jun 10 2011 Jon Ciesla <limb@jcomserv.net> - 1.05-1
- Silenced a few compiler warnings.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 18 2010 Jon Ciesla <limb@jcomserv.net> - 1.04-1
- Made any upstream flags non-mandatory.

* Tue Mar 16 2010 Jon Ciesla <limb@jcomserv.net> - 1.03-1
- Fixed flags, macros, icon scriptlets, linking, timestamps,
- description and sumamry.

* Fri Jan 15 2010 Jon Ciesla <limb@jcomserv.net> - 1.02-1
- Renamed project.

* Thu Jan 07 2010 Jon Ciesla <limb@jcomserv.net> - 1.01-1
- Review fixes in summary, macros, vendor desktop tag.

* Wed Jan 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-1
- create.
