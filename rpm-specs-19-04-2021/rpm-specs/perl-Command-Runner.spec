Name:           perl-Command-Runner
Version:        0.103
Release:        3%{?dist}
Summary:        Run external commands and Perl code references
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Command-Runner
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/Command-Runner-%{version}.tar.gz
# Update Command::Runner::Quote to not load Win32::ShellQuote on
# non-MSWin32 systems
Patch0:         Command-Runner-0.100-Dont-load-Win32-ShellQuote.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(String::ShellQuote)

%description
This module runs external commands and Perl code references.

%prep
%setup -q -n Command-Runner-%{version}
%patch0 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Petr Pisar <ppisar@redhat.com> - 0.103-1
- 0.103 bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.102-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.102-1
- 0.102 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.101-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.101-2
- Perl 5.28 rebuild

* Thu May 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.101-1
- 0.101 bump

* Wed May 02 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.100-1
- 0.100 bump

* Mon Apr 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-1
- Specfile autogenerated by cpanspec 1.78.
