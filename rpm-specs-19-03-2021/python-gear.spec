%global owner openstack-infra
%global srcname gear

Name: python-%{srcname}
Version: 0.15.1
Release: 6%{?dist}
Summary: Pure Python Async Gear Protocol Library

License: ASL 2.0
URL: https://opendev.org/opendev/%{srcname}
Source0: %pypi_source

Patch01: 0001-Bump-crypto-requirement-to-accomodate-security-stand.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-pbr

# Test requirements
BuildRequires: python3-pyOpenSSL
BuildRequires: python3-fixtures
BuildRequires: python3-statsd
BuildRequires: python3-testrepository
BuildRequires: python3-testresources
BuildRequires: python3-testscenarios

%global _description\
python-gear implements an asynchronous event-driven interface to Gearman.\
It provides interfaces to build a client or worker, and access to the\
administrative protocol. The design approach is to keep it simple, with a\
relatively thin abstraction of the Gearman protocol itself. It should be\
easy to use to build a client or worker that operates either synchronously\
or asynchronously. The module also provides a simple Gearman server for\
use as a convenience in unit tests. The server is not designed for\
production use under load.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
PYTHON=%{__python3} %{__python3} setup.py testr

%files -n python3-%{srcname}
%doc README.rst CONTRIBUTING.rst doc
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Faben Boucher <fboucher@redhat.com> - 0.15.1-5
- Remove BuildRequire on git
- Let runtime deps to be discovered out from requierements.txt

* Tue Jul 30 2020 Faben Boucher <fboucher@redhat.com> - 0.15.1-4
- Fix FTBFS by providing upstream patch
  0001-Bump-crypto-requirement-to-accomodate-security-stand.patch

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.15.1-2
- Rebuilt for Python 3.9

* Mon Mar 09 2020 Faben Boucher <fboucher@redhat.com> - 0.15.1-1
- Bump to 0.15.1

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.14.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.14.0-5
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.14.0-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.14.0-3
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.14.0-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Fabien Boucher <fboucher@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Tue Jul 30 2019 Fabien Boucher <fboucher@redhat.com> - 0.13.0-1
- Update to 0.13.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.0-7
- Subpackage python2-gear has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.11.0-5
- Rebuilt for Python 3.7

* Fri Apr 6 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11.0-4
- Package the executable in python3 package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Dec 29 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.11.0-1
- Update version (#1529648)
- Add python3 package

* Sat Aug 19 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.9-7
- Python 2 binary package renamed to python2-gear
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Fabien Boucher <fboucher@redhat.com> - 0.5.9-4
- Fix bogus release version inconsistency

* Thu Sep 22 2016 Fabien Boucher <fboucher@redhat.com> - 0.5.9-3
- Remove useless dependencies to python-argparse

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 16 2016 Paul Belanger <pabelanger@redhat.com> - 0.5.9-1
- New upstream 0.5.9 (#1304141)
- Update spec to latest python packaging guidelines
- Enable unit testing

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Fabien Boucher <fboucher@redhat.com> - 0.5.8-1
- Bump gear source to version 0.5.8
- Add python-pbr as dependency as demo geard needs it

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Fabien Boucher <fboucher@redhat.com> - 0.5.7-1
- Bump gear source to version 0.5.7
- Remove dist version in changelog
- Fix license handling

* Thu Apr 23 2015 Fabien Boucher <fboucher@redhat.com> - 0.5.6-0
- Initial packaging
