%ifarch aarch64
# Bootstrap the compiler for a new architecture. Set this to 0 after we've bootstrapped.
%global bootstrap 0
%else
%global bootstrap 0
%endif

Name:           fpc
Version:        3.2.0
Release:        3%{?dist}
Summary:        Free Pascal Compiler

License:        GPLv2+ and LGPLv2+ with exceptions
URL:            http://www.freepascal.org/
Source0:        ftp://ftp.freepascal.org/pub/fpc/dist/%{version}/source/fpcbuild-%{version}.tar.gz

# This is only needed when we're bootstrapping.
# But it's not in an 'if defined' block, since the file has to be included in the srpm
# Thus you should enable this line when we're bootstrapping for any target
#
# Last used for aaarch64 and ppc64le bootstrap.
# For the aarch64 bootstrap, a compiler has been used that has been cross-compiled on a x86_64 system using:
#   make all CPU_TARGET=aarch64 OS_TARGET=linux BINUTILSPREFIX=aarch64-linux-gnu-
# For the ppc64 boostrap, a compiler has been used that has been cross-compiled on a x86_64 system using:
#   make all CPU_TARGET=powerpc64 OS_TARGET=linux BINUTILSPREFIX=powerpc64le-linux-gnu- CROSSOPT="-Cb- -Caelfv2"
#
# in the main directory of fpc-r44016. The compilers were then copied using:
#   cp compiler/ppca64    ~/fpc-3.2.0-bin/ppca64-3.2.0-bootstrap
#   cp compiler/ppcppc64  ~/fpc-3.2.0-bin/ppcppc64-3.2.0-bootstrap
# The zip file was then created using:
#   zip -9 fpc-3.2.0-bin.zip -r fpc-3.2.0-bin/
#
# Source100:	https://suve.fedorapeople.org/fpc-3.2.0-bin--patch0.zip

# Configuration templates:
Source10:        fpc.cft
Source11:        fppkg.cfg
Source12:        default.cft

# On Fedora we do not want stabs debug-information. (even on 32 bit platforms)
# https://bugzilla.redhat.com/show_bug.cgi?id=1475223 
Patch0:         fpc-3.2.0--dwarf-debug.patch

# Allow for reproducible builds
# https://bugzilla.redhat.com/show_bug.cgi?id=1778875
Patch1:         fpc-3.2.0--honor_SOURCE_DATE_EPOCH_in_date.patch

# Upstream assumes /usr/lib/ for aarch64, but Fedora uses /usr/lib64/
Patch2:         fpc-3.2.0--fix-lib-paths-on-aarch64.patch


Requires:       gpm, ncurses, binutils
%if ! 0%{?bootstrap}
BuildRequires:  fpc
%endif
BuildRequires:  glibc-devel
BuildRequires:  tex(tex), tex(latex), tetex-fonts
BuildRequires: make

ExclusiveArch:  %{arm} aarch64 %{ix86} x86_64 ppc64le

%description
Free Pascal is a free 32/64bit Pascal Compiler. It comes with a run-time
library and is fully compatible with Turbo Pascal 7.0 and nearly Delphi
compatible. Some extensions are added to the language, like function
overloading and generics. Shared libraries can be linked. This package
contains the command-line compiler and utilities. Provided units are the
runtime library (RTL), free component library (FCL) and packages.

%package doc
Summary: Free Pascal Compiler - documentation and examples

%description doc
The fpc-doc package contains the documentation (in pdf format) and examples
of Free Pascal.

%package src
Summary:   Free Pascal Compiler - sources
BuildArch: noarch

%description src
The fpc-src package contains the sources of Free Pascal, for documentation or
automatical-code generation purposes.

%global smart _smart
%global fpcopt -k"--build-id"
%global fpcdebugopt -gl
%ifarch %{arm}
  %global fpcopt -dFPC_ARMHF -k"--build-id"
  %global ppcname ppcarm
  %global fpcarchname arm
%else
  %ifarch aarch64
    %global ppcname ppca64
    %global fpcarchname aarch64
  %else
    %ifarch ppc64
      %global ppcname ppcppc64
      %global fpcarchname powerpc64
    %else
      %ifarch ppc64le
        %global fpcopt -Cb- -Caelfv2 -k"--build-id"
        %global ppcname ppcppc64
        %global fpcarchname powerpc64
      %else
        %ifarch x86_64
          %global ppcname ppcx64
          %global fpcarchname x86_64
        %else
          %global ppcname ppc386
          %global fpcarchname i386
        %endif
      %endif
    %endif
  %endif
