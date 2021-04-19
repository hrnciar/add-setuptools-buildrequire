Name:           perl-HTTP-CookieMonster
Version:        0.11
Release:        4%{?dist}
Summary:        Easy access to your jar of HTTP::Cookies
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTTP-CookieMonster
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-CookieMonster-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(Moo) >= 1.000003
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(URI::Escape)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta not heplful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Moo) >= 1.000003

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Moo\\)$

%description
HTTP::CookieMonster gives you a simple interface for getting and setting
cookies in HTTP::Cookies objects.

%prep
%setup -q -n HTTP-CookieMonster-%{version}
# Correct a shebang
perl -i -p -MConfig -e 's{\A#!/usr/bin/env perl\b}{$Config{startperl}}' \
    examples/read_cookies.pl

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
%doc Changes CONTRIBUTORS examples README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-2
- Perl 5.32 rebuild

* Mon Feb 03 2020 Petr Pisar <ppisar@redhat.com> - 0.11-1
- 0.11 bump

* Fri Jan 31 2020 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.30 rebuild

* Fri Feb 01 2019 Petr Pisar <ppisar@redhat.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
