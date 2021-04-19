Name:           ptex
Version:        2.3.2
Release:        4%{?dist}
Summary:        Per-Face Texture Mapping for Production Rendering

License:        BSD
Url:            https://github.com/wdas/%{name}
Source:         https://github.com/wdas/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch:          0001-set-SOVERSION.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  pkgconfig(zlib)

%description
Ptex is a texture mapping system developed by 
Walt Disney Animation Studios for production-quality rendering.

%package devel
Summary: Development files for the Ptex library
Requires:       %{name} = %{version}

%description devel
Development files for Walt Disney Animation Studios Ptex library.

%package doc
Summary: Documentation files for the Ptex library
BuildArch:      noarch

%description doc
Documentation files for Walt Disney Animation Studios Ptex library.

%package libs
Summary:	Libraries for Ptex

%description libs
This package contains the library needed to run programs dynamically
linked with Ptex.

%prep
%autosetup -p1 -n %{name}-%{version}


%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# Detect package version
echo %{version} > version
%cmake \
        -DPTEX_BUILD_STATIC_LIBS=OFF 
%cmake_build


%install
%cmake_install

# Create a pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/Ptex.pc << EOF
# pkg-config configuration for Ptex
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: Ptex
Description: Per-Face Texture Mapping for Production Rendering
Version: 2.3.2%{version}
Libs: -L${libdir} -llibPtex -pthread -lpthread
Libs.private: -lz
Cflags: -I${includedir} -pthread
EOF


%files
%doc src/doc/README 
%license src/doc/License.txt
%{_bindir}/ptxinfo
%dir %{_datadir}/cmake/Ptex
%{_datadir}/cmake/Ptex/*

%files libs
%{_libdir}/libPtex.so.2.3

%files doc
%dir %{_datadir}/doc/Ptex
%doc %{_datadir}/doc/Ptex/*

%files devel
%{_includedir}/Ptex*.h
%{_libdir}/pkgconfig/Ptex.pc
%{_libdir}/libPtex.so

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 03 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 2.3.2-3
- Patch for .so versioning
- Clean cmake option

* Sat Oct 03 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 2.3.2-2
- Add missing isa for arch
- Drop expliciting out of source tree for cmake build
- Move unversioned .so files to devel

* Sat Oct 03 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 2.3.2-1
- Initial package based upstream from
