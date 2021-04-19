# Enable JSON support
%bcond_without perl_CryptX_enables_json
# Run optional test
%bcond_without perl_CryptX_enables_optional_test

Name:           perl-CryptX
Version:        0.053
Release:        19%{?dist}
Summary:        Cryptographic toolkit
# Other file:   GPL+ or Artistic
## Unbundled
# src/ltc/hashes/blake2s.c: CC0 or OpenSSL or ASL 2.0
# src/ltc/stream/rc4/rc4.c: Public Domain
# src/ltm/bncore.c:         Public Domain
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CryptX
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/CryptX-%{version}.tar.gz
# Unbundle libtomcrypt,
# libtomcrypt-1.8.2 is missing features needed by CryptX.
# CryptX-0.057 is incompatible with libtomcrypt-1.8.2, it requires
# <https://github.com/libtom/libtomcrypt/commit/24c0eb84f989de52c53f7129704dd7322296f3be>
# to be merged from a "develop" branch into a "master" libtomcrypt branch and
# to be released.
Patch0:         CryptX-0.053-Disable-ECC-and-unbundle-libtomcrypt.patch
# Validate decode_b58b input properly, in upstream 0.058
Patch1:         CryptX-0.053-bug-decode_b58b-invalid-input.patch
# Adapt tests to changes in Math::BigInt 1.999813, in upstream 0.060
Patch2:         CryptX-0.059-remove-buggy-Math-BigInt-related-tests.patch
# Adapt to changes in libtomcrypt 1.18.2, bug #1605403, in upstream after 0.060
Patch3:         CryptX-0.053-adopt-to-the-new-libtomcrypt.patch
# Adapt to changes in Math-BigInt 1.999815, in upstream after 0.062,
# <https://github.com/DCIT/perl-CryptX/issues/46>
Patch4:         CryptX-0.053-Math-BigInt-LTM-proper-fix-for-46.patch
# Adapt to changes in Math-BigInt 1.999815, in upstream after 0.062,
# <https://github.com/DCIT/perl-CryptX/issues/46>
Patch5:         CryptX-0.062-HACK-needed-for-MBI-1.999715-compatibility.patch
# Adapt to changes in Math-BigInt 1.999817, bug #1769850,
# in upstream after 0.064, <https://github.com/DCIT/perl-CryptX/issues/56>
Patch6:         CryptX-0.064-fix-56-Math-BigInt-1.999817-breaks-the-tests-of-Cryp.patch
# Fix handling PEM decoding failures, in upstream 0.071,
# <https://github.com/DCIT/perl-CryptX/issues/67>
Patch7:         CryptX-0.053-fix-67-better-handling-of-PEM-decoding-failures.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtomcrypt-devel
BuildRequires:  libtommath-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Optional run-time:
%if %{with perl_CryptX_enables_json}
# Cpanel::JSON::XS or JSON::XS or JSON::PP
BuildRequires:  perl(Cpanel::JSON::XS)
%endif
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
%if %{with perl_CryptX_enables_optional_test}
# Optional tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Math::BigFloat) >= 1.999715
BuildRequires:  perl(Math::BigInt) >= 1.9997
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Storable) >= 2.0
BuildRequires:  perl(Test::Pod)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if %{with perl_CryptX_enables_json}
# Cpanel::JSON::XS or JSON::XS or JSON::PP
Recommends:     perl(Cpanel::JSON::XS)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Math::BigFloat|Math::BigInt|Storable)\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(\\.::
# Remove disabled modules, libtomcrypt-1.8.2 does not support ECC
%global __requires_exclude %{__requires_exclude}|^perl\\(Crypt::PK::ECC\\)

%description
This Perl library provides a cryptography based on LibTomCrypt library.

ECC support is disabled because it's not yet fully supported by LibTomCrypt.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_CryptX_enables_json}
# Cpanel::JSON::XS or JSON::XS or JSON::PP
Requires:       perl(Cpanel::JSON::XS)
%endif
%if %{with perl_CryptX_enables_optional_test}
Requires:       perl(File::Find)
Requires:       perl(Math::BigFloat) >= 1.999715
Requires:       perl(Math::BigInt) >= 1.9997
Requires:       perl(Math::Complex)
Requires:       perl(Storable) >= 2.0
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n CryptX-%{version}
# Unbundle libtomcrypt and libtommath
%patch0 -p1
rm -rf ./src
perl -i -ne 'print $_ unless m{\A(?:src/|lib/Crypt/PK/ECC\.pm)}' MANIFEST
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
# Remove t/wycheproof.t test. It was removed by upstream in
# cf2422dc467f1e10a8c20cd362f7b3b296c24529 comit and the test reveals a bug in
# libtommath-1.2.0, bug #1850650, not related to perl-CryptX, bug #1850379.
rm t/wycheproof.t
perl -i -ne 'print $_ unless m{^t/wycheproof\.t\b}' MANIFEST
# Fix permissions
chmod -x t/data/openssl_rsa-x509.pem
# Remove unsed tests
%if !%{with perl_CryptX_enables_optional_test}
for F in t/002_all_pm.t t/003_all_pm_pod.t t/mbi_ltm_bigfltpm.t \
        t/mbi_ltm_bigintpm.t t/mbi_ltm_biglog.t t/mbi_ltm_bigroot.t \
        t/mbi_ltm/bigintpm.inc t/mbi_ltm/bigfltpm.inc t/mbi_ltm_storable.t; do
    rm "${F}"
    perl -i -ne 'print $_ unless m{\A\Q'"${F}"'\E}' MANIFEST
done
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_CryptX_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/{002_all_pm,003_all_pm_pod}.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/crypt-misc.t writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/CryptX.pm
%{perl_vendorarch}/Math
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 30 2021 Petr Pisar <ppisar@redhat.com> - 0.053-19
- Fix handling PEM decoding failures (upstream bug #67)
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.053-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.053-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.053-16
- Perl 5.32 rebuild

* Wed Jun 24 2020 Petr Pisar <ppisar@redhat.com> - 0.053-15
- Remove t/wycheproof.t test (bug #1850379)

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.053-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.053-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Petr Pisar <ppisar@redhat.com> - 0.053-12
- Adapt to changes in Math-BigInt 1.999817 (bug #1769850)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.053-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Petr Pisar <ppisar@redhat.com> - 0.053-10
- Require Math::Complex for running tests

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.053-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.053-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Petr Pisar <ppisar@redhat.com> - 0.053-7
- Adapt to changes in libtomcrypt-1.18.2 (bug #1605403)
- Adapt to changes in Math-BigInt-1.999815

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.053-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.053-5
- Perl 5.28 rebuild

* Thu May 03 2018 Petr Pisar <ppisar@redhat.com> - 0.053-4
- Adapt tests to changes in Math::BigInt 1.999813

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 0.053-3
- Rebuild with new redhat-rpm-config/perl build flags

* Wed Feb 28 2018 Petr Pisar <ppisar@redhat.com> - 0.053-2
- Validate decode_b58b input properly

* Thu Feb 15 2018 Petr Pisar <ppisar@redhat.com> 0.053-1
- Specfile autogenerated by cpanspec 1.78.
