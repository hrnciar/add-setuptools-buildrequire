Name:           perl-File-DirList
Version:        0.05
Release:        2%{?dist}
Summary:        Provide a sorted list of directory content
# Standard perl license, see README.md
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/File-DirList
Source0:        https://cpan.metacpan.org/authors/id/T/TP/TPABA/File-DirList/File-DirList-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  sed


Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
File::DirList can be used to get sorted directory content list.


%prep
%autosetup -p1 -n File-DirList-%{version}

# Fix line endings
sed -i 's|\r||g' README


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/File::DirList*.*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Sandro Mani <manisandro@gmail.com> - 0.05-1
- Initial package
