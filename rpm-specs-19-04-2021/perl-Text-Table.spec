Name:           perl-Text-Table
Version:        1.134
Release:        4%{?dist}
Summary:        Organize Data in Tables
License:        ISC

URL:            https://metacpan.org/release/Text-Table
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Text-Table-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Text::Aligner) >= 0.05
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Optional tests are skipped
Requires:       perl(:MODULE_COMPAT_%(eval "$(/usr/bin/perl -V:version)"; echo $version))
Requires:       perl(Text::Aligner) >= 0.05

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Text::Aligner\\)$

%description
Organization of data in table form is a time-honored and useful method of
data representation. While columns of data are trivially generated by
computer through formatted output, even simple tasks like keeping titles
aligned with the data columns are not trivial, and the one-shot solutions
one comes up with tend to be particularly hard to maintain. Text::Table
allows you to create and maintain tables that adapt to alignment
requirements as you use them.

%prep
%setup -q -n Text-Table-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.134-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.134-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.134-2
- Perl 5.32 rebuild

* Sun May 17 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.134-1
- Update to 1.134
- Specify full path to perl

* Fri Mar 13 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.133-9
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.133-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.133-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.133-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.133-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.133-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.133-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.133-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.133-1
- Update to 1.133
- Drop Group tag

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.132-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.132-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.132-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.132-1
- Update to 1.132

* Mon Aug 08 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.131-1
- Update to 1.131

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.130-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.130-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.130-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.130-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.130-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Petr Šabata <contyk@redhat.com> - 1.130-1
- META changes only

* Thu Feb 06 2014 Petr Šabata <contyk@redhat.com> - 1.129-1
- META updates only
- Fix a changelog bogus date

* Tue Oct 29 2013 Petr Šabata <contyk@redhat.com> - 1.128-1
- 1.128 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.127-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.127-2
- Perl 5.18 rebuild

* Wed May 22 2013 Petr Šabata <contyk@redhat.com> - 1.127-1
- 1.127 bump, test suite enhancements
- Correcting license tag to ISC

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.126-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Petr Pisar <ppisar@redhat.com> - 1.126-1
- 1.126 bump

* Mon Sep 03 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-1
- 1.125 bump
- Specify all dependencies.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.124-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.124-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.124-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Petr Pisar <ppisar@redhat.com> - 1.124-1
- 1.124 bump
- Remove RPM-4.8-style dependency filters

* Mon Jul 25 2011 Iain Arnell <iarnell@gmail.com> 1.123-3
- update filtering for rpm 4.9

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.123-2
- Perl mass rebuild

* Mon Jun 13 2011 Petr Sabata <contyk@redhat.com> - 1.123-1
- 1.123 bump

* Mon Jun  6 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.122-1
- 1.122 bump

* Mon May 30 2011 Petr Sabata <contyk@redhat.com> 1.121-1
- 1.121 bump

* Mon May 16 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.120-1
- 1.120 bump
- clean deffattr
- license changed since 1.120 to ISC = BSD (2 clause)

* Fri May  6 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.118-1
- 1.118 bump

* Thu Apr 21 2011 Petr Sabata <psabata@redhat.com> - 1.117-1
- 1.117 bump
- Buildroot removed
- Source URL corrected

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.116-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.116-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Sep 22 2010 Petr Pisar <ppisar@redhat.com> - 1.116-1
- 1.116 bump
- Filter unversioned Text::Alignt Requires out

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.114-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.114-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.114-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.114-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.114-1
- Specfile autogenerated by cpanspec 1.78.
