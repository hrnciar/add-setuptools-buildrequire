%{?mingw_package_header}

%global pkgname librttopo

Name:          mingw-%{pkgname}
Version:       1.1.0
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       GPLv2+
BuildArch:     noarch
URL:           https://git.osgeo.org/gitea/rttopo/%{pkgname}
Source0:       https://git.osgeo.org/gitea/rttopo/%{pkgname}/archive/%{pkgname}-%{version}.tar.gz
# Use pkgconfig to find geos
Patch0:        librttopo_geos.patch

BuildRequires: make
BuildRequires: autoconf automake libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-geos

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-geos


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows Leptonica library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}


%build
autoreconf -ifv
MINGW32_CONFIGURE_ARGS="PKGCONFIG=%{mingw32_target}-pkg-config" \
MINGW64_CONFIGURE_ARGS="PKGCONFIG=%{mingw64_target}-pkg-config" \
%mingw_configure  --disable-static
%mingw_make_build


%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/%{pkgname}-1.dll
%{mingw32_includedir}/%{pkgname}.h
%{mingw32_includedir}/%{pkgname}_geom.h
%{mingw32_libdir}/%{pkgname}.dll.a
%{mingw32_libdir}/pkgconfig/rttopo.pc

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/%{pkgname}-1.dll
%{mingw64_includedir}/%{pkgname}.h
%{mingw64_includedir}/%{pkgname}_geom.h
%{mingw64_libdir}/%{pkgname}.dll.a
%{mingw64_libdir}/pkgconfig/rttopo.pc


%changelog
* Sat Feb 27 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-1
- Initial package
