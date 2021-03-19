# remirepo/fedora spec file for php-psr-container
#
# Copyright (c) 2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    b7ce3b176482dbbc1245ebf52b181af44c2cf55f
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   container

%global pk_vendor    psr
%global pk_project   container

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:      php-%{pk_vendor}-%{pk_project}
Version:   1.0.0
Release:   9%{?dist}
Summary:   Common Container Interface

License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:   %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz

BuildArch: noarch
# For tests
BuildRequires: php(language) >= 5.3.0
BuildRequires: php-cli
BuildRequires: php-composer(fedora/autoloader)

# From composer.json,    "require": {
#        "php": ">=5.3.0"
Requires:  php(language) >= 5.3.0
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:  php-composer(fedora/autoloader)

# Composer
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This package holds all interfaces/classes/traits related to PSR-11.

Note that this is not a container implementation of its own. 

Autoloader: %{_datadir}/php/Psr/Container/autoload.php


%prep
%setup -qn %{gh_project}-%{gh_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{pk_vendor}/%{pk_project} and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Psr\\Container\\', __DIR__);
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p   %{buildroot}%{_datadir}/php/Psr
cp -rp src %{buildroot}%{_datadir}/php/Psr/Container


%check
: Test autoloader
php -r '
require "%{buildroot}%{_datadir}/php/Psr/Container/autoload.php";
exit (interface_exists("Psr\\Container\\ContainerInterface") ? 0 : 1);
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/Psr
     %{_datadir}/php/Psr/Container


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Remi Collet <remi@remirepo.net> - 1.0.0-1
- Initial package, version 1.0.0

