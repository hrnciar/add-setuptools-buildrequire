%{?python_enable_dependency_generator}

%if 0%{?rhel} == 7
%bcond_with    python3
%bcond_without python2
%else
%bcond_with    python2
%bcond_without python3
%endif

%if 0%{?rhel} == 7
%global py3 python%{python3_pkgversion}
%global py3dev python%{python3_pkgversion}
Patch0:     python-kubernetes-el7.patch
%endif
%if 0%{?rhel} == 8
%global py3 python3
%global py3dev python36
%endif
%if 0%{?fedora}
%global py3 python3
%global py3dev python3
%endif

%global library kubernetes
%global basehash d30f1e6fd4e2725aae04fa2f4982a4cfec7c682b

Name:       python-%{library}
Epoch:      1
Version:    11.0.0
Release:    7%{?dist}
Summary:    Python client for the kubernetes API.
License:    ASL 2.0
URL:        https://pypi.python.org/pypi/kubernetes

Source0:    https://github.com/kubernetes-client/python/archive/v%{version}.tar.gz
Source1:    https://github.com/kubernetes-client/python-base/archive/%{basehash}.tar.gz
BuildArch:  noarch

%if 0%{?with_python2}
%package -n python2-%{library}
Summary:    Kubernetes Python Client
%{?python_provide:%python_provide python2-%{library}}
BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?rhel} != 7
Requires:  python-adal
%endif
Requires:  python-certifi
Requires:  python-six
Requires:  python-dateutil
Requires:  python-setuptools
Requires:  python-urllib3
Requires:  PyYAML
Requires:  python-google-auth
Requires:  python-ipaddress
Requires:  python-websocket-client
Requires:  python-requests
Requires:  python-requests-oauthlib

%description -n python2-%{library}
Python client for the kubernetes API.

%package -n python2-%{library}-tests
Summary:    Tests python-kubernetes library

Requires:  python-nose
Requires:  python-py
Requires:  python-mock
Requires:  python2-%{library} = 1:%{version}-%{release}

%description -n python2-%{library}-tests
Tests python-kubernetes library
%endif

%if 0%{?with_python3}
%package -n %{py3}-%{library}
Summary:    Kubernetes Python Client
BuildRequires:  git
BuildRequires:  %{py3dev}-devel
BuildRequires:  %{py3dev}-rpm-macros
BuildRequires:  %{py3}-setuptools 
%if %{undefined __pythondist_requires}
%if 0%{?fedora}
Requires:  %{py3}-adal
%endif
Requires:  %{py3}-certifi
Requires:  %{py3}-six
Requires:  %{py3}-dateutil
Requires:  %{py3}-setuptools 
Requires:  %{py3}-urllib3
Requires:  %{py3}-PyYAML
Requires:  %{py3}-google-auth
Requires:  %{py3}-websocket-client
%endif

%description -n %{py3}-%{library}
Python client for the kubernetes API.

%package -n %{py3}-%{library}-tests
Summary:    Tests python-kubernetes library

Requires:  %{py3}-nose
Requires:  %{py3}-py
Requires:  %{py3}-mock
Requires:  %{py3}-%{library} = 1:%{version}-%{release}

%description -n %{py3}-%{library}-tests
Tests python-kubernetes library

%endif

#recommonmark not available for docs in EPEL
%if 0%{?fedora}
%package doc
Summary: Documentation for %{name}.
Provides: %{name}-doc = 1:%{version}-%{release}
%if 0%{?with_python3}
BuildRequires: %{py3}-sphinx
BuildRequires: %{py3}-recommonmark
%else
BuildRequires: python2-sphinx
BuildRequires: python2-recommonmark
%endif
%description doc
%{summary}
%endif

%description
Python client for the kubernetes API.

%prep
%autosetup -n python-%{version} -S git

#This is needed until CentOS 8.1. The dep was
#updated because of a CVE in urllib3 and the
#corresponding package update is in EL 8.1
%if 0%{?rhel} == 8
sed -i 's/1.24.2/1.23/g' requirements.txt
%endif

#BZ1758141 - python autorequires do not handles asterisks properly.
#Fedora is using 0.56.0+ since at least Fedora 31 so this works aorund
#the issue by setting the minimum version above the problem versions.
%if 0%{?fedora} > 30
sed -i 's/websocket-client.*/websocket-client>=0.43.0/g' requirements.txt
%endif

pushd kubernetes
rm -rf base
tar zxvf %{SOURCE1}
mv python-base-%{basehash} base
popd

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

#11.0 adds spinx-markdown-tables as a requirement
#It is not packaged in Fedora
#%if 0%{?fedora}
#sphinx-build doc/source/ html
#%{__rm} -rf html/.buildinfo
#%endif

