# remirepo/fedora spec file for php-ramsey-uuid
#
# Copyright (c) 2020-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without tests

# Github
%global gh_commit    cd4032040a750077205918c86049aa0f43d22947
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     ramsey
%global gh_project   uuid
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# Namespace
%global ns_vendor    Ramsey
%global ns_project   Uuid

Name:           php-%{pk_vendor}-%{pk_name}
Version:        4.1.1
Release:        3%{?dist}
Summary:        Library for generating and working with UUIDs

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

# don't use codeception/aspect-mock
Patch0:         %{name}-tests.patch
Patch1:         https://patch-diff.githubusercontent.com/raw/ramsey/uuid/pull/352.patch

BuildArch:      noarch

BuildRequires:  php(language) >= 7.2
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "codeception/aspect-mock": "^3",
#        "dealerdirect/phpcodesniffer-composer-installer": "^0.6.2 || ^0.7.0",
#        "doctrine/annotations": "^1.8",
#        "goaop/framework": "^2",
#        "mockery/mockery": "^1.3",
#        "moontoast/math": "^1.1",
#        "paragonie/random-lib": "^2",
#        "php-mock/php-mock-mockery": "^1.3",
#        "php-mock/php-mock-phpunit": "^2.5",
#        "php-parallel-lint/php-parallel-lint": "^1.1",
#        "phpbench/phpbench": "^0.17.1",
#        "phpstan/extension-installer": "^1.0",
#        "phpstan/phpstan": "^0.12",
#        "phpstan/phpstan-mockery": "^0.12",
#        "phpstan/phpstan-phpunit": "^0.12",
#        "phpunit/phpunit": "^8.5",
#        "psy/psysh": "^0.10.0",
#        "slevomat/coding-standard": "^6.0",
#        "squizlabs/php_codesniffer": "^3.5",
#        "vimeo/psalm": "3.9.4"
%if %{with tests}
BuildRequires: (php-composer(brick/math)            >= 0.8   with php-composer(brick/math)            < 0.10)
BuildRequires: (php-composer(ramsey/collection)     >= 1.0   with php-composer(ramsey/collection)     < 2)
BuildRequires: (php-composer(mockery/mockery)       >= 1.3   with php-composer(mockery/mockery)       < 2)
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
# https://github.com/ramsey/uuid/pull/350
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
%else
BuildRequires:  phpunit8 >= 8.5
%global phpunit %{_bindir}/phpunit8
%endif
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.2 || ^8",
#        "ext-json": "*",
#        "brick/math": "^0.8 || ^0.9",
#        "ramsey/collection": "^1.0",
#        "symfony/polyfill-ctype": "^1.8"
Requires:       php(language) >= 7.2
Requires:       php-ctype
Requires:       php-json
Requires:      (php-composer(brick/math)        >= 0.8   with php-composer(brick/math)        < 0.10)
Requires:      (php-composer(ramsey/collection) >= 1.0   with php-composer(ramsey/collection) < 2)
# From phpcompatifo report for 4.1.1
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
ramsey/uuid is a PHP library for generating and working with universally
unique identifiers (UUIDs).

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1 -b .rpm
%patch1 -p1 -b .pr352


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src
cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Brick/Math/autoload.php',
    '%{_datadir}/php/Ramsey/Collection/autoload.php',
    __DIR__ . '/functions.php',
]);
EOF

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with tests}
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Test\\', dirname(__DIR__) . '/tests');
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Mockery1/autoload.php',
]);
EOF

: Ignore tests using missing mocking libraries
find tests -type f -exec grep -Eq '(PHPMockery|Aspec|Moontoast)' {} \; -delete -print

: Ignore test with erratic result on Koji
FILTER="--filter '^((?!(testSerializationOfNodeProviderCollection)).)*$'"
: Test failing with recent depdencies
rm tests/Generator/RandomLibAdapterTest.php

: Run upstream test suite
ret=0
for cmdarg in "php %{?phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --no-coverage \
      --verbose $FILTER || ret=1
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
%{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Fri Jan 29 2021 Remi Collet <remi@remirepo.net> - 4.1.1-3
- ignore 2 tests and fix FTBFS

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 2020 Remi Collet <remi@remirepo.net> - 4.1.1-2
- add patch for PHP 8 from merged PR
  https://github.com/ramsey/uuid/pull/352
- switch to phpunit9
  https://github.com/ramsey/uuid/pull/350
- ignore 1 test with erratic result from review #1884542

* Fri Oct  2 2020 Remi Collet <remi@remirepo.net> - 4.1.1-1
- initial package
