# remirepo/fedora spec file for php-cs-fixer
#
# Copyright (c) 2016-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    e0f6d05c8b157f50029ca6c65c19ed2694f475bf
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     FriendsOfPHP
%global gh_project   PHP-CS-Fixer
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

# Bundled this fork which is not designed for use outside of php-cs-fixer
# https://github.com/PHP-CS-Fixer/diff/releases
%global gh_diff_owner   PHP-CS-Fixer
%global gh_diff_version 1.3.1
%global gh_diff_commit  dbd31aeb251639ac0b9e7e29405c1441907f5759
%global gh_diff_short   %(c=%{gh_diff_commit}; echo ${c:0:7})

Name:           php-cs-fixer
Version:        2.18.5
Release:        1%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        A tool to automatically fix PHP code style

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        %{name}-diff-%{gh_diff_version}-%{gh_diff_short}.tgz
Source2:        makesrc.sh

# Use our autoloader
Patch0:         %{name}-autoload.patch

BuildArch:      noarch
%if %{with_tests}
# For tests
# as we use phpunit9
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-tokenizer
BuildRequires:  (php-composer(composer/semver)               >= 3.0 with php-composer(composer/semver)               < 4)
BuildRequires:  (php-composer(composer/xdebug-handler)       >= 1.0 with php-composer(composer/xdebug-handler)       < 2)
BuildRequires:  (php-composer(doctrine/annotations)          >= 1.2 with php-composer(doctrine/annotations)          < 2)
BuildRequires:  (php-composer(sebastian/diff)                >= 1.4 with php-composer(sebastian/diff)                < 2)
BuildRequires:  php-symfony3-console
BuildRequires:  php-symfony3-event-dispatcher
BuildRequires:  php-symfony3-filesystem
BuildRequires:  php-symfony3-finder
BuildRequires:  php-symfony3-options-resolver
BuildRequires:  php-symfony3-process
BuildRequires:  php-symfony3-stopwatch
BuildRequires:  php-symfony3-yaml
BuildRequires:  php-mbstring
BuildRequires:  php-xml
BuildRequires:  php-reflection
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-phar
BuildRequires:  php-spl
BuildRequires:  php-xml
# Missing dependency for Console
BuildRequires:  php-symfony3-debug
BuildRequires:  php-symfony3-debug
# From composer.json,     "require-dev": {
# NOTICE: listener disabled during test suite
#        "johnkary/phpunit-speedtrap": "^1.1 || ^2.0 || ^3.0",
#        "keradus/cli-executor": "^1.4",
#        "justinrainbow/json-schema": "^5.0",
#        "mikey179/vfsstream": "^1.6",
#        "php-coveralls/php-coveralls": "^2.4.1",
#        "php-cs-fixer/accessible-object": "^1.0",
#        "php-cs-fixer/phpunit-constraint-isidenticalstring": "^1.2",
#        "php-cs-fixer/phpunit-constraint-xmlmatchesxsd": "^1.2.1",
#        "phpspec/prophecy-phpunit": "^1.1 || ^2.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.20 || ^8.5.13 || ^9.5",
#        "phpunitgoodpractices/polyfill": "^1.5",
#        "phpunitgoodpractices/traits": "^1.9.1",
#        "sanmai/phpunit-legacy-adapter": "^6.4 || ^8.2.1",
#        "symfony/phpunit-bridge": "^5.2.1",
#        "symfony/yaml": "^3.0 || ^4.0 || ^5.0"
# ignored as test using it fail strangely
#BuildRequires: php-composer(keradus/cli-executor) <  2
#BuildRequires: php-composer(keradus/cli-executor) >= 1.0
BuildRequires:  (php-composer(justinrainbow/json-schema)                         >= 5.0   with php-composer(justinrainbow/json-schema)                         < 6)
BuildRequires:  (php-composer(mikey179/vfsstream)                                >= 1.6   with php-composer(mikey179/vfsstream)                                < 2)
BuildRequires:  (php-composer(php-cs-fixer/accessible-object)                    >= 1.0   with php-composer(php-cs-fixer/accessible-object)                    < 2)
BuildRequires:  (php-composer(php-cs-fixer/phpunit-constraint-isidenticalstring) >= 1.2   with php-composer(php-cs-fixer/phpunit-constraint-isidenticalstring) < 2)
BuildRequires:  (php-composer(php-cs-fixer/phpunit-constraint-xmlmatchesxsd)     >= 1.2.1 with php-composer(php-cs-fixer/phpunit-constraint-xmlmatchesxsd)     < 2)
BuildRequires:  (php-composer(phpspec/prophecy-phpunit)                          >= 2.0   with php-composer(phpspec/prophecy-phpunit)                          < 3)
BuildRequires:  (php-composer(phpunitgoodpractices/polyfill)                     >= 1.5   with php-composer(phpunitgoodpractices/polyfill)                     < 2)
BuildRequires:  (php-composer(phpunitgoodpractices/traits)                       >= 1.9.1 with php-composer(phpunitgoodpractices/traits)                       < 2)
BuildRequires:  (php-composer(sanmai/phpunit-legacy-adapter)                     >= 8.2.1 with php-composer(sanmai/phpunit-legacy-adapter)                     < 9)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9                                                        >= 9.4.4
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json,     "require": {
#        "php": "^5.6 || ^7.0 || ^8.0",
#        "ext-json": "*",
#        "ext-tokenizer": "*",
#        "composer/semver": "^1.4 || ^2.0 || ^3.0",
#        "composer/xdebug-handler": "^1.2",
#        "doctrine/annotations": "^1.2",
#        "php-cs-fixer/diff": "^1.3",
#        "symfony/console": "^3.4.43 || ^4.1.6 || ^5.0",
#        "symfony/event-dispatcher": "^3.0 || ^4.0 || ^5.0",
#        "symfony/filesystem": "^3.0 || ^4.0 || ^5.0",
#        "symfony/finder": "^3.0 || ^4.0 || ^5.0",
#        "symfony/options-resolver": "^3.0 || ^4.0",
#        "symfony/polyfill-php70": "^1.0",
#        "symfony/polyfill-php72": "^1.4",
#        "symfony/polyfill-xml": "^1.3",
#        "symfony/process": "^3.0 || ^4.0 || ^5.0",
#        "symfony/stopwatch": "^3.0 || ^4.0 || ^5.0"
Requires:       php(language) >= 7.2
Requires:       php-json
Requires:       php-tokenizer
Requires:       (php-composer(composer/semver)               >= 3.0 with php-composer(composer/semver)               < 4)
Requires:       (php-composer(composer/xdebug-handler)       >= 1.2 with php-composer(composer/xdebug-handler)       < 2)
Requires:       (php-composer(doctrine/annotations)          >= 1.2 with php-composer(doctrine/annotations)          < 2)
Requires:       (php-composer(sebastian/diff)                >= 1.4 with php-composer(sebastian/diff)                < 2)
Requires:       php-symfony3-console
Requires:       php-symfony3-event-dispatcher
Requires:       php-symfony3-filesystem
Requires:       php-symfony3-finder
Requires:       php-symfony3-options-resolver
Requires:       php-symfony3-process
Requires:       php-symfony3-stopwatch
# Missing dependency for Console
Requires:       php-symfony3-debug
# From composer.json, "suggest": {
#        "ext-dom": "For handling output formats in XML",
#        "ext-mbstring": "For handling non-UTF8 characters.",
#        "php-cs-fixer/phpunit-constraint-isidenticalstring": "For IsIdenticalString constraint.",
#        "php-cs-fixer/phpunit-constraint-xmlmatchesxsd": "For XmlMatchesXsd constraint.",
#        "symfony/polyfill-mbstring": "When enabling `ext-mbstring` is not possible."
Requires:       php-dom
Requires:       php-mbstring
Recommends:     php-composer(php-cs-fixer/phpunit-constraint-isidenticalstring)
Recommends:     php-composer(php-cs-fixer/phpunit-constraint-xmlmatchesxsd)
# From phpcompatinfo report for version 2.4.0
Requires:       php-cli
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-phar
Requires:       php-spl
Requires:       php-xml
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       bundled(php-cs-fixer/diff) = %{gh_diff_version}
Provides:       php-composer(friendsofphp/php-cs-fixer) = %{version}


%description
The PHP Coding Standards Fixer tool fixes most issues in your code when you
want to follow the PHP coding standards as defined in the PSR-1 and PSR-2
documents and many more.

If you are already using a linter to identify coding standards problems in
your code, you know that fixing them by hand is tedious, especially on large
projects. This tool does not only detect them, but also fixes them for you.


%prep
%setup -q -n %{gh_project}-%{gh_commit} -a1
%patch0 -p1 -b .rpm
mv diff-%{gh_diff_commit}/src src/diff

find src -name \*rpm -delete -print

# Fix version
sed -e '/VERSION/s/-DEV//' -i src/Console/Application.php

# from composer.json, "autoload" / "classmap"
TESTS="
  tests/Test/AbstractFixerTestCase.php
  tests/Test/AbstractIntegrationCaseFactory.php
  tests/Test/AbstractIntegrationTestCase.php
  tests/Test/Assert/AssertTokensTrait.php
  tests/Test/IntegrationCase.php
  tests/Test/IntegrationCaseFactory.php
  tests/Test/IntegrationCaseFactoryInterface.php
  tests/Test/InternalIntegrationCaseFactory.php
  tests/Test/IsIdenticalConstraint.php
  tests/Test/TokensWithObservedTransformers.php
  tests/TestCase.php
"
for i in $TESTS; do
  mkdir -p src/$(dirname $i)
  cp -p $i src/$i
done

# fix dev-tools path
sed -e 's:../../../ci:ci:' -i src/Console/Command/HelpCommand.php
cp -pr ci-integration.sh  src/Console/Command/

# tolerant because conditional definition in tests/TestCase.php
phpab --template fedora \
      --tolerant \
      --output src/autoload.php \
      src/tests src/diff

cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Autoload::addPsr4('PhpCsFixer\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Composer/Semver3/autoload.php',
    '%{php_home}/Composer/XdebugHandler/autoload.php',
    '%{php_home}/Doctrine/Common/Annotations/autoload.php',
    '%{php_home}/Symfony3/Component/Console/autoload.php',
    '%{php_home}/Symfony3/Component/EventDispatcher/autoload.php',
    '%{php_home}/Symfony3/Component/Filesystem/autoload.php',
    '%{php_home}/Symfony3/Component/Finder/autoload.php',
    '%{php_home}/Symfony3/Component/OptionsResolver/autoload.php',
    '%{php_home}/Symfony3/Component/Process/autoload.php',
    '%{php_home}/Symfony3/Component/Stopwatch/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/PhpCsFixer/PhpunitConstraintIsIdenticalString/autoload.php',
    '%{php_home}/PhpCsFixer/PhpunitConstraintXmlMatchesXsd/autoload.php',
]);
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/PhpCsFixer

