Name:           perl-MojoX-Log-Log4perl
Version:        0.12
Release:        3%{?dist}
Summary:        Log::Log4perl logging for Mojo/Mojolicious
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/MojoX-Log-Log4perl
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GARU/MojoX-Log-Log4perl-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Log::Log4perl) >= 1.25
BuildRequires:  perl(Log::Log4perl::Level)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Mojo::Asset::File)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Mojo)
Requires:       perl(Log::Log4perl::Level)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%description
MojoX::Log::Log4perl provides a Mojo::Log implementation that uses
Log::Log4perl as the underlying log mechanism. It provides all the
methods listed in Mojo::Log (and many more from Log4perl).

%prep
%setup -q -n MojoX-Log-Log4perl-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%{perl_vendorlib}/MojoX*
%{_mandir}/man3/MojoX*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.12-2
- Take into account review feedback (#1880266)

* Mon Sep 07 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.12-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
