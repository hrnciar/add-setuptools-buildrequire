Name:           perl-Alien-Libxml2
Version:        0.17
Release:        2%{?dist}
Summary:        Install the C libxml2 library on your system
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Alien-Libxml2/
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Libxml2-%{version}.tar.gz

%global debug_package %{nil}

# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Alien::Build::MM) >= 2.37
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
# Run-time
BuildRequires:  perl(Alien::Base) >= 2.37
BuildRequires:  perl(Alien::Build) >= 2.37
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Alien::Base) >= 2.37
# This RPM package ensures libxml2 is installed on the system
Requires:       pkgconfig(libxml-2.0) = %(type -p pkgconf >/dev/null && pkgconf --exists libxml-2.0 && pkg-config --modversion libxml-2.0 || echo 0)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$

%description
This module provides libxml2 for other modules to use.

%prep
%setup -q -n Alien-Libxml2-%{version}

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
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Alien*
%{_mandir}/man3/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-1
- 0.17 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.32 rebuild

* Wed Apr 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-1
- 0.16 bump

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-1
- 0.15 bump

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-1
- 0.14 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-1
- 0.12 bump

* Mon Nov 11 2019 Petr Pisar <ppisar@redhat.com> - 0.11-2
- Rebuild against libxml2-2.9.10

* Tue Oct 29 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-1
- 0.11 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.30 rebuild

* Fri May 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-1
- 0.09 bump

* Thu Apr 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-1
- 0.07 bump

* Mon Mar 25 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-1
- Specfile autogenerated by cpanspec 1.78.