: Command
install -Dpm755 %{name} %{buildroot}%{_bindir}/%{name}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Force version for local, when both versions are available
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/org/bovigo/vfs/autoload.php',
    '%{php_home}/JsonSchema5/autoload.php',
    '%{php_home}/PhpCsFixer/AccessibleObject/autoload.php',
    '%{php_home}/Prophecy/PhpUnit/autoload.php',
    '%{php_home}/LegacyPHPUnit/autoload.php',
    '%{php_home}/PHPUnitGoodPractices/Polyfill/autoload.php',
    '%{buildroot}%{php_home}/PhpCsFixer/autoload.php',
    '%{php_home}/Symfony3/Component/Yaml/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('PhpCsFixer\\Tests\\', dirname(__DIR__) . '/tests');
EOF

# test using keradus/cli-executor
rm tests/Smoke/CiIntegrationTest.php
rm tests/Smoke/StdinTest.php
rm tests/Smoke/InstallViaComposerTest.php
# strange failure
rm tests/Fixtures/Integration/priority/combine_consecutive_issets,no_singleline_whitespace_before_semicolons.test
# test checking documentation
rm tests/AutoReview/DocumentationTest.php

# Disable listener
sed -e '/<listeners>/,/<\/listeners>/d' phpunit.xml.dist >phpunit.xml
sed -e '/ExpectDeprecationTrait/d' \
    -i tests/Fixer/CastNotation/LowercaseCastFixerTest.php tests/Fixer/CastNotation/ShortScalarCastFixerTest.php
