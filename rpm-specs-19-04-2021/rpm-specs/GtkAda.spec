Name:           GtkAda
Version:        2.24.2
Release:        37%{?dist}
Summary:        GTKada 2, an Ada binding to GTK+ 2
Summary(sv):    GTKada 2, en adabindning till GTK+ 2
License:        GPLv2+
URL:            http://libre.adacore.com/libre/tools/GtkAda/
# Adacore don't understand how to publish files for downloading, but the source
# is available from here:
# http://libre.adacore.com/libre/download2
Source:         gtkada-gpl-%{version}-src.tgz
# Patch to make project files use fedora-gnat-project-common:
Patch1:         GtkAda-2.14.1-multilib_gpr.patch
# Fedora-specific patch to make gtkada-config use uname:
Patch2:         GtkAda-2.14.1-multilib_gtkada-config.patch
# Patch to fix implicit DSO linking, proposed upstream 2010-02-16:
# http://lists.adacore.com/pipermail/gtkada/2010-February/003871.html
Patch3:         GtkAda-2.18.0-lm.patch
# Patch for a more flexible build system, proposed upstream 2011-02-14:
# http://lists.adacore.com/pipermail/gtkada/2011-February/003969.html
Patch5:         GtkAda-2.24.2-configuration-5.patch
# Hack to get libgtkada_gl in the right place:
Patch7:         GtkAda-2.18.0-gl_placement.patch
# GNU-specific patch to avoid link bloat:
Patch8:         GtkAda-2.18.0-link_as_needed.patch
# Patch to avoid conflicts where two project files claim the same source files,
# fixed upstream 2012-08-07:
# http://lists.adacore.com/pipermail/gtkada/2012-August/004175.html
Patch11:        GtkAda-2.24.2-source_dir.patch
# "Only <glib.h> can be included directly." (said to be fixed upstream):
Patch12:        GtkAda-2.18.0-no_include_gmain.patch
# Patch to remove obsolete manpage cross-references, proposed upstream 2012-07-27:
# http://lists.adacore.com/pipermail/gtkada/2012-July/004160.html
Patch13:        GtkAda-2.24.2-man_xref.patch
# Fix abuse of printf-style format strings:
Patch14:        GtkAda-2.24.2-format_security.patch
# "extern inline" doesn't seem to work in GCC 5:
Patch15:        GtkAda-2.24.2-no_extern_inline.patch
# Build with GPRbuild:
Patch16:        GtkAda-2.24.2-gprbuild.patch
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  gtk2-devel >= 2.21
BuildRequires:  libgnome-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  libbonobo-devel
BuildRequires:  libbonoboui-devel
BuildRequires:  libglade2-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  GConf2-devel
BuildRequires:  fedora-gnat-project-common >= 3
BuildRequires:  make
BuildRequires:  diffutils
BuildRequires:  findutils
BuildRequires:  recode
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
%{name} is an Ada binding to the graphical toolkit GTK+. It allows you to \
develop graphical user interfaces in Ada using GTK+.

%global common_description_sv \
%{name} ??r en adabindning till den grafiska verktygsl??dan GTK+. Med %{name} \
kan du utveckla grafiska anv??ndargr??nssnitt i ada baserade p?? GTK+.

%description %{common_description_en}

%description -l sv %{common_description_sv}


%package devel
Summary:        Development files for GTKada 2
Summary(sv):    Filer f??r programmering med GTKada 2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gnome%{?_isa} = %{version}-%{release}
Requires:       %{name}-gl%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common >= 2
# gtkada.pc requires gtk+-2.0, maybe incorrectly.
Requires:       gtk2-devel%{?_isa}
Recommends:     %{name}-doc
Conflicts:      GtkAda3-devel

