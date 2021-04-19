Name:           sslscan
Version:        2.0.6
Release:        2%{?dist}
Summary:        Security assessment tool for SSL/TLS

# Special exception to allow linking against the OpenSSL libraries
License:        GPLv3+ with exceptions

# rbsec sslscan fork
URL:            https://github.com/rbsec/sslscan/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.openssl.org/source/openssl-1.1.1g.tar.gz
Patch0:         Makefile-override-CFLAGS.patch
Patch1:         Makefile-disable-opensslpull.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel

%description
SSLScan queries SSL services, such as HTTPS, in order to determine the ciphers
that are supported. SSLScan is designed to be easy, lean and fast. 
The output includes preferred ciphers of the SSL service, the certificate
and is in text and XML formats.

%prep
%autosetup -n %{name}-%{version}
mkdir openssl
cd openssl
tar xvf %{SOURCE1} --strip-components=1

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" static

%install
make install DESTDIR=%{buildroot} BINPATH=%{_bindir}/ MANPATH=%{_mandir}/

%files
%doc Changelog README.md TODO
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.6-1
- Update to latest upstream release 2.0.6

* Sat Nov 28 2020 Travis Suel <travis.bugzilla@gmail.com> - 2.0.0-1.beta2
- Switch to rbsec fork of sslscan (#1842763)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.11.11-1
- Update to latest upstream release 1.11.11

* Thu Mar 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.2-12
- Fix BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Michal Ambroz <rebus _AT seznam.cz> - 1.10.2-8
- Fix FTBFS by using compat-openssl10

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.10.2-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Michal Ambroz <rebus at, seznam.cz> 1.10.2-1
- bump to version 1.10.2 fixes issue with client certificates

* Sat Jan 04 2014 Michal Ambroz <rebus at, seznam.cz> 1.10.1-1
- switch to sslscan fork from dinotools.org, update to current version
- brings support for ECC as it is no longer prohibited in Fedora

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 07 2010 Michal Ambroz <rebus at, seznam.cz> 1.8.2-3
- build for rawhide requires explicit -lcrypto

* Mon Jan 18 2010 Michal Ambroz <rebus at, seznam.cz> 1.8.2-2
- fix issue with the patch version

* Sat Jan 16 2010 Michal Ambroz <rebus at, seznam.cz> 1.8.2-1
- Initial SPEC for Fedora 12
