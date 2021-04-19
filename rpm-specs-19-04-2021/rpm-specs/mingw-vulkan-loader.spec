%{?mingw_package_header}

%global pkgname vulkan-loader
%global srcname Vulkan-Loader

#global commit 1bd294a1ddb32e832916aa874d103618f4faf1b3
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3".0"}')

Name:          mingw-%{pkgname}
# NOTE: loader/loader.c hunk of vulkan-mingw.patch should not be needed anymore once mingw-8.0.0 has landed!
Version:       1.2.162.0
Release:       2%{?commit:.git%{shortcommit}}%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       ASL 2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
%if 0%{?commit:1}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/sdk-%{version}/%{srcname}-%{version}.tar.gz
%endif

# Omit def file, results in vulkan-1.dll.a containing non @-decorated symbols, while vulkan-1.dll contains @-decorated symbols
Patch0:        vulkan-loader_mingw.patch


BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-vulkan-headers >= %{baseversion}

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-vulkan-headers >= %{baseversion}


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Provides:      mingw32-vulkan = %{version}-%{release}
Obsoletes:     mingw32-vulkan < %{version}-%{release}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Provides:      mingw64-vulkan = %{version}-%{release}
Obsoletes:     mingw64-vulkan < %{version}-%{release}

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
%mingw_cmake -DUSE_MASM=OFF
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%doc README.md
%license LICENSE.txt
%{mingw32_bindir}/vulkan-1.dll
%{mingw32_libdir}/libvulkan-1.dll.a
%{mingw32_libdir}/pkgconfig/vulkan.pc


%files -n mingw64-%{pkgname}
%doc README.md
%license LICENSE.txt
%{mingw64_bindir}/vulkan-1.dll
%{mingw64_libdir}/libvulkan-1.dll.a
%{mingw64_libdir}/pkgconfig/vulkan.pc


%changelog
* Thu Jan 28 2021 Sandro Mani <manisandro@gmail.com> - 1.2.162.0-2
- Add vulkan-loader_nodef.patch

* Thu Jan 28 2021 Sandro Mani <manisandro@gmail.com> - 1.2.162.0-1
- Update to 1.2.162.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.154.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Sandro Mani <manisandro@gmail.com> - 1.2.154.1-1
- Update to 1.2.154.1

* Mon Nov 02 2020 Sandro Mani <manisandro@gmail.com> - 1.2.148.1-1
- Update to 1.2.148.1

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

* Tue Nov 12 2019 Sandro Mani <manisandro@gmail.com> - 1.1.126.0-1
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

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 1.1.101.1-1
- Update to 1.1.101.1

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

* Sat Jun 09 2018 Sandro Mani <manisandro@gmail.com> - 1.1.74-0.1.git1bd294a
- Initial package
