#
# --with oracle 
#	Build perl-DBIx-SearchBuilder-Oracle subpackage. 
#	Disabled by default, because it depends on packages outside of Fedora
#	at run-time
#

Name:		perl-DBIx-SearchBuilder
Version:	1.68
Release:	3%{?dist}
Summary:	Encapsulate SQL queries and rows in simple perl objects
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/DBIx-SearchBuilder
Source0:	https://cpan.metacpan.org/authors/id/B/BP/BPS/DBIx-SearchBuilder-%{version}.tar.gz

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:	noarch

BuildRequires: make
BuildRequires:	perl-generators
BuildRequires:	perl(Cache::Simple::TimedExpiry) >= 0.21
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::ReturnValue) >= 0.4
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:	perl(Test::More) >= 0.52
BuildRequires:	perl(Want)

# Improved tests:
BuildRequires:	perl(Test::Pod)

# Optional features
BuildRequires:	perl(capitalization) >= 0.03
BuildRequires:	perl(Clone)
BuildRequires:	perl(DBIx::DBSchema)

BuildRequires:  perl(inc::Module::Install)

%description
This module provides an object-oriented mechanism for retrieving and
updating data in a DBI-accessible database.

%prep
%setup -q -n DBIx-SearchBuilder-%{version}
rm -r inc
sed -i -e '/^inc\/.*$/d' MANIFEST

# Perms in tarball are broken 
find -type f -exec chmod -x {} \;

%build
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing 
# missing optional features
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1

make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%doc README ROADMAP
%{perl_vendorlib}/DBIx
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/DBIx/SearchBuilder/Handle/Oracle*
%exclude %{_mandir}/man3/DBIx::SearchBuilder::Handle::Oracle*


%if "%{?_with_oracle}"
%package Oracle
Summary:	DBIx::SearchBuilder bindings for Oracle
Requires:	%name = %{version}-%{release}

%description Oracle
DBIx::SearchBuilder bindings for Oracle

%files Oracle
%{perl_vendorlib}/DBIx/SearchBuilder/Handle/Oracle*
%{_mandir}/man3/DBIx::SearchBuilder::Handle::Oracle*
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.68-1
- Update to 1.68.

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.67-12
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.67-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.67-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.67-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.67-1
- Update to 1.67.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.66-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.66-5
- Modernize spec.
- Remove inc/.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.66-3
- Perl 5.22 rebuild

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.66-2
- Perl 5.20 mass

* Mon Sep 08 2014 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.66-1
- Upstream update.
- Spec cleanup.
- Reflect Source0 having changed.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.65-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.65-2
- Perl 5.18 rebuild

* Fri Jul 12 2013 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.65-1
- Upstream update.
- BR: perl(Scalar::Util).
- Fix up bogus dates in %%changelog.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.63-1
- Upstream update.
- Reflect upstream URL having changed.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.62-2
- Perl 5.16 rebuild

* Thu Apr 12 2012 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.62-1
- Upstream update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.61-1
- Upstream update.

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.59-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 06 2010 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.59-1
- Upstream update.

* Tue Nov 02 2010 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.58-1
- Upstream update.
- Spec cleanup.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.56-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.56-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.56-2
- rebuild against perl 5.10.1

* Wed Jul 29 2009 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.56-1
- Upstream update.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Ralf Cors??pius <corsepiu@fedoraproject.org> - 1.55-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 08 2008 Ralf Cors??pius <rc040203@freenet.de> - 1.54-1
- Upstream update.

* Fri Apr 25 2008 Ralf Cors??pius <rc040203@freenet.de> - 1.53-1
- Upstream update.

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.51-2
- rebuild for new perl

* Mon Jan 21 2008 Ralf Cors??pius <rc040203@freenet.de> - 1.51-1
- Upstream update.

* Sun Nov 25 2007 Ralf Cors??pius <rc040203@freenet.de> - 1.50-1
- Upstream update.

* Tue Sep 04 2007 Ralf Cors??pius <rc040203@freenet.de> - 1.49-1
- Upstream update.
- Update license tag.

* Mon Mar 12 2007 Ralf Cors??pius <rc040203@freenet.de> - 1.48-1
- Upstream update.
- BR: perl(ExtUtils::MakeMaker).

* Fri Mar 02 2007 Ralf Cors??pius <rc040203@freenet.de> - 1.46-1
- Upstream update.
- Use "by-modules" Source0 (upstream maintainer has changed).

* Wed Oct 04 2006 Ralf Cors??pius <rc040203@freenet.de> - 1.45-1
- Upstream update.

* Tue Sep 05 2006 Ralf Cors??pius <rc040203@freenet.de> - 1.43-2
- Mass rebuild.

* Sat Apr 22 2006 Ralf Cors??pius <rc040203@freenet.de> - 1.43-1
- Upstream update.

* Wed Mar 01 2006 Ralf Cors??pius <rc040203@freenet.de> - 1.38-2
- Rebuild for perl-5.8.8.

* Wed Jan 11 2006 Ralf Cors??pius <rc040203@freenet.de> - 1.38-1
- Upstream update.
- Spec cleanup.

* Mon Nov 14 2005 Ralf Corsepius <rc040203@freenet.de> - 1.33-1
- Upstream update to 1.33.

* Sun Nov 13 2005 Ralf Corsepius <rc040203@freenet.de>
- BR: perl(Clone) for 1.35.

* Sun Nov 06 2005 Ralf Corsepius <rc040203@freenet.de>
- BR: perl(DBIx::DBSchema) and perl(capitalization) for 1.33
  (Now in FE >= 5).

* Mon Oct 10 2005 Ralf Corsepius <rc040203@freenet.de> - 1.27-2
- chmod -x *.pm.
- BR: perl(Test::Pod).
- Add --with oracle to allow users to conditionally build the 
  perl-DBIx-SearchBuilder-Oracle subpackage.

* Wed Sep 14 2005 Ralf Corsepius <rc040203@freenet.de> - 1.27-1
- Preps for 1.32.
- Split out Oracle.
- FE submission.
