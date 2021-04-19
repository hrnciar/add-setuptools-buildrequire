Name:		edac-utils
Version:	0.18
Release:	2%{?dist}
Summary:	Userspace helper for kernel EDAC drivers
License:	GPLv2+
URL:		https://github.com/grondo/edac-utils

ExcludeArch:	s390x
Source0:	https://github.com/grondo/edac-utils/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	edac.service

%ifarch %{ix86} x86_64
Requires:	dmidecode
%endif
Requires:	hwdata
Requires:	sysfsutils
Requires:	systemd
BuildRequires:	gcc
BuildRequires:	libsysfs-devel
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	systemd
BuildRequires:	systemd-devel

%description 
EDAC is the current set of drivers in the Linux kernel that handle
detection of ECC errors from memory controllers for most chipsets
on i386 and x86_64 architectures. This userspace component consists
of an init script which makes sure EDAC drivers and DIMM labels
are loaded at system startup, as well as a library and utility
for reporting current error counts from the EDAC sysfs files.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development headers and libraries
for %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static
%{make_build}

%install
%{make_install}
# Remove libtool archive
find %{buildroot} -type f -name "*.la" -delete

install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/edac.service
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/init.d/edac

%ldconfig_scriptlets

%post
%systemd_post edac.service

%preun
%systemd_preun edac.service

%postun
%systemd_postun_with_restart edac.service

%files 
%license COPYING
%doc README NEWS DISCLAIMER
%{_sbindir}/edac-ctl
%{_bindir}/edac-util
%{_libdir}/libedac.so.1*
%{_mandir}/*/edac*
%dir %attr(0755,root,root) %{_sysconfdir}/edac
%config(noreplace) %{_sysconfdir}/edac/*
%{_unitdir}/edac.service

%files devel
%{_libdir}/libedac.so
%{_includedir}/edac.h

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.18-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 02 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.18-1
- Update to 0.18
- Spec cleanup
- New upstream URLs/Source

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 23 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.16-13
- BR: systemd (Fix F23FTBFS, RHBZ#1239443).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 22 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.16-11
- edac supported in the kernel for ppc64/aarch64 too

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug  3 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.16-7
- Minor spec cleanups to fix FTBFS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.16-5
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.16-3
- ARM has support for EDAC so enable the utils

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Aristeu Rozanski <aris@redhat.com> - 0.16-1
- New upstream release 0.16

* Wed Mar 14 2012 Jon Ciesla <limburgher@gmail.com> - 0.9-14
- Migrate to systemd, BZ 767784.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9-9
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9-8
- Autorebuild for GCC 4.3

* Wed Jul 18 2007 Aristeu Rozanski <arozansk@redhat.com> 0.9-7
- including missing .patch file

* Tue Jul 17 2007 Aristeu Rozanski <arozansk@redhat.com> 0.9-6
- building FC7 package

* Thu Jul 09 2007 Aristeu Rozanski <arozansk@redhat.com> 0.9-5
- Fixed start/stop message, missing echo
- Fixed status command to use edac-util

* Thu Jun 15 2007 Aristeu Rozanski <arozansk@redhat.com> 0.9-4
- Removed debug code left by mistake on initrd file
- Fixed model comparing in edac-ctl script

* Wed Jun 13 2007 Aristeu Rozanski <arozansk@redhat.com> 0.9-3
- Adding COPYING to documents
- Fixing Requires to use a single equal sign, instead of two

* Wed Jun 13 2007 Aristeu Rozanski <arozansk@redhat.com> 0.9-2
- Multiple updates in spec file to conform to the standards pointed by
  Jarod Wilson

* Wed Jun 06 2007 Aristeu Rozanski <arozansk@redhat.com> 0.9-1
- Updated version to 0.9, separate project now
- Updated spec file based on upstream edac-utils spec file
- Removed driver loading portion in a separate patch, it'll be removed from
  upstream too
- Fixed init script to use functions and daemon function

* Thu Apr 19 2007 Aristeu Rozanski <arozansk@redhat.com> 20061222-3
- Updated initrd script to start after syslogd, otherwise if the board isn't
  supported, the user will never know.

* Thu Apr 19 2007 Aristeu Rozanski <arozansk@redhat.com> 20061222-2
- Changing this package to noarch and preventing the build on ia64, ppc64,
  s390 and s390x

* Thu Mar 12 2007 Aristeu Rozanski <arozansk@redhat.com> 20061222-1
- Package created

