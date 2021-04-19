%{?mingw_package_header}

%global pkgname geos

Name:          mingw-%{pkgname}
Version:       3.9.1
Release:       1%{?dist}
Summary:       MinGW Windows GEOS library
License:       LGPLv2+
BuildArch:     noarch
URL:           http://trac.osgeo.org/geos/
Source0:       http://download.osgeo.org/%{pkgname}/%{pkgname}-%{version}.tar.bz2
# Add library version suffix also when building with cmake for mingw
Patch0:        geos-3.9.0_version-suffix.patch

BuildRequires: cmake
BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++


%description
MinGW Windows GEOS library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GEOS library

%description -n mingw32-%{pkgname}
MinGW Windows GEOS library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GEOS library

%description -n mingw64-%{pkgname}
MinGW Windows GEOS library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake -DDISABLE_GEOS_INLINE=ON
%mingw_make_build


%install
%mingw_make_install

# Drop cross-compiled geos-config which is not useful
rm -f %{buildroot}%{mingw32_bindir}/geos-config
rm -f %{buildroot}%{mingw64_bindir}/geos-config


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libgeos-3.9.1.dll
%{mingw32_bindir}/libgeos_c-1.dll
%{mingw32_includedir}/geos/
%{mingw32_includedir}/geos_c.h
%{mingw32_libdir}/libgeos.dll.a
%{mingw32_libdir}/libgeos_c.dll.a
%{mingw32_libdir}/cmake/GEOS/
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libgeos-3.9.1.dll
%{mingw64_bindir}/libgeos_c-1.dll
%{mingw64_includedir}/geos/
%{mingw64_includedir}/geos_c.h
%{mingw64_libdir}/libgeos.dll.a
%{mingw64_libdir}/libgeos_c.dll.a
%{mingw64_libdir}/cmake/GEOS/
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc


%changelog
* Thu Feb 11 2021 Sandro Mani <manisandro@gmail.com> - 3.9.1-1
- Update to 3.9.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 18:57:43 CET 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-2
- Disable inline

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Sandro Mani <manisandro@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.7.1-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Sandro Mani <manisandro@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Thu Jan 12 2017 Sandro Mani <manisandro@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Fri Jan 22 2016 Sandro Mani <manisandro@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Tue Apr 14 2015 Sandro Mani <manisandro@gmail.com> - 3.4.2-1
- Initial package