# GTKada 3.x is packaged as GtkAda3, and this is now a compatibility package.
#
# Unlike GTK+, GTKada has no support for installing two versions side by side,
# other than dumping the entire directory tree under some nonstandard prefix
# and requiring users to mess with various environment variables. Despite the
# API incompatibilities, both versions use the filenames "gtkada.gpr" and
# "gtkada-config", and directories named "gtkada".
#
# Hacking the build system to change various filenames from "gtkada" to
# "gtkada3" would be more trouble than it's worth, and would make Fedora
# incompatible with everything that uses GTKada. Both developers and packagers
# would have to do special things to select the right version of the library.
#
# Therefore GtkAda-devel and GtkAda3-devel are allowed to conflict.

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use GTKada 2.x. See also GtkAda3-devel.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel inneh??ller k??llkod och l??nkningsinformation som beh??vs
f??r att utveckla program som anv??nder GTKada 2.x. Se ??ven GtkAda3-devel.


%package gnome
Summary:        GTKada 2 binding to Gnome's GUI libraries
Summary(sv):    GTKada 2:s bindning till Gnomes GUI-bibliotek
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gnome %{common_description_en}

The %{name}-gnome package contains the GTKada binding to Gnome's graphical
user interface libraries.

%description gnome -l sv %{common_description_sv}

Paketet %{name}-gnome inneh??ller GTKadas bindning till Gnomes bibliotek f??r
grafiska anv??ndargr??nssnitt.


%package gl
Summary:        GTKada 2 binding to OpenGL
Summary(sv):    GTKada 2:s bindning till OpenGL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gl %{common_description_en}

The %{name}-gl package contains the GTKada binding to the OpenGL interface.

%description gl -l sv %{common_description_sv}

Paketet %{name}-gl inneh??ller GTKadas bindning till OpenGL-gr??nssnittet.


%package doc
Summary:        Documentation for GTKada 2
Summary(sv):    Dokumentation till GTKada 2
BuildArch:      noarch

%description doc %{common_description_en}

The %{name}-doc package contains the documentation for GTKada 2.x.

%description doc -l sv %{common_description_sv}

Paketet %{name}-doc inneh??ller dokumentationen till GTKada 2.x.


%prep
%setup -q -n gtkada-%{version}-src
%patch5
%patch1
%patch2
%patch3
%patch7
%patch8
%patch11
%patch12
%patch13
%patch14
%patch15
%patch16
find -name .cvsignore | xargs rm -fr

# Transcode the author's name in comments in two source files.
recode ISO-8859-1..UTF-8 testgtk/opengl/lw.[hc]


%build
# This package triggers a GCC failure when building with LTO.  Disable
# LTO for now.  fld_incomplete_type_of, at tree.c:5371
%define _lto_cflags %{nil}

%{configure} --enable-build=Debuginfo --disable-subdirs --disable-static
make src "GPRbuild_optflags=%{GPRbuild_optflags}"

# The documentation is not regenerated because that requires GPS and would
# cause a dependency loop.


%install
%{make_install} gprdir=%{_GNAT_project_dir}

# Also install the gtkada-config manpage.
mkdir -p %{buildroot}%{_mandir}/man1
install --mode=u=rw,go=r,a-s --preserve-timestamps docs/gtkada-config.1 %{buildroot}%{_mandir}/man1

# Put the info documentation in the right place.
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_docdir}/gtkada/gtkada_ug/gtkada_ug.info --target-directory=%{buildroot}%{_infodir}

# Put the examples in the documentation directory, excluding binaries.
mv --no-target-directory %{buildroot}%{_datadir}/examples/gtkada %{buildroot}%{_docdir}/gtkada/examples

# Include these documentation files.
install --mode=u=rw,go=r,a-s --preserve-timestamps AUTHORS README features known-problems %{buildroot}%{_docdir}/gtkada
mkdir --parents %{buildroot}%{_licensedir}/gtkada
install --mode=u=rw,go=r,a-s --preserve-timestamps COPYING %{buildroot}%{_licensedir}/gtkada
# There is a COPYING3 in the 2.24.2 tarball, but the source files' headers say
# version 2 or later, so COPYING3 is left out of the package for now.


%check
%{_rpmconfigdir}/check-rpaths


