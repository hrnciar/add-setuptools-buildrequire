Summary:        SSL/TLS network protocol analyzer
Name:           ssldump
Version:        1.3
Release:        1%{?dist}
License:        BSD with advertising
URL:            https://github.com/adulau/ssldump
Source0:        https://github.com/adulau/ssldump/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        HOWTO
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  openssl-devel
%else
BuildRequires:  openssl11-devel
%endif
BuildRequires:  libpcap-devel
BuildRequires:  libnet-devel
BuildRequires:  json-c-devel

%description
The ssldump program is an SSL/TLS network protocol analyzer. It identifies
TCP connections on the chosen network interface and attempts to interpret
them as SSL/TLS traffic. When ssldump identifies SSL/TLS traffic, ssldump 
decodes the records and displays them in a textual form to stdout. And if
provided with the appropriate keying material, ssldump will also decrypt
the connections and display the application data traffic. This program is
based on tcpdump, a network monitoring and data acquisition tool.

%prep
%setup -q
install -p -m 0644 %{SOURCE1} .

%build
%if 0%{?rhel} == 7
export CFLAGS="$RPM_OPT_FLAGS $(pkg-config --cflags-only-I openssl11) -D_BSD_SOURCE"
export LDFLAGS="$RPM_LD_FLAGS $(pkg-config --libs-only-L openssl11)"
%endif

./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYRIGHT
%doc ChangeLog CREDITS HOWTO README README.md
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Feb 03 2021 Robert Scheck <robert@fedoraproject.org> 1.3-1
- Upgrade to 1.3 (#1924208)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Robert Scheck <robert@fedoraproject.org> 1.2-1
- Upgrade to 1.2 (#1917212)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.22.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.21.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.20.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.19.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.18.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.17.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.16.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.15.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.14.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.13.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.12.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.11.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.10.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Robert Scheck <robert@fedoraproject.org> 0.9-0.9.b3
- Added a patch which adds further link layer offsets
- Added patch to include traffic with(out) the 802.1Q VLAN header
- Added patch for TLSv1.1/TLSv1.2 application data decrypt support
- Added a patch to update known cipher suites according to IANA
- Added patch with new cipher suites for application data decoding

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.8.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.7.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.6.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.5.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Robert Scheck <robert@fedoraproject.org> 0.9-0.4.b3
- Fixed wrong decoder table ends to avoid many segfaults (#747398)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.3.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 06 2010 Robert Scheck <robert@fedoraproject.org> 0.9-0.2.b3
- Added a patch to support AES cipher-suites (#248813 #c5)
- Added backporting patch from CVS 2006-06-19 (#248813 #c5)

* Sat Jan 23 2010 Robert Scheck <robert@fedoraproject.org> 0.9-0.1.b3
- Upgrade to 0.9b3
- Initial spec file for Fedora and Red Hat Enterprise Linux
