%global gitdate   20210201
%global gittag    b56729e6f29672be2edb2885807844df68d8db32
%global shorttag  %(c=%{gittag}; echo ${c:0:7})

Name:          honggfuzz
Version:       2.3.2
Release:       0.1.%{gitdate}git%{shorttag}%{?dist}
Summary:       General-purpose, easy-to-use fuzzer

License:       ASL 2.0
URL:           http://google.github.io/honggfuzz/
# The source contains proprietary binary blobs.  We remove the entire
# third_party/ subdirectory when repackaging this:
# ./generate-tarball.sh %%version %%gittag
Source0:       honggfuzz-%{version}.tar.gz
Source1:       generate-tarball.sh

# Used for sanity-check in %%check section.
Source2:       hello.c

# This software has to be ported to each architecture (see upstream
# file linux/trace.c).  It has not been ported to s390 as of version
# 2.2.
#
# FTBFS on armv7 and ppc64le:
# https://github.com/google/honggfuzz/issues/376
ExcludeArch:   %{arm} %{power64} s390 s390x

BuildRequires: gcc, gcc-c++
BuildRequires: binutils-devel
BuildRequires: libunwind-devel
# This package currently links with lzma but does not require it.
# However we have to keep this BR at the moment until upstream remove
# the link (or edit Makefile).  See also:
# https://github.com/google/honggfuzz/issues/332
BuildRequires: xz-devel
BuildRequires: make

Requires:      gcc, gcc-c++
# Unfortunately it fails unless exactly the same version of clang &
# compiler-rt are installed, but that's a bug in clang not in this
# package.
Requires:      clang
Requires:      compiler-rt


%description
Honggfuzz is a general-purpose fuzzing tool. Given an input corpus
files, honggfuzz modifies input to a test program and utilize the
ptrace() API/POSIX signal interface to detect and log crashes. It
can also use software or hardware-based code coverage techniques
to produce more and more interesting inputs.


%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
# Disable LTO since it breaks linking.
%define _lto_cflags %{nil}
%autosetup


%build
# Upstream removes -D_FORTIFY_SOURCE claiming that "fortify-source
# intercepts some functions", so we also remove it here.
export CFLAGS="$(echo %{__global_cflags} |
                 sed 's/ [^ ]*_FORTIFY_SOURCE[^ ]* / /')"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT

# The rule above doesn't preserve links in the installed binaries.
# Recreate them here.
pushd $RPM_BUILD_ROOT%{_bindir}
for f in hfuzz-clang hfuzz-clang++ hfuzz-g++ hfuzz-gcc; do
    rm $f
    ln hfuzz-cc $f
done
popd

# Make sure the include files aren't chmod +x.
find $RPM_BUILD_ROOT%{_includedir} -type f -exec chmod -x {} \;


%check
# This checks that a simple program can be compiled using the GCC
# wrappers.
ln -s %{SOURCE2} hello.c
ln -s %{SOURCE2} hello.cpp
hfuzz_cc/hfuzz-gcc hello.c -o hello
./hello
hfuzz_cc/hfuzz-g++ hello.cpp -o hello
./hello


%files
%license COPYING
%{_bindir}/honggfuzz
%{_bindir}/hfuzz-cc
%{_bindir}/hfuzz-clang
%{_bindir}/hfuzz-clang++
%{_bindir}/hfuzz-g++
%{_bindir}/hfuzz-gcc


%files devel
%license COPYING
%doc CHANGELOG README.md CONTRIBUTING.md docs/
%{_includedir}/libhfcommon
%{_includedir}/libhfuzz
%{_includedir}/libhnetdriver


%changelog
* Mon Feb 01 2021 Richard W.M. Jones <rjones@redhat.com> 2.3.2-0.1
- Move to git pre-release of the next version after 2.3.1.
- ExcludeArch armv7 and ppc64le.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.5.20200511gita299f3f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Richard W.M. Jones <rjones@redhat.com> 2.2-0.4.20200511gita299f3f
- Disable LTO.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.3.20200511gita299f3f
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.2.20200511gita299f3f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Richard W.M. Jones <rjones@redhat.com> 2.2-0.1.20200511gita299f3f
- New upstream version.

* Wed Nov 02 2016 Daniel Kopecek <dkopecek@redhat.com> 0.8-2.20161101git7ba1010
- Initial package
