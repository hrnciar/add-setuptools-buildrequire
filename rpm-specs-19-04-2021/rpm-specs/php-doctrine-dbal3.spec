# remirepo/Fedora spec file for php-doctrine-dbal3
#
# Copyright (c) 2013-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Adam Williamson <awilliam@redhat.com>
#                         Remi Collet <remi@remirepo.net>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      dbal
%global github_version   3.0.0
%global github_commit    ee6d1260d5cc20ec506455a585945d7bdb98662c
%global major            3

%global composer_vendor  doctrine
%global composer_project dbal

# "php": "^7.3 || ^8"
%global php_min_ver 7.3
# "doctrine/cache": "^1.0"
%global doctrine_cache_min_ver 1.0
%global doctrine_cache_max_ver 2
# "doctrine/event-manager": "^1.0"
%global doctrine_event_min_ver 1.0
%global doctrine_event_max_ver 2
# "symfony/console": "^2.0.5|^3.0|^4.0|^5.0"
# ignore v2
%global symfony_console_min_ver 3.0
%global symfony_console_max_ver 6

%{!?phpdir:  %global phpdir  %{_datadir}/php}

# Build using "--without tests" to disable tests
%bcond_without tests

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Doctrine Database Abstraction Layer (DBAL) version %{major}

License:       MIT
URL:           http://www.doctrine-project.org/projects/dbal.html

# Run "php-doctrine-dbal-get-source.sh" to create source
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Update bin script:
# 1) Add she-bang
# 2) Auto-load using Doctrine\Common\ClassLoader
Patch0:        %{name}-bin.patch

BuildArch: noarch
# Tests
%if %{with tests}
BuildRequires: phpunit9 >= 9.4
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires:(php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) <  %{doctrine_cache_max_ver})
BuildRequires:(php-composer(doctrine/event-manager) >= %{doctrine_event_min_ver} with php-composer(doctrine/event-manager) <  %{doctrine_cache_max_ver})
## composer.json (optional)
BuildRequires:(php-composer(symfony/console) >= %{symfony_console_min_ver} with php-composer(symfony/console) <  %{symfony_console_max_ver})
## phpcompatinfo (computed from version 3.0)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) <  %{doctrine_cache_max_ver})
Requires:     (php-composer(doctrine/event-manager) >= %{doctrine_event_min_ver} with php-composer(doctrine/event-manager) <  %{doctrine_cache_max_ver})
# composer.json (optional)
Requires:     (php-composer(symfony/console) >= %{symfony_console_min_ver} with php-composer(symfony/console) <  %{symfony_console_max_ver})
# phpcompatinfo (computed from version 3.0)
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
The Doctrine database abstraction & access layer (DBAL) offers a lightweight
and thin runtime layer around a PDO-like API and a lot of additional, horizontal
features like database schema introspection and manipulation through an OO API.

The fact that the Doctrine DBAL abstracts the concrete PDO API away through the
use of interfaces that closely resemble the existing PDO API makes it possible
to implement custom drivers that may use existing native or self-made APIs. For
example, the DBAL ships with a driver for Oracle databases that uses the oci8
extension under the hood.

Autoloader: %{phpdir}/Doctrine/DBAL%{major}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Patch bin script and drop composer/package-versions-deprecated usage
%patch0 -p1 -b .rpm
sed -e 's/@VERSION@/%{github_version}/' -i src/Tools/Console/ConsoleRunner.php
find . -name \*.rpm -delete


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

if (!class_exists('Doctrine\\DBAL\\Connection')) {
    \Fedora\Autoloader\Autoload::addPsr4('Doctrine\\DBAL\\', __DIR__);
}
\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    '%{phpdir}/Doctrine/Common/EventManager/autoload.php',
));

