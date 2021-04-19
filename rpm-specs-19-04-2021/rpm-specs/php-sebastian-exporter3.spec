# remirepo/fedora spec file for php-sebastian-exporter3
#
# Copyright (c) 2013-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    6b853149eab67d4da22291d36f5b0631c0fd856e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   exporter
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   Exporter
%global major        3
%global php_home     %{_datadir}/php
%global pear_name    Exporter
%global pear_channel pear.phpunit.de
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

# NOTICE: used by phpunit 6, 7 and 8

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.1.3
Release:        3%{?dist}
Summary:        Export PHP variables for visualization

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^6.0",
#        "ext-mbstring": "*"
BuildRequires:  phpunit8
BuildRequires:  php-mbstring
BuildRequires:  (php-composer(%{pk_vendor}/recursion-context) >= 3.0 with php-composer(%{pk_vendor}/recursion-context) < 4)
%endif

# from composer.json
#        "php": ">=7.0",
#        "sebastian/recursion-context": "^3.0"
Requires:       php(language) >= 7.0
Requires:       (php-composer(%{pk_vendor}/recursion-context) >= 3.0 with php-composer(%{pk_vendor}/recursion-context) < 4)
# from phpcompatinfo report for version 3.0.0
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Provides the functionality to export PHP variables for visualization.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# generate the Autoloader
phpab --template fedora --output src/autoload.php src

# Rely on include_path as in PHPUnit dependencies
cat <<EOF | tee -a src/autoload.php
// Dependency' autoloader
require_once '%{php_home}/%{ns_vendor}/RecursionContext3/autoload.php';
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%if %{with_tests}
%check
mkdir vendor
touch vendor/autoload.php

: Fix for phpunit8
find tests/ -name \*php -exec sed -e 's/setUp()/setUp():void/'  -i {} \;

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    %{_bindir}/php -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
    %{_bindir}/phpunit8	  --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Wed Mar 10 2021 Remi Collet <remi@remirepo.net> - 3.1.3-2
- switch to phpunit8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Remi Collet <remi@remirepo.net> - 3.1.3-1
- update to 3.1.3 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 15 2019 Remi Collet <remi@remirepo.net> - 3.1.2-1
- update to 3.1.2

* Mon Aug 12 2019 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 3.1.0-5
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 3.1.0-3
- use range dependencies on F27+

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr  3 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0

* Mon Mar 13 2017 Remi Collet <remi@remirepo.net> - 3.0.0-2
- non bootstrap build

* Fri Mar  3 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- rename to php-sebastian-exporter3
- raise dependency on PHP 7
- raise dependency on recursion-context 3

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- raise dependency on sebastian/recursion-context 2.0
- switch to fedora/autoloader

* Fri Jun 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2
- run test suite with both PHP 5 and 7 when available

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1 (only CS)

* Fri Jan 30 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Sat Jan 24 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- add dependency on sebastian/recursion-context

* Sun Oct  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2
- enable test suite

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-4
- add composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-2
- cleanup pear registry

* Sun Apr  6 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- get sources from github
- run test suite when build --with tests

* Sun Oct 20 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- rename to lowercase

* Thu Sep 12 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
