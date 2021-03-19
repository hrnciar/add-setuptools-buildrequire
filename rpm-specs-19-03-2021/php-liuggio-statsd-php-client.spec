Name:		php-liuggio-statsd-php-client
Version:	1.0.18
Release:	11%{?dist}
Summary:	Object Oriented Client for etsy/statsd written in php

License:	MIT
URL:		https://github.com/liuggio/statsd-php-client
Source0:	https://github.com/liuggio/statsd-php-client/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}-autoload.php

BuildArch:	noarch

BuildRequires:	php-phpunit-PHPUnit
BuildRequires:	php-composer(symfony/class-loader)
BuildRequires:	php-composer(monolog/monolog) >= 1.2.0

Requires:	php(language) >= 5.3.2
Requires:	php-pcre
Requires:	php-sockets
Requires:	php-spl

Provides:	php-composer(liuggio/statsd-php-client) = %{version}


%description
statsd-php-client is an Open Source, and Object Oriented Client for etsy/statsd
written in php.


%prep
%setup -qn statsd-php-client-%{version}


%build


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/Liuggio/StatsdClient
cp -rp src/Liuggio/StatsdClient/* %{buildroot}%{_datadir}/php/Liuggio/StatsdClient
cp -p %{SOURCE1} %{buildroot}%{_datadir}/php/Liuggio/StatsdClient/autoload.php


%check
phpunit -v \
    --bootstrap=%{buildroot}%{_datadir}/php/Liuggio/StatsdClient/autoload.php


%files
%license LICENSE
%doc CHANGELOG.md composer.json README.md
%{_datadir}/php/Liuggio


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 24 2015 Michael Cronenworth <mike@cchtml.com> - 1.0.18-1
- version update

* Tue Jun 23 2015 Michael Cronenworth <mike@cchtml.com> - 1.0.16-3
- Fix Requires, install autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Michael Cronenworth <mike@cchtml.com> - 1.0.16-1
- Initial package

