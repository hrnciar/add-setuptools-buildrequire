Name:           perl-DateTime-Format-Atom
Version:        1.2.0
Release:        16%{?dist}
Summary:        Parse and format Atom date-time strings
License:        CC0
URL:            https://metacpan.org/release/DateTime-Format-Atom
Source0:        https://cpan.metacpan.org/authors/id/I/IK/IKEGAMI/DateTime-Format-Atom-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime::Format::RFC3339)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(DateTime)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.22
# Test::Pod::Coverage 1.08 not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This Perl module understands the Atom date/time format, an ISO 8601 profile,
defined at <http://tools.ietf.org/html/rfc4287>.

%prep
%setup -q -n DateTime-Format-Atom-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE.txt
%doc Changes README.txt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Petr Pisar <ppisar@redhat.com> - 1.2.0-1
- 1.2.0 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.2-2
- Perl 5.22 rebuild

* Mon Mar 02 2015 Petr Pisar <ppisar@redhat.com> 1.0.2-1
- Specfile autogenerated by cpanspec 1.78.