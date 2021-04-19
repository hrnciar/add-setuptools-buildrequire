# remirepo/fedora spec file for php-bartlett-php-compatinfo-db
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# See https://github.com/llaville/php-compatinfo-db/releases
%global gh_commit    35e3902e44f3345dae2dcb85f3fb903600ab19af
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20151031
%global gh_owner     llaville
%global gh_project   php-compatinfo-db
# Namespace
%global ns_vendor    Bartlett
%global ns_project   CompatInfoDb
# Composer
%global c_vendor     bartlett
%global c_project    php-compatinfo-db
%if 0%{?fedora} >= 32
# only enabled with 7.4+
%bcond_without       tests
%else
# disabled as too much issues, e.g. with symfony-polyfill
%bcond_with          tests
%endif

%global upstream_version  3.4.2
#global upstream_prever   RC1

Name:           php-%{c_vendor}-%{c_project}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        Reference Database to be used with php-compatinfo library

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{upstream_version}%{?upstream_prever}-%{gh_short}.tar.gz

# Fix autoloader and config path
# Fix sqlite database path
# Fix version and avoir composer/package-versions-deprecated (relying on composer.lock)
Patch0:         %{name}-3.4-rpm.patch
# CURL_SSLVERSION constants have been backported
Patch1:         %{name}-curltls.patch

# upstream patches

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-pdo
BuildRequires:  php-phar
BuildRequires:  php-spl
# From composer.json, "require-dev"
#        "composer/composer": "^2.0",
#        "psr/log": "^1.0",
#        "symfony/phpunit-bridge": "^5.1"
BuildRequires: (php-composer(composer/semver)               >= 3.0   with php-composer(composer/semver)               <  4)
BuildRequires: (php-composer(doctrine/orm)                  >= 2.7   with php-composer(doctrine/orm)                  <  4)
BuildRequires: (php-composer(symfony/requirements-checker)  >= 2.0   with php-composer(symfony/requirements-checker)  <  3)
BuildRequires:  php-symfony4-config                         >= 4.4
BuildRequires:  php-symfony4-console                        >= 4.4
BuildRequires:  php-symfony4-dependency-injection           >= 4.4
BuildRequires:  php-symfony4-event-dispatcher               >= 4.4
BuildRequires:  php-symfony4-messenger                      >= 4.4
BuildRequires:  php-symfony4-stopwatch                      >= 4.4
# For our patch / autoloader
BuildRequires:  php-composer(fedora/autoloader)
# From composer.json, "require-dev": {
#        "phpunit/php-timer": "^2.0"
BuildRequires:  php-cli
%if %{with tests}
BuildRequires:  phpunit9
%endif

# From composer.json, "require"
#        "php": "^7.2|^8.0",
#        "ext-json": "*",
#        "ext-pcre": "*",
#        "ext-pdo": "*",
#        "ext-phar": "*",
#        "ext-spl": "*",
#        "composer/package-versions-deprecated": "^1.8",
#        "composer/semver": "^1.0|^2.0|^3.0",
#        "doctrine/orm": "^2.7",
#        "symfony/config": "^4.4|^5.0",
#        "symfony/console": "^4.4|^5.0",
#        "symfony/dependency-injection": "^4.4|^5.0",
#        "symfony/event-dispatcher": "^4.4|^5.0",
#        "symfony/messenger": "^4.4|^5.0",
#        "symfony/requirements-checker": "^2.0",
#        "symfony/stopwatch": "^4.4|^5.0"
Requires:       php(language) >= 7.2
Requires:       php-json
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-phar
Requires:       php-spl
Requires:      (php-composer(composer/semver)               >= 3.0   with php-composer(composer/semver)               <  4)
Requires:      (php-composer(doctrine/orm)                  >= 2.7   with php-composer(doctrine/orm)                  <  4)
Requires:      (php-composer(symfony/requirements-checker)  >= 2.0   with php-composer(symfony/requirements-checker)  <  3)
Requires:       php-symfony4-config                         >= 4.4
Requires:       php-symfony4-console                        >= 4.4
Requires:       php-symfony4-dependency-injection           >= 4.4
Requires:       php-symfony4-event-dispatcher               >= 4.4
Requires:       php-symfony4-messenger                      >= 4.4
Requires:       php-symfony4-stopwatch                      >= 4.4
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{c_vendor}/%{c_project}) = %{version}
# Extracted from bartlett/php-compatinfo 4
Conflicts:      php-bartlett-PHP-CompatInfo < 5


