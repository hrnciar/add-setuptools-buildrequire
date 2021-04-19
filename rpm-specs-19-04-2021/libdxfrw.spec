Name:		libdxfrw
Version:	0.6.3
Release:	17%{?dist}
Summary:	Library to read/write DXF files
License:	GPLv2+
URL:		http://sourceforge.net/p/libdxfrw/home/Home/
Source0:	http://downloads.sourceforge.net/project/libdxfrw/%{name}-%{version}.tar.bz2
Patch0:		libdxfrw-LibreCad-2.1.0-changes.patch
# https://github.com/LibreCAD/LibreCAD/commit/6da7cc5f7f31afb008f03dbd11e07207ccd82085
# https://github.com/LibreCAD/LibreCAD/commit/8604f171ee380f294102da6154adf77ab754d403
Patch1:		libdxfrw-0.6.3-CVE-2018-19105.patch
# https://github.com/LibreCAD/LibreCAD/commit/a413e791461c6c620a453f3332d0a3691adce328
Patch2:		libdxfrw-0.6.3-fix-compile-warnings.patch
# https://github.com/LibreCAD/LibreCAD/commit/0f74d95c6784731a11955d0df5f9f19d34431ea5
Patch3:		libdxfrw-0.6.3-fixed-polyline-vertex-processing.patch
# https://github.com/LibreCAD/LibreCAD/commit/ca126ae7e35d238ebb2e2935562a0dd6fc24edea
Patch4:		libdxfrw-0.6.3-fix-DXF-files-with-comments-in-SECTIONs.patch
# https://github.com/LibreCAD/LibreCAD/commit/8f06b2474a6847dfacc0478708298b1626f80553
# https://github.com/LibreCAD/LibreCAD/commit/41c3dbf0dfd5dc7d2db5109695f2675a0aefdbc9
Patch5:		libdxfrw-0.6.3-fix-spelling-mistakes.patch
# https://github.com/LibreCAD/LibreCAD/commit/913218d2deadb5b5056061743af6d0ded99e431d
Patch6:		librecad-0.6.3-page-margins-and-page-preview.patch
# https://github.com/LibreCAD/LibreCAD/commit/17ca3ccc58a2334310952138cc7a6f2697fbea73
Patch7:		librecad-0.6.3-tiled-printing.patch
# https://github.com/LibreCAD/LibreCAD/commit/e1cb7f6c7bc1b110eb327956544dc7e253c8d0cc
Patch8:		librecad-0.6.3-remove-useless-operator.patch
# https://github.com/LibreCAD/LibreCAD/commit/06739fd1ba59f03cb1e66b21455a863613b5c4f3
Patch9:		librecad-add-missing-subclass-marker-to-PLOTSETTINGS.patch
# https://github.com/LibreCAD/LibreCAD/commit/ce59dd5dc00e4b0d66ae4d29e4ccb8f60b374bd4
# https://github.com/LibreCAD/LibreCAD/commit/f9b6520d4a8fc0819cca83f60ab5f5b5eb04148d
Patch10:	librecad-spline-fixes.patch
# https://github.com/LibreCAD/LibreCAD/commit/973e81c9df803fcdd258f3c549bb664efd045bf9
Patch11:	librecad-hatch-read-fix.patch

BuildRequires:  gcc-c++
BuildRequires: make

%description
libdxfrw is a free C++ library to read and write DXF files in both formats, 
ASCII and binary form.

%package devel
Summary:	Development files for libdxfrw
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libdxfrw.

%prep
%setup -q
%patch0 -p1 -b .lc210
%patch1 -p1 -b .CVE-2018-19105
%patch2 -p1 -b .fix-compile-warnings
%patch3 -p1 -b .fixed-polyline-vertex-processing
%patch4 -p1 -b .fix-dxf-files-with-comments-in-SECTIONs
%patch5 -p1 -b .fix-spelling-mistakes
%patch6 -p1 -b .page-margins-and-page-preview
%patch7 -p1 -b .tiled-printing
%patch8 -p1 -b .remove-useless-operator
%patch9 -p1 -b .add-missing-subclass-marker-to-PLOTSETTINGS
%patch10 -p1 -b .spline-fixes
%patch11 -p1 -b .hatch-read-fix

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="/usr/bin/install -c -p"
rm -rf %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/dwg2dxf
%{_libdir}/*.so.*

%files devel
%{_includedir}/libdxfrw0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdxfrw0.pc

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Tom Callaway <spot@fedoraproject.org> - 0.6.3-16
- more fixes from LibreCAD git

* Wed Nov  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.6.3-15
- add all of the current fixes from LibreCAD git

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Tom Callaway <spot@fedoraproject.org> - 0.6.3-10
- add fix from librecad for CVE-2018-19105

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun  6 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.3-3
- apply changes from LibreCad 2.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.3-1
- update to 0.6.3

* Fri Sep 11 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.1-1
- update to 0.6.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-4
- Rebuilt for GCC 5 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Tom Callaway <spot@fedoraproject.org> - 0.5.11-1
- update to 0.5.11
- resync with librecad changes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-3
- apply fixes from librecad 2.0.0beta5

* Wed Apr 24 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-2
- drop empty NEWS and TODO files
- force INSTALL to use -p to preseve timestamps

* Sun Feb 24 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-1
- initial package
