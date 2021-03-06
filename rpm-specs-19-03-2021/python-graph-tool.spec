# Koji has two types of builders:
# 16Gb + 6 cores
# 128Gb + 48 cores
# There's no way to choose either, so we rely on luck
#
# This needs about 15 gigs per thread, otherwise OOMs. So, we calculate the number of threads we can afford to use for make:
# meminfo gives output in kB (1000 bytes)
%global numthreads %(awk '/MemTotal:/ {print int($2/15e6)}' /proc/meminfo)
# But make sure it is > 0
%if 0%{numthreads} == 0
%global numthreads 1
%endif

# If _smp_build_ncpus is not defined (on older rpms)
# assume there's only one
%if 0%{?_smp_build_ncpus} == 0
%global _smp_build_ncpus 1
%endif

# Use the smaller number of threads
%if 0%{numthreads} > 0%{?_smp_build_ncpus}
%global numthreads %{?_smp_build_ncpus}
%endif

%global modname graph-tool
%global pymodname graph_tool

# Builds fail with LTO
%global _lto_cflags %{nil}

%global _description %{expand:
Graph-tool is an efficient Python module for manipulation and statistical
analysis of graphs (a.k.a. networks). Contrary to most other python modules
with similar functionality, the core data structures and algorithms are
implemented in C++, making extensive use of template metaprogramming, based
heavily on the Boost Graph Library. This confers it a level of performance that
is comparable (both in memory usage and computation time) to that of a pure
C/C++ library.

Please refer to https://graph-tool.skewed.de/static/doc/index.html for
documentation.}

Name:           python-%{modname}
Version:        2.33
Release:        4%{?dist}
Summary:        Efficient network analysis tool written in Python

License:        LGPLv3+
URL:            https://graph-tool.skewed.de/
Source0:        https://downloads.skewed.de/%{modname}/%{modname}-%{version}.tar.bz2

# Fails on i686: issue filed: https://git.skewed.de/count0/graph-tool/issues/617
# https://bugzilla.redhat.com/show_bug.cgi?id=1771023
# Fails on armv7hl: virtual memory exhausted
# https://bugzilla.redhat.com/show_bug.cgi?id=1771024
# Fails on ppc64le: note: variable tracking size limit exceeded with '-fvar-tracking-assignments', retrying without
# https://bugzilla.redhat.com/show_bug.cgi?id=1771031
# Fails on s390x: note: variable tracking size limit exceeded with '-fvar-tracking-assignments', retrying without
# https://bugzilla.redhat.com/show_bug.cgi?id=1771034
# Takes ~23 hours on x86_64 if we get unlucky and get a 6 core 16gig machine, ~4 hours if we get a 48 core 128gig machine
# Takes ~45 hours on aarch64
ExcludeArch:    i686 armv7hl ppc64le s390x

# Workaround for https://git.skewed.de/count0/graph-tool/issues/613
# CGAL 5.x is now header only
# Required on F32+
%if 0%{?fedora} >= 32
Patch0:         0001-Use-header-only-CGAL-library.patch
%endif

# Remove the compiler flags upstream tries to put
Patch1:         0002-Remove-upstreams-flags.patch
BuildRequires: make
BuildRequires:  git-core
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gawk

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  CGAL-devel
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  expat-devel
BuildRequires:  gcc-g++
BuildRequires:  gmp-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  sparsehash-devel

Provides:       graph-tool%{?_isa} = %{version}-%{release}

# Not a setuptools style project, but leaving this in
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname} %_description

%prep
%autosetup -S git -n %{modname}-%{version}
# Remove shebangs
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'


%build
./autogen.sh
%configure --with-python-module-path=%{python3_sitearch} --with-boost-libdir=%{_libdir}
echo "Building with %{numthreads} of %{?_smp_build_ncpus} available CPUs"
# Uses the latest value set by -j
%make_build -j%{numthreads}

%install
%make_install

# Remove installed doc sources
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/%{modname}

# Remove static objects
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n python3-%{modname}
%license COPYING
%doc README.md ChangeLog AUTHORS
%{python3_sitearch}/%{pymodname}
%{_libdir}/pkgconfig/%{modname}-py%{python3_version}.pc

%changelog
* Fri Feb 12 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.33-4
- Use pkgconfig to BR the required cairomm API/ABI version 1.0 (vs. 1.16)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.33-2
- Rebuilt for Boost 1.75

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.33-1
- Update to latest release
- Disable LTO
- update COPYING file name
- Update license

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 2.29-5
- Rebuilt for Boost 1.73
- Simplify shell command to determine number of threads to use

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.29-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.29-2
- Exclude builds on arches: usually falls short of resources

* Fri Nov 01 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.29-1
- Remove unneeded shebangs

* Tue Oct 22 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.29-1
- Improve conditional to handle cases where _smp_build_ncpus is not defined
- Correct conditional hack

* Tue Oct 15 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.29-1
- Initial build
