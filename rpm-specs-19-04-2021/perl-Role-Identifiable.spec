Name:           perl-Role-Identifiable
Version:        0.007
Release:        19%{?dist}
Summary:        Identifiable roles
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Role-Identifiable
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Role-Identifiable-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides several Moose roles for identifying things.

%prep
%setup -q -n Role-Identifiable-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-17
- Perl 5.32 rebuild

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-16
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-2
- Perl 5.22 rebuild

* Mon Nov 10 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.007-1
- Update to 0.007
- Remove Group tag (no longer used)
- Add %%license tag

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-10
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.005-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.005-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.005-2
- Perl mass rebuild

* Thu Feb 17 2011 Iain Arnell <iarnell@gmail.com> 0.005-1
- Specfile autogenerated by cpanspec 1.79.