# skip as rely on composer autoloader for phpunit
rm tests/Fixer/PhpUnit/PhpUnitNamespacedFixerTest.php
rm tests/AutoReview/ProjectCodeTest.php

# Redirect to buildroot
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' -i %{name}

ret=0
# skip testFix74Deprecated as we don't use symfony/phpunit-bridge
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d memory_limit=2G ${2:-%{_bindir}/phpunit9} \
       --filter '^((?!(testFixerContainsAllPhpunitStaticMethodsInItsList|testFix74Deprecated|testFixersPriorityPairsHaveIntegrationTest|testThereAreNoExtraFiles|testFixersDocumentationIndexFileIsUpToDate|testInheritance|testFixerDefinitions)).)*$' \
      || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{php_home}/PhpCsFixer
%{_bindir}/%{name}


%changelog
* Wed Apr  7 2021 Remi Collet <remi@remirepo.net> - 2.18.5-1
- update to 2.18.5

* Mon Mar 22 2021 Remi Collet <remi@remirepo.net> - 2.18.4-1
- update to 2.18.4

* Thu Mar 11 2021 Remi Collet <remi@remirepo.net> - 2.18.3-1
- update to 2.18.3

* Tue Mar  2 2021 Remi Collet <remi@remirepo.net> - 2.18.2-1
- update to 2.18.2
- switch to phpunit9
  with phpspec/prophecy-phpunit and sanmai/phpunit-legacy-adapter

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Remi Collet <remi@remirepo.net> - 2.17.1-1
- update to 2.17.1

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0

