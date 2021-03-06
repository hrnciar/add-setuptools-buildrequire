# remirepo/fedora spec file for php-tecnickcom-tc-lib-color
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    83cdb57fd900901c6aa2af8cfd67202518fb69b2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global c_vendor     tecnickcom
%global gh_owner     tecnickcom
%global gh_project   tc-lib-color
%global php_project  %{_datadir}/php/Com/Tecnick/Color
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_owner}-%{gh_project}
Version:        1.14.6
Release:        1%{?dist}
Summary:        PHP library to manipulate various color representations

License:        LGPLv3+
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
# For tests
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.0
%else
%global phpunit %{_bindir}/phpunit8
BuildRequires:  phpunit8 >= 8.5.13
%endif
BuildRequires:  php(language) >= 5.3
BuildRequires:  php-pcre
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.3",
#        "ext-pcre": "*"
Requires:       php(language) >= 5.3
Requires:       php-pcre
# From phpcompatinfo report for version 1.12.4
# none
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{c_vendor}/%{gh_project}) = %{version}
# Upstream package name
Provides:       php-%{gh_project} = %{version}


%description
Provides tc-lib-color: PHP library to manipulate various color
representations (GRAY, RGB, HSL, CMYK) and parse Web colors.

The initial source code has been extracted from TCPDF (http://www.tcpdf.org).


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Sanity check
grep -q '^%{version}$' VERSION

: Fix the examples
sed -e 's:^require:////require:' \
    -e 's:^//require:require:'   \
    -i example/*php


%build
phpab --template fedora --output src/autoload.php src


%install
mkdir -p   $(dirname %{buildroot}%{php_project})
cp -pr src %{buildroot}%{php_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Test\\', dirname(__DIR__) . '/test');
EOF

ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
   if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit9} --no-coverage --verbose || ret=1
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
%doc README.md example
%dir %{_datadir}/php/Com
%dir %{_datadir}/php/Com/Tecnick
%{php_project}


%changelog
* Mon Feb  8 2021 Remi Collet <remi@remirepo.net> - 1.14.6-1
- update to 1.14.6 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Remi Collet <remi@remirepo.net> - 1.14.1-1
- update to 1.14.1
- switch to classmap autoloader

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 1.12.15-1
- update to 1.12.15 (no change)

* Fri Sep 20 2019 Remi Collet <remi@remirepo.net> - 1.12.13-1
- update to 1.12.13

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Remi Collet <remi@remirepo.net> - 1.12.12-1
- update to 1.12.12 (no change)

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 1.12.11-1
- update to 1.12.11 (no change)

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 1.12.10-1
- update to 1.12.10 (no change)
- switch to phpunit7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Remi Collet <remi@remirepo.net> - 1.12.8-1
- Update to 1.12.8 (no change)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Remi Collet <remi@fedoraproject.org> - 1.12.6-1
- update to 1.12.6 (no change)
- use phpunit6 on F26+

* Mon Feb  6 2017 Remi Collet <remi@fedoraproject.org> - 1.12.4-1
- update to 1.12.4 (no change)

* Fri Sep  2 2016 Remi Collet <remi@fedoraproject.org> - 1.12.1-1
- update to 1.12.1

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 1.11.0-1
- update to 1.11.0
- raise dependency on php >= 5.4
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Remi Collet <remi@fedoraproject.org> - 1.6.2-1
- update to 1.6.2

* Sun Sep 13 2015 Remi Collet <remi@fedoraproject.org> - 1.5.2-1
- update to 1.5.2
- provide php-composer(tecnickcom/tc-lib-color)

* Fri Jul 24 2015 Remi Collet <remi@fedoraproject.org> - 1.5.1-1
- update to 1.5.1 (no change)

* Thu Jul  2 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Wed Jul  1 2015 Remi Collet <remi@fedoraproject.org> - 1.4.5-1
- initial package, version 1.4.5
