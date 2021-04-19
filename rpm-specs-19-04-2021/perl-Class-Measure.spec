Name:           perl-Class-Measure
Version:        0.09
Release:        1%{?dist}
Summary:        Create, compare and convert units of measurement
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Class-Measure
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/Class-Measure-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter) >= 0.982
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test2::V0) >= 0.000094
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Sub::Exporter) >= 0.982

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Sub::Exporter\\)

%description
This Perl module allows you to create, compare and convert units of
measurement.

%prep
%setup -q -n Class-Measure-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Feb 01 2021 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-2
- Perl 5.30 rebuild

* Thu Mar 14 2019 Petr Pisar <ppisar@redhat.com> - 0.07-1
- 0.07 bump

* Fri Mar 08 2019 Petr Pisar <ppisar@redhat.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.