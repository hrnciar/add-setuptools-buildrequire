Name:           perl-Test2-Plugin-Cover
%global cpan_version 0.000009
Version:        0.0.9
Release:        3%{?dist}
Summary:        Collect minimal file coverage data
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test2-Plugin-Cover
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-Cover-%{cpan_version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Path::Tiny) >= 0.048
BuildRequires:  perl(Test2::API) >= 1.302166
BuildRequires:  perl(Test2::EventFacet) >= 1.302166
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Test2::V0) >= 0.000130
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Path::Tiny) >= 0.048
Requires:       perl(Test2::API) >= 1.302166
Requires:       perl(Test2::EventFacet) >= 1.302166

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Path::Tiny|Test2::API)\\)$

%description
This Test2 plugin will collect minimal file coverage data, and will do so with
a minimal performance impact.

%prep
%setup -q -n Test2-Plugin-Cover-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Test2*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Petr Pisar <ppisar@redhat.com> - 0.0.9-1
- 0.000009 bump

* Thu Jul 09 2020 Petr Pisar <ppisar@redhat.com> 0.0.7-1
- Specfile autogenerated by cpanspec 1.78.
