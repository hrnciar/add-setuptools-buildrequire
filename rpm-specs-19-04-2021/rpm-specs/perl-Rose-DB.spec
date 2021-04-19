Name:		perl-Rose-DB
Version:	0.783
Release:	5%{?dist}
Summary:	DBI wrapper and abstraction layer
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Rose-DB
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-DB-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(constant)
BuildRequires:	perl(Bit::Vector::Overload) >= 6.4
BuildRequires:	perl(Carp)
BuildRequires:	perl(Clone::PP)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(DateTime::Duration)
BuildRequires:	perl(DateTime::Format::MySQL)
BuildRequires:	perl(DateTime::Format::Oracle)
BuildRequires:	perl(DateTime::Format::Pg) >= 0.11
BuildRequires:	perl(DateTime::Infinite)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Rose::DateTime::Util) >= 0.532
BuildRequires:	perl(Rose::Object) >= 0.854
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(SQL::ReservedWords)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::Clock)
BuildRequires:	perl(Test::Pod) >= 1.0
BuildRequires:	perl(warnings)
BuildRequires:	perl(YAML)

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Rose::DB is a wrapper and abstraction layer for DBI-related functionality.
A Rose::DB object "has a" DBI object; it is not a subclass of DBI.

%prep
%setup -q -n Rose-DB-%{version}

%build
find . -type f -executable -exec chmod -x {} \;

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
export AUTOMATED_TESTING=1
make test

%files
%doc Changes
%{perl_vendorlib}/Rose/
%{_mandir}/man3/Rose::DB*.3pm*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.783-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.783-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.783-3
- Perl 5.32 rebuild

* Mon Apr  6 2020 Bill Pemberton <wfp5p@worldbroken.com> - 0.783-2
- add some modules for tests

* Mon Apr  6 2020 Bill Pemberton <wfp5p@worldbroken.com> - 0.783-1
- update to 0.783
- workarounds for DBD::Pg 3.8.0 and later

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.781-3
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.781-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Bill Pemberton <wfp5p@worldbroken.com> - 0.781-1
- update to version 0.781

* Fri Aug  9 2019 Bill Pemberton <wfp5p@worldbroken.com> - 0.779-1
- update to version 0.779
- adds skip_locked support for PostgreSQL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.778-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.778-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.778-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.778-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.778-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.778-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.778-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.778-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.778-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul  4 2016 Bill Pemberton <wfp5p@worldbroken.com> - 0.778-1
- update to version 0.778

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.777-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.777-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.777-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.777-2
- Perl 5.22 rebuild

* Wed Mar 18 2015 Bill Pemberton <wfp5p@worldbroken.com> - 0.777-1
- update to version 0.777
- updates project URLs
- use Clone::PP instead of Clone

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.775-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.775-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Bill Pemberton <wfp5p@worldbroken.com> - 0.775-1
- update to version 0.775

* Mon Nov  4 2013 Bill Pemberton <wfp5p@worldbroken.com> - 0.774-1
- update to version 0.774
- fixes some typos

* Tue Oct 29 2013 Bill Pemberton <wfp5p@worldbroken.com> - 0.773-1
- update to version 0.773

* Mon Aug  5 2013 Bill Pemberton <wfp5p@virginia.edu> - 0.771-1
- update to version 0.771
- This version only makes a minor addition to the documentation

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.770-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.770-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.770-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.770-1
- update to 0.770

* Mon Jul 30 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.769-5
- add more BuildRequires
- remove filter_from_requires

* Mon Jul 16 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.769-4
- remove buildroot and clean
- remove defattr from files section
- add constant to BuildRequires

* Wed Jun 27 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.769-3
- Patch to use Clone instead of Clone::PP

* Tue Jun 26 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.769-2
- Make files more specific

* Mon Feb 15 2010 Bill Pemberton <wfp5p@virginia.edu> - 0.769-1
- Initial version
