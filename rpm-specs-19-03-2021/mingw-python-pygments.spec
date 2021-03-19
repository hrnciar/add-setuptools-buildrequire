%{?mingw_package_header}

%global pkgname pygments
%global pypi_name Pygments

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname}
Version:       2.8.1
Release:       1%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://pygments.org/
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
%{mingw32_bindir}/pygmentize
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_bindir}/pygmentize
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw64_python3_version}.egg-info/


%changelog
* Sun Mar 14 2021 Sandro Mani <manisandro@gmail.com> - 2.8.1-1
- Update to 2.8.1

* Thu Feb 04 2021 Sandro Mani <manisandro@gmail.com> - 2.7.4-1
- Update to 2.7.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Sandro Mani <manisandro@gmail.com> - 2.7.2-1
- Update to 2.7.2

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 2.7.1-1
- Update to 2.7.1

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 2.6.1-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2.6.1-1
- Initial package
