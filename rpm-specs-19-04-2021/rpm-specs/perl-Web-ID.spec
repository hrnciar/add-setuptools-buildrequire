Name:           perl-Web-ID
Version:        1.927
Release:        8%{?dist}
Summary:        Implementation of WebID (a.k.a. FOAF+SSL)
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Web-ID/
Source0:        http://www.cpan.org/modules/by-module/Web/Web-ID-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(Crypt::X509)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(match::simple) >= 0.008
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moose) >= 2.0600
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(namespace::sweep)
BuildRequires:  perl(Path::Tiny) >= 0.017
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(RDF::Query) >= 2.900
BuildRequires:  perl(RDF::Trine) >= 1.000
BuildRequires:  perl(RDF::Trine::NamespaceMap)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Types::DateTime)
BuildRequires:  perl(Types::Standard) >= 0.040
BuildRequires:  perl(Types::URI)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
WebID is a simple authentication protocol based on TLS (Transaction Layer
Security, better known as Secure Socket Layer, SSL) and the Semantic Web.
This module provides a Perl implementation for authenticating clients
using WebID.

%prep
%setup -q -n Web-ID-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.927-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.927-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.927-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.927-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.927-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.927-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.927-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Xavier Bachelot <xavier@bachelot.org> 1.927-1
- Initial package.
