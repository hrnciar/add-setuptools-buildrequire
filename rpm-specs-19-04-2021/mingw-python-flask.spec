%{?mingw_package_header}

%global pkgname flask
%global pypi_name Flask

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       1.1.2
Release:       5%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://palletsprojects.com/p/itsdangerous/
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
Requires:      mingw32-python3-click
Requires:      mingw32-python3-itsdangerous
Requires:      mingw32-python3-jinja2
Requires:      mingw32-python3-werkzeug

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}
Requires:      mingw64-python3-click
Requires:      mingw64-python3-itsdangerous
Requires:      mingw64-python3-jinja2
Requires:      mingw64-python3-werkzeug

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
%license LICENSE.rst
%{mingw32_bindir}/%{pkgname}
%{mingw32_python3_sitearch}/%{pkgname}
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info


%files -n mingw64-python3-%{pkgname}
%license LICENSE.rst
%{mingw64_bindir}/%{pkgname}
%{mingw64_python3_sitearch}/%{pkgname}
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 1.1.2-4
- Switch to py3_build/py3_install macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.1.2-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Wed Oct 30 2019 Sandro Mani <manisandro@gmail.com> - 1.1.1-1
- Update to 1.1.1
- Switch to python3

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 0.11.1-1
- Initial package
