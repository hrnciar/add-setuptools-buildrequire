%{?mingw_package_header}

%global pkgname certifi
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2020.12.5
Release:       2%{?dist}
BuildArch:     noarch

License:       MPL2.0
URL:           https://certifi.io/en/latest/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname}.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


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
%{mingw32_python3_sitearch}/%{pkgname}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pkgname}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Sandro Mani <manisandro@gmail.coM> - 2020.12.5-1
- Update to 2020.12.5

* Wed Nov 11 2020 Sandro Mani <manisandro@gmail.com> - 2020.11.08-1
- Update to 2020.11.08

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 2020.06.20-2
- Switch to py3_build/py3_install macros

* Sat Aug 15 2020 Sandro Mani <manisandro@gmail.com> - 2020.06.20-1
- Update to 2020.06.20

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.05.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 2020.04.05.1-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2020.04.05.1-1
- Update to 2020.04.05.1

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 2019.11.28-1
- Initial package
