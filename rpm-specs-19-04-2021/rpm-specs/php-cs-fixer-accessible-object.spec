# remirepo/fedora spec file for php-cs-fixer-accessible-object
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    a08d2ad0ed28555cca941aa197610db8b45599bd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     PHP-CS-Fixer
%global gh_project   AccessibleObject
%global pk_vendor    php-cs-fixer
%global pk_project   accessible-object
%global ns_vendor    PhpCsFixer
%global ns_project   AccessibleObject
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           %{pk_vendor}-%{pk_project}
Version:        1.1.0
Release:        2%{?dist}
Summary:        A library to reveal object internals

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
# as we use modern phpunit
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "symfony/phpunit-bridge": "^5.1"
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
%else
%global phpunit %{_bindir}/phpunit8
%endif
BuildRequires:  %{phpunit}
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json,     "require": {
#        "php": "^5.3 || ^7.0 || ^8.0"
Requires:       php(language) >= 5.3
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
AccessibleObject is small class allowing you to easily access internals
of any object. In general, it's bad practice to do so. While we strongly
discourage you to using it, it may be helpful in debugging or testing
old, sad, legacy projects.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: generate a classmap autoloader
phpab --template fedora --output src/autoload.php src


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('PhpCsFixer\\AccessibleObject\\Tests\\', dirname(__DIR__) . '/tests');
EOF

: disable listener and add missing test suite name
sed -e '/listener/d' \
    -e 's/<testsuite>/<testsuite name="main">/' \
    phpunit.xml.dist > phpunit.xml

ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
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
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- switch to phpunit9
- switch to classmap autoloader

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov  8 2017 Remi Collet <remi@remirepo.net> - 1.0.0-4
- fix FTBFS from Koschei
- use package name for symfony/phpunit-bridge

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 1.0.0-3
- fix PHP minimal version

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 1.0.0-2
- fix dependency

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