# Currently recommonmark requires an old version of commonmark,
# commonmark (<=0.5.4) wich doesn't exist in fedora rawhide so
# we disable docs generation until recommonmark is fixed to be
# compatible with recent version.
# generate html docs
# {__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?with_python2}
%py2_install
cp -pr kubernetes/test %{buildroot}%{python2_sitelib}/%{library}/
cp -pr kubernetes/e2e_test %{buildroot}%{python2_sitelib}/%{library}/
%endif
%if 0%{?with_python3}
%py3_install
cp -pr kubernetes/test %{buildroot}%{python3_sitelib}/%{library}/
cp -pr kubernetes/e2e_test %{buildroot}%{python3_sitelib}/%{library}/
%endif

%check

%if 0%{?with_python2}
%files -n python2-%{library}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{library}
%{python2_sitelib}/%{library}-*.egg-info
%exclude %{python2_sitelib}/%{library}/test
%exclude %{python2_sitelib}/%{library}/e2e_test

%files -n python2-%{library}-tests
%license LICENSE
%{python2_sitelib}/%{library}/test
%{python2_sitelib}/%{library}/e2e_test
%endif

%if 0%{?fedora}
%files doc
%license LICENSE
#%doc html
%endif

%if 0%{?with_python3}
%files -n %{py3}-%{library}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{library}
%{python3_sitelib}/%{library}-*.egg-info
%exclude %{python3_sitelib}/%{library}/test
%exclude %{python3_sitelib}/%{library}/e2e_test

%files -n %{py3}-%{library}-tests
%license LICENSE
%{python3_sitelib}/%{library}/test
%{python3_sitelib}/%{library}/e2e_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Jason Montleon <jmontleo@redhat.com> - 1:11.0.0-6
- Fix sub-package requirements to account for the epoch

* Fri Dec 11 2020 Jason Montleon <jmontleo@redhat.com> - 1:11.0.0-5
- Revert upadte until https://github.com/kubernetes-client/python/issues/1333 is fixed

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 11.0.0-3
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Jason Montleon <jmontleo@redhat.com> - 11.0.0-2
- Fix EPEL 7 and 8 builds

* Thu Apr 30 2020 Jason Montleon <jmontleo@redhat.com> - 11.0.0-1
- Update to 11.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
- Work around BZ1758141 for BZ1799937

* Fri Nov 08 2019 Jason Montleon <jmontleo@redhat.com> 10.0.1-1
- Update to upstream 10.0.1

* Fri Oct 18 2019 Jason Montleon <jmontleo@redhat.com> 9.0.1-1
- Update to upstream 9.0.1

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 8.0.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 8.0.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Jason Montleon <jmontleo@redhat.com> 8.0.1-1
- Update to upstream 8.0.1

* Sat Feb 2 2019 Jason Montleon <jmontleo@redhat.com> 8.0.0-8
- add upstream patch to make python-adal optional
- remove python-adal requires for EL7 since it's not available in RHEL base, optional, or extras

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jason Montleon <jmontleo@redhat.com> 8.0.0-6
- Only apply EL7 requirement patch on EL7 so Fedora dependency generator works correctly

* Thu Jan 17 2019 Jason Montleon <jmontleo@redhat.com> 8.0.0-5
- Keep python 2 enabled for Fedora 29.

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.0.0-4
- Enable python dependency generator

* Fri Dec 14 2018 Jason Montleon <jmontleo@redhat.com> 8.0.0-3
- Default to python 2 for EPEL 7 and python 3 for Fedora
- Add docs package for Fedora

* Mon Nov 26 2018 Jason Montleon <jmontleo@redhat.com> 8.0.0-2
- Patch setup.py to work with EL7 python-setuptools

* Mon Nov 5 2018 Jason Montleon <jmontleo@redhat.com> 8.0.0-1
- Update to 8.0.0

* Wed Oct 3 2018 Jason Montleon <jmontleo@redhat.com> 7.0.0-3
- Adding missing python3-adal dependency

* Wed Oct 3 2018 Jason Montleon <jmontleo@redhat.com> 7.0.0-2
- Adding missing python-adal dependency

* Wed Oct 3 2018 Jason Montleon <jmontleo@redhat.com> 7.0.0-1
- Update to 7.0.0

* Tue Feb 28 2017 Alfredo Moralejo <amoralej@redhat.com> 1.0.0-0.3.0b3
- Remove BRs for documentation building as it's not creating html docs.

* Mon Feb 27 2017 Alfredo Moralejo <amoralej@redhat.com> 1.0.0-0.2.0b3
- Fixed files section of python3-kubernetes-tests to contain python3 tests.

* Mon Feb 27 2017 Alfredo Moralejo <amoralej@redhat.com> 1.0.0-0.1.0b3
- Initial spec for release 1.0.0b3
