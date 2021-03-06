# remirepo/fedora spec file for php-horde-turba
#
# Copyright (c) 2012-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    turba
%global pear_channel pear.horde.org

Name:           php-horde-turba
Version:        4.2.25
Release:        6%{?dist}
Summary:        A web based address book

License:        ASL 1.0
URL:            http://www.horde.org/apps/turba
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)          >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)          < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Core)          >= 2.12.0 with php-pear(%{pear_channel}/Horde_Core)          < 3)
BuildRequires: (php-pear(%{pear_channel}/content)             >= 2.0.5  with php-pear(%{pear_channel}/content)             < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Core) >= 2.12.0
BuildRequires:  php-pear(%{pear_channel}/content) >= 2.0.5
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}

# Web stuff
Requires:       php(httpd)
Requires:       httpd
# From package.xml required
Requires:       php(language) >= 5.3.0
Requires:       php-gettext
Requires:       php-hash
Requires:       php-json
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/content)             >= 2.0.5   with php-pear(%{pear_channel}/content)             < 3)
Requires:      (php-pear(%{pear_channel}/horde)               >= 5.0.0   with php-pear(%{pear_channel}/horde)               < 6)
Requires:      (php-pear(%{pear_channel}/Horde_Auth)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Auth)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Core)          >= 2.12.0  with php-pear(%{pear_channel}/Horde_Core)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Data)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Data)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Date)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Date)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Dav)           >= 1.0.0   with php-pear(%{pear_channel}/Horde_Dav)           < 2)
Requires:      (php-pear(%{pear_channel}/Horde_Exception)     >= 2.0.0   with php-pear(%{pear_channel}/Horde_Exception)     < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Form)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Form)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Group)         >= 2.0.0   with php-pear(%{pear_channel}/Horde_Group)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_History)       >= 2.1.0   with php-pear(%{pear_channel}/Horde_History)       < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Icalendar)     >= 2.0.0   with php-pear(%{pear_channel}/Horde_Icalendar)     < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mail)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Mail)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mime)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Mime)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Nls)           >= 2.0.0   with php-pear(%{pear_channel}/Horde_Nls)           < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Perms)         >= 2.0.0   with php-pear(%{pear_channel}/Horde_Perms)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Prefs)         >= 2.0.0   with php-pear(%{pear_channel}/Horde_Prefs)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Serialize)     >= 2.0.0   with php-pear(%{pear_channel}/Horde_Serialize)     < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Share)         >= 2.0.0   with php-pear(%{pear_channel}/Horde_Share)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Support)       >= 2.0.0   with php-pear(%{pear_channel}/Horde_Support)       < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Url)           >= 2.0.0   with php-pear(%{pear_channel}/Horde_Url)           < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)          >= 2.5.0   with php-pear(%{pear_channel}/Horde_Util)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Vfs)           >= 2.1.3   with php-pear(%{pear_channel}/Horde_Vfs)           < 3)
Requires:      (php-pear(%{pear_channel}/Horde_View)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_View)          < 3)
# Optional
Recommends:    (php-pear(%{pear_channel}/Horde_Db)            >= 2.0.3   with php-pear(%{pear_channel}/Horde_Db)            < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Imsp)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Imsp)          < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Ldap)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Ldap)          < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Kolab_Format)  >= 2.0.5   with php-pear(%{pear_channel}/Horde_Kolab_Format)  < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Kolab_Storage) >= 2.1.0   with php-pear(%{pear_channel}/Horde_Kolab_Storage) < 3)
%else
Requires:       php-pear(%{pear_channel}/content) >= 2.0.5
Requires:       php-pear(%{pear_channel}/content) <  3.0.0
Requires:       php-pear(%{pear_channel}/horde) >= 5.0.0
Requires:       php-pear(%{pear_channel}/horde) <  6.0.0
Requires:       php-pear(%{pear_channel}/Horde_Auth) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Auth) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Core) >= 2.12.0
Requires:       php-pear(%{pear_channel}/Horde_Core) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Data) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Data) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Dav) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Dav) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Form) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Form) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Group) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Group) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_History) >= 2.1.0
Requires:       php-pear(%{pear_channel}/Horde_History) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mail) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mail) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Nls) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Nls) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Prefs) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Prefs) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Serialize) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Serialize) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Share) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Share) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.5.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Vfs) >= 2.1.3
Requires:       php-pear(%{pear_channel}/Horde_Vfs) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_View) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_View) <  3.0.0
# Optional an implicitly required
#    Horde_Db, Horde_Imsp, Horde_Ldap
#    Horde_Kolab_Format, Horde_Kolab_Storage
%endif
# Not yet available Horde_Service_Facebook
# From phpcompatinfo report for version 4.1.4
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl

