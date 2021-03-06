# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name gtk3
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.15.5
Release:        4%{?dist}
Summary:        Binding to the Gtk+ 3 graphical user interface library

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
Patch0:         gtk3-Debian-ppc64-work-around-pixel-define.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-gtk2hs-buildtools-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cairo-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-gio-prof
BuildRequires:  ghc-glib-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pango-prof
BuildRequires:  ghc-text-prof
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# End cabal-rpm deps

%description
This is the core library of the Gtk2Hs suite of libraries for Haskell based on
Gtk+. Gtk+ is an extensive and mature multi-platform toolkit for creating
graphical user interfaces.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gthread-2.0)
Requires:       pkgconfig(gtk+-3.0)
# End cabal-rpm deps

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
# End cabal-rpm setup
%ifarch ppc64 ppc64le
%patch0 -p1 -b .orig
%endif


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install

# we include the demos in devel docdir
rm -r %{buildroot}%{_datadir}/%{pkg_name}-%{version}


%files -f %{name}.files
# Begin cabal-rpm files:
%license COPYING
# End cabal-rpm files


%files devel -f %{name}-devel.files


%if %{with haddock}
%files doc -f %{name}-doc.files
%license COPYING
%endif
%doc demo


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jens Petersen <petersen@redhat.com> - 0.15.5-2
- re-enable ppc64le

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 0.15.5-1
- update to 0.15.5

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.15.4-1
- update to 0.15.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Jens Petersen <petersen@redhat.com> - 0.15.1-1
- update to 0.15.1
- exclude ppc64le because of #1737587
- move demo/ to new doc subpkg

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.14.9-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.14.9-1
- update to 0.14.9

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.14.8-1
- update to 0.14.8

* Mon Aug 14 2017 Jens Petersen <petersen@redhat.com> - 0.14.6-4
- reenable i686 (#1427000)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 0.14.6-1
- update to 0.14.6
- exclude i686 due to gcc7 __float128

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 Jens Petersen <petersen@redhat.com> - 0.14.2-1
- update to 0.14.2
- Debian patch for ppc64 pixel (#1291501)

* Sun Mar  6 2016 Jens Petersen <petersen@fedoraproject.org> - 0.14.1-3
- rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep  3 2015 Jens Petersen <petersen@fedoraproject.org> - 0.14.1-1
- update to 0.14.1

* Thu Jul  9 2015 Jens Petersen <petersen@redhat.com> - 0.13.8-2
- use license macro (#1045963)

* Mon Jun 29 2015 Jens Petersen <petersen@redhat.com> - 0.13.8-1
- update to 0.13.8
- mention Gtk+3 in summary (#1045963)

* Sat Jun 13 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.13.7-1
- spec file generated by cabal-rpm-0.9.6
