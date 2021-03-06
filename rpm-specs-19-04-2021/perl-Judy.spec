%global __provides_exclude ^perl\\(Judy\\)$

Name:		perl-Judy
Version:	0.41
Release:	21%{?dist}
Summary:	Library for creating and accessing dynamic arrays
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Judy
Source0:	https://cpan.metacpan.org/authors/id/J/JJ/JJORE/Judy-%{version}.tar.gz
Patch0:		avoid-using-alien-judy.patch
BuildRequires:	perl-interpreter
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	Judy-devel
BuildRequires:	perl(Config)
BuildRequires:	perl(File::Spec)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(base)
BuildRequires:	perl(blib)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	coreutils
BuildRequires:	findutils

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:	perl(Judy::_tie)
Provides:	perl(Judy::1::_impl)
Provides:	perl(Judy::1::_obj)
Provides:	perl(Judy::1::_tie)
Provides:	perl(Judy::HS::_impl)
Provides:	perl(Judy::HS::_obj)
Provides:	perl(Judy::HS::_tie)
Provides:	perl(Judy::L::_impl)
Provides:	perl(Judy::L::_obj)
Provides:	perl(Judy::L::_tie)
Provides:	perl(Judy::Mem::_impl)
Provides:	perl(Judy::SL::_dump)
Provides:	perl(Judy::SL::_impl)
Provides:	perl(Judy::SL::_obj)
Provides:	perl(Judy::SL::_tie)

%description
The Judy family of functions supports fully dynamic arrays. These arrays
may be indexed by a 32- or 64-bit word (depending on processor word size)
(Judy::1, Judy::L), a null terminated string (Judy::SL), or an ordinary
perl string (Judy::HS).

%prep
%setup -q -n Judy-%{version}
%patch0 -p1

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Judy*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-19
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-13
- Perl 5.28 rebuild

* Fri Mar 02 2018 Petr Pisar <ppisar@redhat.com> - 0.41-12
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 2 2015 Jan Holcapek <holcapek@gmail.com> 0.41-4
- Bumped release to push an update (#751119)

* Wed Sep 16 2015 Jan Holcapek <holcapek@gmail.com> 0.41-3
- Fixed build deps (#751119)

* Sat Sep 05 2015 Jan Holcapek <holcapek@gmail.com> 0.41-2
- Applied review comments (#751119)

* Fri Nov 08 2013 Jan Holcapek <holcapek@gmail.com> 0.41-1
- Specfile autogenerated by cpanspec 1.78.
