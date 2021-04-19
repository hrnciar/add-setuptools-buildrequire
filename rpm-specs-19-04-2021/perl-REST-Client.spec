Name:           perl-REST-Client
Version:        273
Release:        18%{?dist}
Summary:        Simple client for interacting with RESTful http/https resources
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/REST-Client
Source0:        https://cpan.metacpan.org/authors/id/K/KK/KKANE/REST-Client-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.8
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML)
Requires:       perl(XML::LibXML)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%description
REST::Client provides a simple way to interact with HTTP RESTful resources.

%prep
%setup -q -n REST-Client-%{version}
# Remove bundled libraries
/usr/bin/rm -r inc
/usr/bin/perl -pi -e 's/^inc\/.*//' MANIFEST

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 273-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 273-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 273-16
- Perl 5.32 rebuild

* Wed Feb 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 273-15
- Use Source link as listed on metacpan project page
- Replace calls to %%{__perl} with /usr/bin/perl
- Pass NO_PACKLIST=1 NO_PERLLOCAL=1 to Makefile.PL
- Replace calls to "make install" with %%{make_install}
- Replace calls to make with %%{make_build}

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 273-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 273-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 273-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 273-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 273-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 273-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 273-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 273-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 273-6
- Perl 5.26 rebuild

* Thu May 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 273-5
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 273-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 273-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 273-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 273-1
- 273 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 272-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 272-2
- Perl 5.22 rebuild

* Wed Jan 14 2015 David Dick <ddick@cpan.org> - 272-1
- Update to 272

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 271-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 271-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 David Dick <ddick@cpan.org> - 271-1
- Initial release
