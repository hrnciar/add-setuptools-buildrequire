#
# Fedora spec file for php-webmozart-assert
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# enable bootstrap when need to provide a new autoloader
%global bootstrap 0
%global github_owner     webmozart
%global github_name      assert
%global github_version   1.9.1
%global github_commit    bafc69caeb4d49c39fd0779086c03a3738cbb389

%global composer_vendor  webmozart
%global composer_project assert

# "php": "^5.3.3 || ^7.0 || ^8.0"
%global php_min_ver 5.3.3

# PHPUnit
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
%global phpunit_require phpunit7
%global phpunit_exec    phpunit7
%else
%global phpunit_require php-composer(phpunit/phpunit)
%global phpunit_exec    phpunit
%endif

%if %{bootstrap}
# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}
%else
# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       Assertions to validate method input/output with nice error messages

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-webmozart-assert-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require}
## phpcompatinfo (computed from version 1.7.0)
BuildRequires: php-ctype
BuildRequires: php-filter
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.7.0)
Requires:      php-ctype
Requires:      php-filter
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This library contains efficient assertions to test the input and output of your
methods. With these assertions, you can greatly reduce the amount of coding
needed to write a safe implementation.

All assertions in the Assert class throw an \InvalidArgumentException if they
fail.

Autoloader: %{phpdir}/Webmozart/Assert/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Webmozart\\Assert\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Webmozart
cp -rp src %{buildroot}%{phpdir}/Webmozart/Assert


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
\Fedora\Autoloader\Autoload::addPsr4('Webmozart\\Assert\\Tests\\', __DIR__.'/tests');
\Fedora\Autoloader\Autoload::addPsr4('Webmozart\\Assert\\Bin\\', __DIR__.'/bin/src');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in php %{?rhel:php54 php55 php56 php70 php71 php72} php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC \
            -d auto_prepend_file=%{buildroot}%{phpdir}/Webmozart/Assert/autoload.php \
            $PHPUNIT \
                --bootstrap bootstrap.php \
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
%dir %{phpdir}/Webmozart
     %{phpdir}/Webmozart/Assert


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1 (RHBZ #1825544)

* Sun Feb 23 2020 Shawn Iwinski <shawn@iwin.ski> - 1.7.0-1
- Update to 1.7.0 (RHBZ #1746998)
- Disable bootstrap so tests run by default
- Conditionally use PHPUnit 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 Shawn Iwinski <shawn@iwin.ski> - 1.4.0-1
- Update to 1.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Remi Collet <remi@remirepo.net> - 1.3.0-3
- fix autoloader, use PSR-4 to avoid duplicated definition
- prepend autoloader to ensure we use current version in tests
- fix FTBFS #1605449

* Fri Oct 19 2018 Remi Collet <remi@remirepo.net> - 1.3.0-2
- fix autoloader, use PSR-4 to avoid duplicated definition
- prepend autoloader to ensure we use current version in tests
- fix FTBFS #1605449
- bootstrap build

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 22 2018 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Update to 1.3.0 (RHBZ #1539946)
- Add get source script
- Add composer.json to repo
- Update running of tests

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Update to 1.2.0 (RHBZ #1398043)
- Use php-composer(fedora/autoloader)
- Run upstream tests with SCLs if they are available

* Wed Sep 28 2016 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
