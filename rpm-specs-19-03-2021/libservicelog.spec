Name:          libservicelog
Version:       1.1.18
Release:       10%{?dist}
Summary:       Servicelog Database and Library

#v29_notify_gram.c v29_notify_gram.h are GPLv2+
License:       LGPLv2 and GPLv2+
URL:           https://github.com/power-ras/%{name}/releases
Source:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Link with needed libraries
Patch0: libservicelog-1.1.9-libs.patch

BuildRequires: sqlite-devel autoconf libtool bison librtas-devel flex
BuildRequires: make
Requires(pre): shadow-utils

# because of librtas-devel
ExclusiveArch: ppc %{power64}

%description
The libservicelog package contains a library to create and maintain a
database for storing events related to system service.  This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the system.


%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig sqlite-devel

%description   devel
Contains header files for building with libservicelog.


%prep
%setup -q
%patch0 -p1 -b .libs

%build
autoreconf -fiv
%configure --disable-static
# disable "-Werror=format-security" checking gcc option until we fix
# these errors are fixed in upstream code.
CFLAGS="%{optflags} -fPIC -DPIC"
CFLAGS=`echo $CFLAGS | sed 's/-Werror=format-security//'`
make CFLAGS="$CFLAGS" %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%check
make check || true

%pre
getent group service >/dev/null || /usr/sbin/groupadd -r service

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS
%{_libdir}/libservicelog-*.so.*
%dir %attr(755, root, service) /var/lib/servicelog
%config(noreplace) %verify(not md5 size mtime) %attr(644,root,service) /var/lib/servicelog/servicelog.db

%files devel
%{_includedir}/servicelog-1
%{_libdir}/*.so
%{_libdir}/pkgconfig/servicelog-1.pc


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Than Ngo <than@redhat.com> - 1.1.18-7
- Update Url and Source

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Than Ngo <than@redhat.com> - 1.1.18-5
- enable tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.1.18-1
- Rebase to 1.1.18

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.1.17-1
- Rebase to 1.1.17

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.16-3
- spec file cleanups
- Use %%license

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.16-2
- Rebuild for librtas soname bump

* Mon Mar 21 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.16-1
- Update to latest upstream 1.1.16

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Jaromir Capik <jcapik@redhat.com> - 1.1.15-3
- Creating the 'service' group as a system one (#1212938)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.1.15
- Update to latest upstream 1.1.15

* Fri Aug 01 2014 Brent Baude <bbaude@redhat.com> - 1.1.14-8
- NVR bump for Fedora 21 build on merged koji

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Jakub Čajka <jcajka@redhat.com> - 1.1.14-6
- Spec file clean up

* Mon Mar 10 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.14-5
- Fix CFLAGS

* Fri Mar 07 2014 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.1.14-4
- Disable "-Werror=format-security" gcc option

* Thu Oct 10 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.14-3
- Add ppc64le architecture

* Mon Sep 16 2013 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.1.14-2
- Fix build issue

* Wed Aug 21 2013 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.1.14
- Update to latest upstream 1.1.14

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 18 2013 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.1.13
- Update to latest upstream 1.1.13

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Jiri Skala <jskala@redhat.com> - 1.1.11-1
- update to latest upstream 1.1.11

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 04 2010 Roman Rakus <rrakus@redhat.com> - 1.1.9-4
- Properly handle servicelog.db

* Tue May 18 2010 Roman Rakus <rrakus@redhat.com> - 1.1.9-2
- Link with needed libraries (sqlite, rtas, rtasevent)

* Tue May 11 2010 Roman Rakus <rrakus@redhat.com> - 1.1.9-1
- Update to 1.1.9

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Roman Rakus <rrakus@redhat.com> - 1.0.1-2
- Added missing requires sqlite-devel in devel subpackage

* Fri Feb 20 2009 Roman Rakus <rrakus@redhat.com> - 1.0.1-1
- Initial packaging
