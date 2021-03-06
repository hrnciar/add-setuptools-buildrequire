Name:           perl-RDF-Trine-Node-Literal-XML
Version:        0.16
Release:        7%{?dist}
Summary:        RDF node class for XML literals
# Makefile.PL:  GPL+ or Artistic
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/RDF-Trine-Node-Literal-XML
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-Trine-Node-Literal-XML-%{version}.tar.gz
# Remove build-time dependencies not needed for packaging
Patch0:         RDF-Trine-Node-Literal-XML-0.16-Disable-release-management-in-Makefile.PL.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  libxml2 >= 2.6.27
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(XML::LibXML)
# Run-time:
BuildRequires:  perl(base)
# RDF::Trine::Error version from RDF::Trine in META
BuildRequires:  perl(RDF::Trine::Error) >= 0.111
BuildRequires:  perl(RDF::Trine::Node::Literal)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings)
Requires:       libxml2 >= 2.6.27
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# RDF::Trine::Error version from RDF::Trine in META
Requires:       perl(RDF::Trine::Error) >= 0.111

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(RDF::Trine::Error\\)$

%description
This Perl module encapsulates XML literals into RDF objects.

%prep
%setup -q -n RDF-Trine-Node-Literal-XML-%{version}
%patch0 -p1
# Remove bunlded modules
rm -rf inc/*
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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.30 rebuild

* Thu May 02 2019 Petr Pisar <ppisar@redhat.com> 0.16-1
- Specfile autogenerated by cpanspec 1.78.
