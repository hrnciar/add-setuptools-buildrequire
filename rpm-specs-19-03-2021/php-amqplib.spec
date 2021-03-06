#
# Fedora spec file for php-amqplib
#
# Copyright (c) 2017-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-amqplib
%global github_name      php-amqplib
%global github_version   2.12.0
%global github_commit    dfcccd36bf12b4c7cc3ec74d571e00e0f767232e

%global composer_vendor  php-amqplib
%global composer_project php-amqplib

# "php": ">=5.6.3"
%global php_min_ver 5.6.3
# "phpseclib/phpseclib": "^2.0.0"
%global phpseclib_min_ver 2.0
%global phpseclib_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_project}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       Pure PHP implementation of the AMQP protocol

License:       LGPLv2+
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-php-amqplib-php-amqplib-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit7
BuildRequires: php-mbstring
BuildRequires: php-sockets
%if %{with_range_dependencies}
BuildRequires: (php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver} with php-composer(phpseclib/phpseclib) < %{phpseclib_max_ver})
%else
BuildRequires: php-composer(phpseclib/phpseclib) <  %{phpseclib_max_ver}
BuildRequires: php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver}
%endif
## phpcompatinfo for version 2.12.0
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver} with php-composer(phpseclib/phpseclib) < %{phpseclib_max_ver})
%else
Requires:      php-composer(phpseclib/phpseclib) <  %{phpseclib_max_ver}
Requires:      php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver}
%endif
Requires:      php-mbstring
Requires:      php-sockets
# phpcompatinfo for version 2.12.0
Requires:      php-date
Requires:      php-pcntl
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-pcntl
%endif

# Conflicts
## composer.json
Conflicts:     php(language) = 7.4.0
Conflicts:     php(language) = 7.4.1

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
Provides:      %{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This library is a pure PHP implementation of the AMQP 0-9-1 protocol [1]. It's
been tested against RabbitMQ [2].

Autoloader: %{phpdir}/PhpAmqpLib/autoload.php

[1] http://www.rabbitmq.com/tutorials/amqp-concepts.html
[2] http://www.rabbitmq.com/

%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee PhpAmqpLib/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/phpseclib/autoload.php',
]);

\Fedora\Autoloader\Autoload::addPsr4('PhpAmqpLib\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp PhpAmqpLib %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
date_default_timezone_set('UTC');
require '%{buildroot}%{phpdir}/PhpAmqpLib/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/tests/config.php',
]);

\Fedora\Autoloader\Autoload::addPsr4('PhpAmqpLib\\Tests\\Unit\\', __DIR__.'/tests/Unit');
BOOTSTRAP

: Remove tests requiring a running AMQP service
rm -f tests/Unit/Wire/IO/SocketIOTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit7)
for PHP_EXEC in php %{?rhel:php54 php55 php56 php70} php71 php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            --testsuite="Unit Tests" || RETURN_CODE=1
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
%{phpdir}/PhpAmqpLib


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 05 2020 Shawn Iwinski <shawn@iwin.ski> - 2.12.0-2
- Require phpseclib for runtime in additional to build require

* Sat Sep 05 2020 Shawn Iwinski <shawn@iwin.ski> - 2.12.0-1
- Update to 2.12.0 (RHBZ #1742616)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Shawn Iwinski <shawn@iwin.ski> - 2.9.2-1
- Update to 2.9.2 (RHBZ #1535736)

* Fri May 10 2019 Shawn Iwinski <shawn@iwin.ski> - 2.7.3-1
- Update to 2.7.3
- Update license from LGPLv2 to LGPLv2+

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Shawn Iwinski <shawn@iwin.ski> - 2.7.0-2
- Set default timezone in tests' bootstrap

* Wed Oct 25 2017 Shawn Iwinski <shawn@iwin.ski> - 2.7.0-1
- Initial package