%description
%{summary}.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
%patch1 -p0 -b .curltls

: relocate
mv config src/config

cat << 'EOF' | tee src/autoload.php
<?php
/**
 * Autoloader %{name} and its dependencies
 */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Bartlett\\CompatInfoDb\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Composer/Semver3/autoload.php',
    '%{_datadir}/php/Symfony4/Component/Config/autoload.php',
    '%{_datadir}/php/Symfony4/Component/Console/autoload.php',
    '%{_datadir}/php/Symfony4/Component/DependencyInjection/autoload.php',
    '%{_datadir}/php/Symfony4/Component/EventDispatcher/autoload.php',
    '%{_datadir}/php/Symfony4/Component/Messenger/autoload.php',
    '%{_datadir}/php/Symfony4/Component/Stopwatch/autoload.php',
    '%{_datadir}/php/Symfony/Requirements/autoload.php',
    '%{_datadir}/php/Doctrine/ORM/autoload.php',
    __DIR__ . '/Infrastructure/Framework/Symfony/Polyfill.php',
));
EOF

# Use package version
grep "%{version}" src/Presentation/Console/ApplicationInterface.php

# Cleanup patched files
find src -name \*rpm -delete -print


%build
: Ensure current version is known by reference
OPT=$(php -r '
  require "src/autoload.php";

  switch (PHP_MAJOR_VERSION . PHP_MINOR_VERSION) {
    case "72":
      $max = Bartlett\CompatInfoDb\Domain\Factory\ExtensionVersionProviderInterface::LATEST_PHP_7_2;
      break;
    case "73":
      $max = Bartlett\CompatInfoDb\Domain\Factory\ExtensionVersionProviderInterface::LATEST_PHP_7_3;
      break;
    case "74":
      $max = Bartlett\CompatInfoDb\Domain\Factory\ExtensionVersionProviderInterface::LATEST_PHP_7_4;
      break;
    case "80":
      $max = Bartlett\CompatInfoDb\Domain\Factory\ExtensionVersionProviderInterface::LATEST_PHP_8_0;
      break;
    default:
      exit(0);
  }
  if (version_compare(PHP_VERSION, $max, ">")) {
    fputs(STDERR, "Current: " . PHP_VERSION . " > Known: $max\n\n");
    echo "/LATEST_PHP_" . PHP_MAJOR_VERSION . "_" . PHP_MINOR_VERSION .
         "/s/" . PHP_MAJOR_VERSION . "\." .PHP_MINOR_VERSION . "\.[0-9]*/" . PHP_VERSION . "/";
  } else {
    fputs(STDERR, "Current: " . PHP_VERSION . " = Known: $max\n\n");
  }
')
if [ -n "$OPT" ]; then
  sed -e "$OPT" -i  src/Domain/Factory/ExtensionVersionProviderInterface.php
fi
grep " LATEST" src/Domain/Factory/ExtensionVersionProviderInterface.php

: Create command using local sources
sed -e "s:%{_datadir}/php/%{ns_vendor}/%{ns_project}:$PWD/src:" \
    -e 's:../data:data:' \
    bin/compatinfo-db >compatinfo-db

export DATABASE_URL=sqlite:///${PWD}/compatinfo.sqlite
doctrine orm:schema-tool:create

: Generate the references database
php -d memory_limit=2G -d date.timezone=Europe/Paris compatinfo-db db:init
#php -d memory_limit=2G -d date.timezone=Europe/Paris compatinfo-db db:show xmlrpc

: Diag
%{_bindir}/php -d date.timezone=Europe/Paris compatinfo-db diagnose


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}

