Name:           perl-List-AllUtils
Version:        0.18
Release:        2%{?dist}
Summary:        Combines List::Util and List::SomeUtils
# CODE_OF_CONDUCT.md:   CC-BY
# lib/List/AllUtils.pm: Artistic 2.0
License:        Artistic 2.0 and CC-BY
URL:            https://metacpan.org/release/List-AllUtils
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-AllUtils-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::SomeUtils) >= 0.56
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(List::UtilsBy) >= 0.11
# Tests:
# CPAN::Meta not useful
# CPAN::Meta::Prereqs not usedful
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Are you sick of trying to remember whether a particular helper is defined
in List::Util or List::SomeUtils? I sure am. Now you don't have to remember.
This module will export all of the functions that either of those two
modules defines.

%prep
%setup -q -n List-AllUtils-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.32 rebuild

* Mon Mar 02 2020 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.26 rebuild

* Wed Feb 08 2017 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Mon Oct 17 2016 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump

* Tue Jun 28 2016 Petr Pisar <ppisar@redhat.com> - 0.11-1
- 0.11 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-2
- Perl 5.24 rebuild

* Mon May 09 2016 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-3
- Perl 5.22 rebuild

* Wed Mar 04 2015 Petr Pisar <ppisar@redhat.com> - 0.09-2
- Correct license declaration from (GPL+ or Artistic) to (Artistic 2.0)
  (bug #1198256)

* Wed Oct 08 2014 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump

* Tue Oct 15 2013 Petr Pisar <ppisar@redhat.com> - 0.07-1
- 0.07 bump

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 0.05-1
- 0.05 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 0.03-2
- Perl 5.18 rebuild

* Thu Mar 07 2013 Petr Pisar <ppisar@redhat.com> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
