Name:           arpwatch
Epoch:          14
Version:        3.1
Release:        9%{?dist}
Summary:        Network monitoring tools for tracking IP addresses on a network

License:        BSD with advertising
URL:            https://ee.lbl.gov/

Requires(pre):  shadow-utils

Requires:       %{_sbindir}/sendmail
Requires:       python3

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{_sbindir}/sendmail
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3
BuildRequires:  libpcap-devel

# Note that https://ee.lbl.gov/ may not link to the latest version; the
# directory listing at https://ee.lbl.gov/downloads/arpwatch/ shows all
# available versions.
Source0:        https://ee.lbl.gov/downloads/%{name}/%{name}-%{version}.tar.gz
# This file comes from http://standards-oui.ieee.org/oui/oui.csv; it is used to
# generate ethercodes.dat. Because it is unversioned (and frequently updated),
# we store the file directly in the repository with the spec file; see the
# update-oui-csv script.
#
# File oui.csv last fetched 2021-03-17T20:42:05+00:00.
Source1:        oui.csv
Source2:        %{name}.service
Source3:        %{name}.sysconfig
Source4:        arp2ethers.8
Source5:        massagevendor.8

# Fix section numbers in man page cross-references. With minor changes, this
# patch dates all the way back to arpwatch-2.1a4-man.patch, from RHBZ #15442.
Patch1:         %{name}-man-references.patch
# Add, and document, a -u argument to change to a specified unprivileged user
# after establishing sockets. This combines and improves multiple previous
# patches; see patch header and changelog for notes.
Patch2:         %{name}-change-user.patch
# Fix nonstandard sort flags in arp2ethers script.
Patch3:         %{name}-arp2ethers-sort-invocation.patch
# Fix stray rm (of an undefined variable) in example arpfetch script.
Patch4:         %{name}-arpfetch-stray-rm.patch
# Do not add /usr/local/bin or /usr/local/sbin to the PATH in any scripts
Patch5:         %{name}-no-usr-local-path.patch
# Do not attempt to search for local libpcap libraries lying around in the parent
# of the build directory, or anywhere else random. This is not expected to
# succeed anyway, but it is better to be sure.
Patch6:         %{name}-configure-no-local-pcap.patch
# RHBZ #244606: Correctly handle -n 0/32 to allow the user to disable reporting
# bogons from 0.0.0.0.
Patch7:         %{name}-all-zero-bogon.patch
# When arpwatch is terminated cleanly by a signal (INT/TERM/HUP) handler, the
# exit code should be zero for success instead of nonzero for failure.
Patch8:         %{name}-exitcode.patch
# When -i is not given, do not just try the first device found, but keep
# checking devices until a usable one is found, if any is available.
# Additionally, handle the case where a device provides both supported and
# unsupported datalink types.
Patch9:         %{name}-devlookup.patch

%global pkgstatedir %{_sharedstatedir}/%{name}
%global pkgdatadir %{_datadir}/%{name}
%global service_user %{name}
%global service_group %{name}
# Soft static UID and GID; see
# https://fedoraproject.org/wiki/Packaging:UsersAndGroups#Soft_static_allocation
# for information, and the uidgid file in the setup package
# (https://pagure.io/setup/blob/master/f/uidgid) for the list of allocations,
# including the one for arpwatch.
%global service_uid 77
%global service_gid 77

%description
The %{name} package contains arpwatch and arpsnmp. Arpwatch and arpsnmp are
both network monitoring tools. Both utilities monitor Ethernet or FDDI network
traffic and build databases of Ethernet/IP address pairs, and can report
certain changes via email.

Install the %{name} package if you need networking monitoring devices which
will automatically keep track of the IP addresses on your network.


%prep
%autosetup -p1

# Substitute absolute paths to awk scripts in shell scripts
sed -r -i 's|(-f *)([^[:blank:]+]\.awk)|\1%{pkgdatadir}/\2|' arp2ethers

# Fix default directory in man pages to match ARPDIR in build section. This was
# formerly done by arpwatch-dir-man.patch. For thoroughness, do the same
# replacement in update-ethercodes.sh.in and bihourly.sh, even though they are
# not installed.
sed -r -i 's|/usr/local/arpwatch|%{pkgstatedir}|g' *.8.in *.sh.in *.sh


%build
%configure \
    V_SENDMAIL=%{_sbindir}/sendmail \
    PYTHON=%{__python3}
%make_build ARPDIR=%{pkgstatedir}


