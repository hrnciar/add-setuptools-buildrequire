# Fedora spec file for php-pecl-http
#
# Copyright (c) 2012-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

# The project is pecl_http but the extension is only http
%global proj_name pecl_http
%global pecl_name http
%global with_zts  0%{?__ztsphp:1}
# after 20-iconv 40-raphf
%global ini_name  50-%{pecl_name}.ini
%ifarch %{arm} aarch64
# Test suite disabled because of erratic results on slow ARM (timeout)
%global with_tests 0%{?_with_tests:1}
%else
%global with_tests 0%{!?_without_tests:1}
%endif

%global upstream_version 4.0.0
#global upstream_prever  RC1

Name:           php-pecl-http
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        Extended HTTP support

License:        BSD
URL:            https://pecl.php.net/package/pecl_http
Source0:        https://pecl.php.net/get/%{proj_name}-%{upstream_version}%{?upstream_prever}.tgz

# From http://www.php.net/manual/en/http.configuration.php
Source1:        %{proj_name}.ini

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 8.0
BuildRequires:  php-iconv
BuildRequires:  php-spl
BuildRequires:  php-pear
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel >= 1.2.0.4
BuildRequires:  curl-devel >= 7.18.2
BuildRequires:  libicu-devel
BuildRequires:  php-pecl-raphf-devel >= 2
BuildRequires:  libevent-devel >= 1.4
BuildRequires:  brotli-devel >= 1.0
BuildRequires:  pkgconfig
# only needed in F27+
BuildRequires:  openssl-devel

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-iconv%{?_isa}
Requires:       php-spl%{?_isa}
Requires:       php-raphf%{?_isa} >= 2
# V1 don't support PHP 5.6 https://bugs.php.net/66879
Obsoletes:      php-pecl-http1 < 2
# to allow migration from PHP 7 (last is 2.1.0)
Obsoletes:      php-pecl-propro < 2.2

Provides:       php-pecl(%{proj_name})         = %{version}
Provides:       php-pecl(%{proj_name})%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}


%description
The HTTP extension aims to provide a convenient and powerful set of
functionality for major applications.

The HTTP extension eases handling of HTTP URLs, dates, redirects, headers
and messages in a HTTP context (both incoming and outgoing). It also provides
means for client negotiation of preferred language and charset, as well as
a convenient way to exchange arbitrary data with caching and resuming
capabilities.

Also provided is a powerful request and parallel interface.

Version 2 is completely incompatible to previous version.

Documentation : https://mdref.m6w6.name/http


%package devel
Summary:       Extended HTTP support developer files (header)
Requires:      php-pecl-http%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa} >= 5.3.0
Obsoletes:     php-pecl-http1-devel < 2

%description devel
These are the files needed to compile programs using HTTP extension.


%prep
%setup -c -q 

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

mv %{proj_name}-%{upstream_version}%{?upstream_prever} NTS
cd NTS
extver=$(sed -n '/#define PHP_PECL_HTTP_VERSION/{s/.* "//;s/".*$//;p}' php_http.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}%{?gh_date:dev}"; then
   : Error: Upstream HTTP version is now ${extver}, expecting %{upstream_version}%{?upstream_prever}%{?gh_date:dev}.
   : Update the pdover macro and rebuild.
   exit 1
fi
cd ..

cp %{SOURCE1} %{ini_name}

%if %{with_zts}
# Duplicate source tree for NTS / ZTS build
cp -pr NTS ZTS
%endif


