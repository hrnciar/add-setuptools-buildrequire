%bcond_without perl_Mojo_DOM58_enables_role

Name:           perl-Mojo-DOM58
Version:        2.000
Release:        5%{?dist}
Summary:        Minimalistic HTML/XML DOM parser with CSS selectors
# CONTRIBUTING.md:      CC0
# lib/Mojo/DOM58.pm:    Artistic 2.0
License:        Artistic 2.0 and CC0
URL:            https://metacpan.org/release/Mojo-DOM58
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Mojo-DOM58-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
%if %{with perl_Mojo_DOM58_enables_role}
BuildRequires:  perl(Role::Tiny) >= 2.000001
%endif
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
# Tests:
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Exporter) >= 5.57
%if %{with perl_Mojo_DOM58_enables_role}
Suggests:       perl(Role::Tiny) >= 2.000001
%endif

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Exporter\\)$

%description
Mojo::DOM58 is a minimalistic and relaxed pure-perl HTML/XML DOM parser. It
supports the HTML Living Standard and Extensible Markup Language (XML) 1.0,
and matching based on CSS3 selectors. It will even try to interpret broken
HTML and XML, so you should not use it for validation.

%prep
%setup -q -n Mojo-DOM58-%{version}

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
%doc Changes CONTRIBUTING.md examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.000-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Petr Pisar <ppisar@redhat.com> 2.000-1
- Specfile autogenerated by cpanspec 1.78.
