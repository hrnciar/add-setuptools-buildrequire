Name:       bleachbit
Summary:    Remove sensitive data and free up disk space
URL:        https://www.bleachbit.org/
Version:    4.2.0
Release:    3%{?dist}
License:    GPLv3+ and MIT
BuildArch:  noarch

# Development and bug reports mostly seem to happen BleachBit's GitHub project, but their documentation points to SourceForge for the GPG public key and signatures, so that's where we'll need to get the source tarballs -- https://docs.bleachbit.org/doc/install-on-linux.html#digital-signatures
Source0: https://downloads.sourceforge.net/project/bleachbit/bleachbit/%{version}/bleachbit-%{version}.tar.bz2
Source1: https://downloads.sourceforge.net/project/bleachbit/bleachbit/%{version}/bleachbit-%{version}-sha256sum.txt.asc
Source2: https://downloads.sourceforge.net/project/bleachbit/public_key/andrew2019.key
# TODO: Remove this file when it merges on the next release -- <https://github.com/bleachbit/bleachbit/pull/1087>
Source3: https://raw.githubusercontent.com/terrycloth/bleachbit/473f857716d9fa43c3978fc331840de2e9b4b51b/org.bleachbit.BleachBit.metainfo.xml

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnupg2
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if 0%{?rhel}  &&  0%{?rhel} < 8
BuildRequires: python3-rpm-macros
%endif

Requires: gtk3
Requires: python3-chardet
%if 0%{?rhel}  &&  0%{?rhel} < 8
Requires: python36-gobject
%else
Requires: python3-gobject
%endif

%description
Delete traces of your computer activity and other junk files to free
disk space and maintain privacy.

With BleachBit, you can free cache, delete cookies, clear Internet
history, shred temporary files, delete logs, and discard junk you didn't
know was there. Designed for Linux and Windows systems, it wipes clean
thousands of applications including Firefox, Internet Explorer, Adobe
Flash, Google Chrome, Opera, Safari, and many more. Beyond simply
deleting files, BleachBit includes advanced features such as shredding
files to prevent recovery, wiping free disk space to hide traces of
files deleted by other applications, and cleaning Web browser profiles
to make them run faster.



# EPEL7 still defaults to Python 2.
%if  0%{?rhel}  &&  0%{?rhel} < 8
%global  __python  %{__python3}
%endif

# EPEL7 rpmbuild still defines _metainfodir as /usr/share/appdata/, even though plenty of packages use the newer /usr/share/metainfo/.
%if  0%{?rhel}  &&  0%{?rhel} < 8
%global  _metainfodir  %{_datadir}/metainfo
%endif



%prep
# Can't verify the tarball all at once because upstream switched from detached signature file to a signed checksum...
# %%{gpgverify} --keyring='%%{SOURCE2}' --signature='%%{SOURCE1}' --data='%%{SOURCE0}'
gpg2 --import %{SOURCE2}
gpg2 --verify %{SOURCE1}

cd %{_sourcedir}
# Old version of sha256sum on EPEL7 doesn't support ignoring missing files or PGP signature in the checksum file, so we have to filter for the one line we want.
%if 0%{?rhel}  &&  0%{?rhel} < 8
grep "bleachbit-%{version}.tar.bz2"  %{SOURCE1}  > ./extracted-checksum.txt
sha256sum --check ./extracted-checksum.txt
%else
sha256sum --ignore-missing  --check %{SOURCE1}
%endif



%setup -q

# Disable update notifications, since package will be updated by DNF or Packagekit.
sed 's/online_update_notification_enabled = True/online_update_notification_enabled = False/g'  --in-place ./bleachbit/__init__.py

# These get installed to %%{_datadir} as non-executable files, and so shouldn't need a shebang at all.
find ./bleachbit/  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/.+$||g' --in-place '{}' +

# Replace any remaining env shebangs, or shebangs calling unversioned or unnecessarily specifically versioned Python, with plain python3.
find ./  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/usr/bin/env python3?$|#!%{_bindir}/python3|g' --in-place '{}' +
find ./  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/usr/bin/python[[:digit:][:punct:]]*$|#!%{_bindir}/python3|g' --in-place '{}' +



%build
%py3_build
%make_build --directory ./po/

# Remove Windows-specific functionality.
%make_build delete_windows_files



%install
%make_install  PYTHON=%{__python3}  prefix=%{_prefix}  INSTALL="%{_bindir}/install -Dp"
%make_install --directory ./po/  PYTHON=%{__python3}  prefix=%{_prefix}  INSTALL="%{_bindir}/install -Dp"

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications/  org.bleachbit.BleachBit.desktop
# TODO: Go back to using the repo's original metainfo file when it merges on the next release.
#install -Dp  org.bleachbit.BleachBit.metainfo.xml  %%{buildroot}/%%{_metainfodir}/
install -Dp  %{SOURCE3}  %{buildroot}/%{_metainfodir}/

# "BleachBit As Administrator" app launcher is broken, so we're not shipping any polkit files for now -- https://github.com/bleachbit/bleachbit/issues/950
rm %{buildroot}/%{_datadir}/polkit-1/actions/org.bleachbit.policy

%find_lang %{name}



%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.bleachbit.BleachBit.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml



%files -f %{name}.lang
# TODO: Inconsistency about which doc files to include
# https://github.com/bleachbit/bleachbit/issues/1088
#%%doc  README*  doc/CONTRIBUTING.md
%doc  README*
%license COPYING
%{_bindir}/bleachbit
%{_datadir}/bleachbit/
%{_datadir}/applications/org.bleachbit.BleachBit.desktop
%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml
%{_datadir}/pixmaps/bleachbit.png





%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Audrey Toskin <audrey@tosk.in> - 4.2.0-2
- Adjust package spec to build for EPEL7.

* Wed Jan 6 2021 Audrey Toskin <audrey@tosk.in> - 4.2.0-1
- Bump to upstream version 4.2.0, which, among other things, adds new
  cleaners and regular expression-based searches during deep scans.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Audrey Toskin <audrey@tosk.in> - 4.0.0-2
- Finished unretired package.
- GPG-verify source tarball.
- Omit upstream's "BleachBit As Administrator" app launcher, since it's
  broken on Fedora.

* Wed Apr 22 2020 Audrey Toskin <audrey@tosk.in> - 4.0.0-1
- Prepare to unretire package after upstream ported to GTK3 and Python3.