install -D -p -m 644 compatinfo.sqlite  %{buildroot}%{_datadir}/%{name}/compatinfo.sqlite
install -D -p -m 755 bin/compatinfo-db  %{buildroot}%{_bindir}/%{name}


%if %{with tests}
%check
export DATABASE_URL=sqlite:///%{buildroot}%{_datadir}/%{name}/compatinfo.sqlite

mkdir config
cat << 'EOF' | tee config/bootstrap.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/config/bootstrap.php';
\Fedora\Autoloader\Autoload::addPsr4('Bartlett\\CompatInfoDb\\Tests\\', dirname(__DIR__) . '/tests');
EOF

# https://github.com/llaville/php-compatinfo-db/issues/70
rm -rf tests/Reference/Extension/PhpBundle/Pcre

ret=0
%{_bindir}/phpunit9 \
    --include-path %{buildroot}%{_datadir}/php \
    -d memory_limit=1G || ret=1

exit $ret
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_bindir}/%{name}
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}
     %{_datadir}/%{name}


%changelog
* Mon Mar 15 2021 Remi Collet <remi@remirepo.net> - 3.4.2-1
- update to 3.4.2
- drop dependency on league/tactician
- drop dependency on laminas/laminas-diagnostics
- add dependency on doctrine/orm
- add dependency on symfony/config
- add dependency on symfony/dependency-injection
- add dependency on symfony/event-dispatcher
- add dependency on symfony/messenger
- add dependency on symfony/requirements-checker
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Remi Collet <remi@remirepo.net> - 2.19.0-1
- update to 2.19.0

* Mon Sep 14 2020 Remi Collet <remi@remirepo.net> - 2.18.0-1
- update to 2.18.0

* Mon Aug 17 2020 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0
- switch to composer/semver 3

* Tue Jun 30 2020 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0

* Mon May 18 2020 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency on Symfony 4.4

* Sun Mar 22 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Fri Mar 20 2020 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- switch from Zend to Laminas

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Wed Jan 22 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- open https://github.com/llaville/php-compatinfo-db/issues/38 redis
- open https://github.com/llaville/php-compatinfo-db/issues/39 svn

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0

* Tue Dec  3 2019 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0
- ignore test results with 7.4, reported as
  https://github.com/llaville/php-compatinfo-db/issues/32

* Fri Jul 26 2019 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0

* Sun Jun 16 2019 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0
- bump dependency on PHP 7.1
- add dependency on symfony/console 3 or 4
- add dependency on league/tactician
- add dependency on zendframework/zenddiagnostics
- add php-bartlett-php-compatinfo-db command

* Thu Apr 11 2019 Remi Collet <remi@remirepo.net> - 1.42.0-1
- update to 1.42.0
- open https://github.com/llaville/php-compatinfo-db/issues/28
  missing new reference for memcache 4.0.3 and sqlite3

* Mon Mar 11 2019 Remi Collet <remi@remirepo.net> - 1.41.0-1
- update to 1.41.0

* Mon Feb 25 2019 Remi Collet <remi@remirepo.net> - 1.40.1-1
- update to 1.40.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Remi Collet <remi@remirepo.net> - 1.39.0-1
- update to 1.39.0

* Tue Nov 13 2018 Remi Collet <remi@remirepo.net> - 1.38.0-1
- update to 1.38.0

* Fri Oct 12 2018 Remi Collet <remi@remirepo.net> - 1.37.0-1
- update to 1.37.0
- use symfony3
- ignore test failing because of symfony/polyfill

