Name:           libpgf
Version:        6.14.12
Release:        17%{?dist}
Summary:        PGF (Progressive Graphics File) library

License:        LGPLv2+
URL:            http://www.libpgf.org
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
# Modernize automake usage
Patch0:         libpgf-auto.patch

## backport upstream fixes
Patch147: libpgf-r147.patch
Patch148: libpgf-r148.patch

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires: make

%description
libPGF contains an implementation of the Progressive Graphics File (PGF)
which is a new image file format, that is based on a discrete, fast
wavelet transform with progressive coding features. PGF can be used
for lossless and lossy compression.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
%patch0 -p1 -b .auto
%patch147 -p1 -b .r147
%patch148 -p1 -b .r148
# Fix line endings
sed -i -e 's/\r//' configure.ac README

sed -i 's|$(DESTDIR)$(datadir)/doc/$(DOC_MODULE)|$(RPM_BUILD_DIR)/libpgf|g' doc/Makefile.am

sh autogen.sh


%build
# FIXME/TODO: document need for -DLIBPGF_DISABLE_OPENMP
# commit 52c998909401f404f1c7029b537ec900f3f780d0 doesn't say why, but
# I *think* it's related to digikam -- rex
export CFLAGS="%{optflags} -DLIBPGF_DISABLE_OPENMP"
export CXXFLAGS="%{optflags} -DLIBPGF_DISABLE_OPENMP -std=c++14"

%configure --disable-static

%make_build


%install
%make_install

# unpackaged files
rm -fv %{buildroot}%{_libdir}/libpgf.la


%ldconfig_scriptlets

%files
%doc README
%license COPYING
%{_libdir}/libpgf.so.6*

%files devel
%doc html
%{_includedir}/libpgf/
%{_libdir}/libpgf.so
%{_libdir}/pkgconfig/libpgf.pc
%{_mandir}/man3/*.3*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 6.14.12-16
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 6.14.12-10
- BR: gcc-c++, use %%license %%make_build %%make_install

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 6.14.12-4
- Backport upstream fixes: Use-after-free bug in Decoder.cpp (#1251749)
- .spec cosmetics

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.14.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.14.12-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 23 2015 Orion Poplawski <orion@cora.nwra.com> - 6.14.12-1
- Update to 6.14.12

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13.45-0.3.svn123
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13.45-0.2.svn123
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 11 2013 Alexey Kurov <nucleo@fedoraproject.org> - 6.13.45-0.1.svn123
- libpgf-6.13.45 r123 snapshot

* Fri Oct 25 2013 Alexey Kurov <nucleo@fedoraproject.org> - 6.12.27-0.2.svn119
- disable OpenMP

* Fri Oct 25 2013 Alexey Kurov <nucleo@fedoraproject.org> - 6.12.27-0.1.svn119
- libpgf-6.12.27 r119 snapshot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.12.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.12.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.12.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Alexey Kurov <nucleo@fedoraproject.org> - 6.12.24-2
- libpgf-6.12.24

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.11.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 28 2010 Alexey Kurov <nucleo@fedoraproject.org> - 6.11.42-1
- libpgf-6.11.42

* Thu Sep 23 2010 Alexey Kurov <nucleo@fedoraproject.org> - 6.11.24-1
- Initial RPM release
- added svn r46-48 fixes (6.11.32)
- install docs in -devel
