# Run X11 tests
%{bcond_without perl_Tk_GraphViz_enables_x11_test}

Name:           perl-Tk-GraphViz
Version:        1.10
Release:        3%{?dist}
Summary:        Render an interactive GraphViz graph
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Tk-GraphViz
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Tk-GraphViz-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Tk) >= 800.020
BuildRequires:  perl(Tk::Canvas)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Font)
BuildRequires:  perl(Tk::IO)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(GraphViz)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
%if %{with perl_Tk_GraphViz_enables_x11_test}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       graphviz
Requires:       perl(File::Temp)
Requires:       perl(Pod::Usage)
Requires:       perl(Tk::BrowseEntry)
Requires:       perl(Tk::DialogBox)

Provides:       bundled(perl-Parse-Yapp) = 1.21

# Do not provide private bundled Parse::Yapp::Driver module
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Parse::Yapp::Driver\\)

%description
The GraphViz widget is derived from Tk::Canvas. It adds the ability to
render graphs in the canvas. The graphs can be specified either using the
DOT graph-description language, or using via a GraphViz object.

%prep
%setup -q -n Tk-GraphViz-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%if %{with perl_Tk_GraphViz_enables_x11_test}
    xvfb-run -d make test
%else
    make test
%endif

%files
%doc Changes parseRecordLabel.yp README
%{_bindir}/tkgraphviz
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-2
- Replace Tk::MatchEntry (not package yet) by Tk::BrowseEntry

* Thu Jan 14 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-1
- 1.10 bump

* Thu Nov 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-1
- 1.07 bump

* Mon Nov 16 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-1
- 1.06 bump; Modernize spec
- Run X11 tests using xvfb-run

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-29
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-26
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-23
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Petr Pisar <ppisar@redhat.com> - 1.01-21
- Do not provide private bundled Parse::Yapp::Driver module (bug #829700)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-17
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-14
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.01-11
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.01-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.01-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.01-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 25 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 1.01-2
- Filter Parse::Yapp::Driver provide away

* Tue Jun 09 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 1.01-1
- Specfile autogenerated by cpanspec 1.78.
- Fix up license
