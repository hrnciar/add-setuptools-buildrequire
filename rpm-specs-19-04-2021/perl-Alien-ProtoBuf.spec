Name:           perl-Alien-ProtoBuf
Version:        0.09
Release:        10%{?dist}
Summary:        Find Protocol Buffers library
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Alien-ProtoBuf
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/Alien-ProtoBuf-%{version}.tar.gz
# Although Alien::* modules are usually architecture specific because they
# store architecture specific data, this is not a case of
# perl-Alien-ProtoBuf. We can remain noarch.
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Alien::Base::ModuleBuild) >= 0.023
BuildRequires:  perl(lib)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.11
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(protobuf)
# Run-time:
BuildRequires:  perl(Alien::Base)
# Tests:
BuildRequires:  perl(Test::More)
# Test::Pod not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper)
Requires:       perl(Module::Build) >= 0.28
# A purpose of this package is to ensure a user can develop against protobuf.
# We require exact version because the version is stored into generated
# Alien/ProtoBuf/Install/Files.pm file.
Requires:       pkgconfig(protobuf) = %(type -p pkgconf >/dev/null && pkgconf --exists protobuf && pkg-config --modversion protobuf || echo 0)

%description
Depending on Alien::ProtoBuf Perl module ensures the Protocol Buffers library
is installed on your system.

%prep
%setup -q -n Alien-ProtoBuf-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 16:41:04 CET 2021 Adrian Reber <adrian@lisas.de> - 0.09-9
- Rebuilt for protobuf 3.14

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 0.09-8
- Rebuilt for protobuf 3.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-6
- Perl 5.32 rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 0.09-5
- Rebuilt for protobuf 3.12

* Wed May 06 2020 Petr Pisar <ppisar@redhat.com> - 0.09-4
- Rebuild against protobuf 3.11.4 (bug #1831970)

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 0.09-3
- Fix generating pkgconfig(protobuf) version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-2
- Perl 5.30 rebuild

* Thu Mar 14 2019 Petr Pisar <ppisar@redhat.com> 0.08-1
- Specfile autogenerated by cpanspec 1.78.
