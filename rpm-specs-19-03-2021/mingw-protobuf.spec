%{?mingw_package_header}

%global pkgname protobuf

Name:          mingw-%{pkgname}
Version:       3.14.0
Release:       2%{?dist}
Summary:       MinGW Windows protobuf library

BuildArch:     noarch
License:       BSD
URL:           https://github.com/protocolbuffers/protobuf
Source0:       https://github.com/protocolbuffers/protobuf/archive/v%{version}/%{pkgname}-%{version}-all.tar.gz
# Disable some constexpr constructors, it triggers
# error: call to non-'constexpr' function 'google::protobuf::internal::WrappedMutex::WrappedMutex()'
# note: 'google::protobuf::internal::WrappedMutex::WrappedMutex()' is not usable as a 'constexpr' function because:
# note: defaulted constructor calls non-'constexpr' 'std::mutex::mutex()'
# TODO: Revisit with mingw-w64-8.0.0 and gcc-11
Patch0:        protobuf_constexpr.patch

BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-zlib



%description
MinGW Windows protobuf library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows protobuf library
# Ensure packages stay in sync
Requires:      protobuf-compiler = %{version}

%description -n mingw32-%{pkgname}
MinGW Windows protobuf library.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows protobuf library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows protobuf library.


%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows protobuf library tools

%description -n mingw32-%{pkgname}-tools
MinGW Windows protobuf library tools.



%package -n mingw64-%{pkgname}
Summary:       MinGW Windows protobuf library
# Ensure packages stay in sync
Requires:      protobuf-compiler = %{version}


%description -n mingw64-%{pkgname}
MinGW Windows protobuf library.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows protobuf library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows protobuf library.


%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows protobuf library tools

%description -n mingw64-%{pkgname}-tools
MinGW Windows protobuf library tools.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
./autogen.sh
%mingw_configure
%mingw_make_build


%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libprotobuf-25.dll
%{mingw32_bindir}/libprotobuf-lite-25.dll
%{mingw32_bindir}/libprotoc-25.dll
%dir %{mingw32_includedir}/google
%{mingw32_includedir}/google/protobuf/
%{mingw32_libdir}/pkgconfig/protobuf-lite.pc
%{mingw32_libdir}/pkgconfig/protobuf.pc
%{mingw32_libdir}/libprotobuf-lite.dll.a
%{mingw32_libdir}/libprotobuf.dll.a
%{mingw32_libdir}/libprotoc.dll.a


%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libprotobuf-lite.a
%{mingw32_libdir}/libprotobuf.a
%{mingw32_libdir}/libprotoc.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/i686-w64-mingw32-protoc.exe

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libprotobuf-25.dll
%{mingw64_bindir}/libprotobuf-lite-25.dll
%{mingw64_bindir}/libprotoc-25.dll
%dir %{mingw64_includedir}/google
%{mingw64_includedir}/google/protobuf/
%{mingw64_libdir}/pkgconfig/protobuf-lite.pc
%{mingw64_libdir}/pkgconfig/protobuf.pc
%{mingw64_libdir}/libprotobuf-lite.dll.a
%{mingw64_libdir}/libprotobuf.dll.a
%{mingw64_libdir}/libprotoc.dll.a

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libprotobuf-lite.a
%{mingw64_libdir}/libprotobuf.a
%{mingw64_libdir}/libprotoc.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/x86_64-w64-mingw32-protoc.exe


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Sandro Mani <manisandro@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Thu Jan 14 08:33:00 CET 2021 Adrian Reber <adrian@lisas.de> - 3.13.0-3
- Rebuilt for protobuf 3.14

* Mon Sep 28 2020 Sandro Mani <manisandro@gmail.com> - 3.13.0-2
- Correctly require protobuf-compiler

* Sun Sep 27 2020 Sandro Mani <manisandro@gmail.com> - 3.13.0-1
- Update to 3.13.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Sandro Mani <manisandro@gmail.com> - 3.12.3-1
- Update to 3.12.3

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 3.11.4-1
- Update to 3.11.4

* Wed Feb 05 2020 Sandro Mani <manisandro@gmail.com> - 3.11.2-1
- Update to 3.11.2

* Mon Oct 28 2019 Sandro Mani <manisandro@gmail.com> - 3.6.1-1
- Initial package
