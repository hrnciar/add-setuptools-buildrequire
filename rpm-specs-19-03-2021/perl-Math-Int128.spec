Name:           perl-Math-Int128
Version:        0.22
Release:        2%{?dist}
Summary:        Manipulate 128-bit integers in Perl
# lib/Math/Int128.pm:                   GPL+ or Artistic
# lib/Math/Int128/die_on_overflow.pm:   GPL+ or Artistic
# Makefile.PL:                          GPL+ or Artistic
# ppport.h:                             GPL+ or Artistic
# README.md:                            GPL+ or Artistic
# strtoint128.h:                        BSD
## Unbundled
# inc/Capture/Tiny.pm:                  GPL+ or Artistic
# inc/Config/AutoConf.pm:               GPL+ or Artistic
License:        (GPL+ or Artistic) and BSD
URL:            https://metacpan.org/release/Math-Int128
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Math-Int128-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
# Module::CAPIMaker not used
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::AutoConf)
# ExtUtils:CBuilder for Config::AutoConf->check_default_headers()
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::Int64) >= 0.51
BuildRequires:  perl(overload)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Math::BigInt)
# Pod::Wordlist not used
# Test::CPAN::Changes not used
# Test::EOL not used
# Test::NoTabs not used
# Test::Pod not used
# Test::Spelling not used
# Test::Synopsis not used
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# This software needs a compiler with a 128-bit integer type. GCC for 32-bit
# targets does not support it. Bugs #1871733, #1871735.
ExcludeArch:    %{arm32} %{ix86}

%description
This module adds support for 128-bit integers, signed and unsigned, to Perl.

%prep
%setup -q -n Math-Int128-%{version}
# Remove the bundled modules
rm -r ./inc
perl -i -ne 'print $_ unless m{\Ainc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Petr Pisar <ppisar@redhat.com> 0.22-1
- Specfile autogenerated by cpanspec 1.78.
