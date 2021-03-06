Name:           libplacebo
Version:        3.104.0
Release:        1%{?dist}
Summary:        Reusable library for GPU-accelerated video/image rendering primitives

License:        LGPLv2+
URL:            https://github.com/haasn/libplacebo
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  lcms2-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libshaderc-devel >= 2018.0-1
BuildRequires:  python3-mako
# Use a more modern compiler toolchain on EL7
%if 0%{?rhel} == 7
BuildRequires:  devtoolset-7-toolchain, devtoolset-7-libatomic-devel
# Vulkan is optional, but only available on theses arches for EL7
%ifarch x86_64 ppc64le
BuildRequires:  vulkan-devel
%endif
%else # Fedora
BuildRequires:  vulkan-devel
BuildRequires:  glslang-devel
%endif


%description
libplacebo is essentially the core rendering algorithms and ideas of
mpv turned into a library. This grew out of an interest to accomplish
the following goals:

- Clean up mpv's internal API and make it reusable for other projects.
- Provide a standard library of useful GPU-accelerated image processing
  primitives based on GLSL, so projects like VLC or Firefox can use them
  without incurring a heavy dependency on `libmpv`.
- Rewrite core parts of mpv's GPU-accelerated video renderer on top of
  redesigned abstractions. (Basically, I wanted to eliminate code smell
  like `shader_cache.c` and totally redesign `gpu/video.c`)


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%endif


%build

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%endif

%meson
%meson_build


%install
%meson_install


%ldconfig_scriptlets


%files
%license LICENSE
%doc README.md
%{_libdir}/libplacebo.so.104

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libplacebo.pc


%changelog
* Tue Feb 09 2021 Nicolas Chauvet <kwizart@gmail.com> - 3.104.0-1
- Update to 3.104.0

* Thu Jan 28 2021 Leigh Scott <leigh123linux@gmail.com> - 2.72.2-1
- Update to 2.72.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.72.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.72.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Leigh Scott <leigh123linux@gmail.com> - 2.72.0-1
- Update to 2.72.0

* Sat Feb 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1.29.1-1
- Update to 1.29.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.21.0-1
- Update to 1.21.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.18.0-2
- Rebuild with Meson fix for #1699099

* Sat Apr 06 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.18.0-1
- Update to 1.18.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-2
- Drop WAR patch
- Enforce the shaderc version

* Mon Oct 01 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.4.0-2
- Fix build on EL7

* Mon Feb 12 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.4.0-1
- Initial spec file
