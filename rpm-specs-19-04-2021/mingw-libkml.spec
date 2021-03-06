%{?mingw_package_header}

%global pkgname libkml

Name:           mingw-%{pkgname}
Version:        1.3.0
Release:        16%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        BSD
URL:            https://github.com/libkml/libkml
Source0:        https://github.com/libkml/libkml/archive/%{version}/libkml-%{version}.tar.gz
# TODO: Port to minizip-2.x, meanwhile bundle version 1.3.0
# wget -O minizip-1.3.0.tar.gz http://sourceforge.net/projects/libkml-files/files/1.3.0/minizip.tar.gz/download
Source1:        minizip-1.3.0.tar.gz

## See https://github.com/libkml/libkml/pull/239
Patch0:         0001-Fix-build-failure-due-to-failure-to-convert-pointer-.patch
Patch1:         0002-Fix-mistaken-use-of-std-cerr-instead-of-std-endl.patch
# Mingw build fixes
Patch2:         libkml_mingw.patch
# Don't bytecompile python sources as part of build process, leave it to rpmbuild
Patch3:         libkml_dont-bytecompile.patch


BuildRequires: make
BuildRequires:  cmake
BuildRequires:  swig

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-boost
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-uriparser
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-boost
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-uriparser
BuildRequires:  mingw64-zlib

Provides:       bundled(minizip) = 1.3.0


%description
MinGW Windows %{pkgname} library.

###############################################################################

%package -n mingw32-%{pkgname}
Summary:        MinGW Windows %{pkgname} library
Requires:       mingw32-boost

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:        MinGW Windows Python 3 %{pkgname} library
Requires:       mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python 3 %{pkgname} library.

###############################################################################

%package -n mingw64-%{pkgname}
Summary:        MinGW Windows %{pkgname} library
Requires:       mingw64-boost

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:        MinGW Windows Python 3 %{pkgname} library
Requires:       mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python 3 %{pkgname} library.

###############################################################################

%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version} -a1


%build
# Build bundled minizip
(
cd minizip
%mingw_cmake -DBUILD_SHARED_LIBS=OFF
%mingw_make_build
)

export MINGW32_CMAKE_ARGS="\
  -DCMAKE_INSTALL_DIR=%{mingw32_libdir}/cmake/%{name} \
  -DINCLUDE_INSTALL_DIR=%{mingw32_includedir}/kml \
  -DPYTHON_LIBRARY=%{mingw32_libdir}/libpython%{mingw32_python3_version}.dll.a \
  -DPYTHON_INCLUDE_DIR=%{mingw32_includedir}/python%{mingw32_python3_version}/ \
  -DPYTHON_INSTALL_DIR=%{mingw32_python3_sitearch} \
  -DMINIZIP_INCLUDE_DIR=$PWD -DMINIZIP_LIBRARY=$PWD/minizip/build_win32/libminizip.a"

export MINGW64_CMAKE_ARGS="\
  -DCMAKE_INSTALL_DIR=%{mingw64_libdir}/cmake/%{name} \
  -DINCLUDE_INSTALL_DIR=%{mingw64_includedir}/kml \
  -DPYTHON_LIBRARY=%{mingw64_libdir}/libpython%{mingw64_python3_version}.dll.a \
  -DPYTHON_INCLUDE_DIR=%{mingw64_includedir}/python%{mingw64_python3_version}/ \
  -DPYTHON_INSTALL_DIR=%{mingw64_python3_sitearch} \
  -DMINIZIP_INCLUDE_DIR=$PWD -DMINIZIP_LIBRARY=$PWD/minizip/build_win64/libminizip.a"

%mingw_cmake -DWITH_SWIG=ON -DWITH_PYTHON=ON \
  -DBUILD_TESTING=OFF \
  -DBUILD_EXAMPLES=OFF
%mingw_make_build

%install
%mingw_make_install

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%license LICENSE
%{mingw32_bindir}/%{pkgname}*.dll
%{mingw32_includedir}/kml/
%{mingw32_libdir}/%{pkgname}*.dll.a
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc
%{mingw32_libdir}/cmake/%{pkgname}/

%files -n mingw32-python3-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%{mingw32_python3_sitearch}/*.py*

%files -n mingw64-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%license LICENSE
%{mingw64_bindir}/%{pkgname}*.dll
%{mingw64_includedir}/kml/
%{mingw64_libdir}/%{pkgname}*.dll.a
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc
%{mingw64_libdir}/cmake/%{pkgname}/

%files -n mingw64-python3-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%{mingw64_python3_sitearch}/*.py*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 22:37:04 CET 2020 Sandro Mani <manisandro@gmail.com> - 1.3.0-15
- Switch to bundled legacy minizip

* Wed Nov 04 2020 Sandro Mani <manisandro@gmail.com> - 1.3.0-14
- Exclude debug files in main packages

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 1.3.0-12
- Rebuild (python-3.9)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.3.0-10
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 1.3.0-9
- Rebuild (python 3.8)

* Sun Aug 04 2019 Sandro Mani <manisandro@gmail.com> - 1.3.0-8
- Drop python2 subpackage

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 1.3.0-6
- Add python3 subpackages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 09 2017 Sandro Mani <manisandro@gmail.com> . 1.3.0-2
- Add requires on mingw-boost since public headers require it
- Add requires on mingw-libkml for mingw-python2-libkml

* Mon Oct 30 2017 Sandro Mani <manisandro@gmail.com> - 1.3.0-1
- Initial package
