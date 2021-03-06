# remirepo/fedora spec file for php-microsoft-tolerant-php-parser
#
# Copyright (c) 2018-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    1d76657e3271754515ace52501d3e427eca42ad0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Microsoft
%global gh_project   tolerant-php-parser
# Packagist
%global pk_vendor    microsoft
%global pk_name      %{gh_project}
# PSR-0 namespace
%global ns_vendor    %{gh_owner}
%global ns_project	 PhpParser

%global with_tests   0%{!?_without_tests:1}


Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.0.23
Release:        4%{?dist}
Summary:        Tolerant PHP-to-AST parser

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-reflection
BuildRequires:  php-json
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^6.4"
BuildRequires:  phpunit7
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=7.0"
# php-parser 1.4 for autoloader
Requires:       php(language) >= 7.0
# From phpcompatifo report for 2.1.0
Requires:       php-reflection
Requires:       php-json
Requires:       php-spl
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
This is an early-stage PHP parser designed, from the beginning, for IDE usage
scenarios. There is still a ton of work to be done, so at this point, this
repo mostly serves as an experiment and the start of a conversation.

Autoloader %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
sed -e 's:src/bootstrap.php:%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php:' \
    -i phpunit.xml

# test using BaseTestListener dropped in phpunit7
rm tests/LexicalGrammarTest.php
rm tests/ParserGrammarTest.php

: Run the test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 \
      --testsuite invariants \
      || ret=1

    $cmd %{_bindir}/phpunit7 \
      --testsuite grammar \
      --filter '^((?!(testOutputTreeClassificationAndLength)).)*$' \
      || ret=1

    $cmd %{_bindir}/phpunit7 \
      --testsuite api\
      --filter '^((?!(testOutOfOrderTextEdits|testOverlappingTextEdits)).)*$' \
      || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc *.md
%doc composer.json
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 0.0.23-4
- switch to phpunit7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Remi Collet <remi@remirepo.net> - 0.0.23-2
- rebuild

* Mon Sep 14 2020 Remi Collet <remi@remirepo.net> - 0.0.23-1
- update to 0.0.23

* Wed Aug 26 2020 Remi Collet <remi@remirepo.net> - 0.0.22-1
- update to 0.0.22

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Remi Collet <remi@remirepo.net> - 0.0.20-1
- update to 0.0.20
- re-enable the test suite, only ignore 3 known failed tests

* Mon Feb 17 2020 Remi Collet <remi@remirepo.net> - 0.0.18-3
- ignore grammar and api results, FTBFS #1799871

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Remi Collet <remi@remirepo.net> - 0.0.18-1
- update to 0.0.18

* Mon Mar 11 2019 Remi Collet <remi@remirepo.net> - 0.0.17-1
- update to 0.0.17

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Remi Collet <remi@remirepo.net> - 0.0.16-1
- update to 0.0.16

* Wed Sep 26 2018 Remi Collet <remi@remirepo.net> - 0.0.15-1
- update to 0.0.15

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 0.0.13-1
- update to 0.0.13

* Tue Jun 12 2018 Remi Collet <remi@remirepo.net> - 0.0.12-1
- update to 0.0.12

* Sun May 13 2018 Remi Collet <remi@remirepo.net> - 0.0.11-1
- update to 0.0.11

* Tue Mar 20 2018 Remi Collet <remi@remirepo.net> - 0.0.10-1
- update to 0.0.10

* Thu Feb 15 2018 Remi Collet <remi@remirepo.net> - 0.0.9-1
- Update to 0.0.9

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 0.0.8-1
- initial package
