# remirepo/fedora spec file for php-horde-Horde-Test
#
# Copyright (c) 2012-2021 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Test
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Test
Version:        2.6.4
Release:        2%{?dist}
Summary:        Horde testing base classes

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

# Use unbundled PHPUnit
Patch0:         %{pear_name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml, required
Requires:       php(language) >= 5.3.0
Requires:       php-dom
Requires:       php-json
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Support) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Support) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)    >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)    < 3)
# From package.xml, optional
Recommends:    (php-pear(%{pear_channel}/Horde_Cli)     >= 2.0.0  with php-pear(%{pear_channel}/Horde_Cli)     < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Log)     >= 2.0.0  with php-pear(%{pear_channel}/Horde_Log)     < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Support) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util)    <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util)    >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Cli)     <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Cli)     >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Log)     <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Log)     >= 2.0.0
%endif
# From phpcompatinfo report for version 2.4.0
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-spl
# Required as we drop bundled copy
Requires:       php-phpunit-PHPUnit >= 3.5.0

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-test) = %{version}


%description
Horde-specific PHPUnit base classes.


%prep
%setup -q -c

cd %{pear_name}-%{version}
%patch0 -p1 -b .rpm

# Don't install bundled PHPUnit
# Don't check md5sum for patched files
sed -e '/bundle\/vendor/d' \
    -e '/Autoload.php/s/md5sum="[^"]*"//' \
    -e '/AllTests.php/s/md5sum="[^"]*"//' \
   ../package.xml >%{name}.xml
touch -r ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Test


%changelog
* Tue Mar  9 2021 Remi Collet <remi@remirepo.net> - 2.6.4-2
- use range dependencies

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May  3 2017 Remi Collet <remi@remirepo.net> - 2.6.3-1
- Update to 2.6.3

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Tue Feb 02 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1 (no change)

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Tue Jan 13 2015 Remi Collet <remi@fedoraproject.org> - 2.4.8-1
- Update to 2.4.8 (no change)
- add provides php-composer(horde/horde-test)

* Mon Dec 29 2014 Remi Collet <remi@fedoraproject.org> - 2.4.7-1
- Update to 2.4.7

* Tue Nov 18 2014 Remi Collet <remi@fedoraproject.org> - 2.4.6-1
- Update to 2.4.6

* Mon Nov 10 2014 Remi Collet <remi@fedoraproject.org> - 2.4.5-2
- add upstream patch to fix test failure in turba
  and kronolith, thanks to Koschei

* Tue Oct 28 2014 Remi Collet <remi@fedoraproject.org> - 2.4.5-1
- Update to 2.4.5

* Thu Oct 02 2014 Remi Collet <remi@fedoraproject.org> - 2.4.4-1
- Update to 2.4.4

* Sat Aug 30 2014 Remi Collet <remi@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Mon Jul 07 2014 Remi Collet <remi@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2 (no change)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Remi Collet <remi@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1
- drop bundled PHPUnit and use system one

* Tue Mar 11 2014 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Sat Dec 07 2013 Remi Collet <remi@fedoraproject.org> - 2.2.6-1
- Update to 2.2.6 (stable)

* Tue Nov 12 2013 Remi Collet <remi@fedoraproject.org> - 2.2.5-1
- Update to 2.2.5

* Mon Oct 28 2013 Remi Collet <remi@fedoraproject.org> - 2.2.4-1
- Update to 2.2.4

* Tue Aug 27 2013 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Tue Feb 12 2013 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- cleanups
- add dependency on Horde_Log
- fix License

* Wed Dec 12 2012 Nick Bebout <nb@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Mon Jun 25 2012 Nick Bebout <nb@fedoraproject.org> - 1.3.0-3
- Fix requires

* Wed Jun 20 2012 Nick Bebout <nb@fedoraproject.org> - 1.3.0-2
- Fix packaging issues

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.3.0-1
- Initial package
