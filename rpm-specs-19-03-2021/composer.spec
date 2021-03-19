# remirepo/fedora spec file for composer
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    a5a5632da0b1c2d6fa9a3b65f1f4e90d1f04abb9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_branch    2.0-dev
%global gh_owner     composer
%global gh_project   composer
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%global api_version  2.0.0
%global run_version  2.0.0

%global upstream_version 2.0.11
#global upstream_prever  RC2
#global upstream_lower   rc2

%global symfony_prefix php-symfony4
%global symfony_path   %{_datadir}/php/Symfony4
%global symfony_min    4.4

%global _phpunit       %{_bindir}/phpunit9

Name:           composer
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:        1%{?dist}
Summary:        Dependency Manager for PHP

License:        MIT
URL:            https://getcomposer.org/
Source0:        %{gh_project}-%{upstream_version}%{?upstream_prever}-%{gh_short}.tgz
# Profile scripts
Source3:        %{name}.sh
Source4:        %{name}.csh
# Get a git snapshot to retrieve the test suite
Source5:        makesrc.sh

# Use our autoloader, resources path, fix for tests
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php-cli
%if %{with_tests}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(composer/ca-bundle)        >= 1.0    with  php-composer(composer/ca-bundle)        <  2)
BuildRequires:  (php-composer(composer/semver)           >= 3.0    with  php-composer(composer/semver)           <  4)
BuildRequires:  (php-composer(composer/spdx-licenses)    >= 1.2    with  php-composer(composer/spdx-licenses)    <  2)
BuildRequires:  (php-composer(composer/xdebug-handler)   >= 1.1    with  php-composer(composer/xdebug-handler)   <  2)
BuildRequires:  (php-composer(seld/jsonlint)             >= 1.4    with  php-composer(seld/jsonlint)             <  2)
BuildRequires:  (php-composer(seld/phar-utils)           >= 1.0    with  php-composer(seld/phar-utils)           <  2)
BuildRequires:  (php-composer(psr/log)                   >= 1.0    with  php-composer(psr/log)                   <  2)
BuildRequires:  (php-composer(justinrainbow/json-schema) >= 5.2.10 with  php-composer(justinrainbow/json-schema) <  6)
BuildRequires:  (php-composer(react/promise)             >= 2.7    with  php-composer(react/promise)             <  3)
%else
BuildRequires:  php-composer-ca-bundle
BuildRequires:  php-composer-semver3
BuildRequires:  php-composer-spdx-licenses               >= 1.2
BuildRequires:  php-composer-xdebug-handler              >= 1.1
BuildRequires:  php-jsonlint                             >= 1.4
BuildRequires:  php-seld-phar-utils
BuildRequires:  php-PsrLog
BuildRequires:  php-justinrainbow-json-schema5           >= 5.2.10
BuildRequires:  php-react-promise                        >= 2.7
%endif
BuildRequires:  %{symfony_prefix}-console    >= %{symfony_min}
BuildRequires:  %{symfony_prefix}-finder     >= %{symfony_min}
BuildRequires:  %{symfony_prefix}-filesystem >= %{symfony_min}
BuildRequires:  %{symfony_prefix}-process    >= %{symfony_min}
BuildRequires:  php-zip
# From composer.json, "require-dev": {
#        "symfony/phpunit-bridge": "^4.2 || ^5.0",
#        "phpspec/prophecy": "^1.10"
BuildRequires:  %{_phpunit}
# For autoloader
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-seld-phar-utils >= 1.1
BuildRequires:  php-PsrLog          >= 1.1
%endif

