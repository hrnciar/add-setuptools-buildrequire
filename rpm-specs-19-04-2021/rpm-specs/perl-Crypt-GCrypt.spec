# Perform optional tests
%bcond_without perl_Crypt_GCrypt_enables_optional_test

Name:           perl-Crypt-GCrypt
Version:        1.26
Release:        19%{?dist}
Summary:        Perl interface to libgcrypt library
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Crypt-GCrypt
Source0:        https://cpan.metacpan.org/authors/id/A/AA/AAR/Crypt-GCrypt-%{version}.tar.gz
# For libgcrypt >= 1.6, CPAN RT#97201
Patch0:         Crypt-GCrypt-1.26-libgcrypt_1_6_support.diff
# Correct some warnings, CPAN RT#107300
Patch1:         Crypt-GCrypt-1.26-Correct-some-warnings.patch
# Adjust tests to libgcrypt >= 1.7, bug #1399193, CPAN RT#112504
Patch2:         Crypt-GCrypt-1.26-Use-an-encryption-key-in-the-test-suite.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel >= 1.3.0
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::Liblist)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
%if %{with perl_Crypt_GCrypt_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Devel::Size)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(threads)
BuildRequires:  perl(Thread::Queue)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Crypt::GCrypt provides a Perl interface to the libgcrypt cryptographic
functions. It currently supports symmetric ciphers such as AES/Rijndael,
Twofish, Triple DES, Arcfour etc.

%prep
%setup -q -n Crypt-GCrypt-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if !%{with perl_Crypt_GCrypt_enables_optional_test}
rm t/03-pod.t t/04-podcoverage.t t/05-size.t t/07-thread.t
perl -i -ne 'print $_ unless m{t/(?:03-pod|04-podcoverage|05-size|07-thread)\.t}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changelog README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-17
- Perl 5.32 rebuild

* Mon Apr 27 2020 Petr Pisar <ppisar@redhat.com> - 1.26-16
- Modernize a spec file

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Petr Pisar <ppisar@redhat.com> - 1.26-4
- Adjust tests to libgcrypt >= 1.7 (bug #1399193)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Petr Pisar <ppisar@redhat.com> 1.26-1
- Specfile autogenerated by cpanspec 1.78.
- Enable other optional tests
