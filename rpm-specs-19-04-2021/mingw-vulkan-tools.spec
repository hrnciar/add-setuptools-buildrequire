%{?mingw_package_header}

%global pkgname vulkan-tools
%global srcname Vulkan-Tools

#global commit 634e3658d6fa8f95f9062a3a7831d5567baf0eb3
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3".0"}')

Name:          mingw-%{pkgname}
Version:       1.2.162.1
Release:       1%{?commit:.git%{shortcommit}}%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       ASL 2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
%if 0%{?commit:1}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/sdk-%{version}/%{srcname}-%{version}.tar.gz
%endif

# MinGW build fixes
Patch0:        vulkan-tools_mingw.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: glslang

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-vulkan-headers >= %{baseversion}
BuildRequires: mingw32-vulkan-loader >= %{baseversion}

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-vulkan-headers >= %{baseversion}
BuildRequires: mingw64-vulkan-loader >= %{baseversion}


%description
MinGW Windows %{pkgname}


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.


%{?mingw_debug_package}



%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{srcname}-%{commit}
%else
%autosetup -p1 -n %{srcname}-sdk-%{version}
%endif


%build
%mingw_cmake -DGLSLANG_INSTALL_DIR=%{_prefix}
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license LICENSE.txt
%{mingw32_bindir}/vkcube.exe
%{mingw32_bindir}/vkcubepp.exe
%{mingw32_bindir}/vulkaninfo.exe

%files -n mingw64-%{pkgname}
%license LICENSE.txt
%{mingw64_bindir}/vkcube.exe
%{mingw64_bindir}/vkcubepp.exe
%{mingw64_bindir}/vulkaninfo.exe


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
- Fix build with python 3.8

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

* Wed Feb 13 2019 Sandro Mani <manisandro@gmail.com> - 1.1.97.0-1
- Update to 1.1.97.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.82.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Sandro Mani <manisandro@gmail.com> - 1.1.77-1
- Update to 1.1.77
