%{?mingw_package_header}

%global pkgname lxml
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       4.6.2
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://lxml.de/
Source0:       %{pypi_source}
# Don't attempt to link against librt
Patch0:        lxml-rt.patch

BuildRequires: libxslt-devel

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-libxslt
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-Cython
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-libxslt
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-Cython
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-python3-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-python3-%{pkgname}.debugfiles

%files -n mingw32-python3-%{pkgname} -f mingw32-python3-%{pkgname}.debugfiles
%license LICENSES.txt
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname} -f mingw64-python3-%{pkgname}.debugfiles
%license LICENSES.txt
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Sandro Mani <manisandro@gmail.com> - 4.6.2-1
- Update to 4.6.2

* Tue Sep 22 2020 Sandro Mani <manisandro@gmail.com> - 4.5.1-1
- Update to 4.5.1
- Exclude debug files in main package

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 4.4.1-2
- Rebuild (python-3.9)

* Wed Nov 20 2019 Sandro Mani <manisandro@gmail.com> - 4.4.1-1
- Update to 4.4.1
