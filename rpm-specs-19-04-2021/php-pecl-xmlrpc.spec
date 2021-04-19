# Fedora spec file for php-pecl-xmlrpc
# Without SCL compatibility, from
#
# remirepo spec file for php-pecl-xmlrpc
#
# Copyright (c) 2020-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%bcond_without      tests

%global with_zts    0%{!?_without_zts:%{?__ztsphp:1}}
%global pecl_name   xmlrpc
%global upver       1.0.0
%global rcver       RC2
%global lower       rc2
# After 20-xml
%global ini_name    30-%{pecl_name}.ini

Summary:        Functions to write XML-RPC servers and clients
Name:           php-pecl-%{pecl_name}
Version:        %{upver}%{?lower:~%{lower}}
Release:        2%{?dist}

# Extension is PHP
# Library is BSD
License:        PHP and BSD
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{upver}%{?rcver}.tgz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 8
BuildRequires:  php-pear
BuildRequires:  php-xml

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-xml%{?_isa}

# Set epoch so 1:1.0 > 0:8.0
Obsoletes:      php-%{pecl_name}               < 8.0.0
Provides:       php-%{pecl_name}               = 1:%{version}
Provides:       php-%{pecl_name}%{?_isa}       = 1:%{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This extension provides functions to write XML-RPC servers and clients.

You can find more information about XML-RPC at http://www.xmlrpc.com/,
and more documentation on this extension and its functions at
https://www.php.net/xmlrpc.

The extension is unbundled from php-src as of PHP 8.0.0, because the underlying
libxmlrpc has obviously been abandoned. It is recommended to reevaluate using
this extension.


%prep
%setup -qc
mv %{pecl_name}-%{upver}%{?rcver} NTS

sed -e 's/role="test"/role="src"/' \
    -e '/COPYING/s/role="doc"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd NTS
# Check version as upstream often forget to update this
extver=$(sed -n '/#define PHP_XMLRPC_VERSION/{s/.* "//;s/".*$//;p}' php_xmlrpc.h)
if test "x${extver}" != "x%{upver}%{?rcver}%{?gh_date:-dev}"; then
   : Error: Upstream RECODE version is ${extver}, expecting %{upver}%{?rcver}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable "%{pecl_name}" extension module
extension=%{pecl_name}
EOF


%if %{with_zts}
# duplicate for ZTS build
cp -pr NTS ZTS
%endif


%build
peclconf() {
%configure \
    --with-xmlrpc \
    --with-php-config=$1
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
# Install the NTS stuff
make -C NTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Install the ZTS stuff
%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Test & Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd NTS

: Minimal load test for NTS extension
%{_bindir}/php --no-php-ini \
    --define extension=xml \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with_zts}
cd ../ZTS

: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=xml \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%endif

%if %{with tests}
cd ../NTS

: Run upstream test suite
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=xml -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php -q --show-diff
%endif



%files
%license NTS/LICENSE
%license NTS/libxmlrpc/COPYING
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%{php_ztsextdir}/%{pecl_name}.so
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%endif


%changelog
* Sat Mar  6 2021 Remi Collet <remi@remirepo.net> - 1.0.0~rc2-2
- clean for Fedora review

* Fri Jan 15 2021 Remi Collet <remi@remirepo.net> - 1.0.0~rc2-1
- update to 1.0.0RC2 (beta)

* Tue Jan  5 2021 Remi Collet <remi@remirepo.net> - 1.0.0~rc1-1
- update to 1.0.0RC1 (beta)

* Wed Sep 30 2020 Remi Collet <remi@remirepo.net> - 1.0.0~DEV.20200602-4
- rebuild for PHP 8.0.0RC1

* Wed Sep  2 2020 Remi Collet <remi@remirepo.net> - 1.0.0~DEV.20200202-3
- rebuild for PHP 8.0.0beta3

* Wed Aug  5 2020 Remi Collet <remi@remirepo.net> - 1.0.0~DEV.20200202-2
- rebuild for 8.0.0beta1

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 1.0.0~DEV.20200202-1
- initial package, version 1.0.0-dev
