Name:           perl-Struct-Dumb
Version:        0.12
Release:        4%{?dist}
Summary:        Make simple lightweight record-like structures
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Struct-Dumb
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Struct-Dumb-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
Struct::Dumb creates record-like structure types, similar to the struct
keyword in C, C++ or C#, or Record in Pascal. An invocation of this module
will create a construction function which returns new object references
with the given field values. These references all respond to lvalue methods
that access or modify the values stored.

%prep
%setup -q -n Struct-Dumb-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Struct
%{_mandir}/man3/Struct*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-2
- Perl 5.32 rebuild

* Sun Apr 26 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.12-1
- Update to 0.12

* Sun Apr 19 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.11-1
- Update to 0.11
- Use /usr/bin/perl instead of %%{__perl}

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-10
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-7
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.24 rebuild

* Fri Mar 11 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.09-1
- Update to 0.09

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.08-1
- Update to 0.08

* Wed Oct 14 2015 Emmanuel Seyman <emmanuel@seyman.fr> -  0.07-1
- Update to 0.07

* Fri Oct 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.06-1
- Update to 0.06

* Fri Oct 02 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.04-1
- Update to 0.04

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-3
- Perl 5.22 rebuild

* Mon Oct 20 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.03-2
- Take into account review feedback (#1154405)

* Sun Oct 19 2014 Emmanuel Seyman <emmanuel@seyman.fr> 0.03-1
- Specfile autogenerated by cpanspec 1.78.