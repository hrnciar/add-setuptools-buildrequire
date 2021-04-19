Name:           perl-Convert-Color-XTerm
Version:        0.05
Release:        5%{?dist}
Summary:        Indexed colors used by XTerm
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Convert-Color-XTerm/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Convert-Color-XTerm-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::Color::RGB8) >= 0.06
# Optional - not used for build - perl(Convert::Color::X11)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Convert::Color::RGB)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Convert::Color::RGB8) >= 0.06
Suggests:       perl(Convert::Color::X11)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Convert::Color::RGB8\\)$

%description
This subclass of Convert::Color::RGB8 provides lookup of the colors that
xterm uses by default. Note that the module is not intelligent enough to
actually parse the XTerm configuration on a machine, nor to query a running
terminal for its actual colors. It simply implements the colors that are
present as defaults in the XTerm source code.

%prep
%setup -q -n Convert-Color-XTerm-%{version}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-1
- Specfile autogenerated by cpanspec 1.78.
- Packaging corrected according to the package review (bug #1732821)