Provides:       php-pear(%{pear_channel}/turba) = %{version}
Provides:       php-compposer(horde/turba) = %{version}
Obsoletes:      turba < 4
Provides:       turba = %{version}


%description
Turba is the Horde contact management application. Leveraging the Horde
framework to provide seamless integration with IMP and other Horde
applications, it supports storing contacts in SQL, LDAP, Kolab, and IMSP
address books.

%prep
%setup -q -c

cat <<EOF >httpd.conf
<DirectoryMatch %{pear_hordedir}/%{pear_name}/(config|lib|locale|scripts|templates)>
     Deny from all
</DirectoryMatch>
EOF

cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/htaccess/d' \
    -e '/%{pear_name}.mo/s/md5sum=.*name=/name=/' \
    ../package.xml >%{name}.xml
touch -r ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}

# Regenerate the locales
for po in $(find locale -name \*.po)
do
   : msgfmt --statistics $po -o $(dirname $po)/$(basename $po .po).mo
done


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -Dpm 644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml

# Install Apache configuration
install -Dpm 0644 ../httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Move configuration to /etc
mkdir -p %{buildroot}%{_sysconfdir}/horde
mv %{buildroot}%{pear_hordedir}/%{pear_name}/config \
   %{buildroot}%{_sysconfdir}/horde/%{pear_name}
ln -s %{_sysconfdir}/horde/%{pear_name} %{buildroot}%{pear_hordedir}/%{pear_name}/config

# Locales
for loc in locale/?? locale/??_??
do
    lang=$(basename $loc)
    echo "%%lang(${lang%_*}) %{pear_hordedir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%check
cd %{pear_name}-%{version}/test/Turba
# disable as this test use Horde_ActiveSync (non-free)
sed -e 's/function testDuplicateDetectionFromAsWithNoEmail/function SKIP_testDuplicateDetectionFromAsWithNoEmail/' \
    -i Unit/Driver/Base.php

ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap bootstrap.php --verbose . || ret=1
  fi
done
exit $ret


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.horde.org/%{pear_name} >/dev/null || :
fi


