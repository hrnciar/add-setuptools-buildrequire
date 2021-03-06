%global srcname Werkzeug
%global modname werkzeug

Name:           python-%{modname}
Version:        1.0.1
Release:        4%{?dist}
Summary:        Comprehensive WSGI web application library

License:        BSD
URL:            https://werkzeug.palletsprojects.com
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Werkzeug
========

Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).}

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
# Makes tests unreliable
#BuildRequires:  python3dist(pytest-xprocess)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-unixsocket)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(greenlet)

%description -n python3-%{modname} %{_description}

%package -n python3-werkzeug-doc
Summary:        Documentation for python3-werkzeug
%{?python_provide:%python_provide python3-werkzeug-doc}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pallets-sphinx-themes)
BuildRequires:  python3dist(sphinx-issues)
BuildRequires:  python3dist(sphinxcontrib-log-cabinet)
Requires:       python3-werkzeug = %{version}-%{release}

%description -n python3-werkzeug-doc
Documentation and examples for python3-werkzeug.


%prep
%autosetup -p1 -n %{srcname}-%{version}
find examples/ -type f -name '*.png' -executable -print -exec chmod -x "{}" +

%build
%py3_build
pushd docs
make PYTHONPATH=../src/ SPHINXBUILD=sphinx-build-3 html
rm -v _build/html/.buildinfo
popd

%install
%py3_install

%check
PYTHONPATH=./src/ pytest-3

%files -n python3-%{modname}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%files -n python3-werkzeug-doc
%doc docs/_build/html examples

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.9

* Wed Apr 08 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Lum??r Balhar <lbalhar@redhat.com> - 0.16.0-1
- New upstream version 0.16.0 (#1690599)

* Wed Sep 18 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.14.1-12
- Subpackage python2-werkzeug has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.14.1-11
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Petr Viktorin <pviktori@redhat.com> - 0.14.1-10
- Remove non-essential Python 2 test dependencies
  https://fedoraproject.org/wiki/Changes/F31_Mass_Python_2_Package_Removal#Removing_Requirements
- Use system Python interpreter in tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.14.1-8
- Remove python2-werkzeug-doc
  https://fedoraproject.org/wiki/Changes/Sphinx2

* Sun Feb 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14.1-7
- Backport fix to tests using 'python' command

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.14.1-5
- Make sure we ship Python 3 docs in the Python 3 docs package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.14.1-3
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.14.1-2
- Don't BR watchdog, it is not needed

* Wed May 09 2018 Adam Williamson <awilliam@redhat.com> - 0.14.1-1
- Update to 0.14.1 (needed by httpbin)
- Run tests during build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Charalampos Stratakis <cstratak@redhat.com> - 0.12.2-1
- Update to 0.12.2

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.11.10-8
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.10-7
- Python 2 binary package renamed to python2-werkzeug
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.11.10-4
- Rebuild for Python 3.6

* Tue Dec 13 2016 Tomas Orsava <torsava@redhat.com> - 0.11.10-3
- Fixed the building of documentation

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.10-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 28 2016 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 0.11.10-1
- Upstream 0.11.19
- Fix unicode issues with python3

* Thu Apr 14 2016 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 0.11.6-1
- Upstream 0.11.6 (upstream #822)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 0.10.4-3
- Rebuilt for Python3.5 rebuild
- Add werkzeug sphinx theme as a Source1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Ricky Elrod <relrod@redhat.com> - 0.10.4-1
- Upstream 0.10.4.

* Fri Jul 18 2014 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 0.9.6-1
- Upstream 0.9.6
- Fixes RHBZ #1105819

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug 26 2013 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 0.9.4-1
- Upstream 0.9.4

* Thu Jul 25 2013 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 0.9.3-1
- Upstream 0.9.3

* Tue Jul 23 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.9.2-1
- Upstream 0.9.2 release.

* Sat Jun 15 2013 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 0.9.1-1
- upstream 0.9.1
- add python3 flavor

* Fri Jun 14 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.9-1
- Upstream 0.9.0 release.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb  5 2012 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 0.8.3-1
- upstream 0.8.3 (fixes XSS security issues)

* Wed Jan 25 2012 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 0.8.2-1
- upstream 0.8.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.2-1
- Updating because upstream release of Werkzeug 0.6.2

* Fri Mar 05 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6-1
- Updating because upstream release of Werkzeug 0.6

* Tue Aug 25 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.5.1-1
- Initial package
