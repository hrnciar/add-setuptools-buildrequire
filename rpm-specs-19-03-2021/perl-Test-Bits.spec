Name:           perl-Test-Bits
Version:        0.02
Release:        2%{?dist}
Summary:        Provides a bits_is() subroutine for testing binary data
License:        Artistic 2.0
URL:            https://metacpan.org/release/Test-Bits
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Test-Bits-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder::Module)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
# Test::CPAN::Changes not used
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester)
# Optional tests:
# Pod::Coverage::TrustPod not used
# Test::EOL not used
# Test::Pod not used
# Test::Pod::LinkCheck not used
# Test::Pod::Coverage not used
# Test::Pod::No404s not used
# Test::Script not used
# Test::Spelling not used
# Test::NoTabs not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This Perl module provides a single subroutine, bits_is(), for testing
binary data.

%prep
%setup -q -n Test-Bits-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Petr Pisar <ppisar@redhat.com> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
