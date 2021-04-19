Name:           perl-Test-Net-LDAP
Version:        0.07
Release:        3%{?dist}
Summary:        Net::LDAP subclass for testing
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Net-LDAP/
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Net-LDAP-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::Constant)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Net::LDAP::Filter)
BuildRequires:  perl(Net::LDAP::FilterMatch)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Net::LDAP::Bind)
Requires:       perl(Net::LDAP::RootDSE)
Requires:       perl(Net::LDAP::Search)

%description
This module provides some testing methods for LDAP operations, such
as search, add, and modify, where each method is suffixed with either
_ok or _is.

%prep
%setup -q -n Test-Net-LDAP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Xavier Bachelot <xavier@bachelot.org> 0.07-2
- Review fixes

* Tue Oct 20 2020 Xavier Bachelot <xavier@bachelot.org> 0.07-1
- Initial package
