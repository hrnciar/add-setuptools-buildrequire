Name:           perl-WWW-Curl
Version:        4.17
Release:        26%{?dist}
Summary:        Perl extension interface for libcurl
License:        MIT
URL:            https://metacpan.org/release/WWW-Curl
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZBALINT/WWW-Curl-%{version}.tar.gz
Patch0:         WWW-Curl-4.17-Skip-preprocessor-symbol-only-CURL_STRICTER.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=941915
Patch1:         WWW-Curl-4.17-define-CURL-as-void.patch
# Adapt to changes in cURL 7.69.0, bug #1812910, CPAN RT#132197
Patch2:         WWW-Curl-4.17-Adapt-to-changes-in-cURL-7.69.0.patch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
%{?_with_network_tests:BuildRequires:  perl(lib) }
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
# Test::Pod is optional
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  libcurl-devel
Requires:       perl(:MODULE_COMPAT_%(eval "$(/usr/bin/perl -V:version)"; echo $version))

%{?perl_default_filter}

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%setup -q -n WWW-Curl-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
rm -rf inc && sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# These tests require network, use "--with network_tests" to execute them
%{?!_with_network_tests: rm t/01basic.t }
%{?!_with_network_tests: rm t/02callbacks.t }
%{?!_with_network_tests: rm t/04abort-test.t }
%{?!_with_network_tests: rm t/05progress.t }
%{?!_with_network_tests: rm t/08ssl.t }
%{?!_with_network_tests: rm t/09times.t }
%{?!_with_network_tests: rm t/14duphandle.t }
%{?!_with_network_tests: rm t/15duphandle-callback.t }
%{?!_with_network_tests: rm t/18twinhandles.t }
%{?!_with_network_tests: rm t/19multi.t }
%{?!_with_network_tests: rm t/21write-to-scalar.t }
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/WWW*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.17-24
- Perl 5.32 rebuild

* Thu Apr 09 2020 Petr Pisar <ppisar@redhat.com> - 4.17-23
- Adapt to changes in cURL 7.69.0 (bug #1812910)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 4.17-21
- Add Debian patch to fix build (#1754813)
- Replace call to perl with /usr/bin/perl
- Replace call to "make pure_install" with %%{make_install}
- Replace call to make with %%{make_build}

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.17-19
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 4.17-17
- Add missing build requirements (#1605423)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.17-15
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.17-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 4.17-9
- Apply patch to make WWW::Curl work with curl 7.50.2 (#1375176, RT #117793)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.17-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.17-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.17-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Petr ??abata <contyk@redhat.com> - 4.17-1
- 4.17 bump, license change

* Fri Feb 21 2014 Petr ??abata <contyk@redhat.com> - 4.16-1
- 4.16 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 4.15-11
- Perl 5.18 rebuild

* Sun Jul 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 4.15-10
- Update dependencies
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Remove buildroot cleaning

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Jitka Plesnikova <jplesnik@redhat.com> - 4.15-8
- Specify all dependencies
- Modernize spec file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 4.15-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Iain Arnell <iarnell@gmail.com> 4.15-4
- use perl_default_filter

* Wed Jun 29 2011 Marcela Ma??l????ov?? <mmaslano@redhat.com> - 4.15-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.15-1
- Update to 4.15
* Thu Oct 28 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.14-1
- Update to 4.14
- Add a filter provide to avoid private-shared-object-provides error
* Sun Sep  5 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.13-1
- Update to 4.13
* Wed Aug 25 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.12-1
- Update to 4.12
* Thu Jun  3 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.11-3
- Remove test 19 because it requires network
* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.11-2
- Mass rebuild with perl-5.12.0
* Fri Dec 18 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.11-1
- Update to 4.11
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4.09-3
- rebuild against perl 5.10.1
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Sat Jul 11 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.09-1
- Rebuild for 4.09
* Mon Jun  1 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.07-1
- Rebuild for 4.07
* Sat Apr 18 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.06-1
- Step to 4.06
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-4
- Licence update
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-3
- README.Win32 file removed
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-2
- Timestamp preserved
- changelog format fix
- README.Win32 file removed
* Thu Dec 11 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-1
- Initial build with cpan2spec
