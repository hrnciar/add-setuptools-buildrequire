%global compat_build 1

%global maj_ver 9
%global min_ver 0
%global patch_ver 1
#%%global rc_ver 3
%global baserelease 8

%global clang_tools_binaries \
	%{_bindir}/clangd \
	%{_bindir}/clang-apply-replacements \
	%{_bindir}/clang-change-namespace \
	%{_bindir}/clang-doc \
	%{_bindir}/clang-include-fixer \
	%{_bindir}/clang-query \
	%{_bindir}/clang-refactor \
	%{_bindir}/clang-reorder-fields \
	%{_bindir}/clang-rename \
	%{_bindir}/clang-tidy

%global clang_binaries \
	%{_bindir}/clang \
	%{_bindir}/clang++ \
	%{_bindir}/clang-%{maj_ver} \
	%{_bindir}/clang++-%{maj_ver} \
	%{_bindir}/clang-check \
	%{_bindir}/clang-cl \
	%{_bindir}/clang-cpp \
	%{_bindir}/clang-extdef-mapping \
	%{_bindir}/clang-format \
	%{_bindir}/clang-import-test \
	%{_bindir}/clang-offload-bundler \
	%{_bindir}/clang-scan-deps \
	%{_bindir}/diagtool \
	%{_bindir}/hmaptool

%if 0%{?compat_build}
%global pkg_name clang%{maj_ver}.%{min_ver}
# Install clang to same prefix as llvm, so that apps that use llvm-config
# will also be able to find clang libs.
%global install_prefix %{_libdir}/llvm%{maj_ver}.%{min_ver}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib

%global pkg_bindir %{install_bindir}
%global pkg_includedir %{_includedir}/llvm%{maj_ver}.%{min_ver}
%global pkg_libdir %{install_libdir}
%else
%global pkg_name clang
%global install_prefix /usr
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%else
%bcond_with python3
%endif

%global build_install_prefix %{buildroot}%{install_prefix}

%ifarch ppc64le
# Too many threads on ppc64 systems causes OOM errors.
%global _smp_mflags -j8
%endif

%global clang_srcdir clang-%{version}%{?rc_ver:rc%{rc_ver}}.src
%global clang_tools_srcdir clang-tools-extra-%{version}%{?rc_ver:rc%{rc_ver}}.src

Name:		%pkg_name
Version:	%{maj_ver}.%{min_ver}.%{patch_ver}
Release:	%{baserelease}%{?rc_ver:.rc%{rc_ver}}%{?dist}
Summary:	A C language family front-end for LLVM

License:	NCSA
URL:		http://llvm.org
Source0:	http://%{?rc_ver:pre}releases.llvm.org/%{version}/%{?rc_ver:rc%{rc_ver}}/%{clang_srcdir}.tar.xz
%if !0%{?compat_build}
Source1:	http://%{?rc_ver:pre}releases.llvm.org/%{version}/%{?rc_ver:rc%{rc_ver}}/%{clang_tools_srcdir}.tar.xz
%endif

Patch4:		0002-gtest-reorg.patch
Patch11:	0001-ToolChain-Add-lgcc_s-to-the-linker-flags-when-using-.patch
Patch13:	0001-Make-funwind-tables-the-default-for-all-archs.patch
# Fix crash with kernel bpf self-tests
Patch14:	0001-BPF-annotate-DIType-metadata-for-builtin-preseve_arr.patch
Patch15:	altivec.patch

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	ninja-build
%if 0%{?compat_build}
BuildRequires:	llvm%{maj_ver}.%{min_ver}-devel = %{version}
BuildRequires:	llvm%{maj_ver}.%{min_ver}-static = %{version}
%else
BuildRequires:	llvm-devel = %{version}
BuildRequires:	llvm-test = %{version}
# llvm-static is required, because clang-tablegen needs libLLVMTableGen, which
# is not included in libLLVM.so.
BuildRequires:	llvm-static = %{version}
BuildRequires:	llvm-googletest = %{version}
%endif

