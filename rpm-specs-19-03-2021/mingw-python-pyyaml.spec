%{?mingw_package_header}

%global pkgname pyyaml
%global pypi_name PyYAML

Name:          mingw-python-%{pkgname}
Version:       5.3.1
Release:       2%{?dist}
Summary:       MinGW Windows Python %{pkgname}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/yaml/pyyaml
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname}.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python2 %{pkgname}

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python2 %{pkgname}.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python2 %{pkgname}

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python2 %{pkgname}.


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
%{mingw32_python3_sitearch}/yaml/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/yaml/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 5.3.1-2
- Update to 5.3.1

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 5.1.2-2
- Rebuild (python-3.9)

* Sun Nov 03 2019 Sandro Mani <manisandro@gmail.com> - 5.1.2-1
- Update to 5.1.2

* Mon Apr 29 2019 Sandro Mani <manisandro@gmail.com> - 5.1-1
- Initial package
