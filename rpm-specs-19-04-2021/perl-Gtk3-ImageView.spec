Name:           perl-Gtk3-ImageView
Version:        6
Release:        2%{?dist}
Summary:        Image viewer widget for GTK 3
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Gtk3-ImageView
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Gtk3-ImageView-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Cairo)
BuildRequires:  perl(Carp)
BuildRequires:  perl(feature)
BuildRequires:  perl(Glib) >= 1.21
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(if)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp::Always)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  xorg-x11-server-Xvfb
# Optional tests:
# git-core not used
# Test::Perl::Critic not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(if)
Requires:       perl(Glib) >= 1.21

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\)$

%description
The Gtk3::ImageView widget allows the user to zoom, pan and select the
specified image and provides hooks to allow additional tools, e.g. painter,
to be created and used.

%prep
%setup -q -n Gtk3-ImageView-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TEST_AUTHOR
xvfb-run -d make test

%files
%doc README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Petr Pisar <ppisar@redhat.com> - 6-1
- Version 6 bump

* Mon Nov 02 2020 Petr Pisar <ppisar@redhat.com> 4-1
- Specfile autogenerated by cpanspec 1.78.