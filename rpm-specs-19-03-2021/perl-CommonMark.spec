Name:           perl-CommonMark
Version:        0.290000
Release:        8%{?dist}
Summary:        Interface to the CommonMark C library
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/CommonMark
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/CommonMark-%{version}.tar.gz

# build requirements
BuildRequires:  cmark-devel >= 0.21.0
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Encode)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%description
This module is a wrapper around the official CommonMark C library libcmark.
It closely follows the original API.

%prep
%setup -q -n CommonMark-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} %{?_smp_mflags}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/CommonMark*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.290000-6
- Perl 5.32 rebuild

* Tue Feb 04 2020 Petr Pisar <ppisar@redhat.com> - 0.290000-5
- Rebuild against cmark 0.29.0 (bug #1697593)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.290000-3
- Pass NO_PERLLOCAL to Makefile.PL
- Use %%{make_install} instead of make install (thanks to ppisar)

* Thu Aug 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.290000-2
- Take into account review comments (#1735562)

* Tue Jul 30 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.290000-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
