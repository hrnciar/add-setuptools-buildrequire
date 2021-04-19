Name:           perl-Test2-Harness
%global cpan_version 1.000044
Version:        1.0.44
Release:        1%{?dist}
Summary:        Test2 Harness designed for the Test2 event system
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test2-Harness
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Harness-%{cpan_version}.tar.gz
# Help generators to recognize a Perl code
Patch0:         Test2-Harness-1.000043-Adapt-tests-to-shebangs.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Devel::Cover)
# Devel::NYTProf not used at tests
# Email::Stuffer 0.016 not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.11
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(goto::file) >= 0.005
# HTTP::Tiny 0.070 not used at tests
# HTTP::Tiny::Multipart not used at tests
BuildRequires:  perl(Importer) >= 0.025
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Handle) >= 1.27
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Linux::Inotify2)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Long::Jump) >= 0.000001
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::ANSIColor) >= 4.03
BuildRequires:  perl(Term::Table) >= 0.015
BuildRequires:  perl(Test2::API) >= 1.302170
BuildRequires:  perl(Test2::Event) >= 1.302170
BuildRequires:  perl(Test2::Formatter) >= 1.302170
BuildRequires:  perl(Test2::Hub)
# Test2::Plugin::Cover not used at tests
# Test2::Plugin::DBIProfile not used at tests
BuildRequires:  perl(Test2::Plugin::IOEvents) >= 0.001001
BuildRequires:  perl(Test2::Plugin::MemUsage) >= 0.002003
BuildRequires:  perl(Test2::Plugin::UUID) >= 0.002001
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Util) >= 1.302170
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::Util::Table)
BuildRequires:  perl(Test2::Util::Term) >= 0.000127
BuildRequires:  perl(Test2::Util::Times)
BuildRequires:  perl(Test::Builder::Formatter) >= 1.302170
BuildRequires:  perl(Time::HiRes)
# Win32::Console::ANSI not used on Linux
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(ok)
BuildRequires:  perl(Test2::Bundle::Extended) >= 0.000127
BuildRequires:  perl(Test2::Tools::AsyncSubtest) >= 0.000127
BuildRequires:  perl(Test2::Tools::GenTemp)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::Tools::Subtest) >= 0.000127
BuildRequires:  perl(Test2::Tools::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000127
BuildRequires:  perl(Test::Builder) >= 1.302170
BuildRequires:  perl(Test::More) >= 1.302170
BuildRequires:  perl(utf8)
# Optional tests:
# t2/lib/App/Yath/Plugin/SelfTest.pm tries building a C code using a gcc and
# to run a bash script. But SelfTest.pm itself is never executed.
# bash not used
# gcc not used
# App::Yath::Plugin::Git tries "git" command
Suggests:       git-core
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Suggests:       perl(Cpanel::JSON::XS)
Requires:       perl(Data::Dumper)
Suggests:       perl(Devel::Cover)
Suggests:       perl(Devel::NYTProf)
Suggests:       perl(Email::Stuffer) >= 0.016
Requires:       perl(Exporter)
Requires:       perl(File::Find)
Requires:       perl(File::Path) >= 2.11
Suggests:       perl(FindBin)
Requires:       perl(goto::file) >= 0.005
Suggests:       perl(HTTP::Tiny) >= 0.070
Suggests:       perl(HTTP::Tiny::Multipart) >= 0.08
Requires:       perl(Importer) >= 0.025
Requires:       perl(IO::Compress::Bzip2)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::Uncompress::Bunzip2)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Handle) >= 1.27
Suggests:       perl(IO::Pager) >= 1.00
Suggests:       perl(JSON::MaybeXS)
Requires:       perl(JSON::PP)
Suggests:       perl(Linux::Inotify2)
Requires:       perl(Long::Jump) >= 0.000001
Suggests:       perl(Term::ANSIColor) >= 4.03
Requires:       perl(Term::Table) >= 0.015
Requires:       perl(Test2::API) >= 1.302170
Requires:       perl(Test2::Event) >= 1.302170
Requires:       perl(Test2::Formatter) >= 1.302170
Requires:       perl(Test2::Hub)
Suggests:       perl(Test2::Plugin::Cover) >= 0.000007
Suggests:       perl(Test2::Plugin::DBIProfile) >= 0.002002
Requires:       perl(Test2::Plugin::IOEvents) >= 0.001001
Requires:       perl(Test2::Plugin::MemUsage) >= 0.002003
Requires:       perl(Test2::Plugin::UUID) >= 0.002001
Requires:       perl(Test2::Util) >= 1.302170
Requires:       perl(Test2::Util::Term) >= 0.000127
Requires:       perl(Test::Builder::Formatter) >= 1.302170

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::Path|goto::file|Importer|IO::Handle|Long::Jump|Term::Table|Test2::API|Test2::Formatter|Test2::Util|Test2::Util::Term|Test2::V0|Test::Builder|Test::More)\\)$
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\((Bar|Baz|Foo|main::HBase|main::HBase::Wrapped)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((AAA|App::Yath::Command::(Broken|Fake|fake)|App::Yath::Plugin::(Options|SelfTest|Test|TestPlugin)|Bar|Baz|BBB|Broken|CCC|FAST|Foo|Resource|SmokePlugin|TestPreload|TestSimplePreload)\\)

%description
This is a test harness toolkit for Perl Test2 system. It provides a yath tool,
a command-line tool for executing the tests under the Test2 harness.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(FindBin)
Requires:       perl(Test2::V0) >= 0.000127
Requires:       perl(Test::Builder) >= 1.302170
Requires:       perl(Test::More) >= 1.302170

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Test2-Harness-%{cpan_version}
chmod -x t2/non_perl/test.c
# Help generators to recognize a Perl code
%patch0 -p1
for F in test.pl $(find t t2 -name '*.t' -o -name '*.tx') t/unit/App/Yath/Plugin/Git.script; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a test.pl t t2 %{buildroot}%{_libexecdir}/%{name}
# Remove tests which enumerate files in ./lib
for F in t/0-load_all.t t/1-pod_name.t; do
    rm %{buildroot}%{_libexecdir}/%{name}/"$F"
done
# Use /usr/bin/yath
ln -s %{_bindir} %{buildroot}%{_libexecdir}/%{name}/scripts
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/integration/test.t writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset AUTHOR_TESTING AUTOMATED_TESTING DBI_PROFILE FAIL_ALWAYS FAIL_ONCE \
    FAILURE_DO_PASS GIT_BRANCH GIT_LONG_SHA GIT_SHORT_SHA GIT_STATUS \
    HARNESS_IS_VERBOSE RESOURCE_TEST \
    T2_HARNESS_IS_VERBOSE T2_HARNESS_JOB_IS_TRY T2_HARNESS_JOB_FILE \
    T2_HARNESS_STAGE
export AUTOMATED_TESTING=1
T2_HARNESS_JOB_COUNT="$(getconf _NPROCESSORS_ONLN)" ./test.pl
prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r ./t
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING AUTOMATED_TESTING DBI_PROFILE FAIL_ALWAYS FAIL_ONCE \
    FAILURE_DO_PASS GIT_BRANCH GIT_LONG_SHA GIT_SHORT_SHA GIT_STATUS \
    HARNESS_IS_VERBOSE RESOURCE_TEST \
    T2_HARNESS_IS_VERBOSE T2_HARNESS_JOB_IS_TRY T2_HARNESS_JOB_FILE \
    T2_HARNESS_STAGE
export AUTOMATED_TESTING=1
export T2_HARNESS_JOB_COUNT=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; $j=1 unless $j; print "$j"' -- \
    %{?_smp_mflags})
export HARNESS_OPTIONS=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; print "j$j" if $j' -- \
    %{?_smp_mflags})
make test

%files
%license LICENSE
%doc Changes README TODO
%{_bindir}/yath
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Mar 12 2021 Petr Pisar <ppisar@redhat.com> - 1.0.44-1
- 1.000044 bump

* Wed Mar 10 2021 Petr Pisar <ppisar@redhat.com> - 1.0.43-2
- A test needs FindBin

* Mon Mar 08 2021 Petr Pisar <ppisar@redhat.com> - 1.0.43-1
- 1.000043 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Petr Pisar <ppisar@redhat.com> - 1.0.42-1
- 1.000042 bump

* Tue Nov 03 2020 Petr Pisar <ppisar@redhat.com> - 1.0.38-1
- 1.000038 bump

* Fri Oct 30 2020 Petr Pisar <ppisar@redhat.com> - 1.0.35-1
- 1.000035 bump

* Thu Oct 29 2020 Petr Pisar <ppisar@redhat.com> - 1.0.34-1
- 1.000034 bump

* Thu Oct 29 2020 Petr Pisar <ppisar@redhat.com> - 1.0.33-1
- 1.000033 bump

* Mon Oct 26 2020 Petr Pisar <ppisar@redhat.com> - 1.0.32-1
- 1.000032 bump

* Fri Oct 23 2020 Petr Pisar <ppisar@redhat.com> - 1.0.31-1
- 1.000031 bump

* Thu Oct 22 2020 Petr Pisar <ppisar@redhat.com> - 1.0.30-1
- 1.000030 bump

* Mon Oct 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.29-1
- 1.000029 bump

* Tue Sep 29 2020 Petr Pisar <ppisar@redhat.com> - 1.0.28-1
- 1.000028 bump

* Tue Sep 22 2020 Petr Pisar <ppisar@redhat.com> - 1.0.27-1
- 1.000027 bump

* Wed Sep 09 2020 Petr Pisar <ppisar@redhat.com> - 1.0.26-1
- 1.000026 bump

* Tue Aug 25 2020 Petr Pisar <ppisar@redhat.com> - 1.0.24-1
- 1.000024 bump

* Tue Aug 18 2020 Petr Pisar <ppisar@redhat.com> - 1.0.23-1
- 1.000023 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Petr Pisar <ppisar@redhat.com> - 1.0.20-1
- 1.000020 bump

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.19-2
- Perl 5.32 rebuild

* Mon Jun 01 2020 Petr Pisar <ppisar@redhat.com> - 1.0.19-1
- 1.000019 bump

* Tue Apr 14 2020 Petr Pisar <ppisar@redhat.com> - 1.0.18-1
- 1.000018 bump

* Wed Apr 08 2020 Petr Pisar <ppisar@redhat.com> - 1.0.16-1
- 1.000016 bump

* Tue Mar 24 2020 Petr Pisar <ppisar@redhat.com> - 1.0.15-1
- 1.000015 bump

* Mon Mar 23 2020 Petr Pisar <ppisar@redhat.com> - 1.0.14-1
- 1.000014 bump

* Thu Mar 19 2020 Petr Pisar <ppisar@redhat.com> - 1.0.13-1
- 1.000013 bump

* Tue Mar 10 2020 Petr Pisar <ppisar@redhat.com> - 1.0.11-1
- 1.000011 bump

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 1.0.10-1
- 1.000010 bump

* Mon Mar 02 2020 Petr Pisar <ppisar@redhat.com> - 1.0.3-1
- 1.000003 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001099-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Petr Pisar <ppisar@redhat.com> - 0.001099-1
- 0.001099 bump

* Mon Sep 09 2019 Petr Pisar <ppisar@redhat.com> - 0.001097-1
- 0.001097 bump

* Thu Sep 05 2019 Petr Pisar <ppisar@redhat.com> - 0.001095-1
- 0.001095 bump

* Wed Sep 04 2019 Petr Pisar <ppisar@redhat.com> - 0.001093-1
- 0.001093 bump

* Mon Sep 02 2019 Petr Pisar <ppisar@redhat.com> - 0.001091-1
- 0.001091 bump

* Fri Aug 30 2019 Petr Pisar <ppisar@redhat.com> - 0.001088-1
- 0.001088 bump

* Thu Aug 29 2019 Petr Pisar <ppisar@redhat.com> - 0.001086-1
- 0.001086 bump

* Thu Aug 22 2019 Petr Pisar <ppisar@redhat.com> - 0.001085-1
- 0.001085 bump

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> - 0.001084-1
- 0.001084 bump

* Wed Aug 14 2019 Petr Pisar <ppisar@redhat.com> - 0.001081-1
- 0.001081 bump

* Thu Aug 01 2019 Petr Pisar <ppisar@redhat.com> 0.001080-1
- Specfile autogenerated by cpanspec 1.78.
