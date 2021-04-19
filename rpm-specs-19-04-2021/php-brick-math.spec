# remirepo/fedora spec file for php-brick-math
#
# Copyright (c) 2020-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without tests

# Github
%global gh_commit    dff976c2f3487d42c1db75a3b180e2b9f0e72ce0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     brick
%global gh_project   math
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# Namespace
%global ns_vendor    Brick
%global ns_project   Math

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.9.2
Release:        2%{?dist}
Summary:        Arbitrary-precision arithmetic library

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 7.1
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-bcmath
BuildRequires:  php-gmp
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7.5.15 || ^8.5 || ^9.0",
#        "php-coveralls/php-coveralls": "^2.2",
#        "vimeo/psalm": "^3.5"
%if %{with tests}
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
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
#        "php": "^7.1 || ^8.0",
#        "ext-json": "*"
Requires:       php(language) >= 7.1
Requires:       php-json
# From phpcompatifo report for 0.9.1
Requires:       php-pcre
Requires:       php-spl
# See Brick\Math\Internal\Calculator::detect()
Requires:      (php-gmp or php-bcmath)

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
A PHP library to work with arbitrary precision numbers.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src


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
\Fedora\Autoloader\Autoload::addPsr4('Brick\\Math\\Tests\\', dirname(__DIR__) . '/tests');
EOF

: Run upstream test suite
ret=0
# don't test Native with is terribly slow, as bcmath/gmp are set as mandatory
for calc in GMP BCMath; do
  export CALCULATOR=$calc
  for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
    if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit9} \
        --no-coverage --verbose || ret=1
    fi
  done
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Remi Collet <remi@remirepo.net> - 0.9.2-1
- update to 0.9.2
- switch to phpunit9

* Thu Oct  1 2020 Remi Collet <remi@remirepo.net> - 0.9.1-1
- initial package
