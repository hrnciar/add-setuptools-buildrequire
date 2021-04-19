# linking tests fail with undefined references
%bcond_with check

# mcrouter build process is very memory-hungry,
# it fails unpredictably if some of the jobs get terminated
# with no LTO and 1 build job memory usage peaks at ~ 44% with 16GB
%global _lto_cflags %nil

%global forgeurl https://github.com/facebook/mcrouter
%global commit 018f1af489531161e33cf8653eba75bd15b2e099
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20210412

Name:           mcrouter
Version:        0.41.0
Release:        4.%{date}git%{shortcommit}%{?dist}
Summary:        Memcached protocol router for scaling memcached deployments

License:        MIT
URL:            %{forgeurl}
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# Folly is known not to work on big-endian CPUs
# https://bugzilla.redhat.com/show_bug.cgi?id=1892151
ExcludeArch:    s390x
# configure fails to find boost for some reason
# https://bugzilla.redhat.com/show_bug.cgi?id=1943729
ExcludeArch:    ppc64le
# multiple issues due to hardcoded pointer sizes
# https://bugzilla.redhat.com/show_bug.cgi?id=1943736
ExcludeArch:    i686 armv7hl

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  gcc-c++
BuildRequires:  folly-devel
BuildRequires:  fizz-devel
BuildRequires:  wangle-devel
BuildRequires:  fbthrift-devel
BuildRequires:  fbthrift
# for free
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  python3-fbthrift-devel
BuildRequires:  ragel

%description
Mcrouter (pronounced mc router) is a memcached protocol router for scaling
memcached deployments.

Because the routing and feature logic are abstracted from the client in
mcrouter deployments, the client may simply communicate with destination
hosts through mcrouter over a TCP connection using standard memcached
protocol. Typically, little or no client modification is needed to use
mcrouter, which was designed to be a drop-in proxy between the client and
memcached hosts.

%prep
%autosetup -p1 -n %{name}-%{commit}
pushd %{name}
echo "%{version}" > VERSION
autoreconf --install

%build
# do not eat all memory
echo "Available memory:"
free -h
echo "System limits:"
ulimit -a

MCROUTER_SMP_NCPUS="%{_smp_build_ncpus}"
mem_per_process=8192
max_mem=$(LANG=C free -m | sed -n "s|^Mem: *\([0-9]*\).*$|\1|p")
max_jobs="$(($max_mem / $mem_per_process))"
if test "%{_smp_build_ncpus}" -gt "$max_jobs";
then
  echo "Warning: Reducing build parallelism to -j$max_jobs because of memory limits"
  MCROUTER_SMP_NCPUS="-j${max_jobs}"
fi

pushd %{name}
export FBTHRIFT_BIN="%{_bindir}"
export PYTHON_VERSION="%{python3_version}"
%configure --enable-shared --disable-static
%make_build "${MCROUTER_SMP_NCPUS}"

%install
pushd %{name}
%make_install

%if %{with check}
%check
pushd %{name}
%{__make} check "${MCROUTER_SMP_NCPUS}"
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
* Fri Apr 16 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.41.0-4.20210412git018f1af
- Update to snapshot from 20210412
- Stop using forge macros in case we want to build for EPEL8

* Mon Mar 29 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.41.0-4.20210324git7884f76
- Update to snapshot from 20210324
- Use %%forgeautosetup so the configure.ac patch is actually applied
- Determine the number of safe build jobs to use (borrowed from Ceph)

* Fri Mar 26 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.41.0-3.20210322git254a127
- Fix usage of deprecated AC_PROG_LIBTOOL macro; use LT_INIT instead

* Wed Mar 24 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.41.0-2.20210322git254a127
- Update to snapshot from 20210322
- Disable build concurrency and LTO to compensate for high RAM usage

* Tue Mar 16 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.41.0-1.20210316gita3d9640
- Initial package
