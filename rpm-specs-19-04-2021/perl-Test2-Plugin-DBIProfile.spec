Name:           perl-Test2-Plugin-DBIProfile
%global cpan_version 0.002003
Version:        0.2.3
Release:        5%{?dist}
Summary:        Test2 plugin to enable and display DBI profiling
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test2-Plugin-DBIProfile
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-DBIProfile-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.9
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(DBI::Profile)
BuildRequires:  perl(Test2::API) >= 1.302165
BuildRequires:  perl(Test2::Util::Times) >= 0.000126
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite) >= 1.44
BuildRequires:  perl(DBI)
# Test2::Tools::Basic version from Test2::V0 in META
BuildRequires:  perl(Test2::Tools::Basic) >= 0.000124
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Defer)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Test2::API) >= 1.302165
Requires:       perl(Test2::Util::Times) >= 0.000126
# Removed from perl-Test2-Harness-0.001083
Conflicts:      perl-Test2-Harness < 0.001083

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test2::API|Test2::Util::Times)\\)$

%description
This Test2 plugin enables DBI::Profile globally so that DBI profiling data is
collected. Once testing is complete an event will be produced which contains
and displays the profiling data.

%prep
%setup -q -n Test2-Plugin-DBIProfile-%{cpan_version}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.3-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Petr Pisar <ppisar@redhat.com> - 0.2.3-1
- 0.002003 bump

* Mon Aug 26 2019 Petr Pisar <ppisar@redhat.com> - 0.2.2-1
- 0.002002 bump

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> 0.2.1-1
- Specfile autogenerated by cpanspec 1.78.
