Name:               conman
Version:            0.3.0
Release:            5%{?dist}
Summary:            ConMan - The Console Manager

License:            GPLv3+
URL:                https://dun.github.io/conman/
Source0:            https://github.com/dun/%{name}/archive/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:           logrotate
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
BuildRequires:      gcc
BuildRequires:      perl-generators
BuildRequires:      freeipmi-devel
BuildRequires:      systemd
BuildRequires: make

%description
ConMan is a serial console management program designed to support a large
number of console devices and simultaneous users.  It currently supports
local serial devices and remote terminal servers (via the telnet protocol).
Its features include:

  - mapping symbolic names to console devices
  - logging all output from a console device to file
  - supporting monitor (R/O), interactive (R/W), and
    broadcast (W/O) modes of console access
  - allowing clients to join or steal console "write" privileges
  - executing Expect scripts across multiple consoles in parallel


%prep
%setup -qn %{name}-%{name}-%{version}

# fix paths
sed -i -e 's|lib\/|share\/|g' lib/examples/*.exp

# fix shebang
sed -i -e 's|\/usr\/bin\/env perl|\/usr\/bin\/perl|g' conmen


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# clean sysvinit stuff
rm -r $RPM_BUILD_ROOT/etc/{init.d,sysconfig}

# make log directories
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}.old

# examples don't belong in libdir
rm -r $RPM_BUILD_ROOT/usr/lib/%{name}/examples
# move scripts to proper place
mv $RPM_BUILD_ROOT/usr/lib/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod -x $RPM_BUILD_ROOT%{_datadir}/%{name}/*.exp


%post
%systemd_post conman.service

%preun
%systemd_preun conman.service

%postun
%systemd_postun_with_restart conman.service


%files
%license COPYING
%doc AUTHORS FAQ NEWS
%doc lib/examples
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%dir %{_localstatedir}/log/%{name}
%dir %{_localstatedir}/log/%{name}.old
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/%{name}/
%{_mandir}/*/*


%changelog
* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.0-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Dan Hor??k <dan[at]danny.cz> - 0.3.0-1
- updated to 0.3.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.9-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Dan Hor??k <dan[at]danny.cz> - 0.2.9-1
- updated to 0.2.9 (#1526194)
- build without tcp_wrappers (https://fedoraproject.org/wiki/Changes/Deprecate_TCP_wrappers)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Dan Hor??k <dan[at]danny.cz> - 0.2.8-1
- updated to 0.2.8
- spec cleanups (#1244218)
- enable IPMI support

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 David Sommerseth <davids@redhat.com> - 0.2.7-9
- Minor cleanup, corrected URL and %%Source0 to new upstream hosting
- Align package license with upstream license - GPLv3+

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- BR: systemd-units for %%{_unitdir} macro definition

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.2.7-4
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.7-1
- Migrate to systemd, BZ 771474.

* Sun Apr 15 2012 Steven M. Parrish <smparrish@gmail.com> - 0.2.7-0
- New upstream release

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 0.2.5-0
- New upstream release

* Mon Apr 20 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 0.2.4.1-1
- New upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 06 2008 Jarod Wilson <jarod@redhat.com> 0.2.2-2
- The console option in conman.conf is case-insensitive, so relax
  defined consoles check in initscript (Mark McLoughlin, #465777)

* Mon Sep 08 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.2.2-1
- New upstream release

* Fri May 02 2008 Jarod Wilson <jwilson@redhat.com> 0.2.1-1
- New upstream release

* Wed Feb 13 2008 Jarod Wilson <jwilson@redhat.com> 0.1.9.2-8
- Bump and rebuild for gcc 4.3

* Thu Apr 26 2007 Jarod Wilson <jwilson@redhat.com> 0.1.9.2-7
- Update project urls
- Fix up initscript exit codes (#237936)

* Tue Sep 05 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.2-6
- Bump for new glibc

* Fri Jul 28 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.2-5
- Properly enable smp_mflags this time

* Fri Jul 28 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.2-4
- Add Reqs on chkconfig and service
- Turn on smp_mflags
- Initial build for RHEL5

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.2-3
- Add missing condrestart fuction to initscript

* Tue Jun 27 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.2-2
- Don't strip bins on make install, leave for find-debug.sh

* Tue Jun 27 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.2-1
- Update to 0.1.9.2

* Tue Jun 20 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.1-3
- Add Requires: logrotate
- Ugh, conmand exits cleanly if no CONSOLE(s) are defined in
  /etc/conman.conf, add check to initscript to report failure
  if none are defined

* Wed Jun 14 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.1-2
- Create log directories and install working logrotate config
- Use a much cleaner RH/FC-specific initscript

* Tue Jun 13 2006 Jarod Wilson <jwilson@redhat.com> 0.1.9.1-1
- Initial build for Fedora Extras
