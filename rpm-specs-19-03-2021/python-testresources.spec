%global pypi_name testresources

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        2%{?dist}
Summary:        Testresources, a pyunit extension for managing expensive test resources

License:        ASL 2.0 and BSD and GPLv2+
# file testresources/tests/TestUtil.py is GPLv2+
URL:            https://launchpad.net/testresources
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%package -n python3-%{pypi_name}
Summary:        Testresources, a pyunit extension for managing expensive test resources
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-testtools
BuildRequires: python3-fixtures

%description -n python3-%{pypi_name}
testresources: extensions to python unittest to allow declarative use
of resources by test cases.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf lib/%{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%doc README.rst NEWS doc
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Joel Capitao <jcapitao@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-11
- Subpackage python2-testresources has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb  8 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0.0-6
- Use versioned macros

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 18 2016 Matthias Runge <mrunge@redhat.com> - 1.0.0-1
- update to 1.0.0 (rhbz#1309577)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Matthias Runge <mrunge@redhat.com> - 0.2.7-3
- lice
* Fri May 31 2013 Matthias Runge <mrunge@redhat.com> - 0.2.7-2
- spec cleanups, added NEWS, doc/ to doc, really removed bundled egg-info

* Wed May 29 2013 Matthias Runge <mrunge@redhat.com> - 0.2.7-1
- Initial package.