%files
%{_libdir}/libgtkada-*.so.*
%license %{_licensedir}/gtkada
%dir %{_docdir}/gtkada
%{_docdir}/gtkada/AUTHORS
%{_docdir}/gtkada/README


%files gnome
%{_libdir}/libgnomeada-*.so.*


%files gl
%{_libdir}/libgtkada_gl-*.so.*


%files devel
%{_bindir}/*
%{_includedir}/gtkada
%{_libdir}/gtkada
%{_GNAT_project_dir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man*/*


%files doc
# features and known-problems belong with the documentation for developers.
# The license, the list of authors and the directories need to be replicated in
# the doc subpackage as it doesn't depend on the main package.
%license %{_licensedir}/gtkada
%dir %{_docdir}/gtkada
%{_docdir}/gtkada/AUTHORS
%{_docdir}/gtkada/features
%{_docdir}/gtkada/known-problems
%{_docdir}/gtkada/gtkada_ug
%{_docdir}/gtkada/gtkada_rm
%{_docdir}/gtkada/examples
%{_infodir}/*
%{_datadir}/gps


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Bj??rn Persson <Bjorn@Rombobj??rn.se> - 2.24.2-36
- Rebuilt with GCC 11.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jeff Law <law@redhat.com> - 2.24.2-34
- Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Bj??rn Persson <Bjorn@Rombobj??rn.se> - 2.24.2-31
- Built for x86.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.24.2-28
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Bj??rn Persson <Bjorn@Rombobj??rn.se> - 2.24.2-26
- Switched to building with GPRbuild as project file support was removed from
  Gnatmake in GCC 8.
- Dropped gtkada-dialog as it's useless and didn't build correctly.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2.24.2-24
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Bj??rn Persson <Bjorn@Rombobj??rn.se> - 2.24.2-21
- Rebuilt with GCC 7 prerelease.

* Fri Aug 12 2016 Bj??rn Persson <Bjorn@Rombobj??rn.se> - 2.24.2-20
- Rebuilt to let it be built on new architectures.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Bj??rn Persson <Bjorn@Rombobj??rn.se> - 2.24.2-18
- Rebuilt with GCC 6 prerelease.

* Sat Dec 26 2015 Bj??rn Persson <Bjorn@Rombobj??rn.se> - 2.24.2-17
- GtkAda-devel now recommends GtkAda-doc.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-15
- Tagged the license file as such.

* Mon Mar 16 2015 Than Ngo <than@redhat.com> - 2.24.2-14
- bump release and rebuild so that koji-shadow can rebuild it
  against new gcc on secondary arch

* Sat Feb 07 2015 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-13
- Patched out "extern inline".

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-11
- Made it clear that this is now a compatibility package of GTKada 2.
- Collected documentation files in %%{_docdir}/gtkada.
- Verify that the generated Ada code is the same as what the developers
  upstream have reviewed and tested.
- Moved the GPS plug-in to GtkAda-doc.
- Tightened dependencies.
- Preserve timestamps on documentation files.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-9
- Rebuilt with GCC 4.9.0 prerelease.

* Thu Nov 21 2013 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-8
- Fixed abuse of g_snprintf.

* Sat Aug 03 2013 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-7
- Require libbonobo-devel instead of bonobo-activation-devel.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 24 2013 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-5
- Rebuilt with GCC 4.8.

* Tue Jul 31 2012 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-4
- Removed the manpage for Gate, as Gate itself has been removed.
- Removed obsolete references from the manpage for gtkada-config.

* Fri Jul 20 2012 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-3
- The info version of the user's guide is now installed correctly.
- Improved the descriptions a little.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 07 2012 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.24.2-1
- Upgraded to 2.24.2.
- The binding to Libglade has been removed, so there is no GtkAda-glade package
  anymore.

* Thu Feb 23 2012 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.18.0-4
- Rebuilt with fedora-gnat-project-common 3.4 and
  redhat-rpm-config-9.1.0-27.fc18.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jan 05 2012 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.18.0-2
- Patched to adapt to Glib changes.

* Sun Aug 14 2011 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.18.0-1
- Upgraded to 2.18.0.
- Moved the documentation to a directory that can remain constant across
  releases.
- Improved the package descriptions.

* Tue May 03 2011 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.1-7
- Updated for fedora-gnat-project-common 3.

* Wed Mar 09 2011 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.1-6
- Corrected dependencies.
- Put the sublibraries in the right group.
- Improved the description of the -devel package.

* Mon Feb 14 2011 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.1-5
- Made some dependencies architecture-specific.
- Made _GNAT_project_dir affect the build system.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.1-3
- Rebuilt with GCC 4.6.

* Wed Jan 19 2011 Dan Hor??k <dan[at]danny.cz> - 2.14.1-2
- updated the supported arch list

* Mon Jan 17 2011 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.1-1
- new release 2.14.1
- Patched the GtkAda build system quite a lot to disable static libraries,
  put files in the right directories and reduce the number of workarounds in
  the RPM spec.

* Sun Jul 11 2010 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.0-7
- Hacked in missing link options to get the subpackages to depend on
  the main package.
- Implemented a better way of enabling debug information, making it
  possible to build with GCC 4.5.

* Sun Jun 27 2010 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.0-5
- Patched to build against GTK+ 2.21 (#599780).

* Sun Feb 14 2010 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.0-4
- Link testgtk to libm explicitly (#564610).

* Mon Nov 30 2009 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.0-3
- Enabled debug information.

* Sun Nov 29 2009 Bj??rn Persson <bjorn@rombobj??rn.se> - 2.14.0-2
- Fixed project files and gtkada-config for multilib systems.
- Marked the doc subpackage as noarch.

* Sun Aug  9 2009 Gerard Milmeister <gemi@bluewin.ch> - 2.14.0-1
- new release 2.14.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 13 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.10.2-1
- new release 2.10.2

* Wed Jan 30 2008 Michel Salim <michel.sylvan@gmail.com> - 2.10.0-4
- Add missing BRs on gtk2-devel and pkgconfig

* Tue Jan 29 2008 Michel Salim <michel.sylvan@gmail.com> - 2.10.0-3
- Make gtkada.pc use _libdir
- Fix URL and source fields

* Sat Jan  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.10.0-2
- exclude arch ppc64

* Sat Jan  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.10.0-1
- new release 2.10.0
- documentation in separate package

* Fri Jan  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 2.8.0-7
- reenabled ppc

* Sat Oct 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8.0-5
- new version 2.8.0

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.4.0-13
- Rebuild for FE6

* Mon Mar 27 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.4.0-12
- BuildReq texinfo -> texinfo-tex

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.4.0
- Rebuild for Fedora Extras 5

* Thu Feb  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.4.0-10
- remove "--param=ssp-buffer-size=4" from gnatmake command line

* Wed Feb  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.4.0-9
- patch to handle all cases

* Thu May 12 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> 2.4.0-6
- Add excludearch ppc ppc64 (no gcc-gnat currently for those) #157550

* Tue May 10 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> 2.4.0-5
- Remove excludearch x86_64 (gcc-gnat now in FC4 for x86_64)
- BR textinfo, tetex-dvips

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 2.4.0-4
- rebuilt

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.4.0-3
- Excluded arch x86_64

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.4.0-2
- Removed touching /usr/include/gtkada/*

* Sat Jan 22 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.4.0-0.fdr.1
- New Version 2.4.0

* Sat May 29 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.1-0.fdr.2
- Replaced XFree86 reference with xorg

* Fri Nov 21 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.1-0.fdr.1
- New Version 2.2.1

* Mon Nov 10 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.0-0.fdr.5
- Work around to compiler bug

* Tue Oct 28 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.0-0.fdr.3
- Better placing of documentation files

* Mon Oct 27 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.0-0.fdr.2
- Improved specfile

* Sun Oct 26 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.0-0.fdr.1
- First Fedora release
