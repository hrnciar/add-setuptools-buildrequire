# Created by pyp2rpm-1.0.1
%global pypi_name pymemcache

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        1%{?dist}
Summary:        A comprehensive, fast, pure Python memcached client

License:        ASL 2.0
URL:            https://github.com/Pinterest/pymemcache
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0001:      0001-Skip-unit-tests-resolving-domain-names.patch
BuildArch:      noarch

%global _description\
pymemcache supports the following features:\
\
* Complete implementation of the memcached text protocol.\
* Configurable timeouts for socket connect and send/recv calls.\
* Access to the "noreply" flag, which can significantly increase the speed of\
  writes.\
* Flexible, simple approach to serialization and deserialization.\
* The (optional) ability to treat network and memcached errors as cache misses.

%description %_description


%package -n python3-%{pypi_name}
Summary:        A comprehensive, fast, pure Python memcached client
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
Requires:       python3-six

%description -n python3-%{pypi_name}
pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the speed of
  writes.
* Flexible, simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache misses.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

%install
%py3_install

%check
py.test-3 ./pymemcache/test/

%files -n python3-%{pypi_name}
%doc README.rst LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Feb 01 2021 Joel Capitao <jcapitao@redhat.com> - 3.4.0-1
- Update to 3.4.0 (#1163328)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Joel Capitao <jcapitao@redhat.com> - 3.3.0-1
- Update to 3.3.0
- Remove Python 2 subpackage

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.1.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.1.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Alfredo Moralejo <amoralej@redhat.com> - 2.1.1-2
- Add python2-future as BR for unit tests in python2.

* Mon Feb 11 2019 Javier Pe??a <jpena@redhat.com> - 2.1.1-1
- Updated to upstream 2.1.1
- Re-introduced python2 subpackage for EL7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.5-15
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.2.5-13
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.5-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.5-10
- Python 2 binary package renamed to python2-pymemcache
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 1.2.5-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 11 2014 Nejc Saje <nsaje@redhat.com> - 1.2.5-2
- Added six to build dependencies, needed during tests

* Tue Sep 09 2014 Nejc Saje <nsaje@redhat.com> - 1.2.5-1
- Initial package.

