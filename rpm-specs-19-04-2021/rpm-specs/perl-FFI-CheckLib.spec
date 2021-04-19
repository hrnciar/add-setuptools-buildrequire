# Run optional test
%{bcond_without perl_FFI_Changes_enables_optional_test}

Name:           perl-FFI-CheckLib
Version:        0.27
Release:        4%{?dist}
Summary:        Check that a library is available for FFI
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/FFI-CheckLib
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/FFI-CheckLib-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Require::EnvVar) >= 0.000060
BuildRequires:  perl(Test2::Require::Module) >= 0.000060
BuildRequires:  perl(Test2::V0) >= 0.000060
%if %{with perl_FFI_Changes_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Env)
BuildRequires:  perl(Test::Exit)
# Test/More.pl is not helpful
# FFI::Platypus not used
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DynaLoader)

%description
This Perl module checks whether a particular dynamic library is available for
Foreign Function Interface (FFI) to use. It is modeled heavily on
Devel::CheckLib, but will find dynamic libraries even when development
packages are not installed. It also provides a find_lib function that will
return the full path to the found dynamic library, which can be feed directly
into FFI::Platypus or FFI::Raw.

%prep
%setup -q -n FFI-CheckLib-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset EXTRA_CI
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-2
- Perl 5.32 rebuild

* Tue May 12 2020 Petr Pisar <ppisar@redhat.com> - 0.27-1
- 0.27 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Petr Pisar <ppisar@redhat.com> - 0.26-1
- 0.26 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Petr Pisar <ppisar@redhat.com> - 0.25-1
- 0.25 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-2
- Perl 5.30 rebuild

* Mon Apr 29 2019 Petr Pisar <ppisar@redhat.com> - 0.24-1
- 0.24 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Petr Pisar <ppisar@redhat.com> - 0.23-1
- 0.23 bump

* Mon Oct 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-1
- 0.22 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-2
- Perl 5.28 rebuild

* Tue Jun 05 2018 Petr Pisar <ppisar@redhat.com> - 0.20-1
- 0.20 bump

* Thu May 31 2018 Petr Pisar <ppisar@redhat.com> - 0.19-1
- 0.19 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- 0.18 bump

* Wed Aug 09 2017 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.26 rebuild

* Fri Mar 10 2017 Petr Pisar <ppisar@redhat.com> 0.15-1
- Specfile autogenerated by cpanspec 1.78.