* Wed Oct 28 2020 Remi Collet <remi@remirepo.net> - 2.16.7-1
- update to 2.16.7
- raise dependency on composer/semver v3

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 2.16.4-3
- raise dependency on PHP 7.2
- drop dependency on symfony-polyfill

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 2.16.4-1
- update to 2.16.4

* Thu Apr 16 2020 Remi Collet <remi@remirepo.net> - 2.16.3-1
- update to 2.16.3

* Mon Apr 13 2020 Remi Collet <remi@remirepo.net> - 2.16.2-1
- update to 2.16.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Remi Collet <remi@remirepo.net> - 2.16.1-1
- update to 2.16.1

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0

* Sun Sep  1 2019 Remi Collet <remi@remirepo.net> - 2.15.3-1
- update to 2.15.3

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.15.2-1
- update to 2.15.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun  4 2019 Remi Collet <remi@remirepo.net> - 2.15.1-1
- update to 2.15.1

* Mon May  6 2019 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0
- add patch for libpcre2 10.33 from
  https://github.com/FriendsOfPHP/PHP-CS-Fixer/pull/4406

* Mon Feb 18 2019 Remi Collet <remi@remirepo.net> - 2.14.2-1
- update to 2.14.2 (no change)

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 2.14.1-1
- update to 2.14.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan  5 2019 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0

* Wed Jan  2 2019 Remi Collet <remi@remirepo.net> - 2.13.2-1
- update to 2.13.2

* Tue Dec 11 2018 Remi Collet <remi@remirepo.net> - 2.13.1-2
- skip 1 test failing with PHPUnit 7.5

* Sun Oct 21 2018 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1

* Fri Aug 24 2018 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 2.12.3-1
- update to 2.12.3
- raise dependency on composer/xdebug-handler 1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul  6 2018 Remi Collet <remi@remirepo.net> - 2.12.2-1
- update to 2.12.2

* Mon Jun 11 2018 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0
- add dependency on composer/xdebug-handler
- add dependency on php-cs-fixer/phpunit-constraint-isidenticalstring
- add dependency on php-cs-fixer/phpunit-constraint-xmlmatchesxsd

* Thu Mar 22 2018 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Wed Mar 21 2018 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- use phpunit7 on F28+

