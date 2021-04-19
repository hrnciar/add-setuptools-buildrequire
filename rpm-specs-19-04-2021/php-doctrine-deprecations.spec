# remirepo/fedora spec file for php-doctrine-deprecations
#
# Copyright (c) 2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    9504165960a1f83cc1480e2be1dd0a0478561314
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   deprecations
# packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Doctrine
%global ns_project   Deprecations

Name:           php-%{pk_vendor}-%{pk_project}
Version:        0.5.3
Release:        2%{?dist}
Summary:        A small layer on top of trigger_error or PSR-3 logging

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Missing license file from
# https://github.com/doctrine/deprecations/pull/27
Patch0:         %{name}-pr27.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# From composer.json
#    "require-dev": {
#        "phpunit/phpunit": "^7.0|^8.0|^9.0",
#        "psr/log": "^1.0",
#        "doctrine/coding-standard": "^6.0|^7.0|^8.0"
BuildRequires: (php-composer(psr/log) >= 1.0   with php-composer(psr/log) < 2)
BuildRequires:  phpunit9
%endif

# From composer.json
#    "require": {
#        "php": "^7.1 || ^8.0",
#    "suggest": {
#        "psr/log": "Allows logging deprecations via PSR-3 logger implementation"

Requires:       php(language) >= 7.1
Requires:      (php-composer(psr/log) >= 1.0   with php-composer(psr/log) < 2)
# From phpcompatinfo report for version 0.5.3
# Only core and standard

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
A small (side-effect free by default) layer on top of
trigger_error(E_USER_DEPRECATED) or PSR-3 logging.

* no side-effects by default, making it a perfect fit for libraries
  that don't know how the error handler works they operate under
* options to avoid having to rely on error handlers global state by
  using PSR-3 logging
* deduplicate deprecation messages to avoid excessive triggering and
  reduce overhead

We recommend to collect Deprecations using a PSR logger instead of
relying on the global error handler.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1


%build
: Generate a simple autoloader
%{_bindir}/phpab \
    --output lib/%{ns_vendor}/%{ns_project}/autoload.php \
    --template fedora \
    lib/%{ns_vendor}

cat << 'EOF' | tee -a lib/%{ns_vendor}/%{ns_project}/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Psr/Log/autoload.php',
]);
EOF


%install
mkdir -p                              %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib/%{ns_vendor}/%{ns_project} %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    test_fixtures/src \
    test_fixtures/vendor/doctrine/foo

cat << 'EOF' | tee -a vendor/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php',
]);
EOF

ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 \
        --verbose || ret=1
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
%{_datadir}/php/%{ns_vendor}/%{ns_project}/


%changelog
* Wed Mar 31 2021 Remi Collet <remi@remirepo.net> - 0.5.3-2
- add LICENSE file copy/pasted from other doctrine project,
  and from https://github.com/doctrine/deprecations/pull/27

* Tue Mar 30 2021 Remi Collet <remi@remirepo.net> - 0.5.3-1
- initial package
- open https://github.com/doctrine/deprecations/issues/26 missing License
