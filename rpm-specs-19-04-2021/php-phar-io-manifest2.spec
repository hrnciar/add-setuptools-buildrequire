# remirepo/fedora spec file for php-phar-io-manifest2
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_with          bootstrap
%if %{with bootstrap}
%bcond_with          tests
%else
%bcond_without       tests
%endif

%global gh_commit    85265efd3af7ba3ca4b2a2c34dbfc5788dd29133
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phar-io
%global gh_project   manifest
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PharIo
%global ns_project   Manifest
%global major        2
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.1
Release:        3%{?dist}
Summary:        Component for reading phar.io manifest information

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-dom
BuildRequires:  php-phar
BuildRequires: (php-composer(%{pk_vendor}/version) >= 3.0.1 with php-composer(%{pk_vendor}/version) <  4)
BuildRequires:  php-filter
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlwriter
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
%if 0%{?fedora} >= 32
%global phpunit %{_bindir}/phpunit9
%else
%global phpunit %{_bindir}/phpunit8
%endif
BuildRequires:  %{phpunit}
%endif

# from composer.json
#    "php": "^7.2 || ^8.0",
#    "ext-dom": "*",
#    "ext-phar": "*",
#    "ext-xmlwriter": "*",
#    "phar-io/version": "^3.0.1"
Requires:       php(language) >= 7.2
Requires:       php-dom
Requires:       php-phar
Requires:       php-xmlwriter
Requires:      (php-composer(%{pk_vendor}/version) >= 3.0.1 with php-composer(%{pk_vendor}/version) <  4)
# from phpcompatinfo report for version 2.0.0
Requires:       php-filter
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Component for reading phar.io manifest information from a PHP Archive (PHAR).

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{ns_vendor}/Version3/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmd; then
    set $cmd
    $1 -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      ${2:-%{_bindir}/phpunit9} \
        --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc README.md composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 2.0.1-2
- switch to phpunit9

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1 (no change)
- sources from git snapshot

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- rename to php-phar-io-manifest2
- move to /usr/share/php/PharIo/Manifest2
- raise dependency on PHP 7.2
- switch to phpunit8

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3
- allow phar-io/version 2.0
- drop patch merged upstream
- use range dependencies on F27+

* Fri Apr  7 2017 Remi Collet <remi@remirepo.net> - 1.0.1-1
- initial package

