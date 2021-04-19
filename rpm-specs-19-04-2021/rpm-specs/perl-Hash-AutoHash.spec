Name:           perl-Hash-AutoHash
Version:        1.17
Release:        10%{?dist}
Summary:        Object-oriented access to real and tied hashes
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Hash-AutoHash
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NATG/Hash-AutoHash-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.3
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp) >= 1.2
BuildRequires:  perl(List::MoreUtils) >= 0.33
BuildRequires:  perl(Scalar::Util) >= 1.23
BuildRequires:  perl(Tie::Hash) >= 1.04
BuildRequires:  perl(Tie::ToObject) >= 0.03
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter) >= 5.68
BuildRequires:  perl(File::Spec) >= 3.4
BuildRequires:  perl(lib)
BuildRequires:  perl(Storable) >= 2.3
BuildRequires:  perl(Test::Deep) >= 0.11
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Pod) >= 1.48
BuildRequires:  perl(Test::Pod::Content) >= 0.0.6
BuildRequires:  perl(Tie::Hash::MultiValue) >= 1.02
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp) >= 1.2
Requires:       perl(List::MoreUtils) >= 0.33
Requires:       perl(Tie::Hash) >= 1.04
Requires:       perl(Tie::ToObject) >= 0.03

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|List::MoreUtils|Tie::Hash|Tie::ToObject)\\)$

%description
This is yet another Perl module that lets you access or change the elements of
a hash using methods with the same name as the element's key. It follows in
the footsteps of Hash::AsObject, Hash::Inflator, Data::OpenStruct::Deep,
Object::AutoAccessor, and probably others. The main difference between this
module and its forebears is that it supports tied hashes, in addition to
regular hashes.

%prep
%setup -q -n Hash-AutoHash-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-2
- Perl 5.28 rebuild

* Wed Jun 13 2018 Petr Pisar <ppisar@redhat.com> 1.17-1
- Specfile autogenerated by cpanspec 1.78.