%endif


%prep
%setup -n fpcbuild-%{version} -q

%if 0%{?bootstrap}
unzip %{SOURCE100}
%endif

pushd fpcsrc
%patch0
%patch1
%patch2


%build
# The source-files:
mkdir -p fpc_src
cp -a fpcsrc/rtl fpc_src
cp -a fpcsrc/packages fpc_src
rm -rf fpc_src/packages/extra/amunits
rm -rf fpc_src/packages/extra/winunits

%if 0%{?bootstrap}
STARTPP=$(pwd)/fpc-%{version}-bin/%{ppcname}-%{version}-bootstrap
%else
STARTPP=%{ppcname}
%endif

pushd fpcsrc
NEWPP=$(pwd)/compiler/%{ppcname}
DATA2INC=$(pwd)/utils/data2inc
# FIXME: -j1 as there is a race on armv7hl - seen on "missing" `prt0.o' and 'dllprt0.o'.
make -j1 compiler_cycle FPC=${STARTPP} OPT='%{fpcopt} %{fpcdebugopt}'
make %{?_smp_mflags} rtl_clean rtl%{smart} FPC=${NEWPP} OPT='%{fpcopt}'
make %{?_smp_mflags} packages%{smart} FPC=${NEWPP} OPT='%{fpcopt}'
make %{?_smp_mflags} utils_all FPC=${NEWPP} DATA2INC=${DATA2INC} OPT='%{fpcopt} %{fpcdebugopt}'
popd

# FIXME: -j1 as there is a race - seen on "missing" `rtl.xct'.
make -j1 -C fpcdocs pdf FPC=${NEWPP}

%install
pushd fpcsrc
NEWPP=$(pwd)/compiler/%{ppcname}
NEWFPCMAKE=$(pwd)/utils/fpcm/bin/%{fpcarchname}-linux/fpcmake
INSTALLOPTS="-j1 FPC=${NEWPP} FPCMAKE=${NEWFPCMAKE} \
                INSTALL_PREFIX=%{buildroot}%{_prefix} \
                INSTALL_LIBDIR=%{buildroot}%{_libdir} \
                INSTALL_BASEDIR=%{buildroot}%{_libdir}/%{name}/%{version} \
                CODPATH=%{buildroot}%{_libdir}/%{name}/lexyacc \
                INSTALL_DOCDIR=%{buildroot}%{_defaultdocdir}/%{name} \
                INSTALL_BINDIR=%{buildroot}%{_bindir}
                INSTALL_EXAMPLEDIR=%{buildroot}%{_defaultdocdir}/%{name}/examples"
make compiler_distinstall ${INSTALLOPTS}
make rtl_distinstall ${INSTALLOPTS}
make packages_distinstall ${INSTALLOPTS}
make utils_distinstall ${INSTALLOPTS}
popd

pushd install
make -C doc ${INSTALLOPTS}
make -C man ${INSTALLOPTS} INSTALL_MANDIR=%{buildroot}%{_mandir}
popd

make -C fpcdocs pdfinstall ${INSTALLOPTS}

# create link
ln -sf ../%{_lib}/%{name}/%{version}/%{ppcname} %{buildroot}%{_bindir}/%{ppcname}

