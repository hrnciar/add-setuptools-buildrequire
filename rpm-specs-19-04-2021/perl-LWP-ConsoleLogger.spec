# Enable integration with Mojo
%bcond_without perl_LWP_ConsoleLogger_enables_mojo

Name:           perl-LWP-ConsoleLogger
Version:        0.000043
Release:        1%{?dist}
Summary:        LWP tracing and debugging
License:        Artistic 2.0
URL:            https://metacpan.org/release/LWP-ConsoleLogger
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-ConsoleLogger-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.13.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Data::Printer) >= 0.36
BuildRequires:  perl(DateTime)
BuildRequires:  perl(HTML::Restrict)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(HTTP::CookieMonster)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003005
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Log::Dispatch) >= 2.56
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(Parse::MIME)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(String::Trim)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Term::Size::Any)
BuildRequires:  perl(Text::SimpleTable::AutoWidth) >= 0.09
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Common::Numeric)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI::Query)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(XML::Simple)
# Optional run-time:
BuildRequires:  perl(HTML::FormatText::Lynx) >= 23
%if %{with perl_LWP_ConsoleLogger_enables_mojo}
BuildRequires:  perl(Mojo::UserAgent)
%endif
# Tests:
# CPAN::Meta not helpful
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTTP::CookieJar::LWP)
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Plack::Handler::HTTP::Server::Simple) >= 0.016
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Test::Agent)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(version)
BuildRequires:  perl(WWW::Mechanize)
%if %{with perl_LWP_ConsoleLogger_enables_mojo}
# Optional tests:
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojolicious) >= 7.13
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Printer) >= 0.36
Recommends:     perl(HTML::FormatText::Lynx) >= 23
Requires:       perl(JSON::MaybeXS) >= 1.003005
Requires:       perl(Log::Dispatch) >= 2.56
%if %{with perl_LWP_ConsoleLogger_enables_mojo}
Suggests:       perl(Mojo::UserAgent)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::Printer|JSON::MaybeXS|Log::Dispatch)\\)$

%description
It can be hard (or at least tedious) to debug WWW::Mechanize scripts.
LWP::ConsoleLogger::Easy wrapper offers debug_ua() function that instantiates
LWP logging and also returns a LWP::ConsoleLogger object, which you may then
tweak to your heart's desire. If you need to tweak the settings that
LWP::ConsoleLogger::Easy chooses for you, please use LWP::ConsoleLogger. If
you're able to install HTML::FormatText::Lynx then you'll get highly readable
HTML to text conversions.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_LWP_ConsoleLogger_enables_mojo}
Requires:       perl(Mojo::Base)
Requires:       perl(Mojolicious) >= 7.13
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n LWP-ConsoleLogger-%{version}
# Correct shebangs
perl -i -MConfig -pe 's|#!/usr/bin/env perl|$Config{startperl}|' examples/*
# Help generators to recognize Perl scripts
for F in $(find t -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS examples README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Mar 05 2021 Petr Pisar <ppisar@redhat.com> - 0.000043-1
- 0.000043 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.000042-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.000042-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.000042-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.000042-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.000042-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Petr Pisar <ppisar@redhat.com> - 0.000042-1
- 0.000042 bump

* Wed Jun 12 2019 Petr Pisar <ppisar@redhat.com> - 0.000041-1
- 0.000041 bump

* Tue Jun 11 2019 Petr Pisar <ppisar@redhat.com> - 0.000040-1
- 0.000040 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.000039-2
- Perl 5.30 rebuild

* Wed Feb 21 2018 Petr Pisar <ppisar@redhat.com> 0.000039-1
- Specfile autogenerated by cpanspec 1.78.