%files -f %{pear_name}.lang
%doc %{pear_docdir}/%{pear_name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%attr(0770,apache,apache) %dir %{_sysconfdir}/horde/%{pear_name}
%attr(0640,apache,apache) %config %{_sysconfdir}/horde/%{pear_name}/*.dist
%attr(0660,apache,apache) %config(noreplace) %{_sysconfdir}/horde/%{pear_name}/*.php
%attr(0660,apache,apache) %config %{_sysconfdir}/horde/%{pear_name}/*.xml
%{pear_xmldir}/%{name}.xml
%{pear_datadir}/turba
%doc %{pear_testdir}/turba
%{_bindir}/turba-convert-datatree-shares-to-sql
%{_bindir}/turba-convert-sql-shares-to-sqlng
%{_bindir}/turba-import-openxchange
%{_bindir}/turba-import-squirrelmail-file-abook
%{_bindir}/turba-import-squirrelmail-sql-abook
%{_bindir}/turba-import-vcards
%{_bindir}/turba-public-to-horde-share
%dir %{pear_hordedir}/%{pear_name}
%{pear_hordedir}/%{pear_name}/*.php
%{pear_hordedir}/%{pear_name}/addressbooks
%{pear_hordedir}/%{pear_name}/config
%{pear_hordedir}/%{pear_name}/js
%{pear_hordedir}/%{pear_name}/lib
%{pear_hordedir}/%{pear_name}/migration
%{pear_hordedir}/%{pear_name}/themes
%{pear_hordedir}/%{pear_name}/templates
%dir %{pear_hordedir}/%{pear_name}/locale


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 4.2.25-4
- requires php(httpd)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Remi Collet <remi@remirepo.net> - 4.2.25-1
- update to 4.2.25

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 4.2.24-1
- update to 4.2.24
- use range dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 4.2.23-1
- update to 4.2.23

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Remi Collet <remi@remirepo.net> - 4.2.22-1
- update to 4.2.22

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Remi Collet <remi@remirepo.net> - 4.2.21-1
- Update to 4.2.21 (no change)

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 4.2.20-1
- Update to 4.2.20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 4.2.19-1
- Update to 4.2.19

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 4.2.18-2
- Update to 4.2.18
- use upstream locale files

* Thu Nov 03 2016 Remi Collet <remi@fedoraproject.org> - 4.2.17-1
- Update to 4.2.17

* Wed Sep 07 2016 Remi Collet <remi@fedoraproject.org> - 4.2.16-1
- Update to 4.2.16

* Sat Jul 02 2016 Remi Collet <remi@fedoraproject.org> - 4.2.15-1
- Update to 4.2.15

* Tue Apr 05 2016 Remi Collet <remi@fedoraproject.org> - 4.2.14-1
- Update to 4.2.14

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 4.2.13-1
- Update to 4.2.13

* Tue Feb  9 2016 Remi Collet <remi@fedoraproject.org> - 4.2.12-1
- Update to 4.2.12

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Remi Collet <remi@fedoraproject.org> - 4.2.11-1
- Update to 4.2.11

* Thu Oct 22 2015 Remi Collet <remi@fedoraproject.org> - 4.2.10-1
- Update to 4.2.10

* Sat Aug 01 2015 Remi Collet <remi@fedoraproject.org> - 4.2.8-1
- Update to 4.2.8

* Fri Jun 19 2015 Remi Collet <remi@fedoraproject.org> - 4.2.7-1
- Update to 4.2.7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Remi Collet <remi@fedoraproject.org> - 4.2.6-1
- Update to 4.2.6

* Tue Feb 10 2015 Remi Collet <remi@fedoraproject.org> - 4.2.5-1
- Update to 4.2.5
- add provides php-compposer(horde/turba)

* Wed Dec 03 2014 Remi Collet <remi@fedoraproject.org> - 4.2.4-1
- Update to 4.2.4

* Wed Oct 29 2014 Remi Collet <remi@fedoraproject.org> - 4.2.3-1
- Update to 4.2.3

* Sat Sep 06 2014 Remi Collet <remi@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2
- raise dep on Horde_Util 2.5.0

* Tue Aug 05 2014 Remi Collet <remi@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Wed Jul 09 2014 Remi Collet <remi@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0
- add dep on content, Horde_Vfs
- raise dep on Horde_Core

* Mon Jul 07 2014 Remi Collet <remi@fedoraproject.org> - 4.1.5-1
- Update to 4.1.5
- run test suite during build

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Remi Collet <remi@fedoraproject.org> - 4.1.4-2
- preserve package.xml timestamp
- fix license (ASL 1.0) from review #1087742

* Mon Mar 10 2014 Remi Collet <remi@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- add dependency on Horde_Dav

* Tue Oct 29 2013 Remi Collet <remi@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3

* Tue Aug 27 2013 Remi Collet <remi@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2

* Wed Jul 17 2013 Remi Collet <remi@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1

* Wed Jun 05 2013 Remi Collet <remi@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Fri May 31 2013 Remi Collet <remi@fedoraproject.org> - 4.0.4-1
- Update to 4.0.4
- switch from Conflicts to Requires

* Tue Feb 12 2013 Remi Collet <remi@fedoraproject.org> - 4.0.3-1
- Update to 4.0.3

* Sun Jan 13 2013 Remi Collet <RPMS@FamilleCollet.com> - 4.0.2-2
- obsoletes/provides turba

* Thu Jan 10 2013 Remi Collet <RPMS@FamilleCollet.com> - 4.0.2-1
- Update to 4.0.2 for remi repo

* Tue Nov 27 2012 Remi Collet <RPMS@FamilleCollet.com> - 4.0.1-1
- Update to 4.0.1 for remi repo

* Sun Nov  4 2012 Remi Collet <RPMS@FamilleCollet.com> - 4.0.0-1
- Initial package
