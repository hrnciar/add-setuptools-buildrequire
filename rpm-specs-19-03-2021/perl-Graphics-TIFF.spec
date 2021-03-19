# Run optional tests
%{bcond_without perl_Graphics_TIFF_enables_optional_test}

Name:           perl-Graphics-TIFF
Version:        9
Release:        1%{?dist}
Summary:        Perl extension for the LibTIFF library
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Graphics-TIFF
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Graphics-TIFF-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.3
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
%if %{with perl_Graphics_TIFF_enables_optional_test}
# Optional tests:
BuildRequires:  grep
# libtiff-tools for tiffcp, tiff2pdf, tiffinfo
BuildRequires:  libtiff-tools
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(feature)
BuildRequires:  perl(if)
BuildRequires:  perl(Image::Magick)
# Test::Perl::Critic not used
# for hexdump
BuildRequires:  util-linux
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
The Graphics::TIFF module allows a Perl developer to access TIFF images using
LibTIFF library in a Perlish and object-oriented way.

%package tests
Summary:        Tests for %{name}
# Keep full arch for t/90_MANIFEST.t embedding vendorarch
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Graphics_TIFF_enables_optional_test}
# Optional tests:
Requires:       grep
# libtiff-tools for tiffcp, tiff2pdf, tiffinfo
Requires:       libtiff-tools
Requires:       perl(:VERSION) >= 5.10
Requires:       perl(if)
Requires:       perl(Image::Magick)
# Test::Perl::Critic not used
# for hexdump
Requires:       util-linux
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Graphics-TIFF-%{version}
%if !%{with perl_Graphics_TIFF_enables_optional_test}
for F in t/1.t t/92_tiffinfo.t t/93_tiff2pdf.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' MANIFEST
done
%endif
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
perl -i -pe 's{\blib(/Graphics/TIFF.pm)\b}{%{perl_vendorarch}$1}' %{buildroot}/%{_libexecdir}/%{name}/t/90_MANIFEST.t
%if %{with perl_Graphics_TIFF_enables_optional_test}
cp -a examples %{buildroot}/%{_libexecdir}/%{name}
chmod +x %{buildroot}/%{_libexecdir}/%{name}/examples/*
%endif
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset TEST_AUTHOR
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
# Correct permissions
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TEST_AUTHOR
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Graphics*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Feb 11 2021 Petr Pisar <ppisar@redhat.com> - 9-1
- Version 9 bump

* Wed Feb 10 2021 Petr Pisar <ppisar@redhat.com> - 8-2
- Make tests subpackage architecture specific

* Tue Feb 09 2021 Petr Pisar <ppisar@redhat.com> - 8-1
- Version 8 bump
- Package tests and make them parallel-safe

* Mon Feb 08 2021 Petr Pisar <ppisar@redhat.com> - 7-3
- Adapt tests to libtiff-4.2.0 (CPAN RT#134344)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Petr Pisar <ppisar@redhat.com> - 7-1
- Version 7 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 10 2017 Petr Pisar <ppisar@redhat.com> - 6-1
- Version 6 bump

* Tue Aug 01 2017 Petr Pisar <ppisar@redhat.com> - 5-1
- Version 5 bump

* Fri Jul 28 2017 Petr Pisar <ppisar@redhat.com> 4-1
- Specfile autogenerated by cpanspec 1.78.