# From composer.json, "require": {
#        "php": "^5.3.2 || ^7.0",
#        "composer/ca-bundle": "^1.0",
#        "composer/semver": "^3.0",
#        "composer/spdx-licenses": "^1.2",
#        "composer/xdebug-handler": "^1.1",
#        "justinrainbow/json-schema": "^5.2.10",
#        "psr/log": "^1.0"
#        "seld/jsonlint": "~1.4",
#        "seld/phar-utils": "^1.0",
#        "symfony/console": "^2.8.52 || ^3.4.35 || ^4.4 || ^5.0",
#        "symfony/filesystem": "^2.8.52 || ^3.4.35 || ^4.4 || ^5.0",
#        "symfony/finder": "^2.8.52 || ^3.4.35 || ^4.4 || ^5.0",
#        "symfony/process": "^^2.8.52 || ^3.4.35 || ^4.4 || ^5.0",
#        "react/promise": "^1.2 || ^2.7"
Requires:       php(language)                           >= 5.3.2
Requires:       php-cli
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(composer/ca-bundle)        >= 1.0    with  php-composer(composer/ca-bundle)        <  2)
Requires:       (php-composer(composer/semver)           >= 3.0    with  php-composer(composer/semver)           <  4)
Requires:       (php-composer(composer/spdx-licenses)    >= 1.2    with  php-composer(composer/spdx-licenses)    <  2)
Requires:       (php-composer(composer/xdebug-handler)   >= 1.1    with  php-composer(composer/xdebug-handler)   <  2)
Requires:       (php-composer(seld/jsonlint)             >= 1.4    with  php-composer(seld/jsonlint)             <  2)
Requires:       (php-composer(seld/phar-utils)           >= 1.0    with  php-composer(seld/phar-utils)           <  2)
Requires:       (php-composer(psr/log)                   >= 1.0    with  php-composer(psr/log)                   <  2)
Requires:       (php-composer(justinrainbow/json-schema) >= 5.2.10 with  php-composer(justinrainbow/json-schema) <  6)
Requires:       (php-composer(react/promise)             >= 2.7    with  php-composer(react/promise)             <  3)
%else
Requires:       php-composer-ca-bundle
Requires:       php-composer-semver3
Requires:       php-composer-spdx-licenses               >= 1.2
Requires:       php-composer-xdebug-handler              >= 1.1
Requires:       php-jsonlint                             >= 1.4
Requires:       php-seld-phar-utils
Requires:       php-PsrLog
Requires:       php-justinrainbow-json-schema5           >= 5.2.10
Requires:       php-react-promise                        >= 2.7
%endif
Requires:       %{symfony_prefix}-console    >= %{symfony_min}
Requires:       %{symfony_prefix}-finder     >= %{symfony_min}
Requires:       %{symfony_prefix}-process    >= %{symfony_min}
Requires:       %{symfony_prefix}-filesystem >= %{symfony_min}
# From composer.json, suggest
#        "ext-openssl": "Enabling the openssl extension allows you to access https URLs for repositories and packages",
#        "ext-zip": "Enabling the zip extension allows you to unzip archives",
#        "ext-zlib": "Allow gzip compression of HTTP requests"
Requires:       php-openssl
Requires:       php-zip
Requires:       php-zlib
# For our autoloader
Requires:       php-composer(fedora/autoloader)
Requires:       php-seld-phar-utils >= 1.1
Requires:       php-PsrLog          >= 1.1
# From phpcompatinfo for version 2.0.0
Requires:       php-ctype
Requires:       php-curl
Requires:       php-date
Requires:       php-filter
Requires:       php-hash
Requires:       php-iconv
Requires:       php-intl
Requires:       php-json
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-phar
Requires:       php-posix
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-xsl
Requires:       php-zlib

# Composer library
Provides:       php-composer(composer/composer) = %{version}
# Special internal for Plugin API
Provides:       php-composer(composer-plugin-api) = %{api_version}
Provides:       php-composer(composer-runtime-api) = %{run_version}


%description
Composer helps you declare, manage and install dependencies of PHP projects,
ensuring you have the right stack everywhere.

Documentation: https://getcomposer.org/doc/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
find . -name \*.rpm -delete -print

if grep -r '\.\./res'; then
	: Patch need to fixed
	exit 1
fi

phpab --template fedora --output src/Composer/autoload.php src/Composer
cat << 'EOF' | tee -a src/Composer/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{symfony_path}/Component/Console/autoload.php',
    '%{symfony_path}/Component/Finder/autoload.php',
    '%{symfony_path}/Component/Process/autoload.php',
    '%{symfony_path}/Component/Filesystem/autoload.php',
    '%{_datadir}/php/Seld/JsonLint/autoload.php',
    '%{_datadir}/php/Seld/PharUtils/autoload.php',
    '%{_datadir}/php/Composer/CaBundle/autoload.php',
    '%{_datadir}/php/Composer/Spdx/autoload.php',
    '%{_datadir}/php/Composer/Semver3/autoload.php',
    '%{_datadir}/php/Composer/XdebugHandler/autoload.php',
    '%{_datadir}/php/Psr/Log/autoload.php',
    '%{_datadir}/php/JsonSchema5/autoload.php',
    '%{_datadir}/php/React/Promise/autoload.php',
]);
EOF

