%{?mingw_package_header}

%global pkgname zstd

Name:          mingw-%{pkgname}
Version:       1.4.9
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
# BSD or GPLv2: Most files have a sentence that reads "You may select, at your option, one of the above-listed licenses"
# MIT: lib/dictBuilder/divsufsort.{c,h}
License:       (BSD or GPLv2) and MIT
URL:           https://github.com/facebook/%{pkgname}
Source0:       https://github.com/facebook/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz


BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
MINGW32_CMAKE_ARGS="-DCMAKE_INSTALL_INCLUDEDIR=%{mingw32_includedir}/%{pkgname}" \
MINGW64_CMAKE_ARGS="-DCMAKE_INSTALL_INCLUDEDIR=%{mingw64_includedir}/%{pkgname}" \
%mingw_cmake -DZSTD_BUILD_PROGRAMS=OFF -DZSTD_BUILD_STATIC=OFF ../build/cmake/
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/lib%{pkgname}.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/cmake/%{pkgname}/
%{mingw32_libdir}/pkgconfig/lib%{pkgname}.pc
%{mingw32_includedir}/%{pkgname}/

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/lib%{pkgname}.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/cmake/%{pkgname}/
%{mingw64_libdir}/pkgconfig/lib%{pkgname}.pc
%{mingw64_includedir}/%{pkgname}/


%changelog
* Fri Mar 05 2021 Sandro Mani <manisandro@gmail.com> - 1.4.9-1
- Update to 1.4.9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Sandro Mani <manisandro@gmail.com> - 1.4.8-1
- Update to 1.4.8

* Thu Nov 12 2020 Sandro Mani <manisandro@gmail.com> - 1.4.5-2
- Fix source URL
- Fix license tag

* Thu Nov 12 2020 Sandro Mani <manisandro@gmail.com> - 1.4.5-1
- Initial package
