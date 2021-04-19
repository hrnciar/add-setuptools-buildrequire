Name:           mrbs
Version:        1.9.2
Release:        1%{?dist}
Summary:        Meeting Room Booking System

License:        GPLv2
URL:            https://mrbs.sourceforge.net
Source0:        https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        mrbs-httpd.conf

BuildArch:      noarch

Requires:       php >= 5.5.0
# php-imap has been dropped from F34+
%if ! 0%{?fedora} > 33
Requires:       php-imap
%endif
Requires:       php-ldap
Requires:       php-mysqli
Requires:       php-pgsql
Requires:       php-pear-File-Passwd
Requires:       php-pear-Mail
Requires:       php-phpmailer6

Provides:       bundled(js-jquery) = 3.5.1
Provides:       bundled(js-jquery-datatables) = 1.10.21
Provides:       bundled(js-jquery-migrate) = 3.3.0
Provides:       bundled(js-jquery-select2) = 4.0.13
Provides:       bundled(js-jquery-ui) = 1.12.1


%description
The Meeting Room Booking System (MRBS) is a PHP-based application for
booking meeting rooms.


%prep
%setup -q

# Clean up bundled libs
pushd web
rm -rf File* Mail* PEAR.php
rm -rf lib/PHPMailer/
popd

# Fix encoding
for i in INSTALL NEWS AUTHENTICATION ; do {
    iconv -f iso8859-1 -t utf-8 $i > $i.utf8 && \
    touch -r $i $i.utf8 && \
    mv -f $i.utf8 $i; };
done;

# remove exec perms on the perl scripts
chmod a-x *.pl


%build
## Nothing to build ##


%install
# Install the code
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mrbs
cp -a web/* $RPM_BUILD_ROOT/%{_datadir}/mrbs/


# Move the conf to the proper place
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mrbs
mv $RPM_BUILD_ROOT/%{_datadir}/mrbs/config.inc.php-sample \
    $RPM_BUILD_ROOT/%{_sysconfdir}/mrbs/config.inc.php
ln -s %{_sysconfdir}/mrbs/config.inc.php \
    $RPM_BUILD_ROOT/%{_datadir}/mrbs/config.inc.php

# Apache conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -m 0644 %{SOURCE1} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/mrbs.conf


%files
%doc AUTHENTICATION ChangeLog INSTALL LANGUAGE NEWS README
%doc README.sqlapi UPGRADE
%doc *.sql *.pl *.php crypt_passwd.example
%license COPYING
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mrbs.conf
%config(noreplace) %{_sysconfdir}/mrbs/config.inc.php
%{_datadir}/mrbs


%changelog
* Fri Mar 19 2021 Xavier Bachelot <xavier@bachelot.org> 1.9.2-1
- Update to 1.9.2 (RHBZ#1668908)

* Fri Mar 19 2021 Xavier Bachelot <xavier@bachelot.org> 1.7.4.1-1
- Update to 1.7.4.1

* Fri Mar 19 2021 Xavier Bachelot <xavier@bachelot.org> 1.7.2-1
- Update to 1.7.2

* Thu Feb 25 2021 Xavier Bachelot <xavier@bachelot.org> 1.7.1-8
- Fix fail to install on f34+ (RHBZ#1933022)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Xavier Bachelot <xavier@bachelot.org> 1.7.1-1
- Update to 1.7.1 (RHBZ#1544223).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Xavier Bachelot <xavier@bachelot.org> 1.7.0-1
- Update to 1.7.0 (RHBZ#1514285), which fixes CVE-2016-7103.
- Track bundled javascript libraries.
- Remove now useless dependency on php-pear-Crypt-Blowfish.
- Fix perms on config file.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Xavier Bachelot <xavier@bachelot.org> 1.6.1-2
- Add patch to use system PHPMailer lib.

* Mon Feb 27 2017 Xavier Bachelot <xavier@bachelot.org> 1.6.1-1
- Update to 1.6.1 (RHBZ#1426975).

* Wed Feb 22 2017 Xavier Bachelot <xavier@bachelot.org> 1.6.0-1
- Update to 1.6.0 (RHBZ#1421397).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Xavier Bachelot <xavier@bachelot.org> 1.5.0-1
- Update to 1.5.0.
- Fix Requires: php-mysql(i).
- Clean up specfile.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Xavier Bachelot <xavier@bachelot.org> 1.4.10-1
- Update to 1.4.10.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Xavier Bachelot <xavier@bachelot.org> 1.4.9-2
- Fix apache 2.4 configuration (bz #871432)

* Fri Oct 12 2012 Xavier Bachelot <xavier@bachelot.org> 1.4.9-1
- Update to 1.4.9.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 02 2012 Xavier Bachelot <xavier@bachelot.org> 1.4.8-1
- Update to 1.4.8.

* Sat Jul 16 2011 Xavier Bachelot <xavier@bachelot.org> 1.4.7-1
- Update to 1.4.7.

* Fri Feb 11 2011 Xavier Bachelot <xavier@bachelot.org> 1.4.6-1
- Update to 1.4.6.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 03 2010 Xavier Bachelot <xavier@bachelot.org> 1.4.5-1
- Update to 1.4.5.

* Wed Jun 02 2010 Xavier Bachelot <xavier@bachelot.org> 1.4.4.1-1
- Update to 1.4.4.1.

* Mon Mar 01 2010 Xavier Bachelot <xavier@bachelot.org> 1.4.3-1
- Update to 1.4.3.

* Thu Jul 16 2009 Xavier Bachelot <xavier@bachelot.org> 1.4.2-1
- Update to 1.4.2.
- Preserve timestamp on encoding conversion.

* Tue Mar 31 2009 Xavier Bachelot <xavier@bachelot.org> 1.4.1-2
- Add more BR:.

* Sun Feb 22 2009 Xavier Bachelot <xavier@bachelot.org> 1.4.1-1
- Update to 1.4.1.
- Change BR: following this BR: rename.

* Fri Jan 23 2009 Xavier Bachelot <xavier@bachelot.org> 1.4-1
- Initial build.
