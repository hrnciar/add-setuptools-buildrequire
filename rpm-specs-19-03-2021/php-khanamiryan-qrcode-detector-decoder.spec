# remirepo/fedora spec file for php-khanamiryan-qrcode-detector-decoder
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    07fceefb79d895e858e52921afb9c1433d2f3d5e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     khanamiryan
%global gh_project   php-qrcode-detector-decoder

%global pk_vendor    %{gh_owner}
%global pk_project   qrcode-detector-decoder

%global ns_vendor    %nil
%global ns_project   Zxing
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.0.4
Release:        2%{?dist}
Summary:        QR code decoder / reader

Group:          Development/Libraries
# https://github.com/khanamiryan/php-qrcode-detector-decoder/issues/29
License:        MIT and ASL 2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# From https://github.com/khanamiryan/php-qrcode-detector-decoder/pull/80
Patch0:         https://patch-diff.githubusercontent.com/raw/khanamiryan/php-qrcode-detector-decoder/pull/80.patch
# From https://github.com/khanamiryan/php-qrcode-detector-decoder/pull/103
Patch1:         https://patch-diff.githubusercontent.com/raw/khanamiryan/php-qrcode-detector-decoder/pull/103.patch

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-gd
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.0"
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
%else
%global phpunit %{_bindir}/phpunit8
%endif
# Required by autoloader
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.6"
Requires:       php(language) >= 5.6
# From phpcompatinfo report for version 1
Requires:       php-reflection
Requires:       php-date
Requires:       php-gd
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-spl
Suggests:       php-pecl(imagick)
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This is a PHP library to detect and decode QR-codes.

This is first and only QR code reader that works without extensions.
Ported from ZXing library.

Autoloader: %{php_home}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1
%patch1 -p1


%build
%{_bindir}/phpab \
  --output lib/autoload.php \
  --template fedora \
  lib

cat << 'EOF' | tee -a lib/autoload.php
\Fedora\Autoloader\Dependencies::required([
    __DIR__ . '/Common/customFunctions.php',
]);
EOF


%install
: Library
mkdir -p   %{buildroot}%{php_home}
cp -pr lib %{buildroot}%{php_home}/%{ns_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_project}/autoload.php';
EOF

ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} $filter --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE*
%doc composer.json
%doc README.md
%{php_home}/%{ns_project}


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Remi Collet <remi@remirepo.net> - 1.0.4-1
- update to 1.0.4
- add patch for PHP 8 from
  https://github.com/khanamiryan/php-qrcode-detector-decoder/pull/103
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Remi Collet <remi@remirepo.net> - 1.0.2-3
- add LICENSE files
- fix package summary and description

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Tue Apr 17 2018 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1 - broken
- BC break, see https://github.com/khanamiryan/php-qrcode-detector-decoder/issues/40
- missing file, see https://github.com/khanamiryan/php-qrcode-detector-decoder/issues/38

* Tue Jun 27 2017 Remi Collet <remi@remirepo.net> - 1-1
- initial package, version 1
- open https://github.com/khanamiryan/php-qrcode-detector-decoder/issues/29
  License issue, blocker for Fedora
- open https://github.com/khanamiryan/php-qrcode-detector-decoder/pull/30
  drop unneeded permissions
- open https://github.com/khanamiryan/php-qrcode-detector-decoder/pull/31
  use modern PHPUnit
