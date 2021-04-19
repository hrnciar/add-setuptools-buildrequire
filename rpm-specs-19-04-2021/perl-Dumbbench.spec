# SOOT support is optional
%bcond_with perl_Dumbbench_enables_SOOT

Name:           perl-Dumbbench
Version:        0.501
Release:        1%{?dist}
Summary:        More reliable bench-marking with the least amount of thinking
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dumbbench
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Dumbbench-%{version}.tar.gz
# Fix a link a in a documentation, proposed to the upstream,
# <https://github.com/briandfoy/dumbbench/pull/10>
Patch0:         Dumbbench-0.501-Correct-a-link.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# bash for /usr/bin/sh executed by sudo, not used at tests
# bin/dumbbench requires Capture::Tiny only if SOOT is available
%if %{with perl_Dumbbench_enables_SOOT}
BuildRequires:  perl(Capture::Tiny)
%endif
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor) >= 1.05
BuildRequires:  perl(constant)
# Devel::CheckOS not used at tests
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Number::WithError) >= 1.00
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(parent)
# SOOT is optional
# sudo not used at tests
BuildRequires:  perl(Statistics::CaseResampling) >= 0.06
BuildRequires:  perl(Time::HiRes)
# Tests:
# Code from ./simulator is neither executed nor installed
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Test::More) >= 1
# bash for /usr/bin/sh executed by sudo, not used at tests
Requires:       bash
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# bin/dumbbench requires Capture::Tiny only if SOOT is available
%if %{with perl_Dumbbench_enables_SOOT}
Requires:       perl(Capture::Tiny)
%endif
Requires:       perl(Class::XSAccessor) >= 1.05
Requires:       perl(Number::WithError) >= 1.00
Requires:       perl(Statistics::CaseResampling) >= 0.06
Requires:       sudo

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::XSAccessor|Number::WithError|Statistics::CaseResampling|Test::More)\\)$

%description
Dumbbench is a fancier benchmark module for Perl. It times the runs of code,
does some statistical analysis to discard outliers, and prints the results.

%if %{with perl_Dumbbench_enables_SOOT}
%package BoxPlot
Summary:        Dumbbench visualization using ROOT
# This package run-requires perl-SOOT which isn't available on ARM, bug #1139141
ExclusiveArch: %{ix86} x86_64 noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description BoxPlot
Dumbbench::BoxPlot module provides a way how to plot a Dumbbench timing using
ROOT toolkit.
%endif

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 1

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Dumbbench-%{version}
%patch0 -p1
# Normalize shebangs
for F in examples/*.pl; do
    perl -MConfig -i -pe 's/\A#!.*perl/$Config{startperl}/' "$F";
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes examples README.pod
%{_bindir}/*
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Dumbbench/BoxPlot.pm
%{_mandir}/man3/*

%if %{with perl_Dumbbench_enables_SOOT}
%files BoxPlot
%doc r
%{perl_vendorlib}/Dumbbench/BoxPlot.pm
%endif

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Feb 16 2021 Petr Pisar <ppisar@redhat.com> - 0.501-1
- 0.501 bump
- A license changed from "(GPL+ or Artistic) and (Artistic 2.0)" to
  "GPL+ or Artistic"
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.111-10
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.111-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.111-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Petr Pisar <ppisar@redhat.com> - 0.111-1
- 0.111 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-4
- Perl 5.24 rebuild

* Mon May 09 2016 Petr Pisar <ppisar@redhat.com> - 0.10-3
- Disable SOOT support (bug #1326236)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump
- License changed to (GPL+ or Artistic) and (Artistic 2.0)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-5
- Perl 5.22 rebuild

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-4
- Perl 5.20 mass

* Mon Sep 08 2014 Petr Pisar <ppisar@redhat.com> - 0.09-3
- Disable perl-Dumbbench-BoxPlot subpackage on ARM (bug #1139141)

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.20 rebuild

* Tue May 14 2013 Petr Pisar <ppisar@redhat.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
- Enable SOOT (Perl binding for ROOT) support
