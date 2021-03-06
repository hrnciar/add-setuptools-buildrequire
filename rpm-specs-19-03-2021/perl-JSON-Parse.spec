Name:           perl-JSON-Parse
Version:        0.61
Release:        1%{?dist}
Summary:        Read JSON into a Perl variable
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/JSON-Parse
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/JSON-Parse-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
A Perl module for parsing JSON. (JSON means "JavaScript Object Notation" and it
is specified in "RFC 7159".)

%prep
%setup -q -n JSON-Parse-%{version}
/usr/bin/perl -pi -e 's#/home/ben/software/install/bin/perl#/usr/bin/perl#' script/* examples/*
/usr/bin/chmod -x examples/tokenize-synopsis.pl

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/JSON*
%{_mandir}/man3/*
%{_bindir}/validjson

%changelog
* Sun Feb 14 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.61-1
- Update to 0.61

* Sun Jan 31 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.60-1
- Update to 0.60

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.59-1
- Update to 0.59

* Sun Jan 03 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.58-1
- Update to 0.58

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.57-1
- Update to 0.57

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-2
- Perl 5.32 rebuild

* Thu Feb 20 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.56-1
- Update to 0.56
- Use /usr/bin/perl instead of %/usr/bin/perl
- Pass NO_PERLLOCAL=1 to Makefile.PL
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 29 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.55-1
- Update to 0.55

* Fri Oct 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-1
- 0.54 bump

* Fri Aug 18 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.49-2
- Take into account review comments (#1482867)

* Sun Jul 30 2017 Emmanuel Seyman <emmanuel@seyman.fr> 0.49-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
