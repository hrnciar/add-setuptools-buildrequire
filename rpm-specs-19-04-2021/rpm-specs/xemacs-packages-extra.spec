%global hgver   cbe800ed9a7f
%global pkgdir  %{_datadir}/xemacs
%global xemver  21.5.34
%global basever 20190327

# This package install python files into nonstandard places
%global _python_bytecompile_extra 0

Name:           xemacs-packages-extra
Version:        20200216
Release:        5%{?dist}
Summary:        Collection of XEmacs lisp packages

License:        GPLv2+ and GPLv3+
URL:            http://www.xemacs.org/Documentation/packageGuide.html
# Tarball created with Source99
Source0:        %{name}-%{version}.tar.xz
Source10:       Emacs.ad.ja_JP.eucJP
Source11:       Emacs.ad.ko_KR.eucKR
Source12:       Emacs.ad.zh_CN.GB2312
Source13:       Emacs.ad.zh_TW.Big5
Source14:       Emacs.ad.ja_JP.UTF-8
Source15:       Emacs.ad.ko_KR.UTF-8
Source16:       Emacs.ad.zh_CN.UTF-8
Source17:       Emacs.ad.zh_TW.UTF-8
Source99:       %{name}-checkout.sh

# use TrAX by default in xslt-process
Patch0:         %{name}-20060510-trax.patch
# catch harmless errors in mouse-avoidance-too-close-p (avoid.el)
Patch1:         %{name}-20060510-avoid-catch-error-65346.patch
# make egg-wnn use unix domain sockets by default
Patch2:         %{name}-20060510-egg-wnn-host-unix-79826.patch
# use ptex rather than jtex by default for Japanese
Patch3:         %{name}-20150413-auctex-texjp-platex.patch
# adapt to python 3
Patch4:         %{name}-20190315-python3.patch
# fix an invalid eval-when list in prog-modes
Patch5:         %{name}-20190315-eval-when.patch
# add some missing dependencies that fail the build otherwise
Patch6:         %{name}-20190315-deps.patch
# switch from berkeley-db to gdbm now that XEmacs itself has
Patch7:         %{name}-20200216-gdbm.patch

BuildArch:      noarch
BuildRequires:  bdftopcf
BuildRequires:  ImageMagick
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  xemacs
BuildRequires:  texinfo
# For building auctex docs
BuildRequires:  tex(latex)
BuildRequires:  info
BuildRequires:  python3-devel
BuildRequires:  java-devel
Requires:       xemacs-packages-base >= %{basever}
Requires:       xemacs(bin) >= %{xemver}
# Fake release here for historical reasons
Provides:       apel-xemacs = 10.7-1

# https://fedoraproject.org/wiki/Changes/Deprecate_xemacs
# https://bugzilla.redhat.com/show_bug.cgi?id=1916926
Provides:       deprecated()

%description
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

The XEmacs packages collection contains a large collection of useful
lisp packages for XEmacs including mail readers, programming modes and
utilities, and packages related to using XEmacs in multi-lingual
environments.

%package        el
Summary:        Emacs lisp source files for XEmacs packages collection
Requires:       %{name} = %{version}-%{release}
Requires:       xemacs-packages-base-el >= %{basever}

# https://fedoraproject.org/wiki/Changes/Deprecate_xemacs
# https://bugzilla.redhat.com/show_bug.cgi?id=1916926
Provides:       deprecated()

%description    el
This package is not needed to run XEmacs; it contains the lisp source
files for the XEmacs packages collection, mainly of interest when
developing or debugging the packages.

%package        info
Summary:        XEmacs packages documentation in GNU texinfo format
Requires:       %{name} = %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/Deprecate_xemacs
# https://bugzilla.redhat.com/show_bug.cgi?id=1916926
Provides:       deprecated()

%description    info
This package contains optional documentation for the XEmacs packages
collection in GNU texinfo format


%prep
%autosetup -p1

chmod -c -x xemacs-packages/auctex/style/bidi.el

cat << EOF > make.sh
#!/bin/sh
make \\
    XEMACS_BINARY=%{_bindir}/xemacs \\
    XEMACS_INSTALLED_PACKAGES_ROOT=\$RPM_BUILD_ROOT%{pkgdir} \\
    XEMACS_21_5=t \\
    "\$@"