# Remove the version-number from the documentation-directory
mv %{buildroot}%{_defaultdocdir}/%{name}-%{version}/* %{buildroot}%{_defaultdocdir}/%{name}
rmdir %{buildroot}%{_defaultdocdir}/%{name}-%{version}

# Create a version independent compiler-configuration file with build-id
# enabled by default
# For this purpose some non-default templates are used. So the samplecfg
# script could not be used and fpcmkcfg is called directly.
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE10} -d "basepath=%{_exec_prefix}" -o %{buildroot}%{_sysconfdir}/fpc.cfg
# Create the IDE configuration files
%{buildroot}%{_bindir}/fpcmkcfg -p -1 -d "basepath=%{_libdir}/%{name}/\$fpcversion" -o %{buildroot}%{_libdir}/%{name}/%{version}/ide/text/fp.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -2 -o %{buildroot}%{_libdir}/%{name}/%{version}/ide/text/fp.ini
# Create the fppkg configuration files
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE11} -d CompilerConfigDir=%{_sysconfdir}/fppkg -d arch=%{_arch} -o %{buildroot}%{_sysconfdir}/fppkg.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE12} -d fpcbin=%{_bindir}/fpc -d GlobalPrefix=%{_exec_prefix} -d lib=%{_lib} -o %{buildroot}%{_sysconfdir}/fppkg/default_%{_arch}

# Include the COPYING-information for the compiler/rtl/fcl in the documentation
cp -a fpcsrc/compiler/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING
cp -a fpcsrc/rtl/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING.rtl
cp -a fpcsrc/rtl/COPYING.FPC %{buildroot}%{_defaultdocdir}/%{name}/COPYING.FPC

# The source-files:
mkdir -p %{buildroot}%{_datadir}/fpcsrc
cp -a fpc_src/* %{buildroot}%{_datadir}/fpcsrc/

# Workaround:
# newer rpm versions do not allow garbage
# delete lexyacc (The hardcoded library path is necessary because 'make
# install' places this file hardcoded at usr/lib)
rm -rf %{buildroot}/usr/lib/%{name}/lexyacc


%files
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/libpas2jslib.so*
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/fppkg.cfg
%config(noreplace) %{_sysconfdir}/fppkg/default_%{_arch}
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/NEWS
%doc %{_defaultdocdir}/%{name}/README
%doc %{_defaultdocdir}/%{name}/faq*
%license %{_defaultdocdir}/%{name}/COPYING*
%{_mandir}/*/*

%files doc
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/*.pdf
%doc %{_defaultdocdir}/%{name}/*/*

%files src
%{_datadir}/fpcsrc


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-1
- Update to v3.2.0 (official release - no longer using SVN snapshots)
- Drop Patch3 (missing consts - merged upstream)

* Wed Jun 03 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200530svn45533.1
- Update to latest upstream SVN revision

* Mon May 04 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200503svn45235.1
- Update to latest upstream SVN revision

* Sun Apr 12 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200410svn44680.1
- Update to latest upstream SVN revision

* Sat Mar 28 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200327svn44375.1
- Update to latest upstream SVN revision

* Mon Mar 16 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200314svn44301.1
- Update to latest upstream SVN revision

* Mon Feb 24 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200222svn44232.1
- Update to latest upstream SVN revision

* Wed Feb 12 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200212svn44160.1
- Update to latest upstream SVN revision

* Sat Feb 08 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200203svn44109.1
- Update to latest upstream SVN revision

* Sun Feb 02 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200202svn44092.5
- Update to latest upstream SVN revision

* Sat Feb 01 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200130svn44069.4
- Unmark the aarch64 build as requiring bootstrap
- Update to latest upstream SVN revision

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-0.20200122svn44016.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200122svn44016.3
- Bootstrap the compiler for aarch64

* Mon Jan 27 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200122svn44016.2
- Bootstrap the compiler for ppc64le

* Sun Jan 26 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200122svn44016.1
- Update to latest upstream SVN revision
- Drop r1448 and r38400 patches (backports from upstream)

* Sat Dec 21 2019 Artur Iwicki <fedora@svgames.pl> - 3.0.4-8
- Allow for reproducible builds by honoring the SOURCE_DATE_EPOCH variable
  (patch imported from Debian)
- Mark the fpc-src package as noarch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Artur Iwicki <fedora@svgames.pl> - 3.0.4-5
- Add BuildRequires: for glibc-devel

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Richard Shaw <hobbes1069@gmail.com> - 3.0.4-2
- Add patch to fix assembly alignment code, fixes #1526848.

