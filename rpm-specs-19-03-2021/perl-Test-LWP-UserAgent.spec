Name:           perl-Test-LWP-UserAgent
Version:        0.034
Release:        4%{?dist}
Summary:        LWP::UserAgent suitable for simulating and testing network calls
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-LWP-UserAgent
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-LWP-UserAgent-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(parent)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(if)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep) >= 0.110
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Warnings) >= 0.009
# Optional tests
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose::Conflicts)
# Test::RequiresInternet - Optional for tests

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MyApp::Client\\)

%description
This module is a subclass of LWP::UserAgent which overrides a few key low-
level methods that are concerned with actually sending your request over
the network, allowing an interception of that request and simulating a
particular response. This greatly facilitates testing of client networking
code where the server follows a known protocol.

%prep
%setup -q -n Test-LWP-UserAgent-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
NO_NETWORK_TESTING=1 make test

%files
%license LICENCE
%doc Changes CONTRIBUTING docs examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-2
- Perl 5.32 rebuild

* Fri Mar 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-1
- 0.034 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-2
- Perl 5.26 rebuild

* Thu Jun 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-1
- 0.033 bump

* Thu May 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.032-1
- 0.032 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.031-1
- 0.031 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.030-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.030-1
- 0.030 bump

* Fri Jul 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.029-1
- Specfile autogenerated by cpanspec 1.78.