%build
peclconf() {
%configure \
  --with-http \
  --with-http-zlib-dir=%{_prefix} \
  --with-http-libcurl-dir=%{_prefix} \
  --without-http-libidn-dir \
  --without-http-libidn2-dir \
  --without-http-libidnkit-dir \
  --without-http-libidnkit2-dir \
  --with-http-libicu-dir=%{_prefix} \
  --with-http-libevent-dir=%{_prefix} \
  --with-http-libbrotli-dir=%{_prefix} \
  --with-libdir=%{_lib} \
  --with-php-config=$1
grep IDNA config.h
}
cd NTS
%{_bindir}/phpize
peclconf %{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
peclconf %{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
make -C NTS install INSTALL_ROOT=%{buildroot}

# Install XML package description
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# install config file
install -Dpm644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -Dpm644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Test & Documentation
cd NTS
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{proj_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{proj_name}/$i
done


%check
export REPORT_EXIT_STATUS=1
export SKIP_ONLINE_TESTS=1

: ignore tests with erratic results
rm ?TS/tests/client021.phpt
rm ?TS/tests/client022.phpt
rm ?TS/tests/client027.phpt
# sometime on s390x
rm ?TS/tests/client016.phpt
rm ?TS/tests/client028.phpt
rm ?TS/tests/etag001.phpt

# Shared needed extensions
modules=""
for mod in iconv raphf; do
  if [ -f %{php_extdir}/${mod}.so ]; then
    modules="$modules -d extension=${mod}.so"
  fi
done

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    $modules \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_tests}
: Upstream test suite NTS extension
cd NTS
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n $modules -d extension=$PWD/modules/%{pecl_name}.so" \
NO_INTERACTION=1 \
%{__php} -n run-tests.php --show-diff
%endif

%if %{with_zts}
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    $modules \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_tests}
: Upstream test suite ZTS extension
cd ../ZTS
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n $modules -d extension=$PWD/modules/%{pecl_name}.so" \
NO_INTERACTION=1 \
%{__ztsphp} -n run-tests.php --show-diff
%endif
%endif


%files
%license NTS/LICENSE
%doc %{pecl_docdir}/%{proj_name}
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so
%{pecl_xmldir}/%{name}.xml

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif

%files devel
%doc %{pecl_testdir}/%{proj_name}
%{php_incldir}/ext/%{pecl_name}

%if %{with_zts}
%{php_ztsincldir}/ext/%{pecl_name}
%endif


%changelog
* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0 (stable)
- raise dependency on PHP 8.0
- drop dependency on propro extension
- obsolete propro to allow upgrade from 7.x

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Remi Collet <remi@remirepo.net> - 3.2.4-1
- update to 3.2.4

* Tue Sep 15 2020 Remi Collet <remi@remirepo.net> - 3.2.3-4
- rebuild for new libevent

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 3.2.3-2
- Rebuild for ICU 67

* Fri Mar 27 2020 Remi Collet <remi@remirepo.net> - 3.2.3-1
- update to 3.2.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 3.2.2-2
- Rebuild for ICU 65

* Thu Oct 24 2019 Remi Collet <remi@remirepo.net> - 3.2.2-1
- update to 3.2.2

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 3.2.1-3
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun  7 2019 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Mon Feb  4 2019 Remi Collet <remi@remirepo.net> - 3.2.0-3
- ignore failed test with recent libcurl
  reported as https://github.com/m6w6/ext-http/issues/84

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 3.2.0-2
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Thu Jul 19 2018 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0 (php 7, stable)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0~RC1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.2.0~RC1-4
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.2.0~RC1-3
- Rebuild for ICU 61.1

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.2.0~RC1-2
- Rebuild for ICU 61.1

* Tue Apr 10 2018 Remi Collet <remi@remirepo.net> - 3.2.0~RC1-1
- update to 3.2.0RC1
- enable brotli compression support

* Thu Feb 15 2018 Remi Collet <remi@remirepo.net> - 3.1.1~RC1-5
- rebuild for libevent

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1~RC1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 3.1.1~RC1-3
- undefine _strict_symbol_defs_build

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.1.1~RC1-2
- Rebuild for ICU 60.1

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 3.1.1~RC1-1
- update to 3.1.1RC1
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May  9 2017 Remi Collet <remi@remirepo.net> - 3.1.0-4
- drop dependency on libidn, only use libicu

* Fri Apr 28 2017 Remi Collet <remi@fedoraproject.org> - 3.1.0-3
- add missing BR on openssl-devel for new libcurl (FTBFS from Koschei)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0 (php 7, stable)

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1 (php 7, stable)

* Sat Mar 26 2016 Remi Collet <remi@fedoraproject.org> - 2.5.6-2
- add upstream patch to skip a online test
  fix FTBFS detected by Koschei

* Wed Mar  9 2016 Remi Collet <remi@fedoraproject.org> - 2.5.6-1
- Update to 2.5.6 (stable)

* Wed Feb 10 2016 Remi Collet <remi@fedoraproject.org> - 2.5.5-3
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Remi Collet <remi@fedoraproject.org> - 2.5.5-1
- Update to 2.5.5 (stable)

* Fri Sep 25 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3 (stable)

* Thu Sep 10 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2 (stable)

* Tue Jul 28 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1 (stable)
- raise dependency on raphf 1.1.0

* Wed Jul 15 2015 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- update to 2.5.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-0.2.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Remi Collet <remi@fedoraproject.org> - 2.5.0-0.1.RC1
- update to 2.5.0RC1 (beta)

* Wed Apr 08 2015 Remi Collet <remi@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3
- add dependencies on pecl/json_post and pecl/apfd (fedora < 22)
- drop dependency on json
- temporarily disable 2 tests broken by new libcurl (Koschei)

* Thu Mar 12 2015 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2
- disable test suite on slow ARM builder

* Mon Mar  2 2015 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1 (stable)

* Mon Feb  9 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1 (stable)

* Tue Jan 27 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (stable)
- add dependency on libidn

* Thu Nov 06 2014 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4

* Tue Sep  9 2014 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- drop upstream patches

* Wed Sep  3 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- more upstream patch, fix for arm/ppc64

* Mon Sep  1 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0
- ignore known failed tests with PHP 5.3.3
- run test suite during build
- add upstream patch to skip online test
- temporarily ignore test suite result on arm

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 2.0.6-4
- rebuild for https://fedoraproject.org/wiki/Changes/Php56

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-2
- obsoletes php-pecl-http1 (dropped in fedora 21)

* Thu Apr 24 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6

* Thu Apr 24 2014 Remi Collet <rcollet@redhat.com> - 2.0.5-2
- add numerical prefix to extension configuration file

* Fri Apr 04 2014 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Thu Jan 02 2014 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4
- fix link to documentation
- update provided configuration
- add upstream patch for -Werror=format-security

* Tue Dec 10 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3 (stable)
- drop Conflicts with pecl/event

* Tue Nov 26 2013 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 (stable)

* Fri Nov 22 2013 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0 (stable)
- install doc in pecl doc_dir
- install tests in pecl test_dir (in devel)
- spec cleanups, and EPEL-6 compatibility

* Tue Aug 20 2013 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.18.beta5
- update to 2.0.0 beta5
- requires propro and raphf extensions

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.17.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 2.0.0-0.16.beta4
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.15.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.14.beta4
- update to 2.0.0beta4

* Thu Dec 13 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.13.beta3
- update to 2.0.0beta3
- fix requires

* Thu Nov 29 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.12.beta2
- update to 2.0.0beta2
- also provides php-http
- remove old directives from configuration file

* Fri Oct 12 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.11.beta1
- update to 2.0.0beta1
- must be load after json, to rename config to z-http.ini
- spec cleanups

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.10.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.9.alpha1
- update to 2.0.0alpha1

* Sat Mar 31 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.8.dev10
- update to 2.0.0dev10

* Fri Mar 16 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.7.dev8
- update to 2.0.0dev8

* Fri Mar 09 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.6.dev7
- update to 2.0.0dev7

* Fri Mar 02 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.5.dev6
- update to 2.0.0dev6

* Sat Feb 18 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.4.dev5
- update to 2.0.0dev5
- fix filters

* Wed Jan 25 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.3.dev4
- zts binary in /usr/bin with zts prefix

* Mon Jan 23 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.2.dev4
- update to 2.0.0dev4
- fix missing file https://bugs.php.net/60839

* Sun Jan 22 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.1.dev3
- initial package