* Thu Mar 01 2018 Joost van der Sluis <joost@cnoc.nl> - 3.0.4-1
- Generate Dwarf debug by default on 32-bit targets (rhbz#1475223)
- Use the %%license macro instead of %%doc for licence files

* Fri Feb 09 2018 Joost van der Sluis <joost@cnoc.nl> - 3.0.4-1
- Upgrade to upstream release 3.0.4.
- Generate Dwarf- instead of Stabs-debuginfo on i686 and ARMHF
- Force armhf on arm-architectures

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Joost van der Sluis <joost@cnoc.nl> - 3.0.2-1
- Upgrade to upstream release 3.0.2.
- Attempt to fix race-problem during compiler-compilation on ARM

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 4 2017 Joost van der Sluis <joost@cnoc.nl> - 3.0.0-5
- Drop powerpc64-arm binary added for bootstrapping on powerpc64,
  completing the bootstrap procedure

* Mon Jan 30 2017 Joost van der Sluis <joost@cnoc.nl> - 3.0.0-4
- Bootstrap ppc64 using cross-compiled compiler binary

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Joost van der Sluis <joost@cnoc.nl> - 3.0.0-2
- Drop fpc-arm binary added for bootstrapping on ARM, completing the
  bootstrap procedure

* Sat Jan 9 2016 Joost van der Sluis <joost@cnoc.nl> - 3.0.0-1
- Upgrade to upstream release 3.0.0.
- Bootstrap ARM using cross-compiled armhl binaries, because the
  (patched) 2.6.4-ARM compiler in the repository is not able to compile the
  3.0.0 release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 7 2015 Joost van der Sluis <joost@cnoc.nl> - 2.6.4-1
- Upgrade to upstream release 2.6.4.

* Tue Jan 20 2015 Dan Horák <dan[at]danny.cz> - 2.6.2-7
- switch to ExclusiveArch

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Hans de Goede <hdegoede@redhat.com> - 2.6.2-4
- Drop fpc binaries added to the src.rpm for bootstrapping on ARM, completing
  the boostrap procedure (rhbz#992285)

* Thu Aug 08 2013 Hans de Goede <hdegoede@redhat.com> - 2.6.2-3
- Bootstrap for arm using Debian fpc-2.6.2 armhf binaries (rhbz#992285)
- Use an unversioned docdir (rhbz#993758)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Joost van der Sluis <joost@cnoc.nl> - 2.6.2-1
- Upgrade to upstream release 2.6.2.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Bruno Wolff III <bruno@wolff.to> - 2.6.2-0.1.rc1
- Use standard versioning, so non-rc versions will be higher
- Fix issue with some things using 'rc1' appended to version name and others not

* Sat Nov 3 2012 Joost van der Sluis <joost@cnoc.nl> - 2.6.2rc1-1
- Upgrade to upstream release 2.6.2rc1.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Karsten Hopp <karsten@redhat.com> 2.6.0-2
- define ppcname on ppc64

* Fri Jan 27 2012 Joost van der Sluis <joost@cnoc.nl> - 2.6.0-1
- Upgrade to upstream release 2.6.0.
- Do not use samplecfg for generating the configuration files anymore, but
  call fpcmkcfg directly.
- Changed the name of the project from Freepascal to Free Pascal

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 5 2011 Joost van der Sluis <joost@cnoc.nl> - 2.4.2-1
- Upgrade to upstream release 2.4.2.

* Sat Oct 23 2010 Joost van der Sluis <joost@cnoc.nl> - 2.4.2-0.1.rc1
- Upgrade to upstream release 2.4.2rc1.

* Wed May  5 2010 Joost van der Sluis <joost@cnoc.nl> - 2.4.0-1.fc14
- Drop fpc-2.2.4-stackexecute.patch since bug was fixed in 2.4.0

* Tue May  4 2010 Jan Kratochvil <jan.kratochvil@redhat.com> - 2.4.0-0.fc14
- Upgrade to upstream release 2.4.0.
  - Drop fpc-2.2.4-r12475.patch as present in 2.4.0.
- Base the .spec build on upstream released archive (fpcbuild-2.4.0.tar.gz).
- Remove the obsolete .spec BuildRoot tag.
- Remove BuildRequires for binutils and glibc-devel as guaranteed as always
  provided in Fedora Packaging Guidlines.
- Remove Requires glibc as guaranteed on a Fedora system.
- Add %%{?_smp_mflags} and -j1 appropriately, applied one -j1 workaround.
- Change {compiler,rtl}/COPYING to COPYING.txt.

* Tue Oct 6 2009 Joost van der Sluis <joost@cnoc.nl> 2.2.4-4
- fixed procvar parameter passing on ppc/sysv (by value instead of by
  reference -- except for method procvars, for tmethod record compatibility) 

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Dan Horak <dan[at]danny.cz> 2.2.4-2
- Exclude s390/s390x architectures

* Sun Apr 19 2009 Joost van der Sluis <joost@cnoc.nl> 2.2.4-1
- Updated to version 2.2.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.2-3
- Do not distribute the RTL and packages with debug-info included
- Fix the location of the fpc-binary in the samplecfg script

* Sun Oct 19 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.2-2
- Pass -z noexecstack to the linker from within the configuration file fpc.cfg (fpc-bug #11563)
- Added patch to fix fpc-bug #11837 for usage with newer gtk2-versions

* Wed Aug 13 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.2-1
- Updated to version 2.2.2
- Disabled debuginfo for ppc64 again
- Detect 32 or 64 bit compilation in the configuration file fpc.cfg

* Sun Jun 22 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.2rc1-1
- Updated to version 2.2.2rc1
- Enabled debuginfo for ppc64 again
- Do not strip the debugdata on x86_64 anymore
- Packages_base, packages_fcl and packages_extra are merged into packages
- Don't install packages_fv separately anymore
- Fix for incorrect path in official fpc 2.2.2rc1-sourcefile
- Updated licence-tag from "GPL and modified LGPL" to fedora-tag "GPLv2+ and LGPLv2+ with exceptions"
- Removed UsePrebuildcompiler define for ppc64

* Wed Apr 16 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.0-12
- Fix for DWARF-debug generation - fixes some more build problems on x86_64 and F9, bugzilla 337051

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.0-11
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-10
- Strip the debuginfo from grab_vcsa and ppudump, since debugedit chokes on it
- Only strip debugdata on x86_64

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-9
- Strip the debuginfo from mkxmlrpc, since debugedit chokes on it

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-8
- Strip the debuginfo from h2pas, since debugedit chokes on it

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-7
- Include the startcompiler on all targets, for the srpm-building

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-6
- Disabled debuginfo for ppc64 only
- Enabled smart-linking on ppc64
- Added a patch for building documentation without fpc already installed

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-5
- Disabled debuginfo

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-4
- Enabled BuildId, added it to fpc.cfg

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-3
- Disabled smart-linking on ppc64

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-2
- Buildrequirement fpc is not needed when using a pre-built compiler binary

* Sun Oct 14 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-1
- Updated to version 2.2.0
- Updated description
- Enabled smart-linking for ppc
- Do not include the built binary-files in fpc-src
- Added support for ppc64
- Added support to configuration file for dual 32/64 bit installations
- Fixed and enabled debug-package 

* Sat Sep 16 2006 Joost van der Sluis <joost@cnoc.nl> 2.0.4-2
- Fixed documentation building on powerpc

* Fri Sep 15 2006 Joost van der Sluis <joost@cnoc.nl> 2.0.4-1
- Updated to version 2.0.4

* Wed Mar 1 2006 Joost van der Sluis <joost@cnoc.nl> 2.0.2-4
- Rebuild for Fedora Extras 5

* Tue Dec 20 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.2-3
- Disabled smart-linking for ppc

* Tue Dec 20 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.2-2
- Updated fpc-2.0.2-G5.patch

* Tue Dec 20 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.2-1
- Updated to version 2.0.2

* Wed Aug 17 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-4
- Added %%{?dist} to release.

* Wed Aug 17 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-3
- replaced the ppcpcc-2.1.1 startcompilercompiler for the
  ppcppc-2.0.0 startcompiler 

* Wed Aug 17 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-2
- Added a patch for compilation on POWER5, and provided
  the new ppcppc binary/startcompiler

* Fri Aug 5 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-1
- Removed gpm-devel requirement
- Fixed a type in the -src description

* Thu Jul 28 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-1
- Added some requirements
- Added COPYING-info to %%doc

* Tue Jun 28 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.6
- Only rtl, fcl and packages are added to src-subpackage
- Silenced post-script
- disabled the debuginfo-package

* Sun Jun 5 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.5
- Added doc-subpackage
- Added src-subpackage

* Fri Jun 3 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.4
- New fix for lib64 on x86_64
- small patches from Jens Petersen <petersen@redhat.com>

* Thu May 26 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.3
- replaced 'lib' and 'lib64' by %%{_lib}

* Tue May 24 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.2
- Fixed for lib64 on x86_64
- Changed summary, description and license
- Removed examples from installation
- Make clean removed from clean-section
- Clean-up
- replaced $RPM_BUILD_ROOT by %%{buildroot}

* Mon May 23 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.1
- Initial build.
