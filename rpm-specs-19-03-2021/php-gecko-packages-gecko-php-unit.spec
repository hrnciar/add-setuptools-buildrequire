# remirepo/fedora spec file for php-gecko-packages-gecko-php-unit
#
# Copyright (c) 2016-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    a06beb80f63645140c251cfd757ba94a4a540be5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     GeckoPackages
%global gh_project   GeckoPHPUnit
%global pk_owner     gecko-packages
%global pk_project   gecko-php-unit
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_owner}-%{pk_project}
Version:        2.2.1
Release:        7%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Additional PHPUnit asserts and constraints

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.3.6
BuildRequires:  php-dom
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "phpunit/phpunit": "^4.8.35 || ^5.4.3"
BuildRequires:  php-composer(phpunit/phpunit)
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json,     "require": {
#        "php": "^5.3.6 || ^7.0"
Requires:       php(language) >= 5.3.6
# From phpcompatinfo report for version 2.2
Requires:       php-dom
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}


%description
Provides additional asserts to be used in PHPUnit tests.
The asserts are provided using Traits so no changes are needed
in the hierarchy of test classes.

Autoloader: %{php_home}/GeckoPackages/PHPUnit/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/PHPUnit/autoload.php
<?php
/* Autoloader for friendsofphp/php-cs-fixer and its dependencies */

require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('GeckoPackages\\PHPUnit\\', __DIR__);

EOF


%build
# Empty build section, most likely nothing required.


%install
mkdir -p           %{buildroot}%{php_home}/GeckoPackages
cp -pr src/PHPUnit %{buildroot}%{php_home}/GeckoPackages/PHPUnit


%check
%if %{with_tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/GeckoPackages/PHPUnit/autoload.php vendor/autoload.php

: Fix paths in unit tests
for unit in $(find tests -name \*Test.php -print); do
  sed -e 's:PHPUnit/tests:tests:' -i $unit
done

ret=0
for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{php_home}/GeckoPackages
     %{php_home}/GeckoPackages/PHPUnit


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 2.2.1-1
- Update to 2.2.1

* Thu Aug 24 2017 Remi Collet <remi@remirepo.net> - 2.2-1
- Update to 2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Remi Collet <remi@remirepo.net> - 2.1-1
- Update to 2.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- initial package, version 2.0.0

