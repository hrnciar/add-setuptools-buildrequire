# remirepo/Fedora spec file for php-laminas-permissions-acl
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    7af6463695d76dbf25c6b03e6ebb792c8f1ab67e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-permissions-acl
%global zf_name      zend-permissions-acl
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Permissions
%global subproj      Acl
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.8.0
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library}/%{subproj} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-servicemanager": "^3.0.3",
#        "phpunit/phpunit": "^9.5"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 7.3
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-servicemanager": "To support Laminas\\Permissions\\Acl\\Assertion\\AssertionManager plugin manager usage"
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.7.1
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl

Obsoletes:      php-ZendFramework2-Permissions-%{library} < 2.5
Provides:       php-ZendFramework2-Permissions-%{library} = %{version}
# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.7.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Provides a lightweight and flexible access control list (ACL)
implementation for privileges management.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(__DIR__))) . '/%{namespace}/%{library}/%{subproj}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/%{library}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}/%{subproj}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\%{subproj}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\Acl") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
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
%dir %{php_home}/Zend/%{library}
     %{php_home}/Zend/%{library}/%{subproj}
%dir %{php_home}/%{namespace}/%{library}
     %{php_home}/%{namespace}/%{library}/%{subproj}


%changelog
* Fri Apr  9 2021 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- raise dependency on PHP 7.3
- raise dependency on laminas-servicemanager 3.0.3
- switch to phpunit9

* Thu Mar 25 2021 Remi Collet <remi@remirepo.net> - 2.7.2-3
- switch to phpunit8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.7.1-1
- switch to Laminas

* Tue Jun 25 2019 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 2.7.0-2
- update to 2.7.0
- raise dependency on PHP 5.6
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.6.0-4
- switch from zend-loader to fedora/autoloader

* Thu Feb  4 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
