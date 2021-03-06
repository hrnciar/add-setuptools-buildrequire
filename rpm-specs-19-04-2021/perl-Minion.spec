Name:           perl-Minion
Version:        10.21
Release:        1%{?dist}
Summary:        High performance job queue for the Perl programming language
License:        Artistic 2.0 and MIT and OFL

URL:            https://metacpan.org/release/Minion
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/Minion-%{version}.tar.gz

BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Date)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::Pg)
BuildRequires:  perl(Mojo::Server)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious::Command)
BuildRequires:  perl(Mojolicious::Commands)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(YAML::XS) >= 0.67
# Tests
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
Minion is a high performance job queue for the Perl programming language,
with support for multiple named queues, priorities, delayed jobs, job
dependencies, job progress, job results, retries with back-off, rate
limiting, unique jobs, statistics, distributed workers, parallel
processing, auto-scaling, remote control, Mojolicious admin UI, resource
leak protection and multiple backends (such as PostgreSQL).

%prep
%setup -q -n Minion-%{version}
chmod -x lib/Mojolicious/Plugin/Minion/resources/public/minion/epoch/*

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build}

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Minion*
%{perl_vendorlib}/Mojolicious/Plugin/Minion*
%{_mandir}/man3/Minion*
%{_mandir}/man3/Mojolicious::Plugin::Minion*

%changelog
* Sun Mar 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 10.21-1
- Update to 10.21

* Sun Mar 14 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 10.20-1
- Update to 10.20

* Sun Mar 14 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 10.19-1
- Update to 10.19

* Sun Mar 07 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 10.17-1
- Update to 10.17

* Sun Feb 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 10.16-1
- Update to 10.16

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 10.15-1
- Update to 10.15

* Sun Nov 01 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 10.14-1
- Update to 10.14

* Sun Aug 02 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 10.13-1
- Update to 10.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 10.12-1
- Update to 10.12

* Sun Jul 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 10.10-1
- Update to 10.10

* Mon Jun 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 10.08-2
- Perl 5.32 re-rebuild updated packages

* Sun Jun 28 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 10.08-1
- Update to 10.08

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 10.06-2
- Perl 5.32 rebuild

* Sun Jun 14 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 10.06-1
- Update to 10.06

* Sun May 31 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 10.05-1
- Update to 10.05

* Sun Feb 02 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 10.04-1
- Update to 10.04

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 10.02-1
- Update to 10.02

* Sun Nov 17 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 10.0-1
- Update to 10.0

* Sun Sep 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 9.13-1
- Update to 9.13
- Replace calls to "make install" with %%{make_install}
- Replace calls to "make" with %%{make_build}
- Pass NO_PERLLOCAL=1 to Makefile.PL

* Sun Aug 11 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 9.12-1
- Update to 9.12
- Replace calls to %%{__perl} with /usr/bin/perl

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 9.11-1
- Update to 9.11

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 9.10-2
- Perl 5.30 rebuild

* Sun May 19 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 9.10-1
- Update to 9.10

* Sun Feb 03 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 9.09-1
- Update to 9.09

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 21 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 9.07-1
- Update to 9.07

* Sun Sep 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 9.06-1
- Update to 9.06

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 9.03-3
- Perl 5.28 rebuild

* Sat May 19 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 9.03-2
- Take into account review comments (#1578152)

* Mon May 07 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 9.03-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