%install
# The upstream Makefile does not create the directories it requires, so we must
# do it manually. Additionally, it attempts to comment out the installation of
# the init script on non-FreeBSD platforms, but this does not quite work as
# intended. We just let it install the file, then exclude it from the files
# list.
install -d %{buildroot}%{_mandir}/man8 \
    %{buildroot}%{_sbindir} \
    %{buildroot}%{pkgdatadir} \
    %{buildroot}%{pkgstatedir} \
    %{buildroot}%{_unitdir} \
    %{buildroot}%{_prefix}/etc/rc.d

%make_install

install -p -t %{buildroot}%{pkgdatadir} -m 0644 *.awk
install -p -t %{buildroot}%{_sbindir} arp2ethers
install -p massagevendor.py %{buildroot}%{_sbindir}/massagevendor

install -p -t %{buildroot}%{pkgstatedir} -m 0644 *.dat
touch %{buildroot}%{pkgstatedir}/arp.dat- \
    %{buildroot}%{pkgstatedir}/arp.dat.new

install -p -t %{buildroot}%{_unitdir} -m 0644 %{SOURCE2}
%{__python3} massagevendor.py < %{SOURCE1} \
    > %{buildroot}%{pkgstatedir}/ethercodes.dat
touch -r %{SOURCE1} ethercodes.dat

# Add an environment/sysconfig file:
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# Add extra man pages not provided upstream:
install -p -t %{buildroot}%{_mandir}/man8 -m 0644 %{SOURCE4} %{SOURCE5}


%check
# Verify the sed script in the prep section did not miss fixing the ARPDIR
# anywhere
if grep -FrnI '/usr/local/arpwatch' .
then
  echo 'Missed fixing ARPDIR in at least one file' 1>&2
  exit 1
fi

# Verify we did not miss any PATH alterations in arpwatch-no-usr-local-path.patch.
if grep -ErnI --exclude=mkdep --exclude='config.*' '^[^#].*/usr/local/s?bin' .
then
  echo 'Probably missed an uncommented PATH alteration with /usr/local' 1>&2
  exit 1
fi


%post
%systemd_post %{name}.service


%pre
getent group %{service_group} >/dev/null ||
  groupadd -f -g %{service_gid} -r %{service_group}
if ! getent passwd %{service_user} >/dev/null
then
  if ! getent passwd %{service_uid} >/dev/null
  then
    useradd -r -u %{service_uid} -g %{service_group} \
        -d %{pkgstatedir} -s /sbin/nologin \
        -c "Service user for %{name}" %{service_user}
  else
    useradd -r -g %{service_group} \
        -d %{pkgstatedir} -s /sbin/nologin \
        -c "Service user for %{name}" %{service_user}
  fi
fi
exit 0


%postun
%systemd_postun_with_restart %{name}.service


%preun
%systemd_preun %{name}.service


%files
%doc README
%doc CHANGES
%doc arpfetch

# make install uses mode 0555, which is unconventional
%attr(0755,-,-) %{_sbindir}/arpwatch
%attr(0755,-,-) %{_sbindir}/arpsnmp
# manually-installed scripts
%{_sbindir}/arp2ethers
%{_sbindir}/massagevendor

