Name:           perl-Test2-Plugin-UUID
%global cpan_version 0.002001
Version:        0.2.1
Release:        5%{?dist}
Summary:        Use real UUIDs in Test2
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test2-Plugin-UUID
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-UUID-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.9
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Rub-time:
BuildRequires:  perl(Data::UUID) >= 1.148
BuildRequires:  perl(Test2::API) >= 1.302165
BuildRequires:  perl(Test2::Hub)
# Tests:
BuildRequires:  perl(Test2::V0) >= 0.000124
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::UUID) >= 1.148
Requires:       perl(Test2::API) >= 1.302165
Requires:       perl(Test2::Hub)
# Removed from perl-Test2-Harness-0.001083
Conflicts:      perl-Test2-Harness < 0.001083

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::UUID|Test2::API)\\)$

%description
Test2 normally uses unique IDs generated by appending PID, thread ID, and an
incrementing integer. These work fine most of the time, but are not sufficient
if you want to keep a database of events, in that case a real UUID is much
more useful.

%prep
%setup -q -n Test2-Plugin-UUID-%{cpan_version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> 0.2.1-1
- Specfile autogenerated by cpanspec 1.78.
