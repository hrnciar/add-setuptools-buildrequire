Name:           perl-URI-db
Version:        0.19
Release:        8%{?dist}
Summary:        Perl support for database URIs
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/URI-db/
Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/URI-db-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(warnings)
# run deps
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(URI::Nested) >= 0.10
# test deps
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.40
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This class provides support for database URIs. They're inspired by
JDBC URIs and PostgreSQL URIs, though they're a bit more formal.
The specification for their format is documented in README.md.

%prep
%setup -q -n URI-db-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README README.md
%{perl_vendorlib}/URI*
%{_mandir}/man3/URI*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Emmanuel Seyman <emmanuel@seyman.fr> 0.19-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
