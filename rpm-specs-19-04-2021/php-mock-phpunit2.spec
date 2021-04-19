# remirepo/fedora spec file for php-mock-phpunit2
#
# Copyright (c) 2016-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    2877a0e58f12e91b64bf36ccd080a209dcbf6c30
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-mock
%global gh_project   php-mock-phpunit
%global with_tests   0%{!?_without_tests:1}
%global major        2

Name:           php-mock-phpunit%{major}
Version:        2.6.0
Release:        4%{?dist}
Summary:        Mock built-in PHP functions with PHPUnit.

License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7
%if %{with_tests}
BuildRequires: (php-composer(php-mock/php-mock-integration) >= 2.1   with php-composer(php-mock/php-mock-integration) < 3)
BuildRequires: (php-composer(php-mock/php-mock)             >= 2.2   with php-composer(php-mock/php-mock)             < 3)
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
BuildRequires:  phpunit8
%endif
# For autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# from composer.json, "require": {
#        "php": ">=7",
#        "phpunit/phpunit": "^6 || ^7 || ^8 || ^9",
#        "php-mock/php-mock-integration": "^2.1"
#    "conflict": {
#        "phpunit/phpunit-mock-objects": "3.2.0"
Requires:       php(language) >= 7
Requires:      (phpunit8 or phpunit9)
Requires:      (php-composer(php-mock/php-mock-integration) >= 2.1   with php-composer(php-mock/php-mock-integration) < 3)
Requires:      (php-composer(php-mock/php-mock)             >= 2.2   with php-composer(php-mock/php-mock)             < 3)
# From phpcompatinfo report from version 2.1.0
# only Core

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Mock built-in PHP functions (e.g. time()) with PHPUnit.
This package relies on PHP's namespace fallback policy.
No further extension is needed.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Create autoloader
cat << 'AUTOLOAD' | tee rpm.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpmock\\phpunit\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    __DIR__ . '/compatibility.php',
    '%{_datadir}/php/phpmock2/autoload.php',
));
AUTOLOAD


%build
# Nothing


%install
mkdir -p             %{buildroot}%{_datadir}/php/
mkdir -p             %{buildroot}%{_datadir}/php/phpmock%{major}
cp -pr classes       %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit
cp -pr compatibility %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/compatibility
cp -p  autoload.php  %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/compatibility.php
cp -p  rpm.php       %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/autoload.php';
require_once '%{_datadir}/php/phpmock%{major}/autoload.php';
EOF

ret=0
: Run upstream test suite with phpunit6
if [ -x %{_bindir}/phpunit6 ]; then
for cmd in php php72 php73; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit6 --verbose || ret=1
  fi
done
fi

if [ -x %{_bindir}/phpunit7 ]; then
: Run upstream test suite with phpunit7
for cmd in php php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 --verbose || ret=1
  fi
done
fi

if [ -x %{_bindir}/phpunit8 ]; then
: Run upstream test suite with phpunit8
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
fi

if [ -x %{_bindir}/phpunit9 ]; then
: Run upstream test suite with phpunit9
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
fi
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/phpmock%{major}/phpunit


%changelog
* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 2.6.0-4
- drop dependency on phpunit6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0
- raise dependency on php-mock2 2.2
- raise dependency on php-mock-integration2 2.1
- allow phpunit9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  7 2019 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0

* Mon Apr  8 2019 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0
- raise dependency on php-mock2 2.1.1

* Thu Mar  7 2019 Remi Collet <remi@remirepo.net> - 2.2.0-2
- update to 2.2.0
- add dependency on php-mock2 for phpunit8 compatibility
- allow phpunit8
- use php-mock2 2.1 single autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  8 2018 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr  9 2018 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Fri Mar 23 2018 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- add autoloader
- allow phpunit6 and phpunit7

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- rename to php-mock-phpunit2
- Update to 2.0.1
- raise dependency on PHP 7
- raise dependency on php-mock-integration 2
- switch top phpunit6

* Thu May 11 2017 Remi Collet <remi@remirepo.net> - 1.1.2-3
- switch to fedora/autoloader

* Thu Jun 16 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- update to 1.1.2 (no change)

* Mon Feb 22 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- Fix: license is WTFPL

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- initial package
