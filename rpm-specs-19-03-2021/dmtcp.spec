%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		dmtcp
Version:	2.5.2
Release:	6%{?dist}
Summary:	Checkpoint/Restart functionality for Linux processes
License:	LGPLv3+
URL:		http://dmtcp.sourceforge.net
Source0:	http://github.com/dmtcp/dmtcp/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:	python2

# This package is functional on i386, x86_64 and aarch64 architectures.
ExclusiveArch:	%ix86 x86_64 aarch64

%description
DMTCP (Distributed MultiThreaded Checkpointing) is a tool to transparently
checkpointing the state of an arbitrary group of programs including
multi-threaded and distributed computations.  It operates directly on the user
binary executable, with no Linux kernel modules or other kernel mods.

Among the applications supported by DMTCP are Open MPI, MATLAB, Python, Perl,
and many programming languages and shell scripting languages.  DMTCP also
supports GNU screen sessions, including vim/cscope and emacs. With the use of
TightVNC, it can also checkpoint and restart X-Windows applications, as long as
they do not use extensions (e.g.: no OpenGL, no video).

This package contains DMTCP binaries.

%package -n dmtcp-devel
Summary:	DMTCP developer package
Requires:	dmtcp%{?_isa} = %{version}-%{release}

%description -n dmtcp-devel
This package provides files for developing DMTCP plugins.

%prep
%setup -q

%build
%configure --docdir=%{_pkgdocdir}
%make_build

%install
%make_install

%check
%make_build tests

# Test suite disabled for non-x86_64 architectures.
%ifarch x86_64
# Disable syscall-tester, file, and posix-mq tests until fixed upstream.
sed -i -e's:\(runTest("syscall-tester"\):pass #\1:' test/autotest.py
sed -i -e's:\(runTest("file\):pass #\1:' test/autotest.py
sed -i -e's:\(runTest("posix-mq\):pass #\1:' test/autotest.py
./test/autotest.py --retry-once || :
%endif

%files
%license COPYING
%{_bindir}/dmtcp_*
%{_bindir}/mtcp_restart
%{_libdir}/%{name}
%dir %{_pkgdocdir}
%{_pkgdocdir}
%{_mandir}/man1/*gz

%files -n dmtcp-devel
%{_includedir}/dmtcp.h

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.5.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 28 2017 Kapil Arya <kapil@ccs.neu.edu> - 2.5.2-1
- Update to 2.5.2.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.0-1
- Rebuilt for new upstream version, fixes FTBFS rhbz#1423335

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.4-1
= Update to 2.4.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.2-1
- Update to 2.4.2

* Mon Sep 14 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.1-1
- Update to 2.4.1 for newer kernel and glibc support (fix FTBFS)
- ARMv7 and aarch64 now supported
- Add COPYING license file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Kapil Arya <kapil@ccs.neu.edu> - 2.2-1
- Preparing for upstream release 2.2.
- Remove libmtcp* packages.
- Install all docs in _pkgdocdir 
- Added --retry-once flag to autotest.

* Fri Jan 10 2014 Kapil Arya <kapil@ccs.neu.edu> - 2.1-1
- Preparing for upstream release 2.1.

* Thu Dec 12 2013 Ville Skytta <ville.skytta@iki.fi> - 1.2.8-2
- Install docs to %%{_pkgdocdir} where available (#993726).
- Own package level doc dir.

* Tue Jul 30 2013 Kapil Arya <kapil@ccs.neu.edu> - 1.2.8-1
- Preparing for upstream release 1.2.8.

* Mon Mar 11 2013 Kapil Arya <kapil@ccs.neu.edu> - 1.2.7-1
- Preparing for upstream release 1.2.7.
- Use %%{_docdir} instead of %%doc for QUICK-START and COPYING.

* Tue Oct 09 2012 Orion Poplawski <orion@cora.nwra.com> - 1.2.6-1
- Update to 1.2.6
- Use URL for Source0
- Add patch to drop -fstack-protector on mtcp_maybebpt.c
- Drop configure hack
- Run tests

* Sun Jul 08 2012 kapil@ccs.neu.edu
- Preparing for upstream release 1.2.5.

* Tue Jan 24 2012 kapil@ccs.neu.edu
- Preparing for upstream release 1.2.4.

* Mon Jan 23 2012 kapil@ccs.neu.edu
- Updating to svn 1449.

* Tue Oct 25 2011 kapil@ccs.neu.edu
- Updating to svn 1321.
- libdmtcpaware-devel-static renamed to libdmtcpaware-static
- %%{_isa} added to Requires
- disable_option_checking changed from "fatal" to "no"
- QUICK_START and COPYING installed using %%{doc}

* Tue Aug  9 2011 gene@ccs.neu.edu
- Updating to upstream release 1.2.3-1.svn1247M.
- svn revision 1246 adds objcopy to set section attribute in libmtcp.so
  (if debuginfo repo was present during build, limbtcp.so was missing a section)
- dmtcp.spec and 'make install' changed for improved file layout

* Tue Jul 26 2011 kapil@ccs.neu.edu
- Top level configure files updated to fix configure error.

* Fri Jul 22 2011 kapil@ccs.neu.edu
- Updating to upstream release 1.2.3.

* Sat Jul  2 2011 kapil@ccs.neu.edu
- Updating to upstream release 1.2.2.

* Wed Jun 22 2011 kapil@ccs.neu.edu
- Exclude mtcp.c from installation.

* Wed Jun 22 2011 kapil@ccs.neu.edu
- Updating to upstream release 1.2.2.

* Fri Jun 17 2011 kapil@ccs.neu.edu
- libdmtcpaware.a moved to libdmtcpaware-devel-static package.
- dmtcpaware examples moved to libdmtcpaware-doc package.

* Fri Jun 10 2011 kapil@ccs.neu.edu
- Build requirements updated.
- Minor cleanup.

* Tue Jun  7 2011 kapil@ccs.neu.edu
- Added "ExclusiveArch %%ix86 x86_64" and removed ExcludeArch lines.
- buildroot not cleaned in %%install section.

* Sat May 14 2011 kapil@ccs.neu.edu
- dependency on libc.a removed for mtcp_restart.
- Several other bug fixes and improvements.

* Sat Mar 12 2011 kapil@ccs.neu.edu
- Updated to release 1.2.1

* Fri Mar 11 2011 kapil@ccs.neu.edu
- Remove debug flags.

* Fri Mar 11 2011 kapil@ccs.neu.edu
- Updated to revision 935.

* Thu Mar 10 2011 kapil@ccs.neu.edu
- Reverting tarball to prev version.

* Thu Mar 10 2011 kapil@ccs.neu.edu
- Testing fix for restart under 32-bit OSes.

* Thu Mar 10 2011 kapil@ccs.neu.edu
- Updated tarball with compiler warnings fixed.

* Thu Mar 10 2011 kapil@ccs.neu.edu
- Added python to dependency list for running make check.

* Thu Mar 10 2011 kapil@ccs.neu.edu
- Preparing for release 1.2.1. Pulled updates from the latest dmtcp svn.
