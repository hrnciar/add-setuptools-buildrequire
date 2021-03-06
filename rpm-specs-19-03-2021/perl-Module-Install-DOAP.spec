Name:           perl-Module-Install-DOAP
Version:        0.006
Release:        14%{?dist}
Summary:        Generate META.yml data from DOAP
# COPYRIGHT:    Public Domain
# other files:  GPL+ or Artistic
License:        (GPL+ or Artistic) and Public Domain
URL:            https://metacpan.org/release/Module-Install-DOAP
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-DOAP-%{version}.tar.gz
# Break build cycle
Patch0:         Module-Install-DOAP-0.006-Break-build-cycle-with-Module-Package-RDF.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Install::Admin::RDF) >= 0.004
# Module::Install::Base version from Module::Install in META
BuildRequires:  perl(Module::Install::Base) >= 1.00
BuildRequires:  perl(RDF::Trine) >= 0.133
BuildRequires:  perl(RDF::Trine::Namespace)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Module::Install::Admin::RDF) >= 0.004
# Module::Install::Base version from Module::Install in META
Requires:       perl(Module::Install::Base) >= 1.00
Requires:       perl(RDF::Trine) >= 0.133

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::Install::Admin::RDF|Module::Install::Base|RDF::Trine)\\)

%description
This Module::Install plugin generates your META.yml file from RDF data
(especially DOAP) in your distribution's "meta" directory.

%prep
%setup -q -n Module-Install-DOAP-%{version}
%patch0 -p1
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 01 2016 Petr Pisar <ppisar@redhat.com> 0.006-1
- Specfile autogenerated by cpanspec 1.78.
