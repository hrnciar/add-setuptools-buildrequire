Name:           perl-XML-Parser-Lite
# Use three digits since 0.719 -> 0.72
%global cpan_version 0.722
Version:        %{cpan_version}
Release:        8%{?dist}
Summary:        Lightweight regexp-based XML parser
License:        (GPL+ or Artistic) and REX
URL:            https://metacpan.org/release/XML-Parser-Lite
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/XML-Parser-Lite-%{cpan_version}.tar.gz
BuildArch:      noarch
# SOAP::Lite is not actually needed
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(re)
# Tests only
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
This Perl module implements an XML parser with an interface similar to
XML::Parser.  Though not all callbacks are supported, you should be able to
use it in the same way you use XML::Parser.

%prep
%setup -q -n XML-Parser-Lite-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.722-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.722-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.722-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.722-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.722-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.722-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.722-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.722-1
- 0.722 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.721-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.721-12
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.721-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.721-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.721-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.721-8
- Perl 5.26 re-rebuild of bootstrapped packages

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.721-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.721-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.721-5
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.721-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.721-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.721-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Petr Šabata <contyk@redhat.com> - 0.721-1
- 0.721 bumpity
- Patch for rt#98635 incorporated upstream
- Patch for rt#91434 shouldn't be required now

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.720-4
- Perl 5.22 re-rebuild of bootstrapped packages

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.720-3
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 0.720-2
- Break build-cycle: perl-XML-Parser-Lite → perl-XMLRPC-Lite →
  perl-SOAP-Lite → perl-XML-Parser-Lite

* Wed Feb 18 2015 Petr Šabata <contyk@redhat.com> - 0.720-1
- 0.72 bump
- Use three digits in version

* Mon Sep 08 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.719-4
- Perl 5.20 mass

* Fri Sep 05 2014 Petr Šabata <contyk@redhat.com> - 0.719-3
- Avoid koji build failures by correcting the test plan

* Thu Feb 06 2014 Petr Šabata <contyk@redhat.com> - 0.719-2
- Patch the test suite so it actually works

* Wed Feb 05 2014 Petr Šabata <contyk@redhat.com> - 0.719-1
- 0.719 bump

* Wed Nov 20 2013 Petr Šabata <contyk@redhat.com> - 0.717-1
- Specfile autogenerated by cpanspec 1.78.
