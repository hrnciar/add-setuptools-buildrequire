%{?mingw_package_header}

%global mingw32_py3_incdir %(mingw32-python3 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())')
%global mingw64_py3_incdir %(mingw64-python3 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())')

%global pkgname pillow
%global pypi_name Pillow

Name:           mingw-python-%{pkgname}
Version:        8.2.0
Release:        1%{?dist}
Summary:        MinGW Windows Python %{pkgname} library

BuildArch:      noarch
# License: see http://www.pythonware.com/products/pil/license.htm
License:        MIT
URL:            http://python-pillow.github.io/
Source0:        %{pypi_source}

# MinGW build fixes
Patch0:         pillow_mingw.patch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw32-libimagequant
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-openjpeg2
BuildRequires:  mingw32-tk
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw64-libimagequant
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-openjpeg2
BuildRequires:  mingw64-tk
BuildRequires:  mingw64-zlib


%description
MinGW Windows Python %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python2 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python2 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python2 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python2 %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
PKG_CONFIG=mingw32-pkg-config %{mingw32_py3_build}
PKG_CONFIG=mingw64-pkg-config %{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}

install -d %{buildroot}/%{mingw32_py3_incdir}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{mingw32_py3_incdir}/Imaging

install -d %{buildroot}/%{mingw64_py3_incdir}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{mingw64_py3_incdir}/Imaging

# Remove sample scripts
rm -rf %{buildroot}%{mingw32_bindir}
rm -rf %{buildroot}%{mingw64_bindir}

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-python3-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%license docs/COPYING
%{mingw32_python3_sitearch}/PIL/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/
%{mingw32_py3_incdir}/Imaging/

%files -n mingw64-python3-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%license docs/COPYING
%{mingw64_python3_sitearch}/PIL/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/
%{mingw64_py3_incdir}/Imaging/


%changelog
* Sun Apr 04 2021 Sandro Mani <manisandro@gmail.com> - 8.2.0-1
- Update to 8.2.0

* Sat Mar 06 2021 Sandro Mani <manisandro@gmail.com> - 8.1.2-1
- Update to 8.1.2

* Tue Mar 02 2021 Sandro Mani <manisandro@gmail.com> - 8.1.1-1
- Update to 8.1.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Sandro Mani <manisandro@gmail.com> - 8.1.0-1
- Update to 8.1.0

* Mon Nov 09 2020 Sandro Mani <manisandro@gmail.com> - 8.0.1-3
- Switch to mingw32,64_py3_build,install

* Wed Nov 04 2020 Sandro Mani <manisandro@gmail.com> - 8.0.1-2
- Exclude debug files in main package

* Fri Oct 23 2020 Sandro Mani <manisandro@gmail.com> - 8.0.1-1
- Update to 8.0.1

* Sat Oct 17 2020 Sandro Mani <manisandro@gmail.com> - 8.0.0-1
- Update to 8.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Sandro Mani <manisandro@gmail.com> - 7.2.0-1
- Update to 7.2.0

* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 7.1.2-2
- Rebuild (python-3.9)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 7.1.2-1
- Update to 7.1.2

* Tue Sep 05 2017 Sandro Mani <manisandro@gmail.com> - 4.2.1-1
- Initial package
