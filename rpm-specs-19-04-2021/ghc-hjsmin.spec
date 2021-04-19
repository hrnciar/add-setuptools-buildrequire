# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hjsmin
%global pkgver %{pkg_name}-%{version}

# assumes dist-newstyle/
%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.2.0.4
Release:        4%{?dist}
Summary:        Haskell implementation of a javascript minifier

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-language-javascript-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-text-prof
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-unix-devel
%endif
# End cabal-rpm deps

%description
Reduces size of javascript files by stripping out extraneous whitespace and
other syntactic elements, without changing the semantics.


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
chmod a-x Readme.md
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%cabal_test


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc Readme.md
%{_bindir}/%{pkg_name}


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.2.0.4-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.2.0.4-1
- update to 0.2.0.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.2.0.2-11
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.2.0.2-9
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.2.0.2-7
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.2.0.2-4
- rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 0.2.0.2-1
- update to 0.2.0.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Jens Petersen <petersen@redhat.com> - 0.2.0.1-1
- update to 0.2.0.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug  5 2015 Jens Petersen <petersen@redhat.com> - 0.1.4.7-8
- use license macro
- move bindir/hjsmin to devel subpackage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Jens Petersen <petersen@redhat.com> - 0.1.4.7-6
- cblrpm refresh

* Mon Nov 17 2014 Jens Petersen <petersen@redhat.com> - 0.1.4.7-5
- refresh to cblrpm-0.8.11

* Tue Sep 30 2014 Ricky Elrod <relrod@redhat.com> - 0.1.4.7-4
- Rebuild again.

* Tue Sep 23 2014 Ricky Elrod <relrod@redhat.com> - 0.1.4.7-3
- Rebuild for latest optparse-applicative.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Ricky Elrod <relrod@redhat.com> - 0.1.4.7-1
- Latest upstream release.

* Mon May 19 2014 Ricky Elrod <relrod@redhat.com> - 0.1.4.6-4
- Rebuild for hjsmin... Again.

* Fri May 16 2014 Ricky Elrod <relrod@redhat.com> - 0.1.4.6-3
- Rebuild for hjsmin.

* Mon May 12 2014 Ricky Elrod <relrod@redhat.com> - 0.1.4.6-2
- Rebuild for new optparse-applicative.

* Mon May 12 2014 Ricky Elrod <relrod@redhat.com> - 0.1.4.6-1
- Latest upstream release.
- Add optparse-applicative dep.

* Thu Apr 24 2014 Jens Petersen <petersen@redhat.com> - 0.1.4.4-5
- rebuild

* Mon Jan 20 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.1.4.4-4
- Rebuild again.

* Sun Jan 19 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.1.4.4-3
- Rebuild for utf8-light.

* Sat Jan 11 2014 Jens Petersen <petersen@redhat.com> - 0.1.4.4-2
- rebuild

* Thu Dec 5 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.1.4.4-1
- Latest upstream release.

* Thu Nov 7 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.1.4.3-2
- rebuild

* Tue Oct 8 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.1.4.3-1
- Latest upstream release.

* Thu Sep 26 2013 Jens Petersen <petersen@redhat.com> - 0.1.4.1-3
- rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  8 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.4.1-1
- spec file generated by cabal-rpm-0.8.2
