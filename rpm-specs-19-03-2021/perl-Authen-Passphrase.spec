Name:           perl-Authen-Passphrase
Version:        0.008
Release:        11%{?dist}
Summary:        Hashed passwords/passphrases as objects
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Authen-Passphrase
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Authen-Passphrase-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Authen::DecHpwd) >= 2.003
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(Crypt::Eksblowfish::Bcrypt) >= 0.008
BuildRequires:  perl(Crypt::Eksblowfish::Uklblowfish) >= 0.008
BuildRequires:  perl(Crypt::MySQL) >= 0.03
BuildRequires:  perl(Crypt::PasswdMD5) >= 1.0
BuildRequires:  perl(Crypt::UnixCrypt_XS) >= 0.08
BuildRequires:  perl(Data::Entropy::Algorithms)
BuildRequires:  perl(Digest) >= 1.00
BuildRequires:  perl(Digest::MD4) >= 1.2
BuildRequires:  perl(Digest::MD5) >= 1.9953
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(MIME::Base64) >= 2.21
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Runtime) >= 0.011
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
These Perl modules provide a passphrase recognizer. Its job is
to recognize whether an offered passphrase is the right one. Various
passphrase encoding schemes are supported.

%prep
%autosetup -n Authen-Passphrase-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.008-1
- Specfile autogenerated by cpanspec 1.78.