%dir %{pkgdatadir}
%{pkgdatadir}/*.awk

# make install uses mode 0444, which is unconventional
%attr(0644,-,-) %{_mandir}/man8/*.8*

%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%exclude %{_prefix}/etc/rc.d/%{name}

%attr(1775,-,%{service_group}) %dir %{pkgstatedir}
%attr(0644,%{service_user},%{service_group}) %verify(not md5 size mtime) %config(noreplace) %{pkgstatedir}/arp.dat
%attr(0644,%{service_user},%{service_group}) %verify(not md5 size mtime) %config(noreplace) %{pkgstatedir}/arp.dat-
%attr(0600,%{service_user},%{service_group}) %verify(not md5 size mtime) %ghost %{pkgstatedir}/arp.dat.new
%attr(0644,-,%{service_group}) %verify(not md5 size mtime) %config(noreplace) %{pkgstatedir}/ethercodes.dat


%changelog
* Wed Mar 17 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 14:3.1-9
- generate ethercodes.dat from latest oui.csv

* Tue Mar 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 14:3.1-8
- generate ethercodes.dat from latest oui.csv

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 14:3.1-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Sun Jan 31 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 14:3.1-6
- generate ethercodes.dat from latest oui.csv

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14:3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 14:3.1-4
- Fix changelog date

* Sat Jan  9 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 14:3.1-3
- Generate ethercodes.dat from latest oui.csv
- Change systemd BR to systemd-rpm-macros
- Drop Requires on systemd for scriptlets per current guidelines

* Wed Dec 16 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 14:3.1-2
- Add BR on make for
  https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot
- generate ethercodes.dat from latest oui.csv

* Wed Nov 11 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 14:3.1-1
- new upstream version 3.1
- generate ethercodes.dat from latest oui.csv
- improve systemd unit file, including hardening
- add sysconfig (environment) file
- drop arpwatch-2.1a4-fhs.patch: version 3.1 no longer attempts to set
  user/group for installed binaries, and permissions for binaries and man pages
  are now adjusted in the files section of the spec file
- rebase arpwatch-2.1a10-man.patch against version 3.1 as
  arpwatch-man-references.patch, fixing some additional cross-references
- rebase against version 3.1 and combine arpwatch-drop.patch, which provided
  -u; arpwatch-drop-man.patch, which documented it; and
  arpwatch-2.1a15-dropgroup.patch, which fixed CVE-2012-2653 (RHBZ #825328) in
  the original arpwatch-drop.patch, into a single combined
  arpwatch-change-user.patch; remove an unnecessary and unchecked strdup() in
  the original patch that could have theoretically led to a null pointer
  dereference
- drop arpwatch-addr.patch; the -e and -s arguments are now present in upstream
  version 3.1 as -w and -W, respectively
- replace arpwatch-dir-man.patch with a sed invocation
- replace arpwatch-2.1a15-extraman.patch with additional source files
  arp2ethers.8 and massagevendor.8; reformat the contents to match the upstream
  arpwatch.8 and arpsnmp.8 man pages; remove references to Debian; and rewrite
  massagevendor.8 to match the new Python-based massagevendor script
- split arpwatch-scripts.patch into arpwatch-arp2ethers-sort-invocation.patch,
  arpwatch-arpfetch-stray-rm.patch, and arpwatch-no-usr-local-path.patch,
  removing some additional PATH alterations in the last
- rebase arpwatch-2.1a15-nolocalpcap.patch against the version 3.1 configure script
  and rename it as arpwatch-configure-no-local-pcap.patch
- rebase arpwatch-2.1a15-bogon.patch against version 3.1 and rename it as
  arpwatch-all-zero-bogon.patch
- rebase arpwatch-exitcode.patch against version 3.1
- rewrite, combine, and simplify arpwatch-2.1a15-devlookup.patch and
  arpwatch-2.1a15-lookupiselect.patch, which fixed RHBZ #842660, as
  arpwatch-devlookup.patch; upstream version 3.1 will now try the first
  interface when -i is not given, but we still need a patch to search for
  another usable interface if the first one is not usable; additionally, the
  patch now handles the case where a device provides both supported and
  unsupported datalink types.
- drop arpwatch-201301-ethcodes.patch; upstream no longer distributes
  ethercodes.dat anyway, and we are generating it from oui.csv
- drop arpwatch-pie.patch; we are passing in hardened CFLAGS/LDFLAGS the normal
  way
- drop arpwatch-aarch64.patch, as upstream now has a more up-to-date
  config.guess
- drop arpwatch-promisc.patch; the -p flag is now upstream
- drop arpwatch-2.1a15-buffer-overflow-bz1563939.patch, which was a backport
  from this version

* Sat Oct 31 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 14:2.1a15-52
- add rpmlintrc file to suppress expected rpmlint errors

* Sat Oct 31 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 14:2.1a15-51
- touch ghost file arp.dat.new (ghost files should exist in the buildroot)

* Sat Oct 31 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 14:2.1a15-50
- use autosetup macro to apply patches

* Fri Oct 30 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 14:2.1a15-49
- drop explicit _hardened_build macro (default in all current Fedora releases)
- replace _vararpwatch macro with pkgstatedir, and define in terms of
  _sharedstatedir instead of _localstatedir
- use buildroot macro instead of RPM_BUILD_ROOT variable
- use package name macro more widely
- create macros for unprivileged service user and group names
- adjust whitespace throughout the spec file
- update URLs
- remove unnecessary BR on systemd
- use make_build and make_install macros; as a consequence, we now preserve
  timestamps when installing files (install -p)
- since we do not package the massagevendor-old script, do not prep it with the
  others
- instead of embedding awk scripts in the shell scripts that use them, install
  the awk scripts and use their absolute paths in the shell scripts; drop BR on
  perl, which was used to quote the awk scripts
- tidy up manual install steps
- remove user/group renaming code from pre-install script, and replace it with
  the suggested implementation for soft static allocation from
  https://fedoraproject.org/wiki/Packaging:UsersAndGroups;
  the pcap user and group were renamed to arpwatch in 2007
  (https://src.fedoraproject.org/rpms/arpwatch/c/f1b7b51), and we have no need
  to handle such ancient installations anymore

* Tue Oct 27 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 14:2.1a15-48
- fix arpwatch buffer overflow (#1563939)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar  5 2018 Jan Synáček <jsynacek@redhat.com> - 14:2.1a15-42
- make sure arpwatch starts after network devices are up (#1551431)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Jan Synáček <jsynacek@redhat.com> - 14:2.1a15-38
- fix FTBFS (#1423238)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14:2.1a15-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jan Synáček <jsynacek@redhat.com> - 14:2.1a15-35
- fix arpwatch buffer overflow (#1301880)
- add -p option that disables promiscuous mode (#1301853)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb  3 2014 Jan Synáček <jsynacek@redhat.com> 14:2.1a15-31
- reference documentation in the service file
- remove redundant sysconfig-related stuff

* Sun Aug  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 14:2.1a15-30
- Fix FTBFS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Jan Synáček <jsynacek@redhat.com> 14:2.1a15-28
- harden the package (#954336)
- support aarch64 (#925027)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Ales Ledvinka <aledvink@redhat.com> - 14:2.1a15-26
- fix permissions related to collected database
- update ethcodes defaults to current public IEEE OUI-32

* Mon Oct 15 2012 Ales Ledvinka <aledvink@redhat.com> - 14:2.1a15-25
- fix -i with invalid interface specified (#842660)

* Mon Oct 15 2012 Ales Ledvinka <aledvink@redhat.com> - 14:2.1a15-24
- fix devlookup to start with -i interface specified (#842660)

* Wed Aug 22 2012 Jan Synáček <jsynacek@redhat.com> - 14:2.1a15-23
- Add system-rpm macros (#850032)

* Tue Jul 24 2012 Jan Synáček <jsynacek@redhat.com> - 14:2.1a15-22
- add devlookup patch: search for suitable default interface, if -i is not
  specified (#842660)

* Thu Jul 19 2012 Jan Synáček <jsynacek@redhat.com> - 14:2.1a15-21
- make spec slightly more fedora-review-friendly

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 Aleš Ledvinka <aledvink@redhat.com> 14:2.1a15-20
- fix supplementary group list (#825328) (CVE-2012-2653)

* Thu Jan 19 2012 Jan Synáček <jsynacek@redhat.com> 14:2.1a15-19
- Turn on PrivateTmp=true in service file (#782477)

* Thu Jan 05 2012 Jan Synáček <jsynacek@redhat.com> 14:2.1a15-18
- Rebuilt for GCC 4.7

* Fri Jul 08 2011 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-17
- exit with zero error code (#699285)
- change service type to forking (#699285)

* Thu Jul 07 2011 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-16
- replace SysV init script with systemd service (#699285)
- update ethercodes.dat

* Mon Mar 28 2011 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-15
- update ethercodes.dat (#690948)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 30 2010 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-13
- update ethercodes.dat (#577552)
- mark ethercodes.dat as noreplace
- fix init script LSB compliance
- include Debian arp2ethers and massagevendor man pages (#526160)
- don't include massagevendor-old script anymore

* Wed Sep 02 2009 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-12
- update ethercodes.dat

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:2.1a15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 16 2008 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-9
- update ethercodes.dat (#462364)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 14:2.1a15-8
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-7
- rebuild

* Thu Aug 09 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-6
- improve init script (#246869)
- allow -n 0/32 to disable reporting bogons from 0.0.0.0 (#244606)
- update license tag
- update ethercodes.dat

* Wed Jun 13 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-5
- update ethercodes.dat

* Thu May 24 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-4
- fix return codes in init script (#237781)

* Mon Jan 15 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-3
- rename pcap user to arpwatch

* Tue Nov 28 2006 Miroslav Lichvar <mlichvar@redhat.com> 14:2.1a15-2
- split from tcpdump package (#193657)
- update to 2.1a15
- clean up files in /var
- force linking with system libpcap
