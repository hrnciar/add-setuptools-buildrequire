# Enable debugging with Devel::MAT
%bcond_with perl_Object_Pad_enables_Devel_MAT
# Perform optional tests
%bcond_without perl_Object_Pad_enables_optional_test

Name:           perl-Object-Pad
Version:        0.37
Release:        1%{?dist}
Summary:        Simple syntax for lexical slot-based objects
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Object-Pad
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Object-Pad-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
%if %{with perl_Object_Pad_enables_Devel_MAT}
BuildRequires:  perl(Devel::MAT::Dumper::Helper) >= 0.41
%endif
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XS::Parse::Sublike::Builder) >= 0.10
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Carp)
# experimental since perl 5.20
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
# indirect not used (only with 5.20.0 <= perl < 5.31.9)
BuildRequires:  perl(mro)
# XS::Parse::Sublike is loaded from XS generated when running ./Build.PL
BuildRequires:  perl(XS::Parse::Sublike) >= 0.10
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(attributes)
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Refcount)
%if %{with perl_Object_Pad_enables_optional_test} && !%{defined perl_bootstrap}
# A cycle: perl-Future-AsyncAwait → perl-Object-Pad
# A cycle: perl-Syntax-Keyword-Dynamically → perl-Object-Pad
# Optional tests:
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait) >= 0.40
BuildRequires:  perl(Moo)
BuildRequires:  perl(Syntax::Keyword::Dynamically) >= 0.04
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(experimental)
Requires:       perl(XS::Parse::Sublike) >= 0.10

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((ARole|BaseClass)\\)
# Filter under-specified dependencies
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)$

%description
This Perl module provides a simple syntax for creating object classes, which
uses private variables that look like lexical variables for object member
fields.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(strict)
Requires:       perl(Test::More) >= 0.88
%if %{with perl_Object_Pad_enables_optional_test} && !%{defined perl_bootstrap}
Requires:       perl(Future)
Requires:       perl(Future::AsyncAwait) >= 0.40
Requires:       perl(Syntax::Keyword::Dynamically) >= 0.04
Requires:       perl(Test::MemoryGrowth)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Object-Pad-%{version}
%if !%{with perl_Object_Pad_enables_optional_test} || %{defined perl_bootstrap}
for F in t/08extends-Moo.t t/80async-method.t t/80dynamically+Object-Pad.t \
    t/81async-method+dynamically.t t/90leak.t t/99pod.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E\b}' MANIFEST
done
%endif
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
%if %{with perl_Object_Pad_enables_optional_test} && !%{defined perl_bootstrap}
rm %{buildroot}/%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Object*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Apr 06 2021 Petr Pisar <ppisar@redhat.com> - 0.37-1
- 0.37 bump

* Fri Feb 19 2021 Petr Pisar <ppisar@redhat.com> - 0.36-1
- 0.36 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Petr Pisar <ppisar@redhat.com> - 0.35-1
- 0.35 bump

* Thu Nov 05 2020 Petr Pisar <ppisar@redhat.com> - 0.34-1
- 0.34 bump

* Wed Sep 16 2020 Petr Pisar <ppisar@redhat.com> - 0.33-1
- 0.33 bump

* Tue Jul 28 2020 Petr Pisar <ppisar@redhat.com> - 0.31-2
- Finish a bootstrap

* Wed Jul 15 2020 Petr Pisar <ppisar@redhat.com> 0.31-1
- Specfile autogenerated by cpanspec 1.78.
