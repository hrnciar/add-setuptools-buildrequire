Name:           perl-Net-Amazon-EC2-Metadata
Version:        0.10
Release:        28%{?dist}
Summary:        Retrieves data from EC2 Metadata service
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-Amazon-EC2-Metadata
Source0:        https://cpan.metacpan.org/authors/id/N/NM/NMCFARL/Net-Amazon-EC2-Metadata-%{version}.tar.gz
Patch0:         perl-Net-Amazon-EC2-Metadata-0.10-say.patch
# https://rt.cpan.org/Public/Bug/Display.html?id=74949
Patch1:         net-amazon-ec2-metadata.diff
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module queries Amazon's Elastic Compute Cloud Metadata service.
It also fetches 'user_data' which follows the same API but is often no
considered part of the metadata service by Amazons documentation. The
module also ships with a command line tool ec2meta that provides the same
data.


%prep
%setup -q -n Net-Amazon-EC2-Metadata-%{version}
%patch0 -p1
%patch1 -p1


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-26
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-23
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-20
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-17
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-15
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-12
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.10-9
- Bulk sad and useless attempt at consistent SPEC file formatting

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.10-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.10-5
- Perl 5.16 rebuild

* Mon Feb 13 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.10-4
- Fix issues from review (Petr Pisar, #657518)

* Mon Nov 22 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.10-3
- Pull Test::More

* Fri Jul 24 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.10-2
- Patch to support more metadata (Vlastimil Holer, gdc#4395)

* Mon Jul 14 2008 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.10-1
- Specfile autogenerated by cpanspec 1.75.
- Patch away Perl6::Say dependency
- Adjust plist and License tag
