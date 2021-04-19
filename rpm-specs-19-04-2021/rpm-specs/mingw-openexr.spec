%{?mingw_package_header}

%global pkgname openexr

Name:          mingw-%{pkgname}
Version:       2.5.5
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD
URL:           http://www.openexr.com/
BuildArch:     noarch
Source0:       https://github.com/AcademySoftwareFoundation/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# GCC11 build fix
Patch0:        openexr-gcc11.patch


BuildRequires: cmake
BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-zlib

%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Provides:      mingw32-OpenEXR = %{version}-%{release}
Provides:      mingw32-ilmbase = %{version}-%{release}
Obsoletes:     mingw32-OpenEXR < 2.5.3
Obsoletes:     mingw32-OpenEXR-static < 2.5.3
Obsoletes:     mingw32-ilmbase < 2.5.3

%description -n mingw32-%{pkgname}
%{summary}.



%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}
Provides:      mingw32-OpenEXR-tools = %{version}-%{release}
Provides:      mingw32-ilmbase-tools = %{version}-%{release}
Obsoletes:     mingw32-OpenEXR-tools < 2.5.3
Obsoletes:     mingw32-ilmbase-tools < 2.5.3

%description -n mingw32-%{pkgname}-tools
%{summary}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Provides:      mingw64-OpenEXR = %{version}-%{release}
Provides:      mingw64-ilmbase = %{version}-%{release}
Obsoletes:     mingw64-OpenEXR < 2.5.3
Obsoletes:     mingw64-OpenEXR-static < 2.5.3
Obsoletes:     mingw64-ilmbase < 2.5.3

%description -n mingw64-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}
Provides:      mingw64-OpenEXR-tools = %{version}-%{release}
Provides:      mingw64-ilmbase-tools = %{version}-%{release}
Obsoletes:     mingw64-OpenEXR-tools < 2.5.3
Obsoletes:     mingw64-ilmbase-tools < 2.5.3

%description -n mingw64-%{pkgname}-tools
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake \
    -DBUILD_TESTING=OFF \
    -DILMBASE_INSTALL_PKG_CONFIG=ON \
    -DOPENEXR_INSTALL_PKG_CONFIG=ON
%mingw_make_build


%install
%mingw_make_install


# Don't install doc
rm -rf %{buildroot}%{mingw32_docdir}/OpenEXR
rm -rf %{buildroot}%{mingw64_docdir}/OpenEXR


%files -n mingw32-%{pkgname}
%license LICENSE.md
%{mingw32_bindir}/libHalf-2_5.dll
%{mingw32_bindir}/libIex-2_5.dll
%{mingw32_bindir}/libIexMath-2_5.dll
%{mingw32_bindir}/libIlmImf-2_5.dll
%{mingw32_bindir}/libIlmImfUtil-2_5.dll
%{mingw32_bindir}/libIlmThread-2_5.dll
%{mingw32_bindir}/libImath-2_5.dll
%{mingw32_includedir}/OpenEXR/
%{mingw32_libdir}/libHalf-2_5.dll.a
%{mingw32_libdir}/libIex-2_5.dll.a
%{mingw32_libdir}/libIexMath-2_5.dll.a
%{mingw32_libdir}/libIlmImf-2_5.dll.a
%{mingw32_libdir}/libIlmImfUtil-2_5.dll.a
%{mingw32_libdir}/libIlmThread-2_5.dll.a
%{mingw32_libdir}/libImath-2_5.dll.a
%{mingw32_libdir}/cmake/IlmBase/
%{mingw32_libdir}/cmake/OpenEXR/
%{mingw32_libdir}/pkgconfig/OpenEXR.pc
%{mingw32_libdir}/pkgconfig/IlmBase.pc


%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/exr2aces.exe
%{mingw32_bindir}/exrenvmap.exe
%{mingw32_bindir}/exrheader.exe
%{mingw32_bindir}/exrmakepreview.exe
%{mingw32_bindir}/exrmaketiled.exe
%{mingw32_bindir}/exrmultipart.exe
%{mingw32_bindir}/exrmultiview.exe
%{mingw32_bindir}/exrstdattr.exe

%files -n mingw64-%{pkgname}
%license LICENSE.md
%{mingw64_bindir}/libHalf-2_5.dll
%{mingw64_bindir}/libIex-2_5.dll
%{mingw64_bindir}/libIexMath-2_5.dll
%{mingw64_bindir}/libIlmImf-2_5.dll
%{mingw64_bindir}/libIlmImfUtil-2_5.dll
%{mingw64_bindir}/libIlmThread-2_5.dll
%{mingw64_bindir}/libImath-2_5.dll
%{mingw64_includedir}/OpenEXR/
%{mingw64_libdir}/libHalf-2_5.dll.a
%{mingw64_libdir}/libIex-2_5.dll.a
%{mingw64_libdir}/libIexMath-2_5.dll.a
%{mingw64_libdir}/libIlmImf-2_5.dll.a
%{mingw64_libdir}/libIlmImfUtil-2_5.dll.a
%{mingw64_libdir}/libIlmThread-2_5.dll.a
%{mingw64_libdir}/libImath-2_5.dll.a
%{mingw64_libdir}/cmake/IlmBase/
%{mingw64_libdir}/cmake/OpenEXR/
%{mingw64_libdir}/pkgconfig/OpenEXR.pc
%{mingw64_libdir}/pkgconfig/IlmBase.pc


%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/exr2aces.exe
%{mingw64_bindir}/exrenvmap.exe
%{mingw64_bindir}/exrheader.exe
%{mingw64_bindir}/exrmakepreview.exe
%{mingw64_bindir}/exrmaketiled.exe
%{mingw64_bindir}/exrmultipart.exe
%{mingw64_bindir}/exrmultiview.exe
%{mingw64_bindir}/exrstdattr.exe


%changelog
* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 2.5.5-1
- Update to 2.5.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Sandro Mani <manisandro@gmail.com> - 2.5.4-1
- Update to 2.5.4

* Thu Dec 17 2020 Sandro Mani <manisandro@gmail.com> - 2.5.3-1
- Initial package to replace mingw-OpenEXR and mingw-ilmbase
