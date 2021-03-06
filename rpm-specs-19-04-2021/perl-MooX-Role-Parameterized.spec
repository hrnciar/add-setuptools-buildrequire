Name:           perl-MooX-Role-Parameterized
Version:        0.082
Release:        7%{?dist}
Summary:        Roles with composition parameters
License:        MIT

URL:            https://metacpan.org/release/MooX-Role-Parameterized
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PACMAN/MooX-Role-Parameterized-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test deps
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(autodie)
BuildRequires:  perl(utf8)
Requires:       perl(Moo::Role)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This is an experimental port of MooseX::Role::Parameterized to Moo.

%prep
%setup -q -n MooX-Role-Parameterized-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changelog README README.md
%license LICENSE
%{perl_vendorlib}/MooX*
%{_mandir}/man3/MooX*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.082-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.082-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.082-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.082-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.082-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.082-2
- Perl 5.30 rebuild

* Sun Mar 17 2019 Emmanuel Seyman <emmanuel@seyman.fr> 0.082-1
- Specfile autogenerated by cpanspec 1.78.
