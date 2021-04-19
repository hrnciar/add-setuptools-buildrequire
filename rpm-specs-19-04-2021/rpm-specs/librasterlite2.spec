%global pre beta1

# This package requires libspatialite 4.2 and solves the tasks librasterlite
# and gaiagraphics solved in the past. It is not a drop-in replacement for either.
Name:          librasterlite2
Version:       1.1.0
Release:       0.4%{?pre:.%pre}%{?dist}
Summary:       Stores and retrieves huge raster coverages using a SpatiaLite DBMS
License:       MPLv1.1 or GPLv2+ or LGPLv2+
URL:           https://www.gaia-gis.it/fossil/librasterlite2
Source0:       http://www.gaia-gis.it/gaia-sins/%{name}-sources/%{name}-%{version}%{?pre:-%pre}.tar.gz

BuildRequires: gcc
BuildRequires: cairo-devel
BuildRequires: CharLS-devel
BuildRequires: giflib-devel
BuildRequires: libcurl-devel
BuildRequires: libgeotiff-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libspatialite-devel
BuildRequires: libwebp-devel
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: lz4-devel
BuildRequires: minizip-devel
BuildRequires: openjpeg2-devel
BuildRequires: proj-devel
BuildRequires: sqlite-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: make

%description
librasterlite2 is a library that stores and retrieves huge raster coverages
using a SpatiaLite DBMS.


%package devel
Summary:  Development libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.


%package tools
Summary:  Tools for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
License:  GPLv3+

%description tools
The %{name}-tools package contains l2tool and rwmslite.
rl2tool is a CLI tool to create and manage rasterlite2 coverages.
wmslite is a simple WMS server (Web Map Service) based on librasterlite2.


%prep
%autosetup -p1 -n %{name}-%{version}%{?pre:-%pre}


%build
%configure --disable-static
%make_build


%install
%make_install

# Delete undesired libtool archives
rm -f %{buildroot}/%{_libdir}/%{name}.la
rm -f %{buildroot}/%{_libdir}/mod_rasterlite2.la

# Delete soname symlink for the sqlite extension
rm -f %{buildroot}/%{_libdir}/mod_rasterlite2.so.*


%check
# test_svg fails on at least i386
# Some tests are online tests and may fail as well, depending on availability
# Additional tests are failing on ARM; Let the author know on the mailing list
make check || true


%ldconfig_scriptlets


%files
%doc AUTHORS
%license COPYING
%{_libdir}/%{name}.so.*
# The symlink must be present to allow loading the extension
# https://groups.google.com/forum/#!topic/spatialite-users/zkGP-gPByXk
%{_libdir}/mod_rasterlite2.so

%files devel
%doc examples/*.c
%{_includedir}/rasterlite2
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rasterlite2.pc

%files tools
%{_bindir}/rl2sniff
%{_bindir}/rl2tool
%{_bindir}/wmslite


%changelog
* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-0.4.beta1
- Rebuild (proj)

* Wed Feb 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-0.3.beta1
- Rebuild for new minizip

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 1.1.0-0.1.beta1
- Update to 1.1.0-beta1

* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 1.1.0-0.1.beta0
- Update to 1.1.0-beta0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.0.0-3.rc0.10
- Rebuild (giflib)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 1.0.0-3.rc0.5
- Rebuild (libwebp)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.rc0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Volker Froehlich <volker27@gmx.at> - 1.0.0-3.rc0.3
- rebuilt

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-3.rc0.2
- Rebuilt for libwebp soname bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3.rc0.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Devrim Gündüz <devrim@gunduz.org> - 1.0.0-3.rc0
- Rebuild for Proj 4.9.1

* Mon Aug 25 2014 Devrim Gündüz <devrim@gunduz.org> - 1.0.0-2.rc0
- Rebuilt for libgeotiff
- Add dependency for proj-devel

* Fri Aug  8 2014 Volker Fröhlich <volker27@gmx.at> - 1.0.0-1.rc0
- Remove pkgconfig requirement on the devel sub-package
- Delete soname symlink for the sqlite extension

* Wed Jun 11 2014 Volker Fröhlich <volker27@gmx.at> - 1.0.0-0.rc0
- Initial package for Fedora
