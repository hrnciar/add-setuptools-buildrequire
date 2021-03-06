%global abiver 2.40
Name:           librealsense
Version:        2.40.0
Release:        2%{?dist}
Summary:        Cross-platform camera capture for Intel RealSense

License:        ASL 2.0 and BSD
URL:            https://github.com/IntelRealSense/librealsense
Source0:        https://github.com/IntelRealSense/librealsense/archive/v%{version}.tar.gz#/librealsense-%{version}.tar.gz
# Remove custom CFLAGS that override ours.
# This was discussed with upstream, but upstream wants to keep those flags.
Patch0:         librealsense.remove-cflags.patch
Patch1:         librealsense.realsense-file-shared-library.patch

BuildRequires:  cmake
BuildRequires:  cmake(glfw3)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gdb-headless
BuildRequires:  glfw-devel
BuildRequires:  libGL-devel
BuildRequires:  libusb-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Provides:       librealsense2 = %{version}-%{release}

%description
The Intel RealSense SDK is a cross-platform library (Linux, OSX, Windows) for
capturing data from the Intel RealSense D400 and SR 300 depth cameras.

For older devices (F200, R200, LR200, ZR300), please use librealsense1.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       librealsense2-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     python3-%{name}
Summary:        Python bindings for %{name}
%{?python_provide:%python_provide python3-%{name}}
Provides:       python3-librealsense2 = %{version}-%{release}

%description -n python3-%{name}
The python3-%{name} package contains python bindings for %{name}.


%package -n     python3-%{name}-devel
Summary:        Python development files for %{name}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Provides:       python3-librealsense2-devel = %{version}-%{release}

%description -n python3-%{name}-devel
The python3-%{name}-devel package contains libraries and header files for
developing python applications that use %{name}.


%package        doc
BuildArch:      noarch
Summary:        Documentation for %{name}
Provides:       librealsense2-doc = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation for developing applications
with %{name}.

# enable PIE, we need -fPIC anyway
%global _hardened_build 1

%prep
%autosetup -p1


%build
%cmake \
  -DBUILD_UNIT_TESTS=NO \
  -DCMAKE_INSTALL_BINDIR=%{_bindir} \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
  -DBUILD_PYTHON_BINDINGS:bool=true \
  -DPYTHON_EXECUTABLE=%{python3}
%cmake_build

