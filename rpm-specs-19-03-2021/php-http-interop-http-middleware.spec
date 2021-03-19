# remirepo/fedora spec file for php-http-interop-http-middleware
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    b49e1f9f6c584e704317b563302e566b8ce11858
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     http-interop
%global gh_project   http-middleware

Name:           php-%{gh_owner}-%{gh_project}
Version:        0.5.0
Release:        4%{?dist}
Summary:        Common interface for HTTP middleware

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-cli
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 2)
%else
BuildRequires:  php-psr-http-message
%endif
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": ">=5.3.0",
#        "psr/http-message": "^1.0"
Requires:       php(language) > 5.3
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 2)
%else
Requires:       php-psr-http-message
%endif
# From phpcompatinfo: none
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
PSR-15 interfaces for HTTP middleware.

Autoloader: %{_datadir}/php/Interop/Http/Middleware/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
cat << 'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Interop\\Http\\Server\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{_datadir}/php/Interop/Http
cp -pr src %{buildroot}%{_datadir}/php/Interop/Http/Middleware


%check
php -r '
require "%{buildroot}%{_datadir}/php/Interop/Http/Middleware/autoload.php";
if (interface_exists("Interop\\Http\\Server\\MiddlewareInterface")) {
   echo "Autoload OK\n";
   exit (0);
} else {
   echo "Autoload fails\n";
   exit (1);
}'


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/Interop
%dir %{_datadir}/php/Interop/Http
     %{_datadir}/php/Interop/Http/Middleware


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 0.5.0-1
- update to 0.5.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Remi Collet <remi@fedoraproject.org> - 0.2.0-1
- initial package
