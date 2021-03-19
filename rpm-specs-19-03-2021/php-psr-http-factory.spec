# remirepo/fedora spec file for php-psr-http-factory
#
# Copyright (c) 2018-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    12ac7fcd07e5b077433f5f2bee95b3a771bf61be
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-factory

%global pk_vendor    psr
%global pk_project   %{gh_project}

Name:      php-%{pk_vendor}-%{pk_project}
Version:   1.0.1
Release:   5%{?dist}
Summary:   Common interfaces for PSR-7 HTTP message factories

License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:   %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz

BuildArch: noarch
# For tests
BuildRequires: php(language) >= 7
BuildRequires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 2)
BuildRequires: php-cli
BuildRequires: php-fedora-autoloader-devel

# From composer.json,    "require": {
#       "php": ">=7.0.0",
#       "psr/http-message": "^1.0"
Requires:  php(language) >= 7
Requires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 2)
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:  php-composer(fedora/autoloader)

# Composer
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This package holds all interfaces related to
PSR-17 (HTTP Message Factories). 

Please refer to the specification for a description:
https://www.php-fig.org/psr/psr-17/


Autoloader: %{_datadir}/php/Psr/Http/Message/%{pk_project}-autoload.php


%prep
%setup -qn %{gh_project}-%{gh_commit}


%build
: Generate autoloader
%{_bindir}/phpab --template fedora --output src/%{pk_project}-autoload.php src

cat << 'EOF' | tee -a src/%{pk_project}-autoload.php
\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
));
EOF


%install
mkdir -p   %{buildroot}%{_datadir}/php/Psr/Http
cp -rp src %{buildroot}%{_datadir}/php/Psr/Http/Message


%check
: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/Psr/Http/Message/%{pk_project}-autoload.php";
exit (interface_exists("Psr\\Http\\Message\\RequestFactoryInterface") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/Psr/Http/Message/*php


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May  2 2019 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Thu Dec 13 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- Initial package, version 1.0.0

