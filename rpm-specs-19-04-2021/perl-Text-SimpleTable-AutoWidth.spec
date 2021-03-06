Name:           perl-Text-SimpleTable-AutoWidth
Version:        0.09
Release:        7%{?dist}
Summary:        Simple eye-candy ASCII tables with auto-width selection
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Text-SimpleTable-AutoWidth
Source0:        https://cpan.metacpan.org/authors/id/C/CU/CUB/Text-SimpleTable-AutoWidth-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Text::SimpleTable)
# Tests:
# English not used
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
# Optional tests:
# Test::Perl::Critic not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Simple eye-candy ASCII tables with auto-selection columns width, as seen
in Catalyst.

%prep
%setup -q -n Text-SimpleTable-AutoWidth-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING RELEASE_TESTING TEST_POD
make test

%files
%license LICENSE
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.30 rebuild

* Fri Feb 01 2019 Petr Pisar <ppisar@redhat.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