* Sun Oct  7 2018 Remi Collet <remi@remirepo.net> - 1.36.0-2
- update to 1.36.0
- raise dependency on PHP 5.5
- open https://github.com/llaville/php-compatinfo-db/issues/14 zip
- open https://github.com/llaville/php-compatinfo-db/issues/15 http
- open https://github.com/llaville/php-compatinfo-db/issues/16 redis
- open https://github.com/llaville/php-compatinfo-db/issues/17 uopz
- open https://github.com/llaville/php-compatinfo-db/issues/18 varnish

* Wed Aug 29 2018 Remi Collet <remi@remirepo.net> - 1.35.0-2
- update to 1.35.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul  6 2018 Remi Collet <remi@remirepo.net> - 1.33.0-1
- update to 1.33.0

* Fri Apr 27 2018 Remi Collet <remi@remirepo.net> - 1.32.0-1
- update to 1.32.0

* Thu Apr  5 2018 Remi Collet <remi@remirepo.net> - 1.31.0-1
- update to 1.31.0

* Fri Mar  2 2018 Remi Collet <remi@remirepo.net> - 1.30.0-1
- Update to 1.30.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 1.29.0-1
- Update to 1.29.0
- use range dependency on F27+

* Tue Jan  9 2018 Remi Collet <remi@remirepo.net> - 1.28.0-1
- Update to 1.28.0

* Fri Jan  5 2018 Remi Collet <remi@remirepo.net> - 1.27.0-1
- Update to 1.27.0

* Fri Nov 24 2017 Remi Collet <remi@remirepo.net> - 1.26.0-1
- Update to 1.26.0

* Tue Oct 31 2017 Remi Collet <remi@remirepo.net> - 1.25.0-1
- Update to 1.25.0

* Tue Oct  3 2017 Remi Collet <remi@remirepo.net> - 1.24.0-1
- Update to 1.24.0

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 1.23.0-1
- Update to 1.23.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Remi Collet <remi@remirepo.net> - 1.22.0-1
- Update to 1.22.0

* Fri Jun  9 2017 Remi Collet <remi@remirepo.net> - 1.21.0-1
- Update to 1.21.0

* Fri Mar 17 2017 Remi Collet <remi@remirepo.net> - 1.19.0-1
- Update to 1.19.0
- adapt patch fixing DB location

* Fri Feb 24 2017 Remi Collet <remi@fedoraproject.org> - 1.18.0-1
- update to 1.18.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Remi Collet <remi@fedoraproject.org> - 1.17.0-1
- update to 1.17.0

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 1.16.0-1
- update to 1.16.0

* Wed Nov 23 2016 Remi Collet <remi@fedoraproject.org> - 1.15.0-1
- update to 1.15.0
- disable test suite with PHP 7.1, not yet supported
  https://github.com/llaville/php-compatinfo-db/issues/8

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 1.14.0-2
- switch to fedora/autoloader

* Sat Oct 15 2016 Remi Collet <remi@fedoraproject.org> - 1.14.0-1
- update to 1.14.0

* Tue Oct  4 2016 Remi Collet <remi@fedoraproject.org> - 1.13.0-1
- update to 1.13.0

* Tue Jul 26 2016 Remi Collet <remi@fedoraproject.org> - 1.11.0-1
- update to 1.11.0

* Tue Jul  5 2016 Remi Collet <remi@fedoraproject.org> - 1.10.0-1
- update to 1.10.0

* Sat May 28 2016 Remi Collet <remi@fedoraproject.org> - 1.9.0-1
- update to 1.9.0

* Tue May  3 2016 Remi Collet <remi@fedoraproject.org> - 1.8.1-1
- update to 1.8.1

* Tue Apr 12 2016 Remi Collet <remi@fedoraproject.org> - 1.7.0-1
- update to 1.7.0

* Sat Mar  5 2016 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- update to 1.6.0
- use package version as version in database instead of date

* Sat Feb  6 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan  9 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Tue Dec 29 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Thu Dec 10 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- fix reference to ensure current version is known
  as we usually build RC version in rawhide.

* Sat Dec  5 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- add dependency on composer/semver

* Wed Nov  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.alpha1
- Initial package
