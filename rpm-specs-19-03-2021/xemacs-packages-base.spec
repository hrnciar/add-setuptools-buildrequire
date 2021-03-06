%global hgver   cbe800ed9a7f
%global pkgdir  %{_datadir}/xemacs
%global xemver  21.5.34

Name:           xemacs-packages-base
Version:        20190327
Release:        4%{?dist}
Summary:        Base lisp packages for XEmacs

# dired and efs are GPL+, rest GPLv2+
License:        GPLv2+ and GPL+
URL:            http://www.xemacs.org/Documentation/packageGuide.html
# Tarball created with Source99
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}-checkout.sh

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  xemacs-nox

Requires:       xemacs(bin) >= %xemver

# https://fedoraproject.org/wiki/Changes/Deprecate_xemacs
# https://bugzilla.redhat.com/show_bug.cgi?id=1916926
Provides:       deprecated()

%description
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains the minimal recommended set of additional lisp
packages for XEmacs: efs, xemacs-base and mule-base from upstream.

%package        el
Summary:        Emacs lisp source files for the base lisp packages for XEmacs
Requires:       %{name} = %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/Deprecate_xemacs
# https://bugzilla.redhat.com/show_bug.cgi?id=1916926
Provides:       deprecated()

%description    el
This package is not needed to run XEmacs; it contains the lisp source
files for the base lisp packages for XEmacs, mainly of interest when
developing or debugging the packages.


%prep
%setup -q
cat << EOF > make.sh
#!/bin/sh
make \\
    XEMACS_BINARY=%{_bindir}/xemacs-nox \\
    XEMACS_INSTALLED_PACKAGES_ROOT=\$RPM_BUILD_ROOT%{pkgdir} \\
    XEMACS_21_5=t \\
    "\$@"
EOF
chmod +x make.sh

# Get reproducible builds by setting the compiling username
mkdir ~/.xemacs
echo >> ~/.xemacs/custom.el << EOF
(custom-set-variables
 '(user-mail-address "mockbuild@fedoraproject.org"))
EOF


%build
apkgs="apel dired efs fsf-compat xemacs-base"
xpkgs="efs xemacs-base"
mpkgs="mule-base"
./make.sh -C xemacs-packages autoloads PACKAGES="$apkgs"
./make.sh -C mule-packages   autoloads PACKAGES="$mpkgs"
./make.sh -C xemacs-packages           PACKAGES="$xpkgs"
./make.sh -C mule-packages             PACKAGES="$mpkgs"


%install
mkdir -p $RPM_BUILD_ROOT%{pkgdir}
./make.sh -C xemacs-packages/xemacs-base install
./make.sh -C xemacs-packages/efs         install
./make.sh -C mule-packages/mule-base     install

# separate files
rm -f *.files
touch base-files el-files

find $RPM_BUILD_ROOT%{pkgdir}/* \
  \( -type f -name '*.el.orig' -delete \) -o \
  \( -type f -not -name '*.el' -fprint base-non-el.files \) -o \
  \( -type d -not -name info -fprintf dir.files "%%%%dir %%p\n" \) -o \
  \( -name '*.el' \( -exec test -e '{}'c \; -fprint el-bytecomped.files -o \
     -fprint base-el-not-bytecomped.files \) \)

sed -i -e "s|$RPM_BUILD_ROOT||" *.files
cat base-*.files dir.files | grep -v /info/ >> base-files
cat el-*.files                              >> el-files

# all info files packaged in xemacs-packages-extra-info for simplicity
rm -rf $RPM_BUILD_ROOT%{pkgdir}/*-packages/info

sed -i -e 's/^\(.*\(\.ja\|-ja\.texi\)\)$/%lang(ja) \1/' base-files


%files -f base-files

%files el -f el-files


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190327-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Jerry James <loganjerry@gmail.com> - 20190327-3
- Mark as deprecated (bz 1916926)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190327-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190327-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Jerry James <loganjerry@gmail.com> - 20190327-1
- Update comint.el in xemacs-base

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180610-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Jerry James <loganjerry@gmail.com> - 20180610-1
- Update to latest package releases

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170330-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170330-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170330-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 Jerry James <loganjerry@gmail.com> - 20170330-1
- Update to latest package releases

* Sat Aug  5 2017 Jerry James <loganjerry@gmail.com> - 20160621-4
- Workaround for bz 1478722

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160621-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160621-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 Jerry James <loganjerry@gmail.com> - 20160621-1
- Update to latest package releases

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 20160208-1
- Update to latest package releases

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150919-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct  7 2015 Jerry James <loganjerry@gmail.com> - 20150919-1
- Update to latest package releases

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150413-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Jerry James <loganjerry@gmail.com> - 20150413-1
- Update to latest package releases
- Set the build username for reproducible builds

* Thu Aug  7 2014 Jerry James <loganjerry@gmail.com> - 20140715-1
- Update to latest package releases

* Mon Jul  7 2014 Jerry James <loganjerry@gmail.com> - 20140705-1
- Update to latest package releases
- Drop upstreamed -texi patch
- Update checkout script for mercurial

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130408-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130408-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr  9 2013 Jerry James <loganjerry@gmail.com> - 20130408-1
- Update to latest package releases
- Add -texi patch to fix build with texinfo 5

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121228-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 20121228-1
- Update to latest package releases
- Drop xz BR; it is on the list of exceptions

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjeryr@gmail.com> - 20110502-2
- Mass rebuild for Fedora 17

* Tue May  3 2011 Jerry James <loganjerry@gmail.com> - 20110502-1
- Update to latest package releases
- Drop BuildRoot tag, clean script, and clean at start of install script

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100727-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 13 2010 Jerry James <loganjerry@gmail.com> - 20100727-1
- Update to new package release.
- New upstream CVS location in checkout script.
- Drop upstreamed patches.
- Use xz instead of lzma to compress.

* Tue Sep  1 2009 Jerry James <loganjerry@gmail.com> - 20090217-4
- Add mule-base patch to fix bz 480845 and hopefully bz 520248.

* Mon Aug 24 2009 Jerry James <loganjerry@gmail.com> - 20090217-3
- Add APEL patch to fix bz 503185 for XEmacs.
- Add dired patch to fix bz 504422.
- Add itimer patch preemptively.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar  7 2009 Ville Skytt?? <ville.skytta at iki.fi> - 20090217-1
- Update to 2009-02-17.
- Compress source tarball with lzma.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070427-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 16 2007 Ville Skytt?? <ville.skytta at iki.fi> - 20070427-2
- License: GPLv2+ and GPL+

* Fri May 18 2007 Ville Skytt?? <ville.skytta at iki.fi> - 20070427-1
- 2007-04-27.
- Require an actual XEmacs editor, not just -common.

* Mon Apr  2 2007 Ville Skytt?? <ville.skytta at iki.fi> - 20061221-1
- 2006-12-21.

* Sun Sep 10 2006 Ville Skytt?? <ville.skytta at iki.fi> - 20060510-3
- Split minimal set of packages from xemacs-sumo.
- Really build from sources.
