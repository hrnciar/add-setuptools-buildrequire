# Perform optional tests
%bcond_without perl_PDF_Builder_enables_optional_test
# Fully support PNG images with a libpng library
%bcond_without perl_PDF_Builder_enables_png
# Fully support TIFF images with libtiff library
%bcond_without perl_PDF_Builder_enables_tiff

Name:           perl-PDF-Builder
Version:        3.022
Release:        1%{?dist}
Summary:        Creation and modification of PDF files in Perl
# docs/buildDoc.pl:             same as PDF-Builder
# INFO/LICENSE:                 LGPLv2+
# lib/PDF/Builder/Basic/PDF/Pages.pm:   MIT or Artistic
# lib/PDF/Builder.pm:           LGPLv2+
# lib/PDF/Builder/Matrix.pm:    LGPLv2+ (same as PDF::API2)
# README:                       LGPLv2+ (v2+ according to the upstream)
License:        LGPLv2+ and (MIT or Artistic)
URL:            https://metacpan.org/release/PDF-Builder
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMPERRY/PDF-Builder-%{version}.tar.gz
# Fix running the tests from a read-only location, proposed to an upstream,
# <https://github.com/PhilterPaper/Perl-PDF-Builder/pull/153>
Patch0:         PDF-Builder-3.022-tests-Write-files-to-a-temporary-directory.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib) >= 1
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Font::TTF::Font)
%if %{with perl_PDF_Builder_enables_tiff}
BuildRequires:  perl(Graphics::TIFF) >= 7
%endif
%if %{with perl_PDF_Builder_enables_png}
BuildRequires:  perl(Image::PNG::Const)
BuildRequires:  perl(Image::PNG::Libpng) >= 0.56
%endif
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(English)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle) >= 1
BuildRequires:  perl(Test::More)
%if %{with perl_PDF_Builder_enables_optional_test}
# Optional tests:
# For "gs" program
BuildRequires:  ghostscript
# For "convert" program
BuildRequires:  ImageMagick
# For tiffcp program
BuildRequires:  libtiff-tools
BuildRequires:  perl(GD)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Compress::Zlib) >= 1
# They can be disabled at run-time. There is an imperfect pure-Perl fallback.
%if %{with perl_PDF_Builder_enables_tiff}
Recommends:     perl(Graphics::TIFF) >= 7
%endif
%if %{with perl_PDF_Builder_enables_png}
Recommends:     perl(Image::PNG::Const)
Recommends:     perl(Image::PNG::Libpng) >= 0.56
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Compress::Zlib|Test::Memory::Cycle)\\)$

# Remove disabled features.
# Originally I subpackaged PDF::Builder::Resource::XObject::Image/* modules
# which depend on the optional features. But it broke if the
# dependencies were installed, but the plugins were misssing. Also upstream
# exposes the checks for the dependencies in an API and a documentation. We would
# have to divert the code and the documentation from the upstream. Thus
# I decided to keep the plugins there and weaken the dependencies.
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Graphics::TIFF\\)|Image::PNG::)

%description
This Perl library enables you to create, import and modify documents in
Portagble Document Format (mostly compliant to PDF 1.4 version).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Memory::Cycle) >= 1
%if %{with perl_PDF_Builder_enables_optional_test}
# For "gs" program
Requires:       ghostscript
# For "convert" program
Requires:       ImageMagick
# For tiffcp program
Requires:       libtiff-tools
Requires:       perl(GD)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n PDF-Builder-%{version}
%patch0 -p1
# Remove unused tests and disabled features
for F in \
    t/author-critic.t t/author-pod-syntax.t \
%if !%{with perl_PDF_Builder_enables_optional_test}
    t/gd.t \
%endif
;do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 </dev/null
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-all-usable.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license INFO/LICENSE
%doc Changes contrib CONTRIBUTING examples README.md tools
%doc INFO/CONVERSION INFO/DEPRECATED INFO/Changes* INFO/KNOWN_INCOMP
%doc INFO/PATENTS INFO/RoadMap INFO/SUPPORT
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon Mar 29 2021 Petr Pisar <ppisar@redhat.com> - 3.022-1
- 3.022 bump
- Package tests

* Mon Feb 08 2021 Petr Pisar <ppisar@redhat.com> - 3.021-2
- Correct BlackIs1 for LZW- and G3-compressed bitonal images

* Thu Feb 04 2021 Petr Pisar <ppisar@redhat.com> - 3.021-1
- 3.021 bump
- License changed to "LGPLv2+ and (MIT or Artistic)"

* Fri Jan 29 2021 Petr Pisar <ppisar@redhat.com> - 3.019-2
- Clarify a license
- Adapt to Image-PNG-Libpng-0.56

* Mon Nov 02 2020 Petr Pisar <ppisar@redhat.com> 3.019-1
- Specfile autogenerated by cpanspec 1.78.
