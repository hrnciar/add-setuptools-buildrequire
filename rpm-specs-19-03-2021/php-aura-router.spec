# remirepo/Fedora spec file for php-aura-router
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global bootstrap    0
%global gh_commit    52507bc813c92511dbcacc7463f163ef5149ad38
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     auraphp
%global gh_project   Aura.Router
%global pk_owner     aura
%global pk_project   router
%global ns_owner     Aura
%global ns_project   Router
%global php_home     %{_datadir}/php

Name:           php-%{pk_owner}-%{pk_project}
Version:        3.1.0
Release:        9%{?dist}
Summary:        Powerful, flexible web routing for PSR-7 requests

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-composer(fedora/autoloader)
# Tests
%if %{with tests}
BuildRequires:  php(language) >= 5.5.0
BuildRequires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 2)
BuildRequires: (php-composer(psr/log)          >= 1.0   with php-composer(psr/log)          < 2)
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "zendframework/zend-diactoros": "~1.0",
#        "phpunit/phpunit": "~5.7 || ~4.8"
BuildRequires: (php-composer(zendframework/zend-diactoros) >= 1.0 with php-composer(zendframework/zend-diactoros) < 2)
BuildRequires:  phpunit
%endif

# From composer, "require": {
#        "php": ">=5.5.0",
#        "psr/http-message": "~1.0",
#        "psr/log": "~1.0"
Requires:       php(language) >= 5.5.0
Requires:      (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 2)
Requires:      (php-composer(psr/log)          >= 1.0   with php-composer(psr/log)          < 2)
# From phpcompatinfo report for version 2.3.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}


%description
Powerful, flexible web routing for PSR-7 requests.

Autoloader: %{php_home}/%{ns_owner}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
cat << 'EOF' | tee -a src/autoload.php
<?php
/* Autoloader for %{pk_owner}/%{pk_project} and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Aura\\Router\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    '%{php_home}/Psr/Http/Message/autoload.php',
    '%{php_home}/Psr/Log/autoload.php',
));
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_owner}
cp -pr src %{buildroot}%{php_home}/%{ns_owner}/%{ns_project}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require '%{buildroot}/%{php_home}/%{ns_owner}/%{ns_project}/autoload.php';
require '%{php_home}/Zend/Diactoros/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Aura\\Router\\', dirname(__DIR__) . '/tests');
EOF

ret=0
for cmd in php php72 php73 php74 php80; do
  if which php56; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done

exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_owner}/
     %{php_home}/%{ns_owner}/%{ns_project}/


%changelog
* Fri Jan 29 2021 Remi Collet <remi@remirepo.net> - 3.1.0-9
- use range dependencies, fix FTBFS

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar  2 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.0
- License is now MIT
- update package Summary and Description
- raise dependency on PHP 5.5
- add dependency on psr/http-message and psr/log
- switch to fedora/autoloader

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- initial package

