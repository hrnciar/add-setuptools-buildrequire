## Run optional test
#%%bcond_without perl_MooseX_Util_enables_optional_test

Name:           perl-MooseX-Util
Version:        0.006
Release:        12%{?dist}
Summary:        Moose::Util extensions
License:        LGPLv2
URL:            https://metacpan.org/release/MooseX-Util
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-Util-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::TraitFor::Meta::Class::BetterAnonClassNames) >= 0.002001
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(Sub::Exporter::Progressive)
# Tests:
BuildRequires:  perl(aliased)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::Moose::More) >= 0.016
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Requires)
#%%if %%{with perl_MooseX_Util_enables_optional_test} 
# Optional tests:
# Reindeer not yet packaged
# Reindeer::Role not yet packaged
#%%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Moose::Meta::Class)
Requires:       perl(MooseX::TraitFor::Meta::Class::BetterAnonClassNames) >= 0.002001

%description
This Perl module handles all of the same functions that Moose::Util handles.
In fact, most of the functions are simply re-exports from Moose::Util.
However, we've re-implemented a number of the functions, for a variety of
reasons.

%prep
%setup -q -n MooseX-Util-%{version}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-10
- Perl 5.32 rebuild

* Wed Mar 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-9
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Petr Pisar <ppisar@redhat.com> 0.006-1
- Specfile autogenerated by cpanspec 1.78.
