%global srcname lazy-object-proxy
%global sum A fast and thorough lazy object proxy

Name:           python-%{srcname}
Version:        1.6.0
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD
Url:            https://github.com/ionelmc/python-%{srcname}
Source0:        https://github.com/ionelmc/python-%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

Patch0:         scmver.patch

BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm

%description
A fast and thorough lazy object proxy.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
A fast and thorough lazy object proxy.


%prep
%autosetup -n python-%{srcname}-%{version} -p0

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/*
%attr(0755, root, root) %{python3_sitearch}/lazy_object_proxy/*.so
%exclude %{python3_sitearch}/lazy_object_proxy/cext.c

%changelog
* Wed Mar 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-2
- Patch for setuptools-scm >=6.0

* Mon Mar 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-1
- 1.6.0

* Tue Feb 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-3
- Drop scm-deversion patch

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-1
- 1.5.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.1-1
- 1.5.1

* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-1
- 1.5.0

* Sat May 23 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.4.3-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.3-2
- Allow build with EL-8 version of setuptools.

* Sun Oct 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.3-1
- 1.4.3

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Brian C. Lane <bcl@redhat.com> - 1.4.2-1
- New upstream version 1.4.2

* Fri Aug 16 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.3.1-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.3.1-8
- Subpackage python2-lazy-object-proxy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.3.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Christian Dersch <lupinix@mailbox.org> - 1.3.1-1
- new version

* Thu Mar 09 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-1
- Update to 1.2.2
- Enable build for EPEL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.2.1-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Brian C. Lane <bcl@redhat.com> 1.2.1-2
- Fix the permissions on the cext.so file

* Tue Dec 01 2015 Brian C. Lane <bcl@redhat.com> 1.2.1-1
- Initial creation

