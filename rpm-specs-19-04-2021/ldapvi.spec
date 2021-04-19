Name:           ldapvi
Version:        1.7
Release:        37%{?dist}
Summary:        An interactive LDAP client

License:        GPLv2+
URL:            http://www.lichteblau.com/ldapvi/
Source0:        http://www.lichteblau.com/download/ldapvi-%{version}.tar.gz
Patch0:         GNUmakefile.in.patch
Patch1:         %{name}-1.7-getline.patch
# discussed upstream
# http://lists.askja.de/pipermail/ldapvi/2011-January/000089.html
# but never applied
Patch2:         dont-set-encoding-in-vim-modeline.diff
# Reported upstream
# http://lists.askja.de/pipermail/ldapvi/2013-April/000114.html
Patch3:         ldapvi-1.7-fix-use-after-free-in-sasl-code.patch
# Reported upstream
# http://lists.askja.de/pipermail/ldapvi/2013-September/000116.html
Patch4:         ldapvi-1.7-incorrect-FSF-address.patch
# http://lists.askja.de/pipermail/ldapvi/2017-December/000120.html
Patch5:         0001-Don-t-switch-off-canonical-mode.patch


BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openldap-devel, ncurses-devel, readline-devel, pkgconfig
BuildRequires:  libxslt, glib2-devel, openssl-devel
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires: popt
%else
BuildRequires: popt-devel
%endif

%description
ldapvi is an interactive LDAP client for Unix terminals. Using it, you can
update LDAP entries with a text editor, which is the same as vi. Think of
it as vipw(1) for LDAP.

%prep
%setup -q
%patch0 -p0 -b .gnumk
%patch1 -p2 -b .getline
%patch2 -p2 -b .encoding
%patch3 -p2 -b .doubleFree
%patch4 -p1 -b .FSFaddress
%patch5 -p1 -b .nopassword

%build
%configure
make %{?_smp_mflags}
cd manual
make manual.html


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install



%files
%doc NEWS COPYING manual/bg.png
%doc manual/manual.html manual/manual.css
%{_mandir}/man1/ldapvi.1.gz
%{_bindir}/ldapvi


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7-33
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.7-31
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Matěj Cepl <mcepl@redhat.com> - 1.7-29
- Add patch 0001-Don-t-switch-off-canonical-mode.patch (avoid password
  in logs)
- Add BR gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.7-27
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.7-23
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Matej Cepl <mcepl@redhat.com> - 1.7-20
- Add popt-devel BR even for RHEL-7 (#1161952)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 11 2013 Matěj Cepl <mcepl@redhat.com> - 1.7-17
- Add fix of double free() crash (#949157)
- Fix old FSF address

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 12 2011 Matěj Cepl <mcepl@redhat.com> - 1.7-12
- don't play with the file encoding (#691958)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 07 2009 Matěj Cepl <mcepl@redhat.com> - 1.7-10
- Improving .spec file to work both on Fedora and RHEL

* Fri Sep 18 2009 Matěj Cepl <mcepl@redhat.com> - 1.7-9
- Fixed build to cure FTBFS (#511746)
  Thanks for sharkcz for making the patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.7-7
- rebuild with new openssl

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7-6
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.7-5
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.7-4
 - Rebuild for deps

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.7-3
- Build Require popt-devel instead of popt.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.7-2
- Rebuild for selinux ppc32 issue.

* Thu Jul 05 2007 Gavin Henry <ghenry@suretecsystems.com> - 1.7-1
- Initial version