* Thu Mar  8 2018 Remi Collet <remi@remirepo.net> - 2.10.4-1
- update to 2.10.4

* Fri Feb 23 2018 Remi Collet <remi@remirepo.net> - 2.10.3-1
- Update to 2.10.3
- drop dependency on gecko-packages/gecko-php-unit
- update bundled php-cs-fixer/diff to 1.3.0

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 2.10.2-1
- Update to 2.10.2
- use range dependencies

* Thu Jan 11 2018 Remi Collet <remi@remirepo.net> - 2.10.0-1
- Update to 2.10.0

* Thu Dec 28 2017 Remi Collet <remi@remirepo.net> - 2.9.0-2
- mikey179/vfsStream only required at builtime

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 2.9.0-1
- Update to 2.9.0

* Mon Nov 27 2017 Remi Collet <remi@remirepo.net> - 2.8.3-1
- Update to 2.8.3
- open https://github.com/FriendsOfPHP/PHP-CS-Fixer/issues/3279
  bad tag for 2.8.3

* Mon Nov 20 2017 Remi Collet <remi@remirepo.net> - 2.8.2-1
- Update to 2.8.2

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Tue Nov  7 2017 Remi Collet <remi@remirepo.net> - 2.8.0-2
- fix FTBFS from Koschei using symfony package names

* Fri Nov  3 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0

* Mon Oct  2 2017 Remi Collet <remi@remirepo.net> - 2.7.1-1
- Update to 2.7.1
- drop dependency on sebastian/diff, bundle fork instead

* Tue Sep 12 2017 Remi Collet <remi@remirepo.net> - 2.6.0-1
- Update to 2.6.0
- add dependency on composer/semver

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 2.5.0-1
- Update to 2.5.0
- add dependency on php-cs-fixer/accessible-object
- raise dependency on symfony 3.2

* Thu Aug  3 2017 Remi Collet <remi@remirepo.net> - 2.4.0-1
- Update to 2.4.0
- add dependency on symfony/polyfill-php72

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Remi Collet <remi@remirepo.net> - 2.3.2-1
- Update to 2.3.2
- add dependency on gecko-packages/gecko-php-unit

* Tue May  9 2017 Remi Collet <remi@remirepo.net> - 2.3.1-1
- Update to 2.3.1
- raise dependency on PHP 5.6
- raise dependency on Symfony 3

* Wed Apr 26 2017 Remi Collet <remi@remirepo.net> - 2.2.3-1
- Update to 2.2.3

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 2.2.2-1
- Update to 2.2.2
- raise dependency on sebastian/diff >= 1.4

* Mon Apr 10 2017 Remi Collet <remi@remirepo.net> - 2.2.1-1
- Update to 2.2.1

* Sat Apr  1 2017 Remi Collet <remi@remirepo.net> - 2.2.0-1
- Update to 2.2.0
- add dependency on doctrine/annotations
- add dependency on symfony/options-resolver
- raise dependency on symfony 2.6
- fix autoloader to allow Symfony 3

* Fri Mar 31 2017 Remi Collet <remi@remirepo.net> - 2.1.3-1
- Update to 2.1.3
- add dependency on php-mbstring

* Wed Mar 15 2017 Remi Collet <remi@remirepo.net> - 2.1.2-1
- Update to 2.1.2

* Sat Feb 11 2017 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- add dependency on symfony/polyfill-php55 (for EPEL-7)

* Thu Feb  9 2017 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0

* Tue Nov 29 2016 Remi Collet <remi@fedoraproject.org> - 1.13.0-1
- update to 1.13.0

* Tue Nov 15 2016 Remi Collet <remi@fedoraproject.org> - 1.12.4-1
- update to 1.12.4

* Sun Oct 30 2016 Remi Collet <remi@fedoraproject.org> - 1.12.3-1
- update to 1.12.3
- switch from symfony/class-loader to fedora/autoloader

* Tue Sep 27 2016 Remi Collet <remi@fedoraproject.org> - 1.12.2-1
- update to 1.12.2

* Fri Sep  9 2016 Remi Collet <remi@fedoraproject.org> - 1.12.1-1
- initial package, version 1.12.1

