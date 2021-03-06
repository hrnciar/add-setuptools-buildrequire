# Get post-release fixes
%global owner    freetdi
%global srcname  tdlib
%global gittag   4c6109e917e032aaa9ee480de2ce6d1ed5c15305
%global shorttag %(cut -b -7 <<< %{gittag})
%global gitdate  20200404

Name:           python-%{srcname}
Version:        0.9.0
Release:        9.%{gitdate}.%{shorttag}%{?dist}
Summary:        Tree decomposition algorithms

License:        GPLv2+
URL:            https://github.com/%{owner}/%{srcname}
Source0:        %{url}/archive/%{gittag}/%{srcname}-%{shorttag}.tar.gz
# Fix a broken test to find the python header files
Patch0:         %{name}-python-includes.patch
# Fix FTBFS on 32-bit systems
Patch1:         %{name}-32bit.patch
# Fix FTBFS due to missing includes with gcc-11
Patch2:         %{name}-gcc11.patch

BuildRequires:  boost-devel
BuildRequires:  freetdi-gala-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}

%global _description %{expand:
This package provides tree decomposition algorithms.

A tree decomposition of a simple, loopless, undirected graph G is a tree
T with bags at its nodes containing vertices from G.  The usual
conditions apply.  By convention, a tree is an acyclic graph with exactly
one connected component.  The bagsize of T is the size of the biggest
bag, which is a notion for the (width of T)+1.}

%description %_description

%package -n    python3-%{srcname}
Summary:       Tree decomposition algorithms for python 3
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{srcname} %_description

%package -n    python3-%{srcname}-devel
Summary:       Headers for python3-%{srcname}
BuildArch:     noarch
Requires:      python3-%{srcname} = %{version}-%{release}
Requires:      freetdi-gala-devel

%description -n python3-%{srcname}-devel
Headers for developing applications that use python3-%{srcname}.

%prep
%autosetup -p1 -n %{srcname}-%{gittag}

# Tell cython to generate python 3 code
sed -i 's/--cplus/-3 &/' cython.am

# Install into the arch-specific python directory
sed -i 's/pythondir/pyexecdir/' tdlib/Makefile.am

# Do not override Fedora build flags
sed -i 's/ -Os -march=native//' examples/Makefile.am

# Generate the configure script and Makefile.in files
autoreconf -fi .

%build
%configure --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install
rm -f %{buildroot}%{python3_sitearch}/tdlib/*.la

%files
%license COPYING GPL-2 GPL-3
%doc AUTHORS BUGS NEWS README THANKS TODO
%{_libexecdir}/treedec/

%files -n      python3-%{srcname}
%{python3_sitearch}/tdlib/

%files -n      python3-%{srcname}-devel
%{_includedir}/treedec/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9.20200404.4c6109e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.0-8.20200404.4c6109e
- Rebuilt for Boost 1.75

* Fri Oct 16 2020 Jeff Law <law@redhat.com> - 0.9.0-7.20200404.4c6109e
- Fix missing #include for gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6.20200404.4c6109e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Jerry James <loganjerry@gmail.com> - 0.9.0-5.20200404.4c6109e
- Update to latest git snapshot

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.9.0-4.20191218.6611c7c
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3.20191218.6611c7c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Jerry James <loganjerry@gmail.com> - 0.9.0-2.20191218.6611c7c
- Install into the arch-specific directory

* Thu Dec 19 2019 Jerry James <loganjerry@gmail.com> - 0.9.0-1.20191218.6611c7c
- Initial RPM
