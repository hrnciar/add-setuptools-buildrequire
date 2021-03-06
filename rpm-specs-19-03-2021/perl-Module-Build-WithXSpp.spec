Name:           perl-Module-Build-WithXSpp
Version:        0.14
Release:        20%{?dist}
Summary:        XS++ enhanced flavor of Module::Build
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Module-Build-WithXSpp
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Module-Build-WithXSpp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.04
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.26
BuildRequires:  perl(Test::More)
Requires:       perl(ExtUtils::CppGuess) >= 0.04
Requires:       perl(ExtUtils::ParseXS) >= 2.2205
Requires:       perl(ExtUtils::Typemaps) >= 1.00
Requires:       perl(ExtUtils::XSpp) >= 0.11
Requires:       perl(File::Basename)
Requires:       perl(File::Spec)
Requires:       perl(Module::Build) >= 0.26
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Filtering unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Build\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ExtUtils::CppGuess\\)$

%description
This subclass of Module::Build adds some tools and processes to make it
easier to use for wrapping C++ using XS++ (ExtUtils::XSpp).

%prep
%setup -q -n Module-Build-WithXSpp-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-18
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 26 2013 Miro Hron??ok <mhroncok@redhat.com> - 0.14-1
- New version 0.14 (#1014201)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.13-2
- Perl 5.18 rebuild

* Tue Jan 29 2013 Miro Hron??ok <mhroncok@redhat.com> - 0.13-1
- New version

* Thu Dec 20 2012 Miro Hron??ok <miro@hroncok.cz> - 0.12-3
- Removed deleting empty dirs in %%install section
- Do not package META.json
- Removed (B)Rs: perl(XSLoader), perl(Digest::MD5), perl(ExtUtils::CBuilder)
- Removed BRs: perl(ExtUtils::ParseXS), perl(ExtUtils::Typemaps), perl(ExtUtils::XSpp)
- Filter unversioned Requires: perl(Module::Build), perl(ExtUtils::CppGuess)
- Sort (B)Rs lexicografically

* Fri Nov 16 2012 Miro Hron??ok <miro@hroncok.cz> - 0.12-2
- Removed BRs provided by perl package

* Wed Nov 14 2012 Miro Hron??ok <miro@hroncok.cz> 0.12-1
- New version.

* Mon Oct 01 2012 Miro Hron??ok <miro@hroncok.cz> 0.11-1
- Specfile autogenerated by cpanspec 1.78 and revised.
