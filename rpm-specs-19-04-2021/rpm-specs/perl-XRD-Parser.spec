# Recommend RDF::Trine::Node::Literal::XML for RDFied XML literals
%bcond_without perl_XRD_Parser_enables_literal

Name:           perl-XRD-Parser
Version:        0.201
Release:        5%{?dist}
Summary:        Parse XRD and host-meta files into RDF::Trine models
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/XRD-Parser
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XRD-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(Module::Package::RDF)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Link::Parser) >= 0.102
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Object::AUTHORITY)
BuildRequires:  perl(RDF::Trine) >= 0.135
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.70
# Optional run-time:
%if %{with perl_XRD_Parser_enables_literal}
# RDF::Trine::Node::Literal::XML not used at tests
%endif
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if %{with perl_XRD_Parser_enables_literal}
Recommends:     perl(RDF::Trine::Node::Literal::XML)
%endif

%description
While XRD has a rather different history, it turns out it can mostly be
thought of as a serialization format for a limited subset of RDF.

This parser ignores the order of Link elements, as RDF is a graph format with
no concept of statements coming in an "order". The XRD spec says that grokking
the order of Link elements is only a SHOULD. That said, if you're concerned
about the order of Link elements, the callback routines allowed by this
package may be of use.

This package aims to be roughly compatible with RDF::RDFa::Parser's interface.


%prep
%setup -q -n XRD-Parser-%{version}
# Remove bundled modules
rm -rf inc
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.201-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.201-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.201-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri May 03 2019 Petr Pisar <ppisar@redhat.com> 0.201-1
- Specfile autogenerated by cpanspec 1.78.
