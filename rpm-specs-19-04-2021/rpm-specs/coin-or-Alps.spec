%global		module		Alps

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:		coin-or-%{module}
Summary:	COIN-OR High-Performance Parallel Search Framework
Version:	1.5.7
Release:	6%{?dist}
License:	EPL-1.0
URL:		https://github.com/coin-or/CHiPPS-ALPS
Source0:	https://github.com/coin-or/CHiPPS-ALPS/archive/releases/%{version}/CHiPPS-ALPS-%{version}.tar.gz
BuildRequires:	coin-or-Cgl-devel
BuildRequires:	coin-or-Clp-devel
BuildRequires:	coin-or-CoinUtils-doc
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	glpk-devel
BuildRequires:	make
BuildRequires:	%{blaslib}-devel

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Bad #define generated if svnversion is available
Patch1:		%{name}-svnversion.patch

%description
CHiPPS is the COIN-OR High-Performance Parallel Search Framework, a framework
for implementing parallel algorithms based on tree search. The current CHiPPS
architecture consists of three layers. The Abstract Library for Parallel Search
(ALPS) is the base layer of a hierarchy consisting of implementations of
various tree search algorithms for specific problem types. The Branch,
Constrain, and Price Software (BiCePS) is a data management layer built on
top of ALPS for implementing relaxation-based branch and bound algorithms.
The BiCePS Linear Integer Solver (BLIS) is a concretization of the BiCePS
layer for solving mixed-integer linear programs. ALPS, BiCePS, and BLIS
are sub-repositories of the CHiPPS Subversion repository.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-CoinUtils-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-CoinUtils-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n CHiPPS-ALPS-releases-%{version}

%build
%configure \
  --with-blas-incdir=%{_includedir}/%{blaslib} \
  --with-blas-lib=-l%{blaslib} \
  --with-glpk-incdir=%{_includedir} \
  --with-glpk-lib=-lglpk \
  --with-lapack-incdir=%{_includedir}/%{blaslib} \
  --with-lapack-lib=-l%{blaslib}

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all
%make_build -C Alps doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,alps_addlibs.txt}
cp -a Alps/doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%ldconfig_scriptlets

%files
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/README
%{_libdir}/libAlps.so.0
%{_libdir}/libAlps.so.0.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libAlps.so
%{_libdir}/pkgconfig/alps.pc

%files		doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/alps_doxy.tag

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 I??aki ??car <iucar@fedoraproject.org> - 1.5.7-5
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.5.7-1
- Update to latest 1.5.x upstream release (bz 1413567)
- Update URLs
- Change License from EPL to EPL-1.0
- Eliminate unnecessary BRs and Rs
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Package doxygen tag file to enable cross-linking

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.5.5-8
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.5-1
- Update to latest upstream release (#1313326)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.4-1
- Update to latest upstream release (#1265642)

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.3-4
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.3-2
- Rebuild to ensure built after all dependencies available.

* Sun Jun 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.3-1
- Update to latest upstream release (#1227739)

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.2-1
- Update to latest upstream release (#1209030)

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.1-2
- Rebuild to ensure using latest C++ abi changes.

* Sat Feb 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.1-1
- Update to latest upstream release (#1191432).

* Mon Feb  9 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.5.0-1
- Update to latest upstream release (#1184772).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar  8 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.10-3
- Correct misspelling of _smp_mflags.
- Make devel subpackage require coin-or-CoinUtils-devel.

* Sat Mar  8 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.10-2
- Add missing bzip2-devel and texlive-epstopdf build requires.

* Sat Mar  8 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.10-1
- Update to latest upstream release.

* Wed Jan  8 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.9-1
- Update to latest upstream release.

* Wed Jan  8 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.8-1
- Update to latest upstream release.

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.5-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.2-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.2-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.2-2
- Rename package to coin-or-Alps.
- Do not package Thirdy party data or data without clean license.

* Sat Sep 29 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.2-1
- Initial coinor-Alps spec.
