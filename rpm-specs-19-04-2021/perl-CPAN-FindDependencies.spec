%global pkgname CPAN-FindDependencies

# Do not perform tests that need the Internet
%bcond_with perl_CPAN_FindDependencies_enables_network
# Perform optional tests
%bcond_without perl_CPAN_FindDependencies_enables_optional_test

Name:           perl-CPAN-FindDependencies
Version:        3.05
Release:        1%{?dist}
Summary:        Find dependencies for modules on CPAN
License:        GPLv2+ or Artistic
URL:            https://metacpan.org/release/CPAN-FindDependencies
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  bzip2
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(constant)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Type)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Parse::CPAN::Packages)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Devel::CheckOS)
%if %{with perl_CPAN_FindDependencies_enables_network}
BuildRequires:  perl(File::Path)
%endif
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Time)
%if %{with perl_CPAN_FindDependencies_enables_optional_test}
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
Requires:       bzip2
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Pod::Perldoc)

%description
This module provides tools to find a module's dependencies (and their
dependencies, and so on) without having to download the modules in
their entirety.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -qn %{pkgname}-%{version}
for F in \
%if !%{with perl_CPAN_FindDependencies_enables_network}
    t/cpandeps-diff-script.t \
%endif
%if !%{with perl_CPAN_FindDependencies_enables_optional_test}
    t/pod.t t/pod-coverage.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t t/cache/Tie-Scalar-Decay-1.1.1/Tie-Scalar-Decay-1.1.1.MakefilePL; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_CPAN_FindDependencies_enables_optional_test}
    rm %{buildroot}%{_libexecdir}/%{name}/t/pod{,-coverage}.t
%endif
mkdir %{buildroot}%{_libexecdir}/%{name}/blib
ln -s %{_bindir} %{buildroot}%{_libexecdir}/%{name}/blib/script
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/multi.t writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license ARTISTIC.txt GPL2.txt
%doc CHANGELOG README TODO
%{_bindir}/cpandeps
%{_bindir}/cpandeps-diff
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Feb 25 2021 Petr Pisar <ppisar@redhat.com> - 3.05-1
- 3.05 bump
- Package tests

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.04-1
- 3.04 bump

* Fri Oct 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.03-1
- 3.03 bump

* Thu Oct 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.02-1
- 3.02 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.49-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.49-1
- 2.49 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.48-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.48-1
- 2.48 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.47-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.47-2
- Perl 5.26 rebuild

* Tue Apr 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.47-1
- 2.47 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Petr Pisar <ppisar@redhat.com> - 2.46-1
- 2.46 bump

* Thu Sep 08 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.45-1
- 2.45 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.44-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.44-1
- 2.44 bump

* Thu Jun 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.43-1
- 2.43 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-7
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 2.42-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Christopher Meng <rpm@cicku.me> - 2.42-2
- Fix the license.

* Thu May 30 2013 Christopher Meng <rpm@cicku.me> - 2.42-1
- Initial Package.
