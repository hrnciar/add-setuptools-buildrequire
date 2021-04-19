Name:           perl-DBIx-Connector
Version:        0.56
Release:        15%{?dist}
Summary:        Fast, safe DBI connection and transaction management
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DBIx-Connector

Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/DBIx-Connector-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI) >= 1.614

# Testing
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::MockModule)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Carp)

%description
DBIx::Connector provides a simple interface for fast and safe DBI
connection and transaction management. It allows to keep a database
handle to maintain a connection in order to minimize overhead without
having to worry about dropped or corrupted connections.

Borrowing an interface from DBIx::Class, DBIx::Connector also offers
an API that handles the scoping of database transactions. In addition,
it offers an API for savepoints if a database supports them.


%prep
%setup -q -n DBIx-Connector-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# skipped 't/svp_live.t' since requires a real db
./Build test


%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-2
- Perl 5.24 rebuild

* Mon Mar 21 2016 Denis Fateyev <denis@fateyev.com> - 0.56-1
- Update to 0.56 release

* Sat Feb 06 2016 Denis Fateyev <denis@fateyev.com> - 0.55-1
- Update to 0.55 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-3
- Perl 5.22 rebuild

* Sun Sep 14 2014 Denis Fateyev <denis@fateyev.com> - 0.53-2
- Add BuildRequires, spec cleanup

* Fri Sep 12 2014 Denis Fateyev <denis@fateyev.com> - 0.53-1
- Initial release
