%{?mingw_package_header}

%global pkgname graphite2

Name:          mingw-%{pkgname}
Version:       1.3.14
Release:       3%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       LGPLv2+
URL:           https://github.com/silnrsi/graphite
Source0:       https://github.com/silnrsi/graphite/releases/download/%{version}/%{pkgname}-%{version}.tgz

# https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-graphite2/001-graphite2-1.3.8-win64.patch
Patch0:        mingw-graphite2_win64.patch
# https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-graphite2/002-graphite2-1.2.1-pkgconfig.patch
Patch1:        mingw-graphite2_pkgconfig.patch
# https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-graphite2/003-graphite2-1.3.9-staticbuild.patch
Patch2:        mingw-graphite2_staticbuild.patch
# https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-graphite2/004-graphite2-1.3.8-dllimport-fix.patch
Patch3:        mingw-graphite2_dllimport-fix.patch

BuildArch:     noarch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-freetype

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-freetype


%description
Graphite2 is a project within SIL’s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create “smart fonts” capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.


# Win32
%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

# Win64
%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake -DGRAPHITE2_COMPARE_RENDERER=OFF
%mingw_make_build


%install
%mingw_make_install

rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}


# Win32
%files -n mingw32-%{pkgname}
%license LICENSE COPYING
%{mingw32_bindir}/gr2fonttest.exe
%{mingw32_bindir}/lib%{pkgname}.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc
%{mingw32_includedir}/%{pkgname}/

%files -n mingw32-%{pkgname}-static
%license LICENSE COPYING
%{mingw32_libdir}/lib%{pkgname}.a

# Win64
%files -n mingw64-%{pkgname}
%license LICENSE COPYING
%{mingw64_bindir}/gr2fonttest.exe
%{mingw64_bindir}/lib%{pkgname}.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc
%{mingw64_includedir}/%{pkgname}/

%files -n mingw64-%{pkgname}-static
%license LICENSE COPYING
%{mingw64_libdir}/lib%{pkgname}.a


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Sandro Mani <manisandro@gmail.com> - 1.3.14-1
- Update to 1.3.14

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.3.13-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Aug 26 2019 Sandro Mani <manisandro@gmail.com> - 1.3.13-1
- Update to 1.3.13

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Sandro Mani <manisandro@gmail.com> - 1.3.10-4
- Rebuild for ppc64le binutils bug

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Sandro Mani <manisandro@gmail.com> - 1.3.10-2
- License is just LGPLv2+
- Add license to -static subpackages

* Wed Jun 28 2017 Sandro Mani <manisandro@gmail.com> - 1.3.10-1
- Initial package
