# Perform optional tests
%bcond_without perl_MaxMind_DB_Reader_enables_optional_test

Name:           perl-MaxMind-DB-Reader
Version:        1.000014
Release:        2%{?dist}
Summary:        Read MaxMind database files and look up IP addresses
# lib/MaxMind/DB/Reader.pm: Artistic 2.0
# LICENSE:      Artistic 2.0 text
# Makefile.PL:  Artistic 2.0
## Not in any binary package
# maxmind-db/LICENSE:   CC-BY-SA
# maxmind-db/MaxMind-DB-spec.md:    CC-BY-SA
License:        Artistic 2.0
URL:            https://metacpan.org/release/MaxMind-DB-Reader
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Reader-%{version}.tar.gz
# Do not use /bin/env in the shebangs
Patch0:         MaxMind-DB-Reader-1.000014-Normalize-shebangs.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::IEEE754)
BuildRequires:  perl(Data::Printer)
BuildRequires:  perl(Data::Validate::IP) >= 0.25
BuildRequires:  perl(Encode)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MaxMind::DB::Common) >= 0.040001
BuildRequires:  perl(MaxMind::DB::Metadata)
BuildRequires:  perl(MaxMind::DB::Role::Debugs)
BuildRequires:  perl(MaxMind::DB::Types)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Role::Tiny) >= 1.003002
BuildRequires:  perl(Socket) >= 1.87
# Optional run-time:
BuildRequires:  perl(DateTime)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Path::Class) >= 0.27
BuildRequires:  perl(Scalar::Util) >= 1.42
BuildRequires:  perl(Test::Bits)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MaxMind::DB::Common::Data)
BuildRequires:  perl(Test::MaxMind::DB::Common::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
%if %{with perl_MaxMind_DB_Reader_enables_optional_test}
# Optional tests:
# Math::Int128 is not available on 32-bit platforms
%ifnarch %{ix86} %{arm}
BuildRequires:  perl(Math::Int128)
BuildRequires:  perl(Net::Works::Network) >= 0.21
%endif
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Recommends:     perl(DateTime)
Suggests:       perl(MaxMind::DB::Reader::XS) >= 1.000003

%description
This module provides a low-level interface to the MaxMind database file format
<http://maxmind.github.io/MaxMind-DB/>.

%prep
%setup -q -n MaxMind-DB-Reader-%{version}
%patch0 -p1
chmod -x eg/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes eg CONTRIBUTING.md README.md
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Petr Pisar <ppisar@redhat.com> 1.000014-1
- Specfile autogenerated by cpanspec 1.78.
