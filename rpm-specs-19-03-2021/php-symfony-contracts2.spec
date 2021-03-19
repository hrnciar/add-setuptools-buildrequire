# remirepo/fedora spec file for php-symfony-contracts2
#
# Copyright (c) 2019-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    f7783bdec14b06c323d30a5f74ba70a17ec0ce81
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     symfony
%global gh_project   contracts
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Symfony
%global ns_project   Contracts
%global php_home     %{_datadir}/php

%global major        2


Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.3.1
Release:        2%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        A set of abstractions extracted out of the Symfony, version %{major}

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.2.5
BuildRequires:  php-reflection
BuildRequires:  php-intl
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-zlib
# From composer.json, "require-dev": {
#        "symfony/polyfill-intl-idn": "^1.10"
BuildRequires: (php-composer(psr/cache)            >= 1.0  with php-composer(psr/cache)            < 2)
BuildRequires: (php-composer(psr/container)        >= 1.0  with php-composer(psr/container)        < 2)
BuildRequires: (php-composer(psr/event-dispatcher) >= 1.0  with php-composer(psr/event-dispatcher) < 2)
%if 0%{?fedora} >= 31 || 0%{?rhel} >=9
%global phpunit %{_bindir}/phpunit9
%else
%global phpunit %{_bindir}/phpunit8
%endif
BuildRequires: %{phpunit}
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=7.2.5"
#        "psr/cache": "^1.0",
#        "psr/container": "^1.0",
#        "psr/event-dispatcher": "^1.0"
Requires:       php(language) >= 7.2.5
# From composer.json, "suggest": {
#        "symfony/cache-implementation": "",
#        "symfony/event-dispatcher-implementation": "",
#        "symfony/http-client-implementation": "",
#        "symfony/service-implementation": "",
#        "symfony/translation-implementation": ""
Requires:      (php-composer(psr/cache)            >= 1.0  with php-composer(psr/cache)            < 2)
Requires:      (php-composer(psr/container)        >= 1.0  with php-composer(psr/container)        < 2)
Requires:      (php-composer(psr/event-dispatcher) >= 1.0  with php-composer(psr/event-dispatcher) < 2)
# From phpcompatinfo report for version 2.3.1
Requires:       php-reflection
Requires:       php-intl
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-zlib
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project})              = %{version}
Provides:       php-composer(%{pk_vendor}/cache-contracts)            = %{version}
Provides:       php-composer(%{pk_vendor}/event-dispatcher-contracts) = %{version}
Provides:       php-composer(%{pk_vendor}/http-client-contracts)      = %{version}
Provides:       php-composer(%{pk_vendor}/service-contracts)          = %{version}
Provides:       php-composer(%{pk_vendor}/translation-contracts)      = %{version}
Provides:       php-composer(%{pk_vendor}/deprecation-contracts)      = %{version}


%description
A set of abstractions extracted out of the Symfony components.

Can be used to build on semantics that the Symfony components
proved useful - and that already have battle tested implementations.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

# sub CHANGELOG and README only refer to main file
rm */*.md

for i in */composer.json */LICENSE
do
  mv $i $(dirname $i)_$(basename $i)
done


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Psr/Cache/autoload.php',
    '%{php_home}/Psr/Container/autoload.php',
    '%{php_home}/Psr/EventDispatcher/autoload.php',
    __DIR__ . '/Deprecation/function.php',
]);
AUTOLOAD


%install
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
for i in autoload.php Cache EventDispatcher HttpClient Service Translation Deprecation
do
  rm -f $i/.gitignore
  cp -pr $i %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/$i
done


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF

ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --no-coverage \
      --verbose
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license *LICENSE
%doc *composer.json
%doc *.md
%dir %{php_home}/%{ns_vendor}/
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Remi Collet <remi@remirepo.net> - 2.3.1-1
- update to 2.3.1
- rename to php-symfony-contracts2
- install in /usr/share/php/Symfony/Contracts2
- raise dependency on PHP 7.2.5
- add symfony/deprecation-contracts

* Wed Sep  9 2020 Remi Collet <remi@remirepo.net> - 1.1.10-1
- update to 1.1.10

* Thu Nov 21 2019 Remi Collet <remi@remirepo.net> - 1.1.8-1
- update to 1.1.8
- psr/cache and psr/container are mandatory

* Tue Nov  5 2019 Remi Collet <remi@remirepo.net> - 1.1.7-1
- update to 1.1.7
- add missing EventDispatcher and HttpClient directories
- add weak dependency on psr/event-dispatcher

* Thu Jun  6 2019 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2 (no change)

* Tue May 28 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Thu May 16 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Mon Jan  7 2019 Remi Collet <remi@remirepo.net> - 1.0.2-1
- initial package, version 1.0.2
