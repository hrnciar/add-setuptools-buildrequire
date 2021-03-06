# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name parallel
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        3.2.2.0
Release:        10%{?dist}
Summary:        Parallel programming library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
# End cabal-rpm deps

%description
This package provides a library for parallel programming.

For documentation start from the "Control.Parallel.Strategies" module below.

For more tutorial documentation, see the book
<http://simonmar.github.io/pages/pcph.html Parallel and Concurrent Programming
in Haskell>.

To understand the principles behind the library, see
<http://simonmar.github.io/bib/papers/strategies.pdf Seq no more: Better
Strategies for Parallel Haskell>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc changelog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 3.2.2.0-7
- refresh to cabal-rpm-2.0.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 3.2.2.0-5
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 3.2.2.0-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Jens Petersen <petersen@redhat.com> - 3.2.2.0-1
- update to 3.2.2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 3.2.1.1-1
- update to 3.2.1.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 3.2.1.0-3
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Jens Petersen <petersen@redhat.com> - 3.2.1.0-1
- update to 3.2.1.0

* Tue Jun  7 2016 Jens Petersen <petersen@redhat.com> - 3.2.0.6-1
- update to 3.2.0.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug  8 2014 Jens Petersen <petersen@redhat.com> - 3.2.0.4-1
- update to 3.2.0.4

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 3.2.0.3-35
- update to cblrpm-0.8.11

* Mon Mar 31 2014 Jens Petersen <petersen@redhat.com> - 3.2.0.3-34
- update to 3.2.0.3 with cabal-rpm

* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 3.2.0.2-1
- update to 3.2.0.2

* Sun Mar 18 2012 Jens Petersen <petersen@redhat.com> - 3.1.0.1-9
- update to cabal2spec-0.25

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0.1-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Marcela Ma??l????ov?? <mmaslano@redhat.com> - 3.1.0.1-7.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Ma??l????ov?? <mmaslano@redhat.com> - 3.1.0.1-7.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 3.1.0.1-7.1
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 3.1.0.1-7
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 3.1.0.1-6
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Fri May 27 2011 Jens Petersen <petersen@redhat.com> - 3.1.0.1-5
- update to cabal2spec-0.23: add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.0.1-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Jens Petersen <petersen@redhat.com> - 3.1.0.1-2
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 3.1.0.1-1
- update to 3.1.0.1
- update url and drop -o obsoletes

* Sat Sep  4 2010 Jens Petersen <petersen@redhat.com> - 2.2.0.1-4
- add hscolour and doc obsolete (cabal2spec-0.22.2)

* Sun Jun 27 2010 Jens Petersen <petersen@redhat.com> - 2.2.0.1-3
- sync cabal2spec-0.22.1

* Tue Apr 27 2010 Jens Petersen <petersen@redhat.com> - 2.2.0.1-2
- rebuild against ghc-6.12.2

* Wed Mar 24 2010 Jens Petersen <petersen@redhat.com> - 2.2.0.1-1
- update to 2.2.0.1 for haskell-platform-2010.1.0.0
- new dep on deepseq

* Thu Jan 21 2010 Jens Petersen <petersen@redhat.com> - 1.1.0.1-2
- BSD license
- summary and description
- note part of haskell-platform-2009.2.0.2

* Thu Jan 21 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 1.1.0.1-1
- initial packaging for Fedora automatically generated by cabal2spec-0.21.1
