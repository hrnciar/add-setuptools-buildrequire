%global composer_vendor         paragonie
%global composer_project        constant_time_encoding
%global composer_namespace      ParagonIE/ConstantTime

%global github_owner            paragonie
%global github_name             constant_time_encoding

%global commit0 f34c2b11eb9d2c9318e13540a1dbc2a3afbd939c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


Name:       php-%{composer_vendor}-constant-time-encoding
Version:    2.4.0
Release:    3%{?dist}
Summary:    Constant-time Implementations of RFC 4648 Encoding

License:    MIT

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:  noarch

# "php": "^7|^8"
BuildRequires:  php(language) >= 7
BuildRequires:  php-mbstring
BuildRequires:  php-spl
# "phpunit/phpunit": "^6|^7|^8|^9"
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
%else
BuildRequires:  phpunit8
%global phpunit %{_bindir}/phpunit8
%endif

BuildRequires:  php-fedora-autoloader-devel

# "php": "^7|^8"
Requires:   php(language) >= 7
Requires:   php-mbstring
Requires:   php-spl

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Based on the constant-time base64 implementation made by Steve "Sc00bz" 
Thomas, this library aims to offer character encoding functions that do 
not leak information about what you are encoding/decoding via processor 
cache misses.

%prep
%setup -n %{github_name}-%{commit0}

%build
%{_bindir}/phpab -t fedora -o src/autoload.php src

%install
mkdir -p %{buildroot}%{_datadir}/php/%{composer_namespace}
cp -pr src/* %{buildroot}%{_datadir}/php/%{composer_namespace}

%check
%{phpunit} tests --verbose --bootstrap=src/autoload.php

%files
%dir %{_datadir}/php/ParagonIE
%{_datadir}/php/%{composer_namespace}
%doc README.md composer.json
%license LICENSE.txt

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Fran??ois Kooman <fkooman@tuxed.net> - 2.4.0-2
- support PHPUnit 8/9 for future PHP 8 support (patch by Remi Collet)

* Mon Dec  7 2020 Fran??ois Kooman <fkooman@tuxed.net> - 2.4.0-1
- update to 2.4.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Fran??ois Kooman <fkooman@tuxed.net> - 2.3.0-1
- update to 2.3.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Fran??ois Kooman <fkooman@tuxed.net> - 2.2.3-1
- update to 2.2.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Fran??ois Kooman <fkooman@tuxed.net> - 2.2.2-4
- also BuildRequire phpunit7 for future EL release

* Thu May 03 2018 Fran??ois Kooman <fkooman@tuxed.net> - 2.2.2-3
- simplify detection and use of PHPUnit 6 / PHPUnit 7

* Wed May 02 2018 Fran??ois Kooman <fkooman@tuxed.net> - 2.2.2-2
- use Fedora template for generating autoloader
- match phpunit version with composer.json

* Tue May 01 2018 Fran??ois Kooman <fkooman@tuxed.net> - 2.2.2-1
- update to 2.2.2 for PHP >= 7
- update dependencies
- switch to phpab autoload generator

* Mon Apr 30 2018 Fran??ois Kooman <fkooman@tuxed.net> - 1.0.3-1
- update to 1.0.3

* Sat Mar 10 2018 Fran??ois Kooman <fkooman@tuxed.net> - 1.0.2-1
- update to 1.0.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Fran??ois Kooman <fkooman@tuxed.net> - 1.0.1-4
- own parent directory
- remove Requires paragonie/random_compat, only needed for build
- BuildRequire php-pcre
- rework check autoloader

* Mon Mar 13 2017 Fran??ois Kooman <fkooman@tuxed.net> - 1.0.1-3
- better follow SourceURL package guidelines for GH

* Mon Feb 13 2017 Fran??ois Kooman <fkooman@tuxed.net> - 1.0.1-2
- add random_compat as dependency to be able to run tests on PHP < 7

* Mon Feb 13 2017 Fran??ois Kooman <fkooman@tuxed.net> - 1.0.1-1
- initial package
