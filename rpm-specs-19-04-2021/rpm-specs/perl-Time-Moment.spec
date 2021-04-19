%global         _hardened_build 1

Name:           perl-Time-Moment
Version:        0.44
Release:        10%{?dist}
Summary:        Represents a date and time of day with an offset from UTC
License:        (GPL+ or Artistic) and BSD
URL:            https://metacpan.org/release/Time-Moment

Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/Time-Moment-%{version}.tar.gz

Provides:       bundled(c-dt)

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
Buildrequires:  perl-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader) >= 0.02

# Testing
BuildRequires:  perl(CBOR::XS) >= 1.3
BuildRequires:  perl(DateTime)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Params::Coerce)
BuildRequires:  perl(Sereal) >= 2.060
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal) >= 0.006
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Number::Delta) >= 1.06
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::Piece)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Exporter)
Requires:       perl(XSLoader) >= 0.02

%description
Time::Moment is an immutable object representing a date and time of day
with an offset from UTC in the ISO 8601 calendar system.

%prep
%setup -q -n Time-Moment-%{version}

%build
# partially fixing hardening if not fully supported
export CFLAGS="%{optflags} -Wl,-z,relro -Wl,-z,now"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,now -Wl,--as-needed"

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$CFLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

# fixing scripts provided in docs
chmod a-x -c eg/*.pl

%check
make test

%files
%doc Changes README eg/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Time*
%{_mandir}/man3/*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-2
- Perl 5.28 rebuild

* Fri May 11 2018 Denis Fateyev <denis@fateyev.com> - 0.44-1
- Update to 0.44 release

* Fri Mar 09 2018 Denis Fateyev <denis@fateyev.com> - 0.43-1
- Update to 0.43 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-2
- Perl 5.26 rebuild

* Fri Apr 14 2017 Denis Fateyev <denis@fateyev.com> - 0.42-1
- Update to 0.42 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Denis Fateyev <denis@fateyev.com> - 0.41-1
- Update to 0.41 release

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-3
- Perl 5.24 rebuild

* Thu Feb 11 2016 Denis Fateyev <denis@fateyev.com> - 0.38-2
- Spec cleanup

* Tue Feb 09 2016 Denis Fateyev <denis@fateyev.com> - 0.38-1
- Initial release
