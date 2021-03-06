%global _python_bytecompile_extra 0
%global srcname pyqtgraph
%global py3_deps python3-PyQt5 python3-numpy python3-pyopengl

Name:           python-%{srcname}
Version:        0.12.1
Release:        1%{?dist}
Summary:        Scientific Graphics and GUI Library for Python
License:        MIT
URL:            http://www.pyqtgraph.org/
Source0:        %{pypi_source}
# git clone https://github.com/pyqtgraph/test-data
# tar -zcf pyqtgraph-test-data-5498050.tar.gz test-data
Source1:        pyqtgraph-test-data-5498050.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For Docs
BuildRequires:  make %{py3_dist sphinx sphinx_rtd_theme}
# For Tests
BuildRequires:  %{py3_dist h5py pytest scipy six}
BuildRequires:  git-core mesa-dri-drivers xorg-x11-server-Xvfb %{py3_deps}

%global _description %{expand:
PyQtGraph is a pure-python graphics and GUI library built on PyQt4 / PySide and
numpy. It is intended for use in mathematics / scientific /engineering
applications. Despite being written entirely in python, the library is very
fast due to its heavy leverage of numpy for number crunching and Qt\'s
GraphicsView framework for fast display.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       %{py3_deps}

%description -n python3-%{srcname} %_description

%package doc
Summary:        Documentation for the %{srcname} library

%description doc
This package provides documentation for the %{srcname} library.

%prep
%autosetup -p1 -n %{srcname}-%{version}
%setup -T -D -b 1 -n %{srcname}-%{version}
mkdir ~/.pyqtgraph
mv ../test-data ~/.pyqtgraph

%build
%py3_build
make -C doc html

%install
%py3_install
rm -rf %{buildroot}/%{python3_sitelib}/pyqtgraph/examples
rm -f doc/build/html/.buildinfo
rm -f doc/build/html/objects.inv

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 xvfb-run -a py.test-%{python3_version} -k "not (test_reload)"

%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGELOG README.md
%{python3_sitelib}/*

%files doc
%doc examples doc/build/html

%changelog
* Sat Apr 10 2021 Scott Talbert <swt@techie.net> - 0.12.1-1
- Update to new upstream release 0.12.1 (#1946852)

* Sat Mar 27 2021 Scott Talbert <swt@techie.net> - 0.12.0-3
- BR setuptools

* Fri Mar 26 2021 Scott Talbert <swt@techie.net> - 0.12.0-2
- Apply upstream patch for Python 3.10 fixes (#1901925)

* Thu Mar 25 2021 Scott Talbert <swt@techie.net> - 0.12.0-1
- Update to new upstream release 0.12.0 (#1943345)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 13:59:44 EST 2020 Scott Talbert <swt@techie.net> - 0.11.1-1
- Update to new upstream release 0.11.1 (#1909448)

* Thu Nov 26 10:00:39 EST 2020 Scott Talbert <swt@techie.net> - 0.11.0-1
- Update to new upstream release (#1901997)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.10.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Scott Talbert <swt@techie.net> - 0.10.0-13
- Fix FTBFS with Python 3.9 (#1792947)

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.10.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.10.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Scott Talbert <swt@techie.net> - 0.10.0-8
- Disable writing bytecode when running tests to avoid packaging pycache files

* Thu Sep 13 2018 Scott Talbert <swt@techie.net> - 0.10.0-7
- Indicate that we don't want to bytecompile the extra python files

* Tue Sep 11 2018 Scott Talbert <swt@techie.net> - 0.10.0-6
- Remove Python 2 subpackage (appears to be unused)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.10.0-4
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Scott Talbert <swt@techie.net> - 0.10.0-3
- Disable additional tests that only fail under Koji, fixes FTBFS (#1556569)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jul 30 2017 Scott Talbert <swt@techie.net> - 0.10.0-1
- New upstream release 0.10.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 0.9.10-12
- Rebuild for Python 3.6

* Wed Jul 20 2016 Scott Talbert <swt@techie.net> - 0.9.10-11
- De-fuzz the disable-failing-tests patch to fix F25 FTBFS

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 01 2016 Scott Talbert <swt@techie.net> - 0.9.10-9
- Update dependency names

* Sat Feb 06 2016 Scott Talbert <swt@techie.net> - 0.9.10-8
- Cherry-pick a couple of upstream patches to fix test failures on F24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Scott Talbert <swt@techie.net> - 0.9.10-6
- Remove pytest path patch on F23+ - fixes FTBFS with Python 3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug 07 2015 Scott Talbert <swt@techie.net> - 0.9.10-4
- Moved documentation to subpackage

* Tue Aug 04 2015 Scott Talbert <swt@techie.net> - 0.9.10-3
- Fix and run tests, move examples to docs, add docs

* Sun Aug 02 2015 Scott Talbert <swt@techie.net> - 0.9.10-2
- Build python2 package also; update to latest python packaging standards

* Fri Jul 31 2015 Scott Talbert <swt@techie.net> 0.9.10-1
- Initial packaging.
