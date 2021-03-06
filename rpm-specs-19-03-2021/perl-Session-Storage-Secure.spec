Name:           perl-Session-Storage-Secure
Version:        0.011
Release:        11%{?dist}
Summary:        Encrypted, expiring, compressed, serialized session data with integrity
License:        ASL 2.0
URL:            https://metacpan.org/release/Session-Storage-Secure
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Session-Storage-Secure-%{version}.tar.gz
# Suppress a Crypt::CBC warning about deprecated opensslv1 PBKDF, bug #1939427,
# proposed to the upstream
# <https://github.com/dagolden/Session-Storage-Secure/issues/8>.
Patch0:         Session-Storage-Secure-0.011-Silent-Crypt-CBC-encode-warning-about-deprecated-ope.patch
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
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Math::Random::ISAAC::XS)
BuildRequires:  perl(MIME::Base64) >= 3.12
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base) >= 0.16
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Sereal::Decoder) >= 4.005
BuildRequires:  perl(Sereal::Encoder) >= 4.005
BuildRequires:  perl(String::Compare::ConstantTime)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tolerant)
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Sereal::Decoder) >= 4.005
Requires:       perl(Sereal::Encoder) >= 4.005

# Remove under-specified dependencies
%global __requieres_exclude %{?__requieres_exclude:%{__requieres_exclude}|}^perl\\(Sereal::Decoder|Sereal::Encoder\\)$

%description
This module implements a secure way to encode session data. It is primarily
intended for storing session data in browser cookies, but could be used
with other back-end storage where security of stored session data is
important.

%prep
%setup -q -n Session-Storage-Secure-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 16 2021 Petr Pisar <ppisar@redhat.com> - 0.011-11
- Suppress a Crypt::CBC warning about deprecated opensslv1 PBKDF (bug #1939427)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.011-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.011-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.011-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-2
- Perl 5.28 rebuild

* Fri May 04 2018 Petr Pisar <ppisar@redhat.com> - 0.011-1
- 0.011 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-2
- Perl 5.22 rebuild

* Fri Oct 10 2014 Petr Pisar <ppisar@redhat.com> 0.010-1
- Specfile autogenerated by cpanspec 1.78.