BuildRequires:	libxml2-devel
BuildRequires:	perl-generators
BuildRequires:	ncurses-devel
# According to https://fedoraproject.org/wiki/Packaging:Emacs a package
# should BuildRequires: emacs if it packages emacs integration files.
BuildRequires:	emacs

# These build dependencies are required for the test suite.
%if %with python3
# The testsuite uses /usr/bin/lit which is part of the python3-lit package.
BuildRequires:	python3-lit
%endif

BuildRequires:	python3-sphinx
BuildRequires:	libatomic

# We need python3-devel for pathfix.py.
BuildRequires:	python3-devel

# Needed for %%multilib_fix_c_header
BuildRequires:	multilib-rpm-config
BuildRequires: chrpath

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

# clang requires gcc, clang++ requires libstdc++-devel
# - https://bugzilla.redhat.com/show_bug.cgi?id=1021645
# - https://bugzilla.redhat.com/show_bug.cgi?id=1158594
Requires:	libstdc++-devel
Requires:	gcc-c++

Requires:	emacs-filesystem

Provides:	clang(major) = %{maj_ver}

%description
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extensible.

%package libs
Summary: Runtime library for clang
Recommends: compiler-rt%{?_isa} = %{version}
Recommends: libomp%{_isa} = %{version}

%description libs
Runtime library for clang.

%package devel
Summary: Development header files for clang
%if !0%{?compat_build}
Requires: %{name}%{?_isa} = %{version}-%{release}
# The clang CMake files reference tools from clang-tools-extra.
Requires: %{name}-tools-extra%{?_isa} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
%endif

%description devel
Development header files for clang.

%if !0%{?compat_build}
%package analyzer
Summary:	A source code analysis framework
License:	NCSA and MIT
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package tools-extra
Summary:	Extra tools for clang
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	emacs-filesystem

%description tools-extra
A set of extra tools built using Clang's tooling API.

# Put git-clang-format in its own package, because it Requires git
# and we don't want to force users to install all those dependenices if they
# just want clang.
%package -n git-clang-format
Summary:	Integration of clang-format for git
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	git
Requires:	python3

%description -n git-clang-format
clang-format integration for git.

 
%package -n python3-clang
Summary:       Python3 bindings for clang
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      python3
%description -n python3-clang
%{summary}.


%endif


%prep
%if 0%{?compat_build}
%autosetup -n %{clang_srcdir} -p2
%else
%setup -T -q -b 1 -n %{clang_tools_srcdir}


