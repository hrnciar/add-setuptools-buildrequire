%global debug_package %{nil}

Name:           ncrack
Version:        0.7
Release:        3%{?dist}
Summary:        A high-speed network auth cracking tool

License:        GPLv2 with exceptions
URL:            http://nmap.org/ncrack/
Source0:        http://nmap.org/ncrack/dist/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
Ncrack is a high-speed network authentication cracking tool. It was
built to help companies secure their networks by proactively testing
all their hosts and networking devices for poor passwords. Security
professionals also rely on Ncrack when auditing their clients. Ncrack
was designed using a modular approach, a command-line syntax similar to
Nmap and a dynamic engine that can adapt its behaviour based on network
feedback. It allows for rapid, yet reliable large-scale auditing of
multiple hosts.

%prep
%autosetup -p1

%build
export CFLAGS="${RPM_OPT_FLAGS} -fcommon"
%configure
%make_build

%install
%make_install

%files
%doc CHANGELOG README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7-1
- Update to latest upstream release 0.7 (rhbz#1747007)
- Fix FTBFS (rhbz#1799676)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Update to latest upstream release 0.6 (rhbz#1505196)

* Fri Jul 20 2018 Steve Milner <smilner@fedoraproject.org> 0.5-8
- Add g++ dep per RHBZ#1604929

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Apr 13 2017 Michal Ambroz <rebus _AT seznam.cz> - 0.5-2
- Fix FTBFS by using compat-openssl10.
- fix nullcheck error build for gcc7

* Mon Feb 20 2017 Michal Ambroz <rebus _AT seznam.cz> - 0.5-1
- bump to 0.5 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.11.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.10.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
	
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.9.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4-0.8.ALPHA
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.7.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.6.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.5.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.4.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.3.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.2.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 27 2011 Steve Milner <smilner@fedoraproject.org> 0.4-0.1.ALPHA
- Update for upstream release.
- Update spec changelog to fedora address

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.2.ALPHA
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Steve Milner <smilner@fedoraproject.org> 0.3-0.1.ALPHA
- Update for upstream release.

* Mon Jun 14 2010 Steve Milner <smilner@fedoraproject.org> 0.2-0.1.ALPHA
- Update for upstream release.

* Mon Oct  5 2009 Steve Milner <smilner@fedoraproject.org> 0.01-0.7.ALPHA
- Added --without-zlib-version-check to configure to allow building on EL-4.

* Tue Sep 29 2009 Steve Milner <smilner@fedoraproject.org> 0.01-0.6.ALPHA
- Removed custom patches after discussion with upstream and reviewers.
- Moved what we thought was a config back to it's default location.

* Wed Sep 23 2009 Steve Milner <smilner@fedoraproject.org> 0.01-0.5.ALPHA
- Added Martin Gieseking's ncrack-config-in-etc patch moving configs to sysconfdir.

* Mon Sep 21 2009 Steve Milner <smilner@fedoraproject.org> 0.01-0.4.ALPHA
- Man page now using glob.
- Added strip to prep section to avoid empty debug package.

* Wed Sep 16 2009 Steve Milner <smilner@fedoraproject.org> 0.01-0.3.ALPHA
- updated previous change log to reflect the changes.
- removed COPYING.OpenSSL from doc
- now following proper pre-release versioning

* Tue Sep 15 2009 Steve Milner <smilner@fedoraproject.org> 0.01-0.2.ALPHA
- updated license tag to GPLv2 with restrictions
- preserve timestamp of file COPYING.OpenSSH

* Thu Sep 10 2009 Steve Milner <smilner@fedoraproject.org> 0.01-0.1.ALPHA
- Initial package
