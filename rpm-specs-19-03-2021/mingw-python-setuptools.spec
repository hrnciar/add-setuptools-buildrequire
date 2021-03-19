%{?mingw_package_header}

%global pkgname setuptools
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       54.1.2
Release:       1%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://pypi.python.org/pypi/%{pkgname}
Source0:       %{pypi_source %{pypi_name} %{version}}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3

# Don't call patch_for_msvc_specialized_compiler, MSVC was not used to compile python
# Hit when running python3.exe get-pip.py
Patch0:        mingw-python-setuptools_no-msvc.patch


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

# Remove bundled exes
rm -f setuptools/*.exe

# Strip shebangs on python modules
find setuptools -name \*.py | xargs sed -i -e '1 {/^#!\//d}'


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}

find %{buildroot}%{mingw32_python3_sitearch}/ -name '*.exe' | xargs rm -f
find %{buildroot}%{mingw64_python3_sitearch}/ -name '*.exe' | xargs rm -f


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/pkg_resources/
%{mingw32_python3_sitearch}/_distutils_hack/
%{mingw32_python3_sitearch}/distutils-precedence.pth
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/pkg_resources/
%{mingw64_python3_sitearch}/_distutils_hack/
%{mingw64_python3_sitearch}/distutils-precedence.pth
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Thu Mar 18 2021 Sandro Mani <manisandro@gmail.com> - 54.1.2-1
- Update to 54.1.2

* Mon Feb 15 2021 Sandro Mani <manisandro@gmail.com> - 53.0.0-2
- Add mingw-python-setuptools_no-msvc.patch

* Thu Feb 04 2021 Sandro Mani <manisandro@gmail.com> - 53.0.0-1
- Update to 53.0.0

* Thu Jan 28 2021 Sandro Mani <manisandro@gmail.com> - 52.0.0-1
- Update to 52.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 51.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Sandro Mani <manisandro@gmail.com> - 51.1.2-1
- Update to 51.1.2

* Wed Dec 30 2020 Sandro Mani <manisandro@gmail.com> - 51.1.1-1
- Update to 51.1.1

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 50.3.2-2
- Switch to py3_build/py3_install macros

* Wed Oct 28 2020 Sandro Mani <manisandro@gmail.com> - 50.3.2-1
- Update to 50.3.2

* Fri Sep 11 2020 Sandro Mani <manisandro@gmail.com> - 50.1.0-1
- Update to 50.1.0

* Thu Aug 27 2020 Sandro Mani <manisandro@gmail.com> - 49.6.0-1
- Update to 49.6.0

* Thu Jul 30 2020 Sandro Mani <manisandro@gmail.com> - 49.1.3-1
- Update to 49.1.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 47.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Sandro Mani <manisandro@gmail.com> - 47.3.1-1
- Update to 47.3.1

* Fri Jun 12 2020 Sandro Mani <manisandro@gmail.com> - 47.1.1-1
- Update to 47.1.1

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 46.4.0-2
- Rebuild (python-3.9)

* Mon May 18 2020 Sandro Mani <manisandro@gmail.com> - 46.4.0-1
- Update to 46.4.0

* Thu May 14 2020 Sandro Mani <manisandro@gmail.com> - 46.2.0-1
- Update to 46.2.0

* Thu Apr 02 2020 Sandro Mani <manisandro@gmail.com> - 46.1.2-1
- Update to 46.1.2

* Fri Mar 13 2020 Sandro Mani <manisandro@gmail.com> - 46.0.0-1
- Update to 46.0.0

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 45.2.0-1
- Update to 45.2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 41.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Sandro Mani <manisandro@gmail.com> - 41.6.0-1
- Update to 41.6.0

* Thu Sep 26 2019 Sandro Mani <manisandro@gmail.com> - 41.2.0-1
- Update to 41.2.0

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 41.0.1-3
- Drop python2 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 41.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 41.0.1-1
- Update to 41.0.1
- Add python3 subpackages

* Wed Feb 06 2019 Sandro Mani <manisandro@gmail.com> - 40.8.0-1
- Update to 40.8.0

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 40.7.3-1
- Update to 40.7.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 40.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Sandro Mani <manisandro@gmail.com> - 40.7.1-1
- Update to 40.7.1

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 40.4.3-1
- Update to 40.4.3

* Thu Sep 20 2018 Sandro Mani <manisandro@gmail.com> - 40.4.1-1
- Update to 40.4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 39.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Sandro Mani <manisandro@gmail.com> - 39.2.0-1
- Update to 39.2.0

* Wed Mar 21 2018 Sandro Mani <manisandro@gmail.com> - 39.0.1-1
- Update to 39.0.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 38.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Sandro Mani <manisandro@gmail.com> - 38.4.0-1
- Update to 38.4.0

* Wed Jan 03 2018 Sandro Mani <manisandro@gmail.com> - 38.2.5-1
- Update to 38.2.5

* Thu Nov 23 2017 Sandro Mani <manisandro@gmail.com> - 37.0.0-1
- Update to 37.0.0

* Tue Sep 05 2017 Sandro Mani <manisandro@gmail.com> - 36.2.0-2
- Remove bundled exes
- Remove shebangs on python modules
- Delete exes underneath site-packages

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 36.2.0-1
- Initial package
