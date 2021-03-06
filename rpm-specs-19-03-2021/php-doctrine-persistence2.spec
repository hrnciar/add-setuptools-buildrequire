# remirepo/fedora spec file for php-doctrine-persistence2
#
# Copyright (c) 2018-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global bootstrap    0
%global gh_commit    3bc796882c9f69526b7833b46ba3cd0c06b0460f
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   persistence
%global major        2
# packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Doctrine
%global ns_project   Common
%global ns_subproj   Persistence
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.1.0
Release:        2%{?dist}
Summary:        Doctrine Persistence abstractions

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-reflection
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json
#        "composer/package-versions-deprecated": "^1.11",
#        "phpstan/phpstan": "^0.12",
#        "doctrine/coding-standard": "^6.0 || ^8.0",
#        "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0",
#        "vimeo/psalm": "^3.11"
BuildRequires: (php-composer(doctrine/annotations)   >= 1.0   with php-composer(doctrine/annotations)   < 2)
BuildRequires: (php-composer(doctrine/cache)         >= 1.0   with php-composer(doctrine/cache)         < 2)
BuildRequires: (php-composer(doctrine/collections)   >= 1.0   with php-composer(doctrine/collections)   < 2)
BuildRequires: (php-composer(doctrine/event-manager) >= 1.0   with php-composer(doctrine/event-manager) < 2)
BuildRequires: (php-composer(doctrine/reflection)    >= 1.2   with php-composer(doctrine/reflection)    < 2)
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9
%else
%global phpunit %{_bindir}/phpunit8
BuildRequires:  phpunit8
%endif
%endif

# From composer.json
#        "php": "^7.1 || ^8.0"
#        "doctrine/annotations": "^1.0",
#        "doctrine/cache": "^1.0",
#        "doctrine/collections": "^1.0",
#        "doctrine/event-manager": "^1.0",
#        "doctrine/reflection": "^1.2"
Requires:       php(language) >= 7.1
Requires:      (php-composer(doctrine/annotations)   >= 1.0   with php-composer(doctrine/annotations)   < 2)
Requires:      (php-composer(doctrine/cache)         >= 1.0   with php-composer(doctrine/cache)         < 2)
Requires:      (php-composer(doctrine/collections)   >= 1.0   with php-composer(doctrine/collections)   < 2)
Requires:      (php-composer(doctrine/event-manager) >= 1.0   with php-composer(doctrine/event-manager) < 2)
Requires:      (php-composer(doctrine/reflection)    >= 1.2   with php-composer(doctrine/reflection)    < 2)
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# Split off doctrine/common
Conflicts:      php-doctrine-common < 1:2.10


%description
The Doctrine Persistence project is a set of shared interfaces and
functionality that the different Doctrine object mappers share.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_subproj}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv lib/%{ns_vendor}/%{ns_subproj} \
   lib/%{ns_vendor}/%{ns_subproj}%{major}
mv lib/%{ns_vendor}/%{ns_project}/%{ns_subproj} \
   lib/%{ns_vendor}/%{ns_project}/%{ns_subproj}%{major}


%build
: Generate a simple autoloader
%{_bindir}/phpab \
    --output lib/%{ns_vendor}/%{ns_subproj}%{major}/autoload.php \
    --template fedora \
    lib/%{ns_vendor}
cat << 'EOF' | tee -a lib/%{ns_vendor}/%{ns_subproj}%{major}/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Annotations/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Cache/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Collections/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/EventManager/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Reflection/autoload.php',
]);
EOF


%install
mkdir -p                %{buildroot}%{_datadir}/php
cp -pr lib/%{ns_vendor} %{buildroot}%{_datadir}/php/%{ns_vendor}


%check
%if %{with_tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    tests

cat << 'EOF' | tee -a vendor/autoload.php
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_subproj}%{major}/autoload.php";
EOF

# we don't want PHPStan (which pull nette framework)
find tests -type f -exec grep -q PHPStan {} \; -delete -print

: Run test suite
ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
        --bootstrap vendor/autoload.php \
        --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}%{major}
%{_datadir}/php/%{ns_vendor}/%{ns_subproj}%{major}


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- rename to php-doctrine-persistence2
- install in /usr/share/php/Doctrine/Persistence2

* Mon Mar 23 2020 Remi Collet <remi@remirepo.net> - 1.3.7-1
- update to 1.3.7 (no change)
- raise dependency on doctrine/reflection 1.2

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 1.3.6-1
- update to 1.3.6
- raise dependency on doctrine/reflection 1.1

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 1.3.5-1
- update to 1.3.5

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 1.3.4-1
- update to 1.3.4

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 1.3.3-1
- update to 1.3.3

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1
- use new namespace Doctrine\Persistence
  and provide compatibility Doctrine\Common\Persistence

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Thu Nov 22 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 1.0.1-1
- initial package, version 1.0.1
