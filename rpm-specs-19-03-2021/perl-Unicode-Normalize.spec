%global base_version 1.25
Name:           perl-Unicode-Normalize
Version:        1.27
Release:        459%{?dist}
Summary:        Unicode Normalization Forms
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Unicode-Normalize
Source0:        https://cpan.metacpan.org/authors/id/K/KH/KHW/Unicode-Normalize-%{base_version}.tar.gz
# Unbundled from perl 5.28.0-RC1
Patch0:         Unicode-Normalize-1.25-Upgrade-to-1.26.patch
# Unbundled from perl 5.32.0
Patch1:         Unicode-Normalize-1.25-Upgrade-to-1.27.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# unicore/CombiningClass.pl and unicore/Decomposition.pl from perl-libs
BuildRequires:  perl-libs
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Conflicts:      perl < 4:5.22.0-347

%description
This package provides Perl functions that can convert strings into various
Unicode normalization forms as defined in Unicode Standard Annex #15.

%prep
%setup -q -n Unicode-Normalize-%{base_version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Unicode
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-459
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-458
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Petr Pisar <ppisar@redhat.com> - 1.27-457
- Modernize a spec file
- Apply a forgotten Unicode-Normalize-1.25-Upgrade-to-1.27.patch patch

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-456
- Upgrade to 1.27 as provided in perl-5.32.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-416
- Increase release to favour standalone package

* Thu May 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-1
- Upgrade to 1.26 as provided in perl-5.28.0-RC1

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 1.25-397
- Modernize spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-393
- Perl 5.26 rebuild

* Mon May 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-367
- Fixes for removal '.' from @INC in Perl 5.26

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Petr ??abata <contyk@redhat.com> - 1.25-1
- 1.25 bump

* Thu Dec 03 2015 Petr Pisar <ppisar@redhat.com> - 1.24-1
- 1.24 bump

* Tue Oct 27 2015 Petr Pisar <ppisar@redhat.com> - 1.23-1
- 1.23 bump

* Fri Oct 09 2015 Petr Pisar <ppisar@redhat.com> - 1.21-1
- 1.21 bump

* Mon Jul 13 2015 Petr Pisar <ppisar@redhat.com> - 1.19-1
- 1.19 bump

* Thu Jul 02 2015 Petr Pisar <ppisar@redhat.com> 1.18-348
- Specfile autogenerated by cpanspec 1.78.