\Fedora\Autoloader\Dependencies::optional([
    [
        (getenv('RPM_SYMFONY_TREE')?:'%{phpdir}/Symfony5') . '/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}/%{phpdir}/Doctrine
cp -rp src %{buildroot}/%{phpdir}/Doctrine/DBAL%{major}

mkdir -p %{buildroot}/%{_bindir}
install -pm 0755 bin/doctrine-dbal.php %{buildroot}/%{_bindir}/doctrine-dbal%{major}


%check
%if %{with tests}
cat > bs.php <<'BOOTSTRAP'
<?php
require_once '%{buildroot}/%{phpdir}/Doctrine/DBAL%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4(
    'Doctrine\\DBAL\\Tests\\',
    __DIR__ . '/tests'
);
BOOTSTRAP

: ignore test using PHPStan
find tests -name \*php -exec grep -q PHPStan {} \; -print -delete

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php73 php74 php80; do
    rm -f /tmp/test_nesting.sqlite
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit9 \
            --bootstrap bs.php \
            --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Doctrine/DBAL%{major}
%{_bindir}/doctrine-dbal%{major}


%changelog
* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 3.0.0-2
- don't register autoloader twice, e.g. by doctrine/dbal v3

* Mon Nov 16 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-doctrine-dbal3
- move to /usr/share/php/Doctrine/DBAL3

* Mon Nov 16 2020 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1

* Fri Oct 23 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Wed Oct 21 2020 Remi Collet <remi@remirepo.net> - 2.11.3-1
- update to 2.11.3

* Mon Oct 19 2020 Remi Collet <remi@remirepo.net> - 2.11.2-1
- update to 2.11.2

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Mon Sep 21 2020 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Mon Sep 14 2020 Remi Collet <remi@remirepo.net> - 2.10.4-1
- update to 2.10.4

* Wed Sep  2 2020 Remi Collet <remi@remirepo.net> - 2.10.3-1
- update to 2.10.3

* Tue Apr 21 2020 Remi Collet <remi@remirepo.net> - 2.10.2-1
- update to 2.10.2

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependencies on PHP 7.2
- switch to phpunit8

* Wed Jan  2 2019 Remi Collet <remi@remirepo.net> - 2.9.2-1
- update to 2.9.2

* Fri Dec 14 2018 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Mon Dec 10 2018 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- drop dependency on doctrine/common
- add dependency on doctrine/cache
- add dependency on doctrine/event-manager
- allow Symfony 4

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2
- raise dependencies on PHP 7.1
- use range dependencies
- switch to phpunit7

* Tue May 30 2017 Remi Collet <remi@remirepo.net> - 2.5.12-3
- allow to force Symfony version using RPM_SYMFONY_TREE

* Sat Mar 11 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.12-1
- Updated to 2.5.12 (RHBZ #1412852)
- Switch autoloader to php-composer(fedora/autoloader)
- Run upstream tests with SCLs if available

* Wed Feb  8 2017 Remi Collet <remi@remirepo.net> - 2.5.12-1
- update to 2.5.12

* Mon Feb  6 2017 Remi Collet <remi@remirepo.net> - 2.5.11-1
- update to 2.5.11

* Tue Jan 24 2017 Remi Collet <remi@remirepo.net> - 2.5.10-1
- update to 2.5.10

* Fri Jan 20 2017 Remi Collet <remi@remirepo.net> - 2.5.9-1
- update to 2.5.9

* Mon Sep 26 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.5-1
- Updated to 2.5.5 (RHBZ #1374891)

* Mon Jun 13 2016 Remi Collet <remi@fedoraproject.org> - 2.5.4-2
- add workaround for test suite with PHPUnit 5.4

* Mon Mar 14 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.4-1
- Updated to 2.5.4 (RHBZ #1153987)
- Added autoloader

* Wed Jan 14 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.1-1
- Updated to 2.5.1 (BZ #1153987)

* Fri Jan 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.1-0.2.20150101git185b886
- Updated to latest snapshot
- Fixed bin script
- Added tests

* Thu Jul 31 2014 Remi Collet <rpms@famillecollet.com> 2.4.2-6
- backport for remi repo
- fix license handling

* Tue Jul 29 2014 Adam Williamson <awilliam@redhat.com> - 2.4.2-6
- really apply the patch

* Tue Jul 29 2014 Adam Williamson <awilliam@redhat.com> - 2.4.2-5
- backport another OwnCloud-related pgsql fix from upstream master

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-4
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Updated Doctrine dependencies to use php-composer virtual provides

* Sat Jan 11 2014 Remi Collet <rpms@famillecollet.com> 2.4.2-2
- backport for remi repo

* Tue Jan 07 2014 Adam Williamson <awilliam@redhat.com> - 2.4.2-2
- primary_index: one OwnCloud patch still isn't in upstream

* Sat Jan 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4.2-1
- Updated to 2.4.2
- Conditional %%{?dist}

* Tue Dec 31 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4.1-2.20131231gitd08b11c
- Updated to latest snapshot
- Removed patches (pulled into latest snapshot)

* Sun Dec 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4.1-1
- Initial package
