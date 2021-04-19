# Run optional test
%bcond_without perl_Types_URI_enables_optional_test

Name:           perl-Types-URI
Version:        0.007
Release:        6%{?dist}
Summary:        Type constraints and coercions for URIs
# COPYRIGHT:    Public Domain
# other files:  GPL+ or Artistic
License:        (GPL+ or Artistic) and Public Domain
URL:            https://metacpan.org/release/Types-URI
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Types-URI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Type::Library) >= 1.000000
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::UUID)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::data)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(URI::FromHash)
BuildRequires:  perl(URI::WithBase)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(if)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
# Test::Warnings not used
# Build cycle: perl-Attean → perl-Types-URI
%if %{with perl_Types_URI_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(Attean)
BuildRequires:  perl(Attean::IRI)
BuildRequires:  perl(IRI) >= 0.004
BuildRequires:  perl(Moose) >= 2.0000
BuildRequires:  perl(RDF::Trine) >= 1.000
BuildRequires:  perl(Types::Attean) >= 0.024
BuildRequires:  perl(Types::Namespace) >= 1.10
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Type::Library) >= 1.000000

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Type::Library\\)$

%description
Types::URI is a type constraint Perl library suitable for use with Moo/Moose
attributes, Kavorka sub signatures, and so forth.

%prep
%setup -q -n Types-URI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-4
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Petr Pisar <ppisar@redhat.com> - 0.007-1
- 0.007 bump

* Mon Nov 11 2019 Petr Pisar <ppisar@redhat.com> - 0.006-8
- Modernize a spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Petr Pisar <ppisar@redhat.com> 0.006-1
- Specfile autogenerated by cpanspec 1.78.