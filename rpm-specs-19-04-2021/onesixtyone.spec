Name:           onesixtyone
Version:        0.3.2
Release:        25%{?dist}
Summary:        An efficient SNMP scanner

License:        GPLv2+
URL:            http://www.phreedom.org/software/onesixtyone/
Source0:        http://www.phreedom.org/software/onesixtyone/releases/%{name}-%{version}.tar.gz
#GPG Signature  by "Solar Eclipse <solareclipse@phreedom.org>"
Source1:        http://www.phreedom.org/software/onesixtyone/releases/%{name}-%{version}.tar.gz.sig
#Manpage
Source2:        %{name}.1
Patch0:         onesixtyone-makefile.patch

BuildRequires: make
BuildRequires:  gcc

%description
onesixtyone takes a different approach to SNMP scanning. It takes advantage of
the fact that SNMP is a connection-less protocol and sends all SNMP requests
as fast as it can. Then the scanner waits for responses to come back and logs
them, in a fashion similar to Nmap ping sweeps.

%prep
%setup -q
%patch0 -p0

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
# Not needed for Fedora, but package exists for EPEL as well
rm -rf %{buildroot}
install -D onesixtyone %{buildroot}%{_bindir}/onesixtyone
install -D -m 0644 dict.txt %{buildroot}%{_datadir}/onesixtyone/dict.txt
install -m 0644 -pD %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}.1

%files
# No copy of GPL in tarball, licencing info in .c file.
%doc ChangeLog README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.2-19
- Fix BR

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 20 2011 Michal Ambroz <rebus at, seznam.cz> - 0.3.2-8
- Ressurect the package for F16/17

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.2-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.2-4
- Autorebuild for GCC 4.3

* Wed May 23 2007 Sindre Pedersen Bj??rdal <foolish[AT]guezz.net> - 0.3.2-3
- Add patch to really call proper flags, promise
* Tue May 22 2007 Sindre Pedersen Bj??rdal <foolish[AT]guezz.net> - 0.3.2-2
- Change make to really call proper flags
* Fri May 04 2007 Sindre Pedersen Bj??rdal <foolish[AT]guezz.net> - 0.3.2-1
- Initial build