pathfix.py -i %{__python3} -pn \
	clang-tidy/tool/*.py \
	clang-include-fixer/find-all-symbols/tool/run-find-all-symbols.py

%setup -q -n %{clang_srcdir}

%patch4 -p2 -b .gtest
%patch11 -p2 -b .libcxx-fix
%patch14 -p2 -b .bpf-fix
%patch15 -p2 -b .altivec

mv ../%{clang_tools_srcdir} tools/extra

pathfix.py -i %{__python3} -pn \
	tools/clang-format/*.py \
	tools/clang-format/git-clang-format \
	utils/hmaptool/hmaptool \
	tools/scan-view/bin/scan-view
%endif

%build

%if 0%{?__isa_bits} == 64
sed -i 's/\@FEDORA_LLVM_LIB_SUFFIX\@/64/g' test/lit.cfg.py
%else
sed -i 's/\@FEDORA_LLVM_LIB_SUFFIX\@//g' test/lit.cfg.py
%endif

mkdir -p _build
cd _build

%ifarch s390 s390x %{arm} %ix86 ppc64le
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# -DCMAKE_INSTALL_RPATH=";" is a workaround for llvm manually setting the
# rpath of libraries and binaries.  llvm will skip the manual setting
# if CAMKE_INSTALL_RPATH is set to a value, but cmake interprets this value
# as nothing, so it sets the rpath to "" when installing.
%cmake .. -G Ninja \
	-DLLVM_PARALLEL_LINK_JOBS=1 \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DPYTHON_EXECUTABLE=%{__python3} \
	-DCMAKE_INSTALL_RPATH:BOOL=";" \
%ifarch s390 s390x %{arm} %ix86 ppc64le
        -DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
        -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
%endif
%if 0%{?compat_build}
	-DLLVM_CONFIG:FILEPATH=%{_bindir}/llvm-config-%{maj_ver}.%{min_ver}-%{__isa_bits} \
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \
	-DCLANG_INCLUDE_TESTS:BOOL=OFF \
%else
	-DCLANG_INCLUDE_TESTS:BOOL=ON \
	-DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
	-DLLVM_MAIN_SRC_DIR=%{_datadir}/llvm/src \
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64 \
%else
	-DLLVM_LIBDIR_SUFFIX= \
%endif
%endif
	\
%if !0%{compat_build}
	-DLLVM_TABLEGEN_EXE:FILEPATH=%{_bindir}/llvm-tblgen \
%else
	-DLLVM_TABLEGEN_EXE:FILEPATH=%{_bindir}/llvm-tblgen-%{maj_ver}.%{min_ver} \
%endif
	-DCLANG_ENABLE_ARCMT:BOOL=ON \
	-DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \
	-DCLANG_INCLUDE_DOCS:BOOL=ON \
	-DCLANG_PLUGIN_SUPPORT:BOOL=ON \
	-DENABLE_LINKER_BUILD_ID:BOOL=ON \
	-DLLVM_ENABLE_EH=ON \
	-DLLVM_ENABLE_RTTI=ON \
	-DLLVM_BUILD_DOCS=ON \
	-DLLVM_ENABLE_SPHINX=ON \
	-DCLANG_LINK_CLANG_DYLIB=ON \
	-DSPHINX_WARNINGS_AS_ERRORS=OFF \
	\
	-DCLANG_BUILD_EXAMPLES:BOOL=OFF \
	-DCLANG_REPOSITORY_STRING="%{?fedora:Fedora}%{?rhel:Red Hat} %{version}-%{release}"

%ninja_build

%install
%ninja_install -C _build

%if 0%{?compat_build}

# Remove binaries/other files
rm -Rf %{buildroot}%{install_bindir}
rm -Rf %{buildroot}%{install_prefix}/share
rm -Rf %{buildroot}%{install_prefix}/libexec

# Move include files
mkdir -p %{buildroot}%{pkg_includedir}
for dir in clang clang-c; do
  mv  %{buildroot}/%{install_includedir}/$dir %{buildroot}/%{pkg_includedir}/
  # Add symlinks in install_includedir so that the CLANG_INCLUDE_DIRS variable
  # can be used to find includes.
  ln -s {%{pkg_includedir},%{buildroot}%{install_includedir}}/$dir
done

%else

# install clang python bindings
mkdir -p %{buildroot}%{python3_sitelib}/clang/
install -p -m644 bindings/python/clang/* %{buildroot}%{python3_sitelib}/clang/
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/clang

# multilib fix
%multilib_fix_c_header --file %{_includedir}/clang/Config/config.h

# Move emacs integration files to the correct directory
mkdir -p %{buildroot}%{_emacs_sitestartdir}
for f in clang-format.el clang-rename.el clang-include-fixer.el; do
mv %{buildroot}{%{_datadir}/clang,%{_emacs_sitestartdir}}/$f
done

# remove editor integrations (bbedit, sublime, emacs, vim)
rm -vf %{buildroot}%{_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{_datadir}/clang/clang-format-sublime.py*

# TODO: Package html docs
rm -Rvf %{buildroot}%{_pkgdocdir}

# TODO: What are the Fedora guidelines for packaging bash autocomplete files?
rm -vf %{buildroot}%{_datadir}/clang/bash-autocomplete.sh

# Create Manpage symlinks
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang++.1.gz
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang-%{maj_ver}.1.gz
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang++-%{maj_ver}.1.gz

# Add clang++-{version} symlink
ln -s clang++ %{buildroot}%{_bindir}/clang++-%{maj_ver}


# Fix permission
chmod u-x %{buildroot}%{_mandir}/man1/scan-build.1*

%endif

%check
%if !0%{?compat_build}
# requires lit.py from LLVM utilities
# FIXME: Fix failing ARM tests, s390x i686 and ppc64le tests
# FIXME: Ignore test failures until rhbz#1715016 is fixed.
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ninja check-all -C _build || \
%ifarch s390x i686 ppc64le %{arm}
:
%else
:
%endif

%endif


%if !0%{?compat_build}
%files
%{clang_binaries}
%{_bindir}/c-index-test
%{_mandir}/man1/clang.1.gz
%{_mandir}/man1/clang++.1.gz
%{_mandir}/man1/clang-%{maj_ver}.1.gz
%{_mandir}/man1/clang++-%{maj_ver}.1.gz
%{_mandir}/man1/diagtool.1.gz
%{_emacs_sitestartdir}/clang-format.el
%{_datadir}/clang/clang-format.py*
%{_datadir}/clang/clang-format-diff.py*
%endif

%files libs
%if !0%{?compat_build}
%{_libdir}/clang/
%{_libdir}/*.so.*
%else
%{pkg_libdir}/*.so.*
%{pkg_libdir}/clang/%{version}
%endif

%files devel
%if !0%{?compat_build}
%{_libdir}/*.so
%{_includedir}/clang/
%{_includedir}/clang-c/
%{_libdir}/cmake/*
%dir %{_datadir}/clang/
%else
%{pkg_libdir}/*.so
%{pkg_includedir}/clang/
%{install_includedir}/clang
%{pkg_includedir}/clang-c/
%{install_includedir}/clang-c
%{pkg_libdir}/cmake/
%endif

%if !0%{?compat_build}
%files analyzer
%{_bindir}/scan-view
%{_bindir}/scan-build
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/c++-analyzer
%{_datadir}/scan-view/
%{_datadir}/scan-build/
%{_mandir}/man1/scan-build.1.*

%files tools-extra
%{clang_tools_binaries}
%{_bindir}/find-all-symbols
%{_bindir}/modularize
%{_emacs_sitestartdir}/clang-rename.el
%{_emacs_sitestartdir}/clang-include-fixer.el
%{_datadir}/clang/clang-include-fixer.py*
%{_datadir}/clang/clang-tidy-diff.py*
%{_datadir}/clang/run-clang-tidy.py*
%{_datadir}/clang/run-find-all-symbols.py*
%{_datadir}/clang/clang-rename.py*

%files -n git-clang-format
%{_bindir}/git-clang-format

%files -n python3-clang
%{python3_sitelib}/clang/


%endif
%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 6 2020 sguelton@redhat.com - 9.0.1-5
- Update header install

* Tue Feb 4 2020 sguelton@redhat.com - 9.0.1-4
- Sync specfile with clang9.0 package

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-2
- Fix crash with kernel bpf self-tests

* Thu Dec 19 2019 Tom Stellard <tstellar@redhat.com> - 9.0.1-1
- 9.0.1 Release

* Wed Dec 11 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-3
- Add explicit requires for clang-libs to fix rpmdiff errors

* Tue Dec 10 2019 sguelton@redhat.com - 9.0.0-2
- Activate -funwind-tables on all arches, see rhbz#1655546.

* Thu Sep 19 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-1
- 9.0.0 Release

* Wed Sep 11 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.2.rc3
- Reduce debug info verbosity on ppc64le to avoid OOM errors in koji

* Thu Aug 22 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.1.rc3
- 9.0.0 Release candidate 3

* Tue Aug 20 2019 sguelton@redhat.com - 8.0.0-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 8.0.0-3.2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 sguelton@redhat.com - 8.0.0-3
- Fix for rhbz#1674031

* Fri Apr 12 2019 sguelton@redhat.com - 8.0.0-2
- Remove useless patch thanks to GCC upgrade

* Wed Mar 20 2019 sguelton@redhat.com - 8.0.0-1
- 8.0.0 final

* Tue Mar 12 2019 sguelton@redhat.com - 8.0.0-0.6.rc4
- 8.0.0 Release candidate 4

* Mon Mar 4 2019 sguelton@redhat.com - 8.0.0-0.5.rc3
- Cleanup specfile after llvm dependency update

* Mon Mar 4 2019 sguelton@redhat.com - 8.0.0-0.4.rc3
- 8.0.0 Release candidate 3

* Mon Feb 25 2019 tstellar@redhat.com - 8.0.0-0.3.rc2
- Fix compiling with -stdlib=libc++

* Thu Feb 21 2019 sguelton@redhat.com - 8.0.0-0.2.rc2
- 8.0.0 Release candidate 2

* Sat Feb 09 2019 sguelton@redhat.com - 8.0.0-0.1.rc1
- 8.0.0 Release candidate 1

* Tue Feb 05 2019 sguelton@redhat.com - 7.0.1-6
- Update patch for Python3 port of scan-view

* Tue Feb 05 2019 sguelton@redhat.com - 7.0.1-5
- Working CI test suite

* Mon Feb 04 2019 sguelton@redhat.com - 7.0.1-4
- Workaround gcc-9 bug when compiling bitfields

* Fri Feb 01 2019 sguelton@redhat.com - 7.0.1-3
- Fix uninitialized error detected by gcc-9

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Tom Stellard <tstellar@redhat.com> - 7.0.1-2
- Fix for rhbz#1657544

* Tue Dec 18 2018 sguelton@redhat.com - 7.0.1-1
- 7.0.1

* Tue Dec 18 2018 sguelton@redhat.com - 7.0.0-10
- Install proper manpage symlinks for clang/clang++ versions

* Fri Dec 14 2018 sguelton@redhat.com - 7.0.0-9
- No longer Ignore -fstack-clash-protection option

* Tue Dec 04 2018 sguelton@redhat.com - 7.0.0-8
- Ensure rpmlint passes on specfile

* Fri Nov 30 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-7
- Drop python2 dependency from clang-tools-extra 

* Wed Nov 21 2018 sguelton@redhat.com - 7.0.0-6
- Prune unneeded reference to llvm-test-suite sub-package

* Mon Nov 19 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-5
- Run 'make check-all' instead of 'make check-clang'

* Mon Nov 19 2018 sergesanspaille <sguelton@redhat.com> - 7.0.0-4
- Avoid Python2 + Python3 dependency for clang-analyzer

* Mon Nov 05 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-3
- User helper macro to fixup config.h for multilib

* Tue Oct 02 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-2
- Use correct shebang substitution for python scripts

* Mon Sep 24 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-1
- 7.0.0 Release

* Wed Sep 19 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.16.rc3
- Move builtin headers into clang-libs sub-package

* Wed Sep 19 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.15.rc3
- Remove ambiguous python shebangs

* Thu Sep 13 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.14.rc3
- Move unversioned shared objects to devel package

* Thu Sep 13 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.13.rc3
- Rebuild with new llvm-devel that disables rpath on install

* Thu Sep 13 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.12.rc3
- Fix clang++-7 symlink

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.11.rc3
- 7.0.0-rc3 Release

* Mon Sep 10 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.10.rc2
- Drop siod from llvm-test-suite

* Fri Sep 07 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.9.rc2
- Drop python2 dependency from clang package

* Thu Sep 06 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.8.rc2
- Drop all uses of python2 from lit tests

* Sat Sep 01 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.7.rc2
- Add Fedora specific version string

* Tue Aug 28 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.6.rc2
- 7.0.0-rc2 Release

* Tue Aug 28 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.5.rc1
- Enable unit tests

* Fri Aug 17 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.4.rc1
- Move llvm-test-suite into a sub-package

* Fri Aug 17 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.3.rc1
- Recommend the same version of compiler-rt

* Wed Aug 15 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.2.rc1
- Rebuild for f30

* Mon Aug 13 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.1.rc1
- 7.0.0-rc1 Release

* Mon Jul 23 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-3
- Sync spec file with the clang6.0 package

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-1
- 6.0.1 Release

* Wed Jun 13 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-0.2.rc2
- 6.0.1-rc2

* Fri May 11 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-0.1.rc1
- 6.0.1-rc1 Release

* Fri Mar 23 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-5
- Add a clang++-{version} symlink rhbz#1534098

* Thu Mar 22 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-4
- Use correct script for running lit tests

* Wed Mar 21 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-3
- Fix toolchain detection so we don't default to using cross-compilers:
  rhbz#1482491

* Mon Mar 12 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-2
- Add Provides: clang(major) rhbz#1547444

* Fri Mar 09 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-1
- 6.0.0 Release

* Mon Feb 12 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.6.rc2
- 6.0.0-rc2 Release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.4.rc1
- Package python helper scripts for tools

* Fri Jan 26 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.3.rc1
- Ignore -fstack-clash-protection option instead of giving an error

* Fri Jan 26 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.2.rc1
- Package emacs integration files

* Wed Jan 24 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.1.rc1
- 6.0.0-rc1 Release

* Wed Jan 24 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-3
- Rebuild against llvm5.0 compatibility package
- rhbz#1538231

* Wed Jan 03 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.0.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Dec 20 2017 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- 5.0.1 Release

* Wed Dec 13 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-3
- Make compiler-rt a weak dependency and add a weak dependency on libomp

* Mon Nov 06 2017 Merlin Mathesius <mmathesi@redhat.com> - 5.0.0-2
- Cleanup spec file conditionals

* Mon Oct 16 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-1
- 5.0.0 Release

* Wed Oct 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.0.1-6
- python2-clang subpkg (#1490997)
- tools-extras: tighten (internal) -libs dep
- %%install: avoid cd

* Wed Aug 30 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-5
- Add Requires: python for git-clang-format

* Sun Aug 06 2017 Bj??rn Esser <besser82@fedoraproject.org> - 4.0.1-4
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-1
- 4.0.1 Release.

* Fri Jun 16 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-8
- Enable make check-clang

* Mon Jun 12 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-7
- Package git-clang-format

* Thu Jun 08 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-6
- Generate man pages

* Thu Jun 08 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-5
- Ignore test-suite failures until all arches are fixed.

* Mon Apr 03 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-4
- Run llvm test-suite

* Mon Mar 27 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-3
- Enable eh/rtti, which are required by lldb.

* Fri Mar 24 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-2
- Fix clang-tools-extra build
- Fix install

* Thu Mar 23 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-1
- clang 4.0.0 final release

* Mon Mar 20 2017 David Goerger <david.goerger@yale.edu> - 3.9.1-3
- add clang-tools-extra rhbz#1328091

* Thu Mar 16 2017 Tom Stellard <tstellar@redhat.com> - 3.9.1-2
- Enable build-id by default rhbz#1432403

* Thu Mar 02 2017 Dave Airlie <airlied@redhat.com> - 3.9.1-1
- clang 3.9.1 final release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3.9.0-3
- Add Requires: compiler-rt to clang-libs.
- Without this, compiling with certain CFLAGS breaks.

* Tue Nov  1 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.9.0-2
- Rebuild for new arches

* Fri Oct 14 2016 Dave Airlie <airlied@redhat.com> - 3.9.0-1
- clang 3.9.0 final release

* Fri Jul 01 2016 Stephan Bergmann <sbergman@redhat.com> - 3.8.0-2
- Resolves: rhbz#1282645 add GCC abi_tag support

* Thu Mar 10 2016 Dave Airlie <airlied@redhat.com> 3.8.0-1
- clang 3.8.0 final release

* Thu Mar 03 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.4
- clang 3.8.0rc3

* Wed Feb 24 2016 Dave Airlie <airlied@redhat.com> - 3.8.0-0.3
- package all libs into clang-libs.

* Wed Feb 24 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.2
- enable dynamic linking of clang against llvm

* Thu Feb 18 2016 Dave Airlie <airlied@redhat.com> - 3.8.0-0.1
- clang 3.8.0rc2

* Fri Feb 12 2016 Dave Airlie <airlied@redhat.com> 3.7.1-4
- rebuild against latest llvm packages
- add BuildRequires llvm-static

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Dave Airlie <airlied@redhat.com> 3.7.1-2
- just accept clang includes moving to /usr/lib64, upstream don't let much else happen

* Thu Jan 28 2016 Dave Airlie <airlied@redhat.com> 3.7.1-1
- initial build in Fedora.

* Tue Oct 06 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- initial version using cmake build system
