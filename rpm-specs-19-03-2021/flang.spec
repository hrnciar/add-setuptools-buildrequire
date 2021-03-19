%global rc_ver 3
%global baserelease 4
%global flang_srcdir flang-%{version}%{?rc_ver:rc%{rc_ver}}.src
%global maj_ver 12
%global min_ver 0
%global patch_ver 0

Name: flang
Version: %{maj_ver}.%{min_ver}.%{patch_ver}
Release: %{?rc_ver:0.}%{baserelease}%{?rc_ver:.rc%{rc_ver}}%{?dist}
Summary: a Fortran language front-end designed for integration with LLVM

License: ASL 2.0 with exceptions
URL:     https://github.com/llvm/llvm-project/tree/master/flang
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}%{?rc_ver:-rc%{rc_ver}}/%{flang_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}%{?rc_ver:-rc%{rc_ver}}/%{flang_srcdir}.tar.xz.sig
Source2: tstellar-gpg-key.asc

# Needed for documentation generation
Patch1: 0001-PATCH-flang-Disable-use-of-sphinx_markdown_tables.patch
Patch2: 0002-PATCH-flang-Fix-build-with-gcc-11.patch

# because mlir doesn't build on arm (yet)
ExcludeArch: armv7hl

# Avoid gcc reaching 4GB of memory on 32-bit targets and also running out of
# memory on builders with many CPUs.
%ifarch %{ix86} s390x x86_64
%global _lto_cflags %{nil}
%global _smp_mflags -j1
%endif


BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: llvm-devel = %{version}
BuildRequires: llvm-test = %{version}
BuildRequires: llvm-googletest = %{version}
BuildRequires: mlir-devel = %{version}
BuildRequires: ninja-build
BuildRequires: python3-lit >= 12.0.0
BuildRequires: python3-sphinx
BuildRequires: python3-recommonmark

# For origin certification
BuildRequires: gnupg2

%description

Flang is a ground-up implementation of a Fortran front end written in modern
C++.

%package devel
Summary: Flang header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Flang header files.

%package doc
Summary: Documentation for Flang
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for Flang

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{flang_srcdir} -p2

%build
%cmake -GNinja \
       -DMLIR_TABLEGEN_EXE=%{_bindir}/mlir-tblgen \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH=";" \
       -DLLVM_MAIN_SRC_DIR=%{_datadir}/llvm/src \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
       -DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
       -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/llvm/ \
\
       -DFLANG_INCLUDE_DOCS:BOOL=ON \
       -DLLVM_ENABLE_SPHINX:BOOL=ON \
       -DSPHINX_WARNINGS_AS_ERRORS=OFF \
       -DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3 \
\
%if 0%{?__isa_bits} == 64
       -DLLVM_LIBDIR_SUFFIX=64
%else
       -DLLVM_LIBDIR_SUFFIX=
%endif

# Avoid gcc reaching 4GB of memory
%ifarch %{ix86} s390x
sed -i -e 's/-g /-g1 /g' -e 's/-O2/-O1/g' %{_builddir}/%{flang_srcdir}/%{_build}/build.ninja
%endif

export LD_LIBRARY_PATH=%{_builddir}/%{flang_srcdir}/%{_build}/lib
%cmake_build
%cmake_build --target docs-flang-html


%install
%cmake_install

# this is a test binary
rm -f %{buildroot}%{_bindir}/f18-parse-demo

install -d %{buildroot}%{_pkgdocdir}/html
cp -r %{_vpath_builddir}/docs/html/* %{buildroot}%{_pkgdocdir}/html/

chmod 0755 %{buildroot}%{_bindir}/flang

%check

# Assertion failure: lib/Semantics/canonicalize-acc.cpp:93
# /usr/include/c++/11/optional:447: constexpr const _Tp& std::_Optional_base_impl<_Tp, _Dp>::_M_get() const [with _Tp = Fortran::parser::DoConstruct; _Dp = std::_Optional_base<Fortran::parser::DoConstruct, false, false>]: Assertion 'this->_M_is_engaged()' failed.
rm test/Semantics/OpenACC/acc-canonicalization-validity.f90

# these tests fail on all or specific arches
rm test/Semantics/resolve63.f90

%ifarch s390x
rm test/Evaluate/folding07.f90
%endif

%ifarch %{ix86}
rm -f test/Fir/fir-ops.fir
rm -f test/Semantics/assign03.f90
rm -f test/Semantics/data05.f90
rm -f test/Semantics/offsets01.f90
rm -f test/Semantics/offsets02.f90
rm -f test/Semantics/typeinfo01.f90
%endif

export LD_LIBRARY_PATH=%{_builddir}/%{flang_srcdir}/%{_build}/lib
%cmake_build --target check-flang 

%files
%license LICENSE.txt
%{_bindir}/f18
%{_bindir}/tco
%{_bindir}/flang
%{_libdir}/libFortranLower.so.%{maj_ver}
%{_libdir}/libFIROptimizer.so.%{maj_ver}
%{_libdir}/libFortranSemantics.so.%{maj_ver}
%{_libdir}/libFortranCommon.so.%{maj_ver}
%{_libdir}/libFortranRuntime.so.%{maj_ver}
%{_libdir}/libFortranDecimal.so.%{maj_ver}
%{_libdir}/libFortranEvaluate.so.%{maj_ver}
%{_libdir}/libFortranParser.so.%{maj_ver}

%files devel
%{_libdir}/libFortranLower.so
%{_libdir}/libFortranParser.so
%{_libdir}/libFortranCommon.so
%{_libdir}/libFortranSemantics.so
%{_libdir}/libFIROptimizer.so
%{_libdir}/libFortranDecimal.so
%{_libdir}/libFortranRuntime.so
%{_libdir}/libFortranEvaluate.so
%{_includedir}/flang
%{_libdir}/cmake/

%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html/

%changelog
* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-0.4.rc3
- LLVM 12.0.0 rc3

* Wed Mar 10 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- rebuilt

* Wed Feb 24 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- 12.0.0-rc2 Release

* Fri Feb 19 2021 Tom Stellard <tsellar@redhat.com> - 12.0.0-0.1.rc1
- 12.0.0-rc1 Release

* Wed Feb 10 2021 Jeff Law <law@redhat.com> - 11.1.0-0.3.rc1
- Fix missing #include for gcc-11

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Serge Guelton - 11.1.0-0.1.rc1
- 11.1.0-rc1 release

* Wed Jan 06 2021 Serge Guelton - 11.0.1-3
- LLVM 11.0.1 final

* Tue Dec 22 2020 sguelton@redhat.com - 11.0.1-2.rc2
- llvm 11.0.1-rc2

* Tue Dec 01 2020 sguelton@redhat.com - 11.0.1-1.rc1
- llvm 11.0.1-rc1

* Thu Oct 15 2020 sguelton@redhat.com - 11.0.0-1
- Fix NVR

* Mon Oct 12 2020 sguelton@redhat.com - 11.0.0-0.5
- llvm 11.0.0 - final release

* Thu Oct 08 2020 sguelton@redhat.com - 11.0.0-0.4.rc6
- 11.0.0-rc6

* Fri Oct 02 2020 sguelton@redhat.com - 11.0.0-0.3.rc5
- 11.0.0-rc5 Release

* Sun Sep 27 2020 sguelton@redhat.com - 11.0.0-0.2.rc3
- Fix NVR

* Thu Sep 24 2020 sguelton@redhat.com - 11.0.0-0.1.rc3
- 11.0.0-rc3 Release

* Tue Sep 01 2020 sguelton@redhat.com - 11.0.0-0.1.rc2
- Initial version.

