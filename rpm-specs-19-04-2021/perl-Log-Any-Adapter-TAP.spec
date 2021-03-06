Name:           perl-Log-Any-Adapter-TAP
Version:        0.003003
Release:        7%{?dist}
Summary:        Logging adapter suitable for use in TAP testcases

License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Log-Any-Adapter-TAP/
Source0:        http://www.cpan.org/modules/by-module/Log/Log-Any-Adapter-TAP-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::Base)
BuildRequires:  perl(Log::Any::Proxy)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
When running testcases, you probably want to see some of your logging
output.  One sensible approach is to have all warn and more serious
messages emitted as diag output on STDERR, and less serious messages
emitted as note comments on STDOUT.


%prep
%autosetup -n Log-Any-Adapter-TAP-%{version} -p 1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
%make_build test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.003003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.003003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.003003-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.003003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.003003-2
- Perl 5.30 rebuild

* Mon Feb 25 2019 Bj??rn Esser <besser82@fedoraproject.org> - 0.003003-1
- Bump release to stable (#1680376)

* Sun Feb 24 2019 Bj??rn Esser <besser82@fedoraproject.org> - 0.003003-0.3
- Changes as suggested in review (#1680376)
- Add a BR for Perl required version
- Add a set of explicit BuildRequires
- Use %%make_install
- Drop cleanups using find
- Drop dist.ini fom %%doc

* Sun Feb 24 2019 Bj??rn Esser <besser82@fedoraproject.org> - 0.003003-0.2
- Add explicit perl module compat requires

* Sun Feb 24 2019 Bj??rn Esser <besser82@fedoraproject.org> - 0.003003-0.1
- Initial rpm release (#1680376)