EOF
chmod +x make.sh

sed -i -e 's|/usr/local/bin/perl5\?|%{_bindir}/perl|g' \
  xemacs-packages/bbdb/utils/*.pl xemacs-packages/hyperbole/file-newer

# Fix encodings
for fil in mule-packages/mule-base/texi/canna-jp.texi \
           xemacs-packages/bbdb/texinfo/bbdb.texinfo \
           xemacs-packages/ecb/ecb.texi \
           xemacs-packages/edit-utils/tempo.texi \
	   xemacs-packages/general-docs/texi/xemacs/fontconfig.texi \
	   xemacs-packages/gnus/texi/emacs-mime.texi \
	   xemacs-packages/gnus/texi/gnus.texi \
	   xemacs-packages/hm--html-menus/hm--html-mode.texi \
	   xemacs-packages/hm--html-menus/umlaute.texi \
	   xemacs-packages/mmm-mode/mmm.texinfo \
           xemacs-packages/prog-modes/prog-modes.texi \
	   xemacs-packages/psgml/psgml.texi; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -f $fil $fil.utf8
  mv -f $fil.utf8 $fil.texi
done

# Get reproducible builds by setting the compiling username
mkdir ~/.xemacs
echo >> ~/.xemacs/custom.el << EOF
(custom-set-variables
 '(user-mail-address "mockbuild@fedoraproject.org"))
EOF

# Do not use env
for fil in xemacs-packages/python-modes/pydoc_lisp.py; do
  sed -ri.orig 's,bin/env (.*),bin/\13,' $fil
  touch -r $fil.orig $fil
  rm -f $fil.orig
done


%build
cd xemacs-packages/xslt-process/java
javac xslt/TrAX.java && jar cvf xslt.jar xslt/*.class && rm xslt/*.class
cd -
./make.sh autoloads
./make.sh


%install
mkdir -p $RPM_BUILD_ROOT%{pkgdir}
./make.sh install

# The X-Symbol font files are only needed on Windows
rm -fr $RPM_BUILD_ROOT%{pkgdir}/xemacs-packages/etc/x-symbol/fonts
rm -fr $RPM_BUILD_ROOT%{pkgdir}/xemacs-packages/etc/x-symbol/origfonts
rm -fr $RPM_BUILD_ROOT%{pkgdir}/xemacs-packages/etc/x-symbol/pcf

cd $RPM_BUILD_ROOT%{pkgdir}/mule-packages/etc/app-defaults
mkdir {de_DE,fr_FR,ro_RO,ja_JP,ko_KR,sv_SE,zh_CN,zh_TW}.UTF-8 \
  ja_JP.eucJP ko_KR.eucKR zh_CN.GB2312 zh_TW.Big5
iconv -f ISO-8859-1  -t UTF-8 de/Emacs > de_DE.UTF-8/Emacs
iconv -f ISO-8859-1  -t UTF-8 fr/Emacs > fr_FR.UTF-8/Emacs
iconv -f ISO-8859-16 -t UTF-8 ro/Emacs > ro_RO.UTF-8/Emacs
iconv -f ISO-8859-1  -t UTF-8 sv/Emacs > sv_SE.UTF-8/Emacs
mv de de_DE
mv fr fr_FR
mv ro ro_RO
mv sv sv_SE
install -pm 644 %{SOURCE10} ja_JP.eucJP/Emacs
install -pm 644 %{SOURCE11} ko_KR.eucKR/Emacs
install -pm 644 %{SOURCE12} zh_CN.GB2312/Emacs
install -pm 644 %{SOURCE13} zh_TW.Big5/Emacs
install -pm 644 %{SOURCE14} ja_JP.UTF-8/Emacs
install -pm 644 %{SOURCE15} ko_KR.UTF-8/Emacs
install -pm 644 %{SOURCE16} zh_CN.UTF-8/Emacs
install -pm 644 %{SOURCE17} zh_TW.UTF-8/Emacs
# these don't seem to appear in manifest
#ln -s ja_JP.eucJP ja_JP
#ln -s ko_KR.eucKR ko_KR
#ln -s zh_CN.GB2312 zh_CN
#ln -s zh_TW.Big5 zh_TW
cd -

remove_package() {
    pdir=$RPM_BUILD_ROOT%{pkgdir}/$2
    %{_bindir}/xemacs -batch -vanilla -l package-admin -eval \
        "(package-admin-delete-binary-package '$1 \"$pdir\")"
    rm -rf $pdir/{etc,lisp,man}/$1
}

# efs, xemacs-base: included in xemacs-packages-base
# jde: not buildable from sources, all deps not met, see 2006-03-03 changelog
for pkg in efs jde xemacs-base ; do
    remove_package $pkg xemacs-packages
done

# mule-base: included in xemacs-packages-base
# skk: provided by xemacs-ddskk
for pkg in mule-base skk ; do
    remove_package $pkg mule-packages
done

# mule-ucs: not needed (and unusable) with >= 21.5
remove_package mule-ucs mule-packages

# info docs: pre-generate "dir"s and compress files
for file in $RPM_BUILD_ROOT%{pkgdir}/*-packages/info/*.info ; do
  /sbin/install-info $file `dirname $file`/dir
done
find $RPM_BUILD_ROOT%{pkgdir} -type f -name '*.info*' | xargs gzip -9

# separate files
rm -f *.files
touch base-files el-files info-files

find $RPM_BUILD_ROOT%{pkgdir}/* \
  \( -type f -name '*.el.orig' -delete \) -o \
  \( -type f -not -name '*.el' -fprint base-non-el.files \) -o \
  \( -type d -not -name info -fprintf dir.files "%%%%dir %%p\n" \) -o \
  \( -name '*.el' \( -exec test -e '{}'c \; -fprint el-bytecomped.files -o \
     -fprint base-el-not-bytecomped.files \) \)

sed -i -e "s|$RPM_BUILD_ROOT||" *.files
cat base-*.files dir.files | grep -v /info/ >> base-files
cat el-*.files                              >> el-files
cat base-non-el.files | grep /info/         >> info-files

sed -i -e 's/^\(.*\(\.ja\|-ja\.texi\)\)$/%lang(ja) \1/' base-files
sed -i -e 's/^\(.*[_-]ja\.info.*\)$/%lang(ja) \1/' info-files

# Byte compile the python files
%py_byte_compile %{python3} $RPM_BUILD_ROOT%{pkgdir}/xemacs-packages/etc/python-modes


%files -f base-files
%{pkgdir}/xemacs-packages/etc/python-modes/__pycache__

%files el -f el-files

%files info -f info-files
%dir %{pkgdir}/*-packages/info/


%changelog
* Mon Mar  8 2021 Jerry James <loganjerry@gmail.com> - 20200216-5
- Add BR on bdftopcf

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200216-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Jerry James <loganjerry@gmail.com> - 20200216-3
- Mark as deprecated (bz 1916926)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200216-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 20200216-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Feb 20 2020 Jerry James <loganjerry@gmail.com> - 20200216-1
- Update to the latest cc-mode and time packages
- Add gdbm patch due to XEmacs switch from libdb to gdbm

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Jerry James <loganjerry@gmail.com> - 20191207-1
- Update to the latest cc-mode and time packages

* Tue Oct  1 2019 Jerry James <loganjerry@gmail.com> - 20190315-3
- New texinfo version assumes UTF-8 input, so convert ISO8859-1 texinfo files

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190315-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Jerry James <loganjerry@gmail.com> - 20190315-1
- Update all packages
- Include mew again, since xemacs-mew no longer exists
- Add -python3 patch and build with python3 instead of python2
- Add -eval-when and -deps patches to fix FTBFS

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20171219-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171219-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171219-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Jerry James <loganjerry@gmail.com> - 20171219-1
- Update cc-mode, edit-utils, prog-modes, and time

* Sat Aug  5 2017 Jerry James <loganjerry@gmail.com> - 20170330-1
- Update all packages, especially CC-Mode to fix FTBFS

* Sat Aug  5 2017 Jerry James <loganjerry@gmail.com> - 20170114-4
- Fix xemacs(bin) dependency
- Eliminate dependencies on /usr/bin/env

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170114-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170114-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Jerry James <loganjerry@gmail.com> - 20170114-1
- Update to mercurial snapshot to fix EDE security issue

* Tue Oct 18 2016 Jerry James <loganjerry@gmail.com> - 20160621-1
- Update to latest packages release

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 20160208-1
- Update to latest packages release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150919-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct  7 2015 Jerry James <loganjerry@gmail.com> - 20150919-1
- Update to latest packages releases

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150413-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Jerry James <loganjerry@gmail.com> - 20150413-1
- Update to latest package releases
- Set the build username for reproducible builds

* Thu Aug  7 2014 Jerry James <loganjerry@gmail.com> - 20140715-1
- Update to new package release (bz 1127518)

* Mon Jul  7 2014 Jerry James <loganjerry@gmail.com> - 20140705-1
- Update to new package release
- Drop upstreamed -aspellenc, -auctex-cvs-keywords, -browsers, -risky, and
  -texi patches
- Update checkout script for mercurial

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130408-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130408-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 20130408-2
- Perl 5.18 rebuild

* Tue Apr  9 2013 Jerry James <loganjerry@gmail.com> - 20130408-1
- Update to new package release
- Add -texi patch to fix issues with texinfo 5

* Mon Feb 11 2013 Jerry James <loganjerry@gmail.com> - 20130208-3
- Fix version dependency in the -el subpackage

* Sun Feb 10 2013 Jerry James <loganjerry@gmail.com> - 20130208-2
- Fix version dependency on xemacs-packages-base

* Sat Feb  9 2013 Jerry James <loganjerry@gmail.com> - 20130208-1
- Update to new package release
- Allow the xemacs-packages-base version to lag behind

* Tue Jan  8 2013 Jerry James <loganjerry@gmail.com> - 20121228-1
- Update to new package release
- Drop BuildRoot
- Drop xz BR; it is on the exceptions list
- Add -risky patch to fix build

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 20110502-2
- Mass rebuild for Fedora 17
- Minor spec file cleanups

* Tue May  3 2011 Jerry James <loganjerry@gmail.com> - 20110502-1
- Update to new package release.
- Erase one more instance of a trademarked work in the checkout script.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100727-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 12 2010 Jerry James <loganjerry@gmail.com> - 20100727-1
- Update to new package release.
- New upstream CVS location in checkout script.
- Drop upstreamed patches.
- Renumber remaining patches.

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 20090217-8
- recompiling .py files against Python 2.7 (rhbz#623419)

* Fri Dec  4 2009 Jerry James <loganjerry@gmail.com> - 20090217-7
- Fix one more ediff problem found during testing (bz 537531).

* Tue Dec  1 2009 Jerry James <loganjerry@gmail.com> - 20090217-6
- The last ediff fix included more Emacs-specific code (bz 537531).
- Don't package x-symbol fonts, which are only needed on Windows anyway.

* Tue Nov  3 2009 Jerry James <loganjerry@gmail.com> - 20090217-5
- Fix Emacs-only coding system in ediff (bz 532620).

* Thu Oct 29 2009 Jerry James <loganjerry@gmail.com> - 20090217-4
- Fix LaTeX BRs.
- Update apel-xemacs Provides.

* Thu Sep  3 2009 Jerry James <loganjerry@gmail.com> - 20090217-3
- Update APEL to a newer version (bz 503185).
- Teach dired about the /bin/ls dot signifying an SELinux context (bz 504422).
- Fix a known timer bug.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar  7 2009 Ville Skytt?? <ville.skytta at iki.fi> - 20090217-1
- Update to 2009-02-17, several patches applied/superseded upstream.
- Apply upstream patch to fix errors and obsolete code in VC menu.
- Drop xemacs-sumo* provides and obsoletes and apel-xemacs obsoletes.
- Drop support for building with xemacs < 21.5.28-11.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070427-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 20070427-4
- Rebuild for Python 2.6

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20070427-3
- fix license tag

* Wed Jun 18 2008 Ville Skytt?? <ville.skytta at iki.fi> - 20070427-2
- Apply upstream security fix for CVE-2008-2142 (#446069).

* Fri May 18 2007 Ville Skytt?? <ville.skytta at iki.fi> - 20070427-1
- 2007-04-27 + upstream post-sumo rpm-spec-mode and locale (#239394) fixes.
- Improve Japanese splash screen (#239394, Jens Petersen).
- Require an actual XEmacs editor, not just -common.

* Mon Apr  2 2007 Ville Skytt?? <ville.skytta at iki.fi> - 20061221-1
- 2006-12-21 + backport of upstream browse-url/xdg-open changes.
- Drop no longer needed ruby-mode-xemacs Provides/Obsoletes.

* Sun Sep 10 2006 Ville Skytt?? <ville.skytta at iki.fi> - 20060510-4
- BuildRequire tetex.

* Sun Sep 10 2006 Ville Skytt?? <ville.skytta at iki.fi> - 20060510-3
- Rename to xemacs-packages-extra; split xemacs-base, efs and mule-base to
  separate xemacs-packages-base package.
- Don't ship mule-ucs for XEmacs >= 21.5, nor Sun for any version.
- Really build from sources.

* Sat May 13 2006 Ville Skytt?? <ville.skytta at iki.fi> - 20060510-2
- Try to work around build system quirks in finding the XEmacs version.

* Wed May 10 2006 Ville Skytt?? <ville.skytta at iki.fi> - 20060510-1
- 2006-05-10; pydoc and latin-unity patches applied upstream.
- Adapt ispell.el to aspell >= 0.60's encoding behaviour (#190151).
- Drop no longer relevant obsoletes and conflicts.
- Add version to xemacs-common dependency.
- Fix build with XEmacs 21.5.x.
- Don't ship mule-ucs for 21.5.x.
- Require main package in -info.

* Fri Mar  3 2006 Ville Skytt?? <ville.skytta at iki.fi> - 20051208-2
- Drop JDE; the full source for jde.jar doesn't seem to be available
  and even the included parts won't build with gcj eg. due to use of
  com.sun.* things.  Additionally it requires third party jars which are
  not currently available in Fedora Core or Extras.  So let's not inflict
  a crippled version of JDE on anyone; JDE users can install the upstream
  jde package using XEmacs package tools. (#180941)

* Sun Feb 12 2006 Ville Skytt?? <ville.skytta at iki.fi>
- Build xslt.jar ourselves (TrAX only), use TrAX by default in xslt-process.

* Sat Feb 11 2006 Ville Skytt?? <ville.skytta at iki.fi>
- Bundle upstream gnus package version 1.89 to fix #181011.
- Get rid of tli_rbl binary only applet jar in jde's docs (first step
  of fixing #180941).

* Sat Dec 17 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20051208-1
- Patch to support write-region's kludge in latin-unity.

* Fri Dec  9 2005 Ville Skytt?? <ville.skytta at iki.fi>
- 2005-12-08.
- Patch hyperbole to not require csh.
- Patch pydoc.el to find pydoc_lisp.py out of the box.
- Include bytecompiled python files.
- Set %%lang for various docs and info files.
- Prune changelog entries from pre-xemacs-sumo times.

* Sat Jul 16 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050715-1
- 2005-07-15; jde font-lock, sql-mode abbrev, w3 stylesheet and file
  permissions fixed upstream.
- Use sed instead of perl for in-place edits during build.

* Wed Jul 13 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050505-7
- Remove mew and skk, they're in separate packages again (#162952).
- Reformat specfile.

* Thu Jun  2 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050505-6
- Make sure we're using files included in this package
  when byte-recompiling patched *.el; also allows the byte-compilation
  to actually happen even if no previous xemacs-sumo is installed.

* Wed Jun  1 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050505-5
- Bundle upstream cc-mode package version 1.45 (contains cc-mode 5.30.10).
- Fix JDEE font-lock warnings with import statements.

* Tue May 24 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050505-3
- Apply improved upstream patch against JDE font-lock warnings.

* Fri May 20 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050505-2
- Apply upstream patch to fix abbrev error when loading sql-mode.

* Thu May  5 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050505-1
- 2005-05-05, mh-e toolbar specifier fix applied upstream.
- Apply patch from Aidan Kehoe to fix font-lock warnings in JDE.

* Wed Apr  6 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050307-2
- Make scripts in lib-src/ executable (Emmanuel Thom??, #134512).
- Drop no longer needed workaround for #64320.

* Tue Mar  8 2005 Ville Skytt?? <ville.skytta at iki.fi> - 20050307-1
- Update to 2005-03-07.
- Fix up unneeded executable bits on some files.

* Tue Mar  1 2005 Ville Skytt?? <scop@xemacs.org> - 20050118-2
- Revert back to bundled apel, mew and skk in the sumo.
- Drop xemacs-packages* Obsoletes.
- Build with xemacs-nox to fix chicken-egg bootstrap problem.
- Require xemacs-common.
- Remove pre-XEmacs-21.4 %%changelog entries.

* Wed Jan 19 2005 Jens Petersen <petersen@redhat.com> 20050118-1
- update to new sumos
  - update auctex-texjp-platex.patch
  - auctex-texsite-lisp-dir.patch no longer needed
  - auc-tex.info is now correctly auctex.info
- physically remove .el.orig patch backup files

* Tue Dec 14 2004 Jens Petersen <petersen@redhat.com>
- add auctex-texsite-lisp-dir.patch to initialise auctex TeX-lisp-directory
- exclude .orig backup files

* Wed Oct  6 2004 Jens Petersen <petersen@redhat.com> - 20040818-2
- rename auc-tex.info to auctex.info (Francis Tang, 134624)

* Wed Aug 18 2004 Jens Petersen <petersen@redhat.com> 20040818-1
- update to 2004-08-18 sumos
  - no longer need to replace xlib and xwem packages
  - cvs.el-history-log.patch is now upstream

* Mon Aug 16 2004 Ville Skytt?? <scop@xemacs.org> - 20040517-4
- replace xlib-autoload-startup-msg-125415.patch with xlib and xwem pre-release
  pkgs to really make them quiet at startup (125415,130019)
- pre-generate package info dir files and compress all the info files (130019)

* Mon Aug  9 2004 Jens Petersen <petersen@redhat.com> - 20040517-3
- default cvs-no-log-option to nil since cvs no longer accepts "-l" option
  with cvs.el-history-log.patch
- silence startup messages from xlib and xwem (125415) with
  xlib-autoload-startup-msg-125415.patch

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 20 2004 Jens Petersen <petersen@redhat.com> 20040517-1
- update to 2004-05-17 release

* Fri May  7 2004 Jens Petersen <petersen@redhat.com> - 20040202-4
- do not require xemacs, so that it is installable with xemacs-nox

* Thu Apr  1 2004 Jens Petersen <petersen@redhat.com> - 20040202-3
- remove executable flags from erc Changelog files [Ville Skytt??]

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb  4 2004 Jens Petersen <petersen@redhat.com> - 20040202-1
- update to 2004-02-02 sumos
- update browse-url-htmlview-84262.patch
- subtract 100 from all patch numbers

* Tue Nov 18 2003 Jens Petersen <petersen@redhat.com> - 20031113-1
- update to 2003-11-13 release

* Sat Oct 18 2003 Jens Petersen <petersen@redhat.com> - 20031003-3
- fix mh-e toolbar error (#100764) [reported by vonbrand@inf.utfsm.cl,
  fix by Stephen J. Turnbull]

* Fri Oct 17 2003 Jens Petersen <petersen@redhat.com> - 20031003-2
- generate X resource files in utf-8 for de, fr and ro (#107310) [frh@gmx.de]
- move our CJK X resource files here from xemacs with one file for
  native encoding and one for utf-8
- re-enable menubar translations for native CJK encodings (part of #106994)
  [Yukihiro Nakai]

* Mon Oct  6 2003 Jens Petersen <petersen@redhat.com> - 20031003-1
- update to 2003-10-03 release

* Mon Sep  1 2003 Jens Petersen <petersen@redhat.com> - 20030831-1
- update to 2003-08-31 release
- simplify /usr/local/bin/perl cleaning

* Tue Jul  1 2003 Jens Petersen <petersen@redhat.com> - 20030629-1
- update to 2003-06-29 release
- catch harmless mouse-avoidance-mode errors (#65346)
  [suggested by Reuben Thomas]

* Mon May 12 2003 Jens Petersen <petersen@redhat.com> - 20030414-1
- new package to separate xemacs-sumo and xemacs-mule-sumo from
  main xemacs package
