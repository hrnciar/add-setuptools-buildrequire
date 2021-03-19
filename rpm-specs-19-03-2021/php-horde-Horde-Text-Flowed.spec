# remirepo/fedora spec file for php-horde-Horde-Text-Flowed
#
# Copyright (c) 2012-2019 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Text_Flowed
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Text-Flowed
Version:        2.0.4
Release:        4%{?dist}
Summary:        Horde API for flowed text as per RFC 3676

License:        LGPLv2
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-channel(%{pear_channel})
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test) >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Util) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util) < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-pcre
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Util) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util) < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-text-flowed) = %{version}


%description
The Horde_Text_Flowed:: class provides common methods for manipulating text
using the encoding described in RFC 3676 ('flowed' text).


%prep
%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


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


%check
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)

ret=0
for cmd in php php56 php70 php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
       --bootstrap=bootstrap.php \
       --verbose  . || ret=1
  fi
done
exit $ret


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
%{pear_phpdir}/Horde/Text
%doc %{pear_testdir}/%{pear_name}


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Remi Collet <remi@remirepo.net> - 2.0.4-1
- update to 2.0.4
- use range dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Remi Collet <remi@remirepo.net> - 2.0.3-4
- Fix FTBFS from Koschei, add upstream patch for PHP 7.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 02 2016 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3 (no change)
- PHP 7 compatible version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- add provides php-composer(horde/horde-text-flowed)

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-6
- fix FTBFS (include path for test)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 17 2013 Remi Collet <remi@fedoraproject.org> - 2.0.1-4
- fix dependencies

* Wed Feb 6 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.1-3
- Update for review

* Tue Feb 5 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.1-2
- Remove BuildRoot, change php(language) to php-common

* Mon Nov 19 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Fri Nov  2 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Jun 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.1-1
- Upgrade to 1.0.1

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.0-1
- Initial package
