%undefine __cmake_in_source_build
# Upstream has only made 1 release tarball, so we build from git
%global gittag   d59c325fb31812047e61aba3d75cc037f92c2b3d
%global shorttag %(cut -b -7 <<< %{gittag})

Name:           tlx
Version:        0.5.20200222
Release:        3%{?dist}
Summary:        Sophisticated C++ data structures, algorithms, and helpers

License:        Boost
URL:            http://panthema.net/tlx
Source0:        https://github.com/tlx/tlx/archive/%{gittag}/%{name}-%{shorttag}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make

%description
TLX is a collection of sophisticated C++ data structures, algorithms,
and miscellaneous helpers.  It contains:
- The fast tournament (loser) trees from MCSTL by Johannes Singler, with
  many fixes.
- A fast intrusive reference counter called CountingPtr, which has
  considerably less overhead than std::shared_ptr.
- Efficient and fast multiway merging algorithms from Johannes Singler,
  which were previously included with gcc.  The tlx version has many
  fixes and is available for clang and MSVC++.
- Many string manipulation algorithms for std::string.
- An improved version of the stx-btree implementation, which is
  basically always a better alternative to std::map (but not
  std::unordered_map).
- A copy of siphash for string hashing.
- Efficient sequential string sorting implementations such as radix sort
  and multikey quicksort.
- Much more; see the doxygen documentation.

%package       devel
Summary:       Headers and library links to build with tlx
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
Headers and library links to build with tlx.

%package       doc
Summary:       Doxygen documentation for tlx
BuildArch:     noarch

%description   doc
Doxygen documentation for tlx.

%prep
%autosetup -n tlx-%{gittag}

%build
%cmake \
  -DTLX_BUILD_SHARED_LIBS:BOOL=ON \
  -DTLX_BUILD_STATIC_LIBS:BOOL=OFF \
  -DTLX_BUILD_STRING_SORTING:BOOL=ON \
  -DTLX_BUILD_TESTS:BOOL=ON \
  %{nil}
%cmake_build
doxygen

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libtlx.so.0
%{_libdir}/libtlx.so.0.*

%files         devel
%{_includedir}/%{name}/
%{_libdir}/cmake/tlx/
%{_libdir}/libtlx.so
%{_libdir}/pkgconfig/tlx.pc

%files         doc
%doc doxygen-html

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20200222-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20200222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Jerry James <loganjerry@gmail.com> - 0.5.20200222-1
- Version 0.5.2020022
- Drop -endian patch

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20191212-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 0.5.20191212-1
- Initial RPM
