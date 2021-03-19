# Enable debugging with Devel::MAT
%bcond_with perl_Future_AsyncAwait_enables_Devel_MAT
# Perform optional tests
%bcond_without perl_Future_AsyncAwait_enables_optional_test
# Declare a role with Role::Tiny
%bcond_without perl_Future_AsyncAwait_enables_role

Name:           perl-Future-AsyncAwait
Version:        0.49
Release:        1%{?dist}
Summary:        Deferred subroutine syntax for futures
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Future-AsyncAwait
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-AsyncAwait-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
%if %{with perl_Future_AsyncAwait_enables_Devel_MAT}
BuildRequires:  perl(Devel::MAT::Dumper::Helper)
%endif
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XS::Parse::Sublike::Builder) >= 0.10
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Future) >= 0.43
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XSLoader)
%if %{with perl_Future_AsyncAwait_enables_role}
# Optional run-time:
BuildRequires:  perl(Role::Tiny)
%endif
# Test:
BuildRequires:  perl(attributes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(List::Util)
%if %{with perl_Future_AsyncAwait_enables_role}
BuildRequires:  perl(Role::Tiny::With)
%endif
BuildRequires:  perl(Test::Future::Deferred)
BuildRequires:  perl(Test::Refcount) >= 0.09
%if %{with perl_Future_AsyncAwait_enables_optional_test}
# Optional tests:
%if %{with perl_Future_AsyncAwait_enables_Devel_MAT}
BuildRequires:  perl(Devel::MAT)
BuildRequires:  perl(Devel::MAT::Dumper)
%endif
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(Object::Pad) >= 0.15
BuildRequires:  perl(Syntax::Keyword::Dynamically) >= 0.04
BuildRequires:  perl(Syntax::Keyword::Try) >= 0.18
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Future) >= 0.43
%if %{with perl_Future_AsyncAwait_enables_role}
Recommends:     perl(Role::Tiny)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Future|Syntax::Keyword::Try|Test::More)\\)$

%description
This Perl module provides syntax for deferring and resuming subroutines while
waiting for Futures to complete. This syntax aims to make code that performs
asynchronous operations using futures look neater and more expressive than
simply using then chaining and other techniques on the futures themselves.

%package Test
Summary:        Conformance tests for Future::AsyncAwait::Awaitable role
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Test::More) >= 0.88

%description Test
This Perl module provides a single test function, which runs a suite of
subtests to check that a given class provides a usable implementation of the
Future::AsyncAwait::Awaitable role. It runs tests that simulate various ways
in which Future::AsyncAwait will try to use an instance of this class, to
check that the implementation is valid.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Future) >= 0.43
%if %{with perl_Future_AsyncAwait_enables_role}
Requires:       perl(Role::Tiny)
Requires:       perl(Role::Tiny::With)
%endif
Requires:       perl(Test::More) >= 0.88
%if %{with perl_Future_AsyncAwait_enables_optional_test}
%if %{with perl_Future_AsyncAwait_enables_Devel_MAT}
Requires:       perl(Devel::MAT)
Requires:       perl(Devel::MAT::Dumper)
%endif
Requires:       perl(IO::Async::Loop)
Requires:       perl(Object::Pad) >= 0.15
Requires:       perl(Syntax::Keyword::Dynamically) >= 0.04
Requires:       perl(Syntax::Keyword::Try) >= 0.18
Requires:       perl(Test::Pod) >= 1.00
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Future-AsyncAwait-%{version}
for F in \
%if !%{with perl_Future_AsyncAwait_enables_optional_test} || !%{with perl_Future_AsyncAwait_enables_Devel_MAT}
    t/82devel-mat-dumper-helper.t \
%endif
%if !%{with perl_Future_AsyncAwait_enables_optional_test}
    t/80await+dynamically.t t/80await+try.t t/81async-method+dynamically.t \
    t/81memory-growth.t t/99pod.t \
%endif
%if !%{with perl_Future_AsyncAwait_enables_role}
    t/51awaitable-role.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
# Move Test subpackage content to a noarch location
install -m 0755 -d ${RPM_BUILD_ROOT}%{perl_vendorlib}
mv ${RPM_BUILD_ROOT}%{perl_vendorarch}/Test ${RPM_BUILD_ROOT}%{perl_vendorlib}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Future_AsyncAwait_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Future*
%{_mandir}/man3/Future::*

%files Test
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Feb 25 2021 Petr Pisar <ppisar@redhat.com> - 0.49-1
- 0.49 bump
- Package tests

* Wed Feb 03 2021 Petr Pisar <ppisar@redhat.com> - 0.48-1
- 0.48 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.47-1
- 0.47 bump

* Mon Nov 09 2020 Petr Pisar <ppisar@redhat.com> - 0.46-1
- 0.46 bump

* Fri Oct 23 2020 Petr Pisar <ppisar@redhat.com> - 0.45-1
- 0.45 bump

* Mon Oct 12 2020 Petr Pisar <ppisar@redhat.com> - 0.44-1
- 0.44 bump

* Wed Jul 15 2020 Petr Pisar <ppisar@redhat.com> 0.43-1
- Specfile autogenerated by cpanspec 1.78.
