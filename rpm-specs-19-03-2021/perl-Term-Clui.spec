Name:           perl-Term-Clui
Version:        1.76
Release:        5%{?dist}
Summary:        Perl module offering a Command-Line User Interface
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Term-Clui
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Term-Clui-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Term::Size)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       perl(Term::Size)
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
Term::Clui offers a high-level user interface to give the user of command-
line applications a consistent "look and feel". Its metaphor for the
computer is as a human-like conversation-partner, and as each
question/response is completed it is summarized onto one line, and remains
on screen, so that the history of the session gradually accumulates on the
screen and is available for review, or for cut/paste. This user interface
can therefore be intermixed with standard applications which write to
STDOUT or STDERR, such as make, pgp, rcs etc.

%prep
%setup -q -n Term-Clui-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README examples
%license LICENSE
%{perl_vendorlib}/Term*
%{_mandir}/man3/Term*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.76-1
- Update to 1.76
- Replace calls to perl with /usr/bin/perl
- Replace calls to "make install" with %%{make_install}
- Replace calls to make with %%{make_build}
- Use %%license tag

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.75-1
- Update to 1.75

* Sun Jul 15 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.73-1
- Update to 1.73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-2
- Perl 5.26 rebuild

* Mon Feb 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.71-1
- Update to 1.71

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-2
- Perl 5.22 rebuild

* Tue Apr 21 2015 Emmanuel Seyman <emmanuel@seyman.fr> -  1.70-1
- Update to 1.70
- Minor improvements to the spec file

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.68-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Kostas Georgiou <georgiou@opengamma.com> 1.68-3
- use DESTDIR instead of PERL_INSTALL_ROOT at install

* Wed Oct 16 2013 Kostas Georgiou <georgiou@opengamma.com> 1.68-2
- Review changes/fixes #1018859.

* Wed Oct 02 2013 Kostas Georgiou <georgiou@opengamma.com> 1.68-1
- Specfile autogenerated by cpanspec 1.78.
