# remirepo/fedora spec file for php-yoast-phpunit-polyfills
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please preserve changelog entries
#
# Github
%global gh_commit    c48e4cf0c44b2d892540846aff19fb0468627bab
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Yoast
%global gh_project   PHPUnit-Polyfills
# Packagist
%global pk_vendor    yoast
%global pk_project   phpunit-polyfills
# Namespace
%global ns_vendor    Yoast
%global ns_project   PHPUnitPolyfills
# don't change major version used in package name
%global major        %nil
%bcond_without       tests
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Set of polyfills for changed PHPUnit functionality

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# autoloader relocated in src tree
Patch0:         %{name}-layout.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-reflection
# From composer.json, "require-dev": {
#        "php-parallel-lint/php-parallel-lint": "^1.2.0",
#        "php-parallel-lint/php-console-highlighter": "^0.5",
#        "yoast/yoastcs": "^2.1.0"
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
BuildRequires:  phpunit9
%endif
BuildRequires:  phpunit8
%if 0%{?fedora} < 35 && 0%{?rhel} < 9
BuildRequires:  phpunit7
BuildRequires:  phpunit6
BuildRequires:  phpunit
%endif
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#        "php": ">=5.5",
#        "phpunit/phpunit": "^4.8.36 || ^5.7.21 || ^6.0 || ^7.0 || ^8.0 || ^9.0"
Requires:       php(language) >= 5.5
# from phpcompatinfo report on version 0.2.0
Requires:       php-reflection

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Set of polyfills for changed PHPUnit functionality to allow for creating
PHPUnit cross-version compatible tests.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

# Fix for RPM layout
%patch0 -p1 -b .rpm
sed -e 's:src/::' phpunitpolyfills-autoload.php > src/autoload.php


%build
# Empty build section, most likely nothing required.


%install
mkdir -p        %{buildroot}/%{php_home}/%{ns_vendor}
cp -pr src      %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Yoast\\PHPUnitPolyfills\\Tests\\', dirname(__DIR__) . '/tests');
require_once '%{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF

: Run upstream test suite
ret=0
if [ -x %{_bindir}/phpunit ]; then
  for cmd in php php71 php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit --no-coverage --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit6 ]; then
  for cmd in php php71 php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit6 --no-coverage --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit7 ]; then
  for cmd in php php71 php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit7 --no-coverage --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --no-coverage --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php73 php74 php80; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --no-coverage --verbose || ret=1
    fi
  done
fi

exit $ret
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/%{ns_vendor}


%changelog
* Wed Mar 10 2021 Remi Collet <remi@remirepo.net> - 0.2.0-2
- reduce build matrix

* Thu Nov 26 2020 Remi Collet <remi@remirepo.net> - 0.2.0-1
- initial rpm
