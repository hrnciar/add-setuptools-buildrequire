Name:           perl-Test-Mock-Time
Version:        0.1.7
Release:        11%{?dist}
Summary:        Deterministic time & timers for event loop tests
License:        MIT

URL:            https://metacpan.org/release/Test-Mock-Time
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POWERMAN/Test-Mock-Time-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Export::Attrs)
BuildRequires:  perl(EV)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Mojolicious) >= 6
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(bignum)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module replaces actual time with simulated time everywhere (core
time(), Time::HiRes, EV, AnyEvent with EV, Mojolicious, …) and provide
a way to write deterministic tests for event loop based applications
with timers.

%prep
%setup -q -n Test-Mock-Time-v%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
AUTHOR_TESTING=1 RELEASE_TESTING=1 ./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.7-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.7-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.7-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.1.7-1
- Update to 0.1.7

* Tue Nov 28 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.1.6-2
- Take into account review feedback (#1517102)

* Fri Nov 24 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.1.6-1
- Specfile autogenerated by cpanspec 1.78.
