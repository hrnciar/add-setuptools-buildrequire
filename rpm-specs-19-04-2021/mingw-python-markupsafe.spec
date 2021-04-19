%{?mingw_package_header}

%global pkgname markupsafe
%global pypi_name MarkupSafe

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       1.1.1
Release:       4%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://pypi.org/project/MarkupSafe/
Source0:       %pypi_source

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-python3
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

# C code errantly gets installed
rm %{buildroot}%{mingw32_python3_sitearch}/markupsafe/*.c
rm %{buildroot}%{mingw64_python3_sitearch}/markupsafe/*.c

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-python3-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%license LICENSE.rst
%{mingw32_python3_sitearch}/markupsafe/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%license LICENSE.rst
%{mingw64_python3_sitearch}/markupsafe/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 1.1.1-3
- Switch to py3_build/py3_install macros

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.1.1-2
- Rebuild (python-3.9)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.1.1-1
- Initial package
