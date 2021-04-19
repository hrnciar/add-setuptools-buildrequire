%global		pkgname	OpenXR-SDK-Source
%global		libmajor 1

Name:		openxr
Version:	1.0.14
Release:	1%{?dist}
Summary:	An API for writing VR and AR software
License:	ASL 2.0
URL:		https://github.com/KhronosGroup/%{pkgname}
Source:		https://github.com/KhronosGroup/%{pkgname}/archive/%{pkgname}-release-%{version}.tar.gz

# Patch addressing .so versioning
# https://github.com/KhronosGroup/OpenXR-SDK-Source/issues/221
# Patch:          %%{name}-1.0.14-soversion.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glslang
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xrandr) 
BuildRequires:  python3dist(jinja2)

%description
OpenXR is an API specification for writing portable, cross-platform,
virtual reality (VR) and augmented reality (AR) software.

%package libs
Summary:        Libraries for writing VR and AR software

%description libs
This package contains the library needed to run programs dynamically
linked with OpenXR.

%package devel
Summary:        Headers and development files of the OpenXR library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description devel
Development files for the OpenXR library. Install this package if you
want to compile applications using the OpenXR library.

%prep
%autosetup -n %{pkgname}-release-%{version}

%build
%cmake \
    -DBUILD_ALL_EXTENSIONS=ON \
    -DBUILD_LOADER=ON \
    -DBUILD_TESTS=ON \
    -DBUILD_WITH_WAYLAND_HEADERS=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_FLAGS="%{optflags} -Wl,--as-needed" \
    -DCMAKE_CXX_FLAGS="%{optflags} -Wl,--as-needed" \
    -DCMAKE_CXX_STANDARD=14 \
    -DDYNAMIC_LOADER=ON 
%cmake_build

%install
%cmake_install

%files
%license LICENSE
# Include license in doc otherwise build complains
%doc CHANGELOG.SDK.md LICENSE README.md
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*

%files libs
%{_libdir}/*.so.%{libmajor}{,.*}

%files devel
%{_libdir}/lib*.so
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jan 28 2021 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.14-1
- Update to 1.0.14
- Use pkgconfig for vulkan-loader-devel as build requirement
- Drop .so versioning patch as suggested by upstream 

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.13-1
- Update to 1.0.13

* Sat Nov 7 2020 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.12-3
- Add patch for .so versioning
- Remove tab spacing
- Drop Group tag

* Sat Nov 7 2020 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.12-2
- Fix source url
- Set arch info (isa) for libs requirement
- Remove OPENGL_glx_LIBRARY=GL parameter
- Specify _includedir

* Mon Oct 26 2020 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.12-1
- Port spec file from Mageia to Fedora

* Sat Sep 19 2020 ghibo <ghibo> 1.0.11-1.mga8
- initial release.
