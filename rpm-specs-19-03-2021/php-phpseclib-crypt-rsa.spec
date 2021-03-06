%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Crypt_RSA

Name:           php-phpseclib-crypt-rsa
Version:        0.3.9
Release:        12%{?dist}
Summary:        Pure-PHP PKCS#1 (v2.1) compliant implementation of RSA

License:        MIT
URL:            http://phpseclib.sourceforge.net/
Source0:        http://phpseclib.sourceforge.net/get/%{pear_name}-%{version}.tgz

# from Remi, fixes openssl config location when installed via PEAR
Patch0:         php-phpseclib-crypt-rsa-0.3.9-config_location.patch

BuildArch:      noarch
BuildRequires:  php-pear(PEAR)

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)
Requires:       php-pear(phpseclib.sourceforge.net/Math_BigInteger) >= 0.3.0
Requires:       php-pear(phpseclib.sourceforge.net/Crypt_Random) >= 0.3.0
Requires:       php-pear(phpseclib.sourceforge.net/Crypt_Hash) >= 0.3.0
Requires:       php-pear(PEAR) >= 1.4.0
Provides:       php-pear(phpseclib.sourceforge.net/Crypt_RSA) = %{version}
BuildRequires:  php-channel(phpseclib.sourceforge.net)
Requires:       php-channel(phpseclib.sourceforge.net)
# phpcompatinfo, generated from 0.3.5
Requires:       php-date
Requires:       php-pcre
Requires:       php-xml

%description
Pure-PHP PKCS#1 (v2.1) compliant implementation of RSA. Optionally uses
openssl.

%prep
%setup -q -c
sed -e 's/\r//' -i %{pear_name}-%{version}/*php
%patch0 -p1
mv package.xml %{pear_name}-%{version}/%{name}.xml

cd %{pear_name}-%{version}

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        phpseclib.sourceforge.net/%{pear_name} >/dev/null || :
fi


%files
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Crypt/RSA.php
%dir %{pear_cfgdir}/%{pear_name}
%config(noreplace) %{pear_cfgdir}/%{pear_name}/openssl.cnf


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Adam Williamson <awilliam@redhat.com> - 0.3.9-1
- new release 0.3.9

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Adam Williamson <awilliam@redhat.com> - 0.3.5-3
- fix up config file install and use (from Remi Collet)

* Sat Jan  4 2014 Adam Williamson <awilliam@redhat.com> - 0.3.5-2
- various review style cleanups

* Tue Dec 31 2013 Adam Williamson <awilliam@redhat.com> - 0.3.5-1
- initial package (generated with pear make-rpm-spec)
