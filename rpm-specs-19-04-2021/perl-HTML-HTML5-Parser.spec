Name:           perl-HTML-HTML5-Parser
Version:        0.301
Release:        14%{?dist}
Summary:        Parse HTML reliably
# COPYRIGHT:    Public Domain
# other files:  GPL+ or Artistic
License:        (GPL+ or Artistic) and Public Domain
URL:            https://metacpan.org/release/HTML-HTML5-Parser
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Parser-%{version}.tar.gz
# Break build cycle with Module-Package-RDF
Patch0:         HTML-HTML5-Parser-0.301-Break-build-cycle-with-Module-Package-RDF.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Encoding)
# These Encode modules do not exist, CPAN RT#118661
# Encode::EUCJP1997 does not exist
# Encode::GLJIS1978 does not exist
# Encode::GLJIS1983 does not exist
# Encode::GLJIS1997 does not exist
# Encode::GLJIS1997Swapped does not exist
# Encode::ShiftJIS1997 does not exist
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(HTML::HTML5::Entities) >= 0.002
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::HTML)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.94
BuildRequires:  perl(XML::LibXML::Devel)
# Optional run-time:
BuildRequires:  perl(XML::LibXML::Devel::SetLineNumber)
# Tests:
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.61
# Optional tests:
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(URI::Escape)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper)
Requires:       perl(Exporter)
Requires:       perl(HTML::HTML5::Entities) >= 0.002
Requires:       perl(XML::LibXML) >= 1.94
Recommends:     perl(XML::LibXML::Devel::SetLineNumber)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((HTML::HTML5::Entities|XML::LibXML)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(HTML::HTML5::Parser::TagSoupParser\\)$

%description
HTML parser with XML::LibXML-like DOM interface.

%prep
%setup -q -n HTML-HTML5-Parser-%{version}
%patch0 -p1
# Remove bundled modules
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS NEWS README TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.301-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.301-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.301-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.301-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.301-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Petr Pisar <ppisar@redhat.com> 0.301-1
- Specfile autogenerated by cpanspec 1.78.
