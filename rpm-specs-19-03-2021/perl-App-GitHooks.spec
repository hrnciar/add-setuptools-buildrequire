Name:           perl-App-GitHooks
Version:        1.9.0
Release:        14%{?dist}
Summary:        Extensible plugins system for git hooks
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/App-GitHooks
Source0:        https://cpan.metacpan.org/modules/by-module/App/App-GitHooks-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  git-core >= 1.7.4.1
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Section)
BuildRequires:  perl(Data::Validate::Type)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Git::Repository)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::Encoding)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Git)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires::Git)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Try::Tiny)
# Tests:
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Compile) >= 1.001
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Type) >= 1.0.2
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       git-core >= 1.7.4.1

%description
App::GitHooks is an extensible and easy to configure git hooks framework
that supports many plugins.

%prep
%setup -q -n App-GitHooks-v%{version}
# Do no use /usr/bin/env in shellbangs
find -type f -exec sed -i -e \
    's|\(#!\)\{0,1\}/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|g' \
    {} +

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export LC_ALL=C.UTF-8
./Build test

%files
%license LICENSE
%doc Changes README.md hooks
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.0-12
- Perl 5.32 rebuild

* Tue Mar 10 2020 Petr Pisar <ppisar@redhat.com> - 1.9.0-11
- Set a UTF-8 locale for tests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.0-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.0-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.0-2
- Perl 5.26 rebuild

* Wed Mar 29 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.0-1
- 1.9.0 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 27 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-1
- 1.8.0 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Petr Pisar <ppisar@redhat.com> - 1.7.3-1
- 1.7.3 bump

* Fri Jun 19 2015 Petr Pisar <ppisar@redhat.com> - 1.7.2-1
- 1.7.2 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.8-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.8-2
- Perl 5.20 rebuild

* Fri Jun 27 2014 David Dick <ddick@cpan.org> - 1.0.8-1
- Initial release
