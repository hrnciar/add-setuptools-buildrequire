%global debug_package %{nil}

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

Name:           CImg
Epoch:          1
Version:        2.9.6
Release:        1%{?dist}
Summary:        C++ Template Image Processing Toolkit
# CImg.h: Dual licensed
# plugins/cimgmatlab.h: LGPLv3
License:        (CeCILL or CeCILL-C) and LGPLv3
URL:            https://github.com/dtschump/CImg
Source0:        http://cimg.eu/files/CImg_%{version}.zip
# This package has no dependencies actually, these below are 
# for %%check only.
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  fftw-devel
BuildRequires:  ImageMagick-c++-devel
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel
BuildRequires:  lapack-devel
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  opencv-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  zlib-devel
BuildRequires: make

%description
The CImg Library is an open-source C++ toolkit for image processing. 
It consists in a single header file 'CImg.h' providing a minimal set of C++ 
classes and methods that can be used in your own sources, to load/save, 
process and display images. Very portable, efficient and easy to use, 
it's a pleasant library for developping image processing algorithms in C++.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
sed -i 's|$(X11PATH)/lib|$(X11PATH)/%{_lib}|g' examples/Makefile
%if %{with flexiblas}
sed -i 's|-lblas -llapack|-lflexiblas|g' examples/Makefile
%endif

%build
# This is a headers only package.

%install
install -pdm755 %{buildroot}%{_includedir}/%{name}/plugins
install -pm644 CImg.h %{buildroot}%{_includedir}/
install -pm644 plugins/*.h %{buildroot}%{_includedir}/%{name}/plugins/

%check
# Build examples based on sources to verify the usability.
# CMake couldn't find -lfftw3_threads so I use
# make directly.
make -C examples linux %{?_smp_mflags}

%files devel
%doc *.txt resources/CImg_reference.pdf
%{_includedir}/CImg.h
%{_includedir}/%{name}/

%changelog
* Wed Feb 10 2021 josef radinger <cheese@nosuchhost.net> - 1:2.9.6-1
- bump version

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 josef radinger <cheese@nosuchhost.net> - 1:2.9.4-1
- bump version

* Thu Nov 19 2020 josef radinger <cheese@nosuchhost.net> - 1:2.9.3-1
- bump version

* Tue Sep 08 2020 josef radinger <cheese@nosuchhost.net> - 1:2.9.2-1
- bump version

* Thu Aug 27 2020 I??aki ??car <iucar@fedoraproject.org> - 1:2.9.1-4
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.9.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 josef radinger <cheese@nosuchhost.net> - 1:2.9.1-1
- bump version

* Mon Mar 30 2020 josef radinger <cheese@nosuchhost.net> - 1:2.9.0-1
- bump version

* Thu Feb 13 2020 josef radinger <cheese@nosuchhost.net> - 1:2.8.4-1
- bump version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 josef radinger <cheese@nosuchhost.net> - 1:2.8.3-1
- bump version

* Wed Jan 15 2020 josef radinger <cheese@nosuchhost.net> - 1:2.8.2-1
- bump version

* Thu Jan 09 2020 josef radinger <cheese@nosuchhost.net> - 1:2.8.1-1
- bump version

* Tue Oct 15 2019 josef radinger <cheese@nosuchhost.net> - 1:2.7.4-1
- bump version

* Fri Sep 06 2019 josef radinger <cheese@nosuchhost.net> - 1:2.7.1-1
- bump version

* Thu Aug 15 2019 josef radinger <cheese@nosuchhost.net> - 1:2.7.0-1
- bump version

* Thu Jul 25 2019 josef radinger <cheese@nosuchhost.net> - 1:2.6.7-1
- bump version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 josef radinger <cheese@nosuchhost.net> - 1:2.6.6-1
- bump version

* Mon Jun 17 2019 josef radinger <cheese@nosuchhost.net> - 1:2.6.5-1
- bump version

* Sat May 25 2019 josef radinger <cheese@nosuchhost.net> - 1:2.6.4-1
- bump version

* Tue Apr 23 2019 josef radinger <cheese@nosuchhost.net> - 1:2.6.2-1
- bump version

* Tue Apr 23 2019 josef radinger <cheese@nosuchhost.net> - 1:2.6.0-1
- bump version

* Thu Apr 18 2019 josef radinger <cheese@nosuchhost.net> - 1:2.5.7-1
- bump version

* Mon Apr 08 2019 josef radinger <cheese@nosuchhost.net> - 1:2.5.6-2
- bump version

* Fri Mar 29 2019 josef radinger <cheese@nosuchhost.net> - 1:2.5.5-1
- bump version

* Sun Mar 17 2019 josef radinger <cheese@nosuchhost.net> - 1:2.5.4-1
- bump version

* Sun Mar 17 2019 josef radinger <cheese@nosuchhost.net> - 1:2.5.3-1
- bump version

* Sat Mar 16 2019 josef radinger <cheese@nosuchhost.net> - 1:2.5.2-2
- fix release in spec-file

* Sat Mar 16 2019 josef radinger <cheese@nosuchhost.net> - 1:2.5.2-1
- bump version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 josef radinger <cheese@nosuchhost.net> - 1:2.4.5-1
- bump version

* Tue Oct 16 2018 Daniel P. Berrang?? <berrange@redhat.com> - 1:2.4.0-1
- Update to 2.4.0 release

* Tue Sep  4 2018 Daniel P. Berrang?? <berrange@redhat.com> - 1:2.3.6-1
- Update to 2.3.6 release

* Wed Aug  1 2018 Daniel P. Berrang?? <berrange@redhat.com> - 1:2.3.3-1
- Update to 2.3.3 release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 202-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 202-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 202-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Tom Callaway <spot@fedoraproject.org> - 202-1
- update to v.202

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
