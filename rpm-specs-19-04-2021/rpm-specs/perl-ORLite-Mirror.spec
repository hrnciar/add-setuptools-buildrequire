Name:           perl-ORLite-Mirror
Version:        1.24
Release:        24%{?dist}
Summary:        Extend ORLite to support remote SQLite databases
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ORLite-Mirror
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/ORLite-Mirror-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir) >= 0.69
BuildRequires:  perl(File::Path) >= 2.04
BuildRequires:  perl(File::Remove) >= 1.42
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Compress::Bzip2) >= 2.008
BuildRequires:  perl(IO::Compress::Gzip) >= 2.008
BuildRequires:  perl(IO::Uncompress::Bunzip2) >= 2.008
BuildRequires:  perl(IO::Uncompress::Gunzip) >= 2.008
BuildRequires:  perl(inc::Module::Install::DSL) >= 1.06
BuildRequires:  perl(LWP::Online) >= 1.07
BuildRequires:  perl(LWP::UserAgent) >= 5.806
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Share)
BuildRequires:  perl(Module::Install::With)
BuildRequires:  perl(ORLite) >= 1.37
BuildRequires:  perl(Params::Util) >= 0.33
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI) >= 1.35
BuildRequires:  perl(URI::file)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
ORLite provides a read-only ORM API when it loads a read-only SQLite database
from your local system. By combining this capability with LWP, ORLite::Mirror
goes one step better and allows you to load a SQLite database from any
arbitrary URI in read-only form as well.

%prep
%setup -q -n ORLite-Mirror-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name stub.db -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-19
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-16
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-13
- Perl 5.26 rebuild

* Thu May 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-12
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-7
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.24-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Iain Arnell <iarnell@gmail.com> 1.24-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.23-2
- Perl 5.16 rebuild

* Fri Feb 03 2012 Iain Arnell <iarnell@gmail.com> 1.23-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Iain Arnell <iarnell@gmail.com> 1.22-1
- update to latest upstream
- drop proxy patch as proxy support is included now

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.21-2
- Perl mass rebuild

* Sun Jun 05 2011 Iain Arnell <iarnell@gmail.com> 1.21-1
- update to latest upstream version

* Tue May 10 2011 Iain Arnell <iarnell@gmail.com> 1.20-4
- add proxy support (rt #61795)

* Tue Apr 26 2011 Iain Arnell <iarnell@gmail.com> 1.20-3
- don't install the test stub.db

* Mon Apr 25 2011 Iain Arnell <iarnell@gmail.com> 1.20-2
- fix spelling in description

* Sun Apr 24 2011 Iain Arnell <iarnell@gmail.com> 1.20-1
- Specfile autogenerated by cpanspec 1.79.
