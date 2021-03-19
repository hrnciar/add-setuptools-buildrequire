%{?mingw_package_header}

%global pkgname libspatialite
#global pre beta0

Name:          mingw-%{pkgname}
Version:       5.0.1
Summary:       MinGW Windows libspatialite library
Release:       2%{?pre:.%pre}%{?dist}

BuildArch:     noarch
License:       MPLv1.1 or GPLv2+ or LGPLv2+
URL:           https://www.gaia-gis.it/fossil/libspatialite
Source0:       http://www.gaia-gis.it/gaia-sins/%{pkgname}-sources/%{pkgname}-%{version}%{?pre:-%pre}.tar.gz
# Fix mingw detection in configure.ac
Patch0:        libspatialite_mingw.patch
# Fix obsolete macros
Patch1:        libspatialite_macros.patch
# Use pkgconfig to find geos
Patch2:        libspatialite_geos.patch

BuildRequires: make
BuildRequires: autoconf automake libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-freexl
BuildRequires: mingw32-geos
BuildRequires: mingw32-libcharset
BuildRequires: mingw32-librttopo
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-minizip
BuildRequires: mingw32-proj
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-freexl
BuildRequires: mingw64-geos
BuildRequires: mingw64-libcharset
BuildRequires: mingw64-librttopo
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-minizip
BuildRequires: mingw64-proj
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-zlib


%description
MinGW Windows libspatialite library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows libspatialite library

%description -n mingw32-%{pkgname}
MinGW Windows libspatialite library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows libspatialite library

%description -n mingw64-%{pkgname}
MinGW Windows libspatialite library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}%{?pre:-%pre}


%build
# Needed for Patch0 and Patch2
autoreconf -ifv

mkdir build_win32$MINGW_BUILDDIR_SUFFIX
(
cd build_win32$MINGW_BUILDDIR_SUFFIX
%mingw32_configure --enable-shared --disable-static \
    --enable-geocallbacks
)
mkdir build_win64$MINGW_BUILDDIR_SUFFIX
(
cd build_win64$MINGW_BUILDDIR_SUFFIX
%mingw64_configure --enable-shared --disable-static \
    --enable-geocallbacks
)

%mingw_make_build


%install
%mingw_make_install

# Delete undesired libtool archives
find %{buildroot} -type f -name "*.la" -delete

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%license COPYING
%{mingw32_bindir}/libspatialite-4.dll
%{mingw32_includedir}/spatialite.h
%{mingw32_includedir}/spatialite/
%{mingw32_libdir}/libspatialite.dll.a
%{mingw32_libdir}/mod_spatialite.dll*
%{mingw32_libdir}/pkgconfig/spatialite.pc

%files -n mingw64-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%license COPYING
%{mingw64_bindir}/libspatialite-4.dll
%{mingw64_includedir}/spatialite.h
%{mingw64_includedir}/spatialite/
%{mingw64_libdir}/libspatialite.dll.a
%{mingw64_libdir}/mod_spatialite.dll*
%{mingw64_libdir}/pkgconfig/spatialite.pc


%changelog
* Mon Mar 08 2021 Sandro Mani <manisandro@gmail.com> - 5.0.1-2
- Rebuild (proj)

* Mon Mar 08 2021 Sandro Mani <manisandro@gmail.com> - 5.0.1-1
- Update to 5.0.1

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 5.0.0-5
- Rebuild (geos)

* Wed Feb 10 2021 Sandro Mani <manisandro@gmail.com> - 5.0.0-4
- Rebuild (minizip)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Sandro Mani <manisandro@gmail.com> - 5.0.0-2
- Enable minizip support

* Thu Nov 12 2020 Sandro Mani <manisandro@gmail.com> - 5.0.0-1
- Update to 5.0.0 final

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.4.beta0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.3.beta0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.0.0-0.2.beta0
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 5.0.0-0.1.beta0
- Update to 5.0.0-beta0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 4.3.0a-8
- Rebuild (proj, geos)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Sandro Mani <manisandro@gmail.com> - 4.3.0a-5
- --enable-geocallbacks

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 4.3.0a-3
- Fix debug file in main package

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 4.3.0a-2
- Add libspatialite_macros.patch

* Fri Jan 22 2016 Sandro Mani <manisandro@gmail.com> - 4.3.0a-1
- Update to 4.3.0a

* Mon May 11 2015 Sandro Mani <manisandro@gmail.com> - 4.2.0-1
- Initial package
