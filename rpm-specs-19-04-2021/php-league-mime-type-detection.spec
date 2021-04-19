# remirepo/fedora spec file for php-league-mime-type-detection
#
# Copyright (c) 2020-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    3b9dff8aaf7323590c1d2e443db701eb1f9aa0d3
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   mime-type-detection
# Packagist
%global pk_vendor    league
%global pk_name      mime-type-detection
# Namespace
%global ns_vendor    League
%global ns_project   MimeTypeDetection

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.7.0
Release:        2%{?dist}
Summary:        Mime-type detection for Flysystem

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 7.2
BuildRequires:  php-fileinfo
BuildRequires:  php-json
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^8.5.8 || ^9.3",
#        "phpstan/phpstan": "^0.12.68",
#        "friendsofphp/php-cs-fixer": "^2.18"
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
BuildRequires:  phpunit9 >= 9.3
%global phpunit %{_bindir}/phpunit9
%else
BuildRequires:  phpunit8 >= 8.5.8
%global phpunit %{_bindir}/phpunit8
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.2 || ^8.0",
#        "ext-fileinfo": "*"
Requires:       php(language) >= 7.2
Requires:       php-fileinfo
# From phpcompatifo report for 1.4.0
Requires:       php-json
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
This package supplies a generic mime-type detection interface with a finfo
based implementation.

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
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
EOF

: Run upstream test suite
# the_generated_map_should_be_up_to_date is online
ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(the_generated_map_should_be_up_to_date)).)*$' \
      --no-coverage \
      --verbose || ret=1
  fi
done
exit $ret


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}/*Test.php


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0

* Mon Oct 19 2020 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Tue Sep 22 2020 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- add patch for test suite from upstream and from
  https://github.com/thephpleague/mime-type-detection/pull/3
- open https://github.com/thephpleague/mime-type-detection/pull/4 phpunit 9
- switch to phpunit9

* Mon Aug 24 2020 Remi Collet <remi@remirepo.net> - 1.4.0-1
- initial package