cat << 'EOF' | tee tests/bootstrap.php
<?php
require 'Composer/autoload.php';
\Fedora\Autoloader\Autoload::addPsr0('Composer\\Test\\', __DIR__ . '/');
EOF

rm src/bootstrap.php


: fix reported version
%if 0%{?gh_date}
DATE=%{gh_date}
DATE=${DATE:0:4}-${DATE:4:2}-${DATE:6:2}
sed -e '/VERSION/s/@package_version@/%{gh_commit}/' \
    -e '/BRANCH_ALIAS_VERSION/s/@package_branch_alias_version@/%{gh_branch}/' \
    -e "/RELEASE_DATE/s/@release_date@/$DATE/" \
    -i src/Composer/Composer.php
%else
sed -e '/BRANCH_ALIAS_VERSION/s/@package_branch_alias_version@//' \
    -i src/Composer/Composer.php
%endif

: check Plugin API version
php -r '
namespace Composer;
include "src/Composer/autoload.php";
if (version_compare(Plugin\PluginInterface::PLUGIN_API_VERSION, "%{api_version}")) {
  printf("Plugin API version is %s, expected %s\n", Plugin\PluginInterface::PLUGIN_API_VERSION, "%{api_version}");
  exit(1);
}
if (version_compare(Composer::RUNTIME_API_VERSION, "%{run_version}")) {
  printf("Runtime API version is %s, expected %s\n", Composer::RUNTIME_API_VERSION, "%{run_version}");
  exit(1);
}'


%build
# Nothing


%install
: Profile scripts
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d/

