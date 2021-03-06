Name:           perl-Mojo-SQLite
Version:        3.005
Release:        1%{?dist}
Summary:        Tiny Mojolicious wrapper for SQLite
License:        Artistic 2.0

URL:            https://metacpan.org/release/Mojo-SQLite/
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Mojo-SQLite-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# run deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite) >= 1.64
BuildRequires:  perl(DBI) >= 1.627
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Collection)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(constant)
# test deps
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.69
BuildRequires:  perl(URI::db) >= 0.15
BuildRequires:  perl(URI::file) >= 4.21
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
Mojo::SQLite is a tiny wrapper around DBD::SQLite that makes SQLite a lot
of fun to use with the Mojolicious real-time web framework. Use all SQL
features SQLite has to offer, generate CRUD queries from data structures,
and manage your database schema with migrations.

%prep
%setup -q -n Mojo-SQLite-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 ./Build test

%files
%doc Changes CONTRIBUTING.md README
%license LICENSE
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
* Sun Feb 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 3.005-1
- Update to 3.005

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.004-1
- Update to 3.004

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.003-1
- Update to 3.003
- Replace calls to %%{__perl} with /usr/bin/perl

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.002-1
- Update to 3.002

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.001-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Emmanuel Seyman <emmanuel@seyman.fr> 3.001-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