sed -i "s:/usr/local/bin:%{_datadir}/realsense:" config/*
sed -i "s/plugdev/users/g" config/*rules

pushd doc/doxygen
# Do not generate Windows help files
sed -i \
  -e "s/GENERATE_HTMLHELP[[:space:]]*=[[:space:]]*YES/GENERATE_HTMLHELP = NO/" \
  doxyfile
doxygen
popd


%install
%cmake_install

mkdir -p %{buildroot}/%{_udevrulesdir}
install -p -m644 config/99-realsense-libusb.rules %{buildroot}/%{_udevrulesdir}
mkdir -p %{buildroot}/%{_datadir}/realsense
install -p -m755 config/usb-R200-in{,_udev} %{buildroot}/%{_datadir}/realsense


%files
%license LICENSE
%doc readme.md
%{_libdir}/librealsense-file.so.%{abiver}*
%{_libdir}/librealsense2-gl.so.%{abiver}*
%{_libdir}/librealsense2.so.%{abiver}*
%{_datadir}/realsense
%{_bindir}/realsense-viewer
%{_bindir}/rs-align
%{_bindir}/rs-align-advanced
%{_bindir}/rs-ar-advanced
%{_bindir}/rs-ar-basic
%{_bindir}/rs-benchmark
%{_bindir}/rs-callback
%{_bindir}/rs-capture
%{_bindir}/rs-color
%{_bindir}/rs-convert
%{_bindir}/rs-data-collect
%{_bindir}/rs-depth
%{_bindir}/rs-depth-quality
%{_bindir}/rs-distance
%{_bindir}/rs-enumerate-devices
%{_bindir}/rs-fw-logger
%{_bindir}/rs-fw-update
%{_bindir}/rs-gl
%{_bindir}/rs-hdr
%{_bindir}/rs-hello-realsense
%{_bindir}/rs-measure
%{_bindir}/rs-motion
%{_bindir}/rs-multicam
%{_bindir}/rs-pointcloud
%{_bindir}/rs-pose
%{_bindir}/rs-pose-and-image
%{_bindir}/rs-pose-predict
%{_bindir}/rs-post-processing
%{_bindir}/rs-record
%{_bindir}/rs-record-playback
%{_bindir}/rs-rosbag-inspector
%{_bindir}/rs-save-to-disk
%{_bindir}/rs-sensor-control
%{_bindir}/rs-software-device
%{_bindir}/rs-terminal
%{_bindir}/rs-tracking-and-depth
%{_bindir}/rs-trajectory
%{_udevrulesdir}/99-realsense-libusb.rules

%files devel
%{_includedir}/librealsense2
%{_includedir}/librealsense2-gl
%{_libdir}/cmake/realsense2
%{_libdir}/cmake/realsense2-gl
%{_libdir}/librealsense-file.so
%{_libdir}/librealsense2-gl.so
%{_libdir}/librealsense2.so
%{_libdir}/pkgconfig/realsense2-gl.pc
%{_libdir}/pkgconfig/realsense2.pc

%files -n python3-%{name}
%dir %{python3_sitearch}/pyrealsense2
%{python3_sitearch}/pyrealsense2/pyrealsense2*.so.%{abiver}*
%{python3_sitearch}/pyrealsense2/pybackend2*.so.2*

%files -n python3-%{name}-devel
%{_libdir}/cmake/pyrealsense2
%{python3_sitearch}/pyrealsense2/pyrealsense2*.so
%{python3_sitearch}/pyrealsense2/pybackend2*.so

%files doc
%license LICENSE
%doc doc/doxygen/html/*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 08:59:25 CET 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.40.0-1
- Update to 2.40.0

* Sun Oct 25 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.39.0-1
- Update to 2.39.0

* Fri Jul 31 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.38.0-1
- Update to 2.38.0
- Adapt to https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.36.0-1
- Update to 2.36.0

* Wed Jun 24 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.35.2-2
- Explicitly BR python3-setuptools
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/)

* Mon Jun 15 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.35.2-1
- Update to 2.35.2

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.33.1-6
- Rebuilt for Python 3.9

* Mon May 04 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.33.1-5
- Add Provides for librealsense2

* Fri Apr 10 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.33.1-4
- Add patch to separate python cmake target from other targets (upstream PR #6220)

* Tue Mar 24 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.33.1-3
- Add patch to make librealsense-file a shared library (#1815567)
- Require python devel sub-package from main sub-package (upstream #6124)

* Tue Mar 03 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.33.1-2
- Add python bindings

* Tue Mar 03 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.33.1-1
- Update to 2.33.1
- Add BR: gdb-headless
- Move cmake files to devel sub-package

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.31.0-1
- Update to 2.31.0

* Wed Nov 06 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.30.0-1
- Update to 2.30.0
- Make doc sub-package noarch

* Sat Sep 28 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.29.0-1
- Update to 2.29.0

* Sun Sep 22 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.28.1-1
- Update to 2.28.1

* Fri Sep 06 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.28.0-1
- Update to 2.28.0
- Remove upstreamed patch

* Thu Aug 22 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.26.0-1
- Update to 2.26.0
- Add patch to fix format security compiler errors
- Add new binaries rs-fw-update and rs-tracking-and-depth
- Adapt soname glob so it always matches the library's soname

* Sat Jul 27 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.24.0-1
- Update to 2.24.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.23.0-1
- Update to 2.23.0

* Mon May 20 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.22.0-1
- Update to 2.22.0

* Tue Apr 23 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.21.0-1
- Update to 2.21.0

* Tue Apr 02 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.19.2-1
- Update to 2.19.2

* Sun Mar 10 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.19.1-1
- Update to 2.19.1

* Sun Mar 10 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.19.0-1
- Update to 2.19.0

* Sat Feb 16 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.18.1-1
- Update to 2.18.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Till Hofmann <thofmann@fedoraproject.org> - 2.18.0-1
- Update to 2.18.0

* Fri Nov 09 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.16.1-1
- Update to 2.16.1

* Mon Aug 13 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.15.0-1
- Update to 2.15.0

* Fri Jul 27 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.14.1-1
- Update to 2.14.1

* Wed Jul 18 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.14.0-1
- Update to 2.14.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.13.0-1
- Update to 2.13.0

* Tue Jun 05 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.12.0-1
- Update to 2.12.0

* Wed May 23 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.11.1-1
- Update to latest release 2.11.1

* Fri Apr 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.10.3-2
- Move pkgconfig file to devel subpackge

* Fri Apr 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.10.3-1
- Update to 2.10.3

* Sat Mar 03 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1

* Fri Feb 09 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.10.0-1
- Update to 2.10.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1

* Mon Jan 01 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0
- Remove upstreamed patch to fix format-security
- Remove all "*.a" files
- Use BR: pkgconfig(libudev) instead of BR: systemd
- Add license file to doc subpackage

* Sat Dec 16 2017 Till Hofmann <thofmann@fedoraproject.org> - 2.8.3-1
- Update to latest release
- Remove upstreamed patch for missing includes
- Add patch to fix format-security

* Tue Sep 26 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.7.9-0.2
- Add patch to remove Threads from the pkgconfig requirements

* Mon Sep 18 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.7.9-0.1
- Update to librealsense2 alpha release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Mar 22 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-7
- Add missing BR: gcc-c++

* Wed Mar 22 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-6
- Add patch for missing include of sys/time.h to fix build error on ppc64

* Wed Mar 22 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-5
- Add patch for missing include of functional header

* Sat Jan 21 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-4
- Add patch to remove any CFLAGS modification in cmake
- Change License to "ASL 2.0 and BSD"
- Remove trademarks from description

* Mon Jan 16 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-3
- Install bash scripts into datadir, not into libdir

* Mon Jan 16 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-2
- Add patch to fix build flags on arm

* Mon Jan 16 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-1
- Update to 1.12.1
- Switch to cmake for building the package

* Mon Jan 16 2017 Till Hofmann <till.hofmann@posteo.de> - 1.9.7-2
- Fix paths in udev rules

* Mon Aug 29 2016 Till Hofmann <till.hofmann@posteo.de> - 1.9.7-1
- Initial package