: Library
mkdir -p     %{buildroot}%{_datadir}/php
cp -pr src/* %{buildroot}%{_datadir}/php

: Resources
mkdir -p       %{buildroot}%{_datadir}/%{name}
cp -pr res     %{buildroot}%{_datadir}/%{name}/res
cp -p  LICENSE %{buildroot}%{_datadir}/%{name}/LICENSE

ln -sf %{_datadir}/%{name}/LICENSE LICENSE

: Command
install -Dpm 755 bin/%{name} %{buildroot}%{_bindir}/%{name}


%check
%if %{with_tests}
: Online tests
rm tests/Composer/Test/Util/RemoteFilesystemTest.php

: Ensure not used
rm -rf res

: Run test suite
export BUILDROOT=%{buildroot}

FILTER="--filter '^((?!(testIntegration)).)*$'"

# Adapt for phunit9
find tests \
  -name \*.php \
  -exec sed -e '/function setUpBeforeClass(/s/$/:void/' \
            -e '/function tearDownAfterClass(/s/$/:void/' \
            -e '/function setUp(/s/$/:void/' \
            -e '/function tearDown(/s/$/:void/' \
            -i {} \;

# testIntegration may hang on local build
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d memory_limit=1G %{_phpunit} \
      $FILTER \
      --include-path %{buildroot}%{_datadir}/php  || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md doc
%doc composer.json
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*
%{_bindir}/%{name}
%{_datadir}/php/Composer
%{_datadir}/%{name}


%changelog
* Wed Feb 24 2021 Remi Collet <remi@remirepo.net> - 2.0.11-1
- update to 2.0.11

* Tue Feb 23 2021 Remi Collet <remi@remirepo.net> - 2.0.10-1
- update to 2.0.10

* Thu Jan 28 2021 Remi Collet <remi@remirepo.net> - 2.0.9-1
- update to 2.0.9
- switch to Symfony 4
- switch to phpunit9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec  4 2020 Remi Collet <remi@remirepo.net> - 2.0.8-1
- update to 2.0.8

* Sat Nov 14 2020 Remi Collet <remi@remirepo.net> - 2.0.7-1
- update to 2.0.7

* Sun Nov  8 2020 Remi Collet <remi@remirepo.net> - 2.0.6-1
- update to 2.0.6

* Sat Oct 31 2020 Remi Collet <remi@remirepo.net> - 2.0.4-1
- update to 2.0.4

* Thu Oct 29 2020 Remi Collet <remi@remirepo.net> - 2.0.3-1
- update to 2.0.3

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2
- raise dependency on composer/semver 3
- add dependency on react/promise 2.7

* Tue Oct 13 2020 Remi Collet <remi@remirepo.net> - 1.10.15-1
- update to 1.10.15

* Wed Sep  9 2020 Remi Collet <remi@remirepo.net> - 1.10.13-1
- update to 1.10.13

* Wed Sep  9 2020 Remi Collet <remi@remirepo.net> - 1.10.12-1
- update to 1.10.12

* Tue Aug  4 2020 Remi Collet <remi@remirepo.net> - 1.10.10-1
- update to 1.10.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Remi Collet <remi@remirepo.net> - 1.10.9-1
- update to 1.10.9

* Thu Jun 25 2020 Remi Collet <remi@remirepo.net> - 1.10.8-1
- update to 1.10.8

* Wed Jun  3 2020 Remi Collet <remi@remirepo.net> - 1.10.7-1
- update to 1.10.7
- raise dependency on justinrainbow/json-schema 5.2.10

* Wed May  6 2020 Remi Collet <remi@remirepo.net> - 1.10.6-1
- update to 1.10.6
- provide php-composer(composer-runtime-api)

* Fri Apr 10 2020 Remi Collet <remi@remirepo.net> - 1.10.5-1
- update to 1.10.5

* Thu Apr  9 2020 Remi Collet <remi@remirepo.net> - 1.10.4-1
- update to 1.10.4

* Sat Mar 14 2020 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1

* Wed Mar 11 2020 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Tue Feb  4 2020 Remi Collet <remi@remirepo.net> - 1.9.3-1
- update to 1.9.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.9.2-1
- update to 1.9.2

* Sat Nov  2 2019 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1

* Wed Oct  9 2019 Remi Collet <remi@remirepo.net> - 1.9.0-2
- add upstream patch for PHP 7.4

* Sat Aug  3 2019 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Remi Collet <remi@remirepo.net> - 1.8.6-1
- update to 1.8.6

* Wed Apr 10 2019 Remi Collet <remi@remirepo.net> - 1.8.5-1
- update to 1.8.5

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 1.8.4-1
- update to 1.8.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Remi Collet <remi@remirepo.net> - 1.8.3-1
- update to 1.8.3

* Mon Dec  3 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Fri Nov  2 2018 Remi Collet <remi@remirepo.net> - 1.7.3-1
- update to 1.7.3

* Fri Aug 17 2018 Remi Collet <remi@remirepo.net> - 1.7.2-1
- update to 1.7.2
- drop dependency on seld/cli-prompt
- add dependency on composer/xdebug-handler

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May  4 2018 Remi Collet <remi@remirepo.net> - 1.6.5-1
- update to 1.6.5

* Mon Apr 16 2018 Remi Collet <remi@remirepo.net> - 1.6.4-1
- update to 1.6.4

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 1.6.3-4
- switch to Symfony2 only

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 1.6.3-2
- undefine __brp_mangle_shebangs (F28)

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 1.6.3-1
- Update to 1.6.3

* Sun Jan  7 2018 Remi Collet <remi@remirepo.net> - 1.6.2-1
- Update to 1.6.2

* Thu Jan  4 2018 Remi Collet <remi@remirepo.net> - 1.6.1-1
- Update to 1.6.1

* Thu Jan  4 2018 Remi Collet <remi@remirepo.net> - 1.6.0-2
- open https://github.com/composer/composer/pull/6974
  Fix dependency on composer/spdx-licenses
- raise dependency on composer/spdx-licenses 1.2

* Mon Dec 18 2017 Remi Collet <remi@remirepo.net> - 1.5.6-1
- Update to 1.5.6
- switch to symfony package names

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 1.5.5-1
- Update to 1.5.5

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 1.5.4-1
- Update to 1.5.4

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 1.5.3-1
- Update to 1.5.3

* Mon Sep 11 2017 Remi Collet <remi@remirepo.net> - 1.5.2-1
- Update to 1.5.2

* Wed Aug  9 2017 Remi Collet <remi@remirepo.net> - 1.5.1-1
- Update to 1.5.1

* Tue Aug  8 2017 Remi Collet <remi@remirepo.net> - 1.5.0-1
- Update to 1.5.0

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 1.4.3-1
- Update to 1.4.3
- ignore 2 failed tests related to BC break in symfony

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 1.4.2-2
- Update to 1.4.2
- fix autoloader to allow symfony 2 and 3
- raise dependency on justinrainbow/json-schema v5
- open https://github.com/composer/composer/pull/6435 - fix tests

* Fri Mar 10 2017 Remi Collet <remi@remirepo.net> - 1.4.1-1
- Update to 1.4.1

* Wed Mar  8 2017 Remi Collet <remi@remirepo.net> - 1.4.0-1
- Update to 1.4.0
- raise dependency on justinrainbow/json-schema version 3 to 5

* Wed Mar  8 2017 Remi Collet <remi@remirepo.net> - 1.3.3-1
- Update to 1.3.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to 1.3.2

* Sat Jan  7 2017 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1

* Sat Dec 24 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0
- raise dependency on symfony 2.7
- allow justinrainbow/json-schema 4

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 1.2.4-2
- fix BR for json-schema, FTBFS from Koschei

* Wed Dec  7 2016 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Thu Nov 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-2
- add profile scripts so globally installed commands
  will be found in default user path #1394577

* Thu Nov  3 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Fri Oct 21 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-2
- switch from symfony/class-loader to fedora/autoloader

* Mon Sep 12 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Tue Jul 19 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- switch to justinrainbow/json-schema v2

* Sun Jun 26 2016 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- update to 1.1.3

* Wed Jun  1 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- update to 1.1.2

* Tue May 31 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- ensure justinrainbow/json-schema v1 is used for the build

* Tue May 17 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1
- add dependency on composer/ca-bundle
- add dependency on psr/log
- bump composer-plugin-api to 1.1.0
- drop dependency on ca-certificates

* Sat Apr 30 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- update to 1.0.3

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- add dependency on ca-certificates
- fix patch for RPM path

* Tue Apr  5 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Tue Mar 29 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.22.beta2
- update to 1.0.0beta2

* Fri Mar  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.21.beta1
- update to 1.0.0beta1

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.20.201602git4c0e163
- new snapshot
- raise dependency on justinrainbow/json-schema ^1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.19.20160106git64b0d72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.18.20160106git64b0d72
- add patch for json-schema 1.6, FTBFS detected by Koschei
  open https://github.com/composer/composer/pull/4756
- new snapshot
- raise dependency on seld/jsonlint ^1.4

* Thu Jan  7 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.16.alpha1
- remove duplicated register in autoloader

* Sat Nov 14 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.15.alpha1
- update to 1.0.0alpha11

* Mon Nov  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.14.20151030git5a5088e
- new snapshot
- allow symfony 3

* Wed Oct 14 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.13.20151013gita54f84f
- new snapshot
- use autoloader from all dependencies

* Sun Oct 11 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.12.20151007git7a9eb02
- new snapshot
- provide php-composer(composer-plugin-api)
- don't check version in diagnose command
- add dependency on composer/semver
- add dependency on symfony/filesystem

* Tue Sep  8 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.9.20150907git9f6fdfd
- new snapshot
- add LICENSE in application data, as used by the code

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.8.20150804gitc83650f
- new snapshot

* Tue Jul 21 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.8.20150720git00c2679
- new snapshot
- add dependency on composer/spdx-licenses

* Thu Jul 16 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.7.20150714git92faf1c
- new snapshot
- raise dependency on justinrainbow/json-schema 1.4.4

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.6.20150626git943107c
- new snapshot
- review autoloader

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150620gitd0ff016
- new snapshot
- add missing BR on php-zip
- open https://github.com/composer/composer/pull/4169 for online test

* Mon Jun 15 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150614git8e9659b
- new snapshot

* Sun Jun  7 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150605git9fb2d4f
- new snapshot

* Tue Jun  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150531git0ec86be
- new snapshot

* Tue May 26 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150525git69210d5
- new snapshot
- ensure /usr/share/php is in include_path (for SCL)

* Wed May 13 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.4.20150511gitbc45d91
- new snapshot

* Mon May  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.4.20150503git42a9561
- new snapshot
- add dependencies on seld/phar-utils and seld/cli-prompt

* Mon Apr 27 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150426git1cb427f
- new snapshot

* Fri Apr 17 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150415git921b3a0
- new snapshot
- raise dependency on justinrainbow/json-schema ~1.4
- keep upstream shebang with /usr/bin/env (for SCL)

* Thu Apr  9 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150408git4d134ce
- new snapshot
- lower dependency on justinrainbow/json-schema ~1.3

* Tue Mar 24 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150324gitc5cd184
- new snapshot
- raise dependency on justinrainbow/json-schema ~1.4

* Thu Mar 19 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20150316git829199c
- new snapshot

* Wed Mar  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20150302giteadc167
- new snapshot

* Sat Feb 28 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20150227git45b1f35
- new snapshot

* Thu Feb 26 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.20150225gite5985a9
- Initial package
