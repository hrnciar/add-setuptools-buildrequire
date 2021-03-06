%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name XStatic-Angular-FileUpload

Name:           python-%{pypi_name}
Version:        12.0.4.0
Release:        18%{?dist}
Summary:        Angular-FileUpload JavaScript library (XStatic packaging standard)

License:        MIT
URL:            https://github.com/danialfarid/ng-file-upload
Source0:        https://pypi.python.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# PyPi source states License: (same as Angular-FileUpload)
Source1:        https://raw.githubusercontent.com/danialfarid/ng-file-upload/master/LICENSE
BuildArch:      noarch

%description
Angular-FileUpload JavaScript library packaged
for setuptools (easy_install) / pip.

Lightweight Angular directive to upload files.

%if %{with python2}
%package -n python2-%{pypi_name}
Summary: Angular-FileUpload JavaScript library (XStatic packaging standard)
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires:       python2-XStatic
Requires:       xstatic-angular-fileupload-common

%description -n python2-%{pypi_name}
Angular-FileUpload JavaScript library packaged
for setuptools (easy_install) / pip.

Lightweight Angular directive to upload files.
%endif

%package -n xstatic-angular-fileupload-common
Summary: Angular-FileUpload (XStatic packaging standard) JavaScript library

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-fileupload-common
Angular-FileUpload JavaScript library packaged
for setuptools (easy_install) / pip.

This package contains the javascript files.

%if %{with python3}
%package -n python3-%{pypi_name}
Summary: Angular-FileUpload JavaScript library (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-fileupload-common

%description -n python3-%{pypi_name}
Angular-FileUpload JavaScript library packaged
for setuptools (easy_install) / pip.

Lightweight Angular directive to upload files.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} .

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_fileupload'|" xstatic/pkg/angular_fileupload/__init__.py

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%{__python2} setup.py install --skip-build --root %{buildroot}

# Move static files
mkdir -p %{buildroot}/%{_jsdir}/angular_fileupload
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_fileupload/data/* %{buildroot}/%{_jsdir}/angular_fileupload/
rmdir %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_fileupload/data/
%endif

%if %{with python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
# Move static files
mkdir -p %{buildroot}/%{_jsdir}/angular_fileupload
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_fileupload/data/* %{buildroot}/%{_jsdir}/angular_fileupload/
rmdir %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_fileupload/data/
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.txt
%license LICENSE
%{python2_sitelib}/xstatic/pkg/angular_fileupload
%{python2_sitelib}/XStatic_Angular_FileUpload-%{version}-py?.?.egg-info
%{python2_sitelib}/XStatic_Angular_FileUpload-%{version}-py?.?-nspkg.pth
%endif

%files -n xstatic-angular-fileupload-common
%doc README.txt
%license LICENSE
%{_jsdir}/angular_fileupload

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.txt
%license LICENSE
%{python3_sitelib}/xstatic/pkg/angular_fileupload
%{python3_sitelib}/XStatic_Angular_FileUpload-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_Angular_FileUpload-%{version}-py%{python3_version}-nspkg.pth
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 12.0.4.0-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 12.0.4.0-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 12.0.4.0-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Javier Pe??a <jpena@redhat.com> - 12.0.4.0-9
- Removed Python 2 package from Fedora 30+ (bz#1630333)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 12.0.4.0-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 12.0.4.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 12.0.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 24 2016 Javier Pe??a <jpena@redhat.com> - 12.0.4.0-1
- Updated to upstream version 12.0.4.0

* Mon May 23 2016 Javier Pe??a <jpena@redhat.com> - 1.4.0.1-2
- Updated path for javascript file

* Fri May 20 2016 Javier Pe??a <jpena@redhat.com> - 1.4.0.1-1
- First version
