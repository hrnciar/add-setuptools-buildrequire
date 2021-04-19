%{?mingw_package_header}

%global pkgname psycopg2
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2.8.6
Release:       3%{?dist}
BuildArch:     noarch


# The exceptions allow linking to OpenSSL and PostgreSQL's libpq
# LGPLv3+ with exceptions: most files
# BSD: psycopg/adapter*.{h,c} and psycopg/microprotocol*.{h,c}
License:       (LGPLv3+ with exceptions) and BSD
URL:           https://www.psycopg.org/
Source0:       %{pypi_source}

# MinGW build fixes
Patch0:        psycopg2_mingw.patch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-postgresql
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-postgresql
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


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/


%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 09 2020 Sandro Mani <manisandro@gmail.com> - 2.8.6-2
- Fix License and URL, use pypi_source

* Mon Nov 09 2020 Sandro Mani <manisandro@gmail.com> - 2.8.6-1
- Update to 2.8.6

* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 2.8.5-2
- Rebuild (python-3.9)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 2.8.5-1
- Initial package
