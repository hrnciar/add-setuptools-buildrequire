Name:           perl-XMLRPC-Lite
Version:        0.717
Release:        20%{?dist}
Summary:        Client and server implementation of XML-RPC protocol
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/XMLRPC-Lite
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/XMLRPC-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(SOAP)
BuildRequires:  perl(SOAP::Data)
BuildRequires:  perl(SOAP::Deserializer)
BuildRequires:  perl(SOAP::Lite) >= 0.716
BuildRequires:  perl(SOAP::Serializer)
BuildRequires:  perl(SOAP::Server)
BuildRequires:  perl(SOAP::Server::Parameters)
BuildRequires:  perl(SOAP::SOM)
BuildRequires:  perl(SOAP::Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(MIME::Base64)
Requires:       perl(SOAP)
Requires:       perl(SOAP::Data)
Requires:       perl(SOAP::Deserializer)
Requires:       perl(SOAP::Lite) >= 0.716
Requires:       perl(SOAP::Serializer)
Requires:       perl(SOAP::Server)
Requires:       perl(SOAP::Server::Parameters)
Requires:       perl(SOAP::SOM)
Requires:       perl(SOAP::Transport::HTTP::Apache)
Requires:       perl(SOAP::Transport::HTTP::CGI)
Requires:       perl(SOAP::Transport::HTTP::Daemon)
Requires:       perl(SOAP::Transport::POP3::Server)
Requires:       perl(SOAP::Transport::TCP) >= 0.715
Requires:       perl(SOAP::Transport::TCP::Server)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(My::.*\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(SOAP::Lite\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(SOAP::Transport::TCP\\)

%description
XMLRPC::Lite is a Perl modules which provides a simple interface to the XML-
RPC protocol both on client and server side. Based on SOAP::Lite module, it
gives you access to all features and transports available in that module.

%prep
%setup -q -n XMLRPC-Lite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.717-18
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.717-15
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.717-12
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.717-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.717-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.717-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.717-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.717-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.717-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.717-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 08 2013 Petr Šabata <contyk@redhat.com> 0.717-1
- Specfile autogenerated by cpanspec 1.78.