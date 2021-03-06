%define upstream_name    Games-Solitaire-Verify

Name:       perl-%{upstream_name}
Version:    0.2403
Release:    4%{?dist}

Summary:    Process and verify solitaire games
License:    MIT
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/Games/%{upstream_name}-%{version}.tar.gz

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires: findutils
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Dir::Manifest)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(List::Util)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(POSIX)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(autodie)
BuildRequires: perl(blib)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
This is a CPAN Perl module that verifies the solutions of various variants
of card Solitaire. It does not aim to try to be a solver for them, because
this is too CPU intensive to be adequately done using perl5 (as of
perl-5.10.0). If you're interested in the latter, look at:

* https://fc-solve.shlomifish.org/

* https://fc-solve.shlomifish.org/links.html#other_solvers

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%__perl Build.PL --installdirs=vendor

./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
chmod 755 %{buildroot}/%{_bindir}/*

%files
%license COPYING LICENSE
%doc Changes README examples
%{_bindir}/expand-solitaire-multi-card-moves
%{_bindir}/verify-solitaire-solution
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2403-2
- Perl 5.32 rebuild

* Wed Apr 22 2020 Shlomi Fish <shlomif@cpan.org> - 0.2303-1
- New upstream version

* Fri Mar 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2300-1
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2202-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2201-2
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1900-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Shlomi Fish <shlomif@cpan.org> 0.1900-1
- Forked from the Mageia package and adapted for Fedora
