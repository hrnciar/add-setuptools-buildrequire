%{?mingw_package_header}

%global pkgname vulkan-validation-layers
%global srcname Vulkan-ValidationLayers

#global commit 571a886b62cc7092626064376a65c7654f5d9b39
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3".0"}')

Name:          mingw-%{pkgname}
Version:       1.2.162.1
Release:       1%{?commit:.git%{shortcommit}}%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       ASL 2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
%if 0%{?commit:1}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/sdk-%{version}/%{srcname}-%{version}.tar.gz
%endif

# Case sensitivity fix
Patch0:        vulkan-validation-layers_mingw.patch


BuildRequires: make
BuildRequires: cmake
BuildRequires: python3

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-glslang
BuildRequires: mingw32-spirv-headers
BuildRequires: mingw32-spirv-tools
BuildRequires: mingw32-vulkan-headers >= %{baseversion}

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-glslang
BuildRequires: mingw64-spirv-headers
BuildRequires: mingw64-spirv-tools
BuildRequires: mingw64-vulkan-headers >= %{baseversion}


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{srcname}-%{commit}
%else
%autosetup -p1 -n %{srcname}-sdk-%{version}
%endif


%build
# Need to specify minimum required windows version to 6.0 (Vista) or newer, else undefined references will occur
MINGW32_CFLAGS="%{mingw32_cflags} -D_WIN32_WINNT=0x0600" \
MINGW64_CFLAGS="%{mingw64_cflags} -D_WIN32_WINNT=0x0600" \
MINGW32_CMAKE_ARGS="-DGLSLANG_INSTALL_DIR=%{mingw32_prefix} -DSPIRV_HEADERS_INSTALL_DIR=%{mingw32_includedir}/spirv -DCMAKE_INSTALL_INCLUDEDIR=%{mingw32_includedir}/vulkan" \
MINGW64_CMAKE_ARGS="-DGLSLANG_INSTALL_DIR=%{mingw64_prefix} -DSPIRV_HEADERS_INSTALL_DIR=%{mingw64_includedir}/spirv -DCMAKE_INSTALL_INCLUDEDIR=%{mingw64_includedir}/vulkan"\
%mingw_cmake
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%doc README.md
%license LICENSE.txt
%{mingw32_bindir}/libVkLayer_khronos_validation.dll
%{mingw32_libdir}/libVkLayer_khronos_validation.dll.a
%{mingw32_libdir}/libVkLayer_utils.a
%{mingw32_libdir}/VkLayer_khronos_validation.json


%files -n mingw64-%{pkgname}
%doc README.md
%license LICENSE.txt
%{mingw64_bindir}/libVkLayer_khronos_validation.dll
%{mingw64_libdir}/libVkLayer_khronos_validation.dll.a
%{mingw64_libdir}/libVkLayer_utils.a
%{mingw64_libdir}/VkLayer_khronos_validation.json


%changelog
* Thu Feb 04 2021 Sandro Mani <manisandro@gmail.com> - 1.2.162.1-1
- Update to 1.2.162.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.154.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Sandro Mani <manisandro@gmail.com> - 1.2.154.0-1
- Update to 1.2.154.0

* Mon Aug 10 2020 Sandro Mani <manisandro@gmail.com> - 1.2.148.0-1
- Update to 1.2.148.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.135.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 1.2.135.0-1
- Update to 1.2.135.0

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 1.2.131.1-1
- Update to 1.2.131.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.126.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 1.1.126.0-1
- Update to 1.1.126.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.1.114.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 1.1.114.0-1
- Update to 1.1.114.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 1.1.108.0-1
- Update to 1.1.108.0

* Sat Apr 20 2019 Sandro Mani <manisandro@gmail.com> - 1.1.106.0-1
- Update to 1.1.106.0

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 1.1.101.0-1
- Update to 1.1.101.0

* Thu Feb 14 2019 Sandro Mani <manisandro@gmail.com> - 1.1.97.0-1
- Update to 1.1.97.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.82.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Sandro Mani <manisandro@gmail.com> - 1.1.77-1
- Update to 1.1.77

* Sat Jun 09 2018 Sandro Mani <manisandro@gmail.com> - 1.1.74-0.1.git571a886
- Initial package
