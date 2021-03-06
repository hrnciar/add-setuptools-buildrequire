# Tests are disbaled by default, they require:
#  a) tested tox to be installed
#  b) internet connection
# To test, do the following:
#  1) Build --without tests (the default)
#     (e.g. fedpkg mockbuild)
#  2) Install the built package
#     (e.g. mock install ./results_python-tox/.../python3-tox-...rpm)
#  3) Build again --with tests (and internet connection)
#     (e.g. fedpkg mockbuild --enable-network --no-clean-all --with tests)
# The Fedora CI tests do this.
%bcond_with tests

Name:           python-tox
Version:        3.21.4
Release:        1%{?dist}
Summary:        Virtualenv-based automation of test activities

License:        MIT
URL:            https://tox.readthedocs.io/
Source0:        %{pypi_source tox}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  /usr/bin/gcc
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/pip
BuildRequires:  /usr/bin/poetry
BuildRequires:  /usr/bin/pytest
BuildRequires:  /usr/bin/python
BuildRequires:  libffi-devel
# The tests only work if the tested tox is installed :(
BuildRequires:  tox = %{version}-%{release}
%endif

%global _description %{expand:
Tox as is a generic virtualenv management and test command line tool you
can use for:

 - checking your package installs correctly with different Python versions
   and interpreters
 - running your tests in each of the environments, configuring your test tool
   of choice
 - acting as a frontend to Continuous Integration servers, greatly reducing
   boilerplate and merging CI and shell-based testing.}

%description %_description


%package -n tox
Summary:        %{summary}

# Recommend "all the Pythons"
# Why? Tox exists to enable developers to test libraries against various Python
# versions, with just "dnf install tox" and a config file.
# See: https://developer.fedoraproject.org/tech/languages/python/python-installation.html#using-virtualenv
# Tox itself runs on the system python3 (i.e. %%{python3_version},
# however it launches other Python versions as subprocesses.
# It recommends all Python versions it supports. (This is an exception to
# the rule that Fedora packages may not require the alternative interpreters.)
Recommends:     python2.7
Recommends:     python3.5
Recommends:     python3.6
Recommends:     python3.7
Recommends:     python3.8
Recommends:     python3.9
Recommends:     pypy2-devel
Recommends:     pypy3-devel
Recommends:     python2-devel
Recommends:     python3-devel

# Replace detox (no longer supported, functionality is now in tox)
# Remove this once Fedora 32 goes EOL
Obsoletes:      python3-detox < 0.19-5

%py_provides    python3-tox
# Remove this once Fedora 36 goes EOL:
Obsoletes:      python3-tox < 3.21.0-2

%description -n tox %_description


%prep
%autosetup -p1 -n tox-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x testing}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tox


%if %{with tests}
%check
%pytest -n auto
%endif


%files -n tox -f %{pyproject_files}
%{_bindir}/tox
%{_bindir}/tox-quickstart


%changelog
* Tue Feb 02 2021 Miro Hron??ok <mhroncok@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Miro Hron??ok <mhroncok@redhat.com> - 3.21.0-2
- Rename the installable package to "tox"

* Fri Jan 08 2021 Miro Hron??ok <mhroncok@redhat.com> - 3.21.0-1
- Update to 3.21.0

* Mon Sep 07 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.20.0-1
- Update to 3.20.0
- Fixes rhbz#1874601

* Fri Aug 07 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.19.0-1
- Update to 3.19.0
- Fixes rhbz#1861313

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Fixes rhbz#1859875

* Tue Jul 14 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.17.0-1
- Update to 3.17.0
- Fixes rhbz#1856985

* Thu Jul 09 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.16.1-1
- Update to 3.16.1
- Fixes rhbz#1851519

* Mon Jun 08 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.15.2-1
- Update to 3.15.2 (#1844689)

* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.15.1-1
- Update to 3.15.1 (#1838137)

* Sat May 23 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.15.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.15.0-1
- Update to 3.15.0
- Stop recommending Python 3.4

* Thu Mar 19 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.14.6-1
- Update to 3.14.6

* Thu Feb 06 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.14.3-1
- Update to 3.14.3 (#1725939)
- Fix invocation with Python 3.9 (#1798929)
- Recommend Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.13.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.13.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.13.2-1
- Update to 3.13.2 (#1699032)

* Tue Apr 30 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.9.0-1
- Update to 3.9.0
- Obsolete detox
- License is MIT

* Fri Feb 15 2019 Lum??r Balhar <lbalhar@redhat.com> - 3.5.3-3
- Recommend Python 3.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Artem Goncharov <artem.goncharov@gmail.com> - 3.5.3-1
- Upgrade to 3.5.3 version

* Mon Nov 19 2018 Artem Goncharov <artem.goncharov@gmail.com> - 3.4.0-1
- Upgrade to 3.4.0 version (#1652657)

* Thu Nov 01 2018 Matthias Runge <mrunge@redhat.com> - 3.0.0-6
- remove and revert the change to recommend python 2.7 (rhbz#1645025)

* Tue Aug 28 2018 Miro Hron??ok <mhroncok@redhat.com> - 3.0.0-4
- Don't recommend Python 2.6, it doesn't work with tox 3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hron??ok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Matthias Runge <mrunge@redhat.com> - 3.0.0-1
- upgrade to 3.0.0

* Sun Jun 17 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.9.1-7
- Rebuilt for Python 3.7

* Tue May 15 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.9.1-6
- Remove the python2 version once again
- Stop recommending python33 (it's retired)

* Mon May 07 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.9.1-5
- Add python2 back, see #1575667

* Mon Apr 30 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.9.1-4
- Remove the python2 version

* Thu Mar 15 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.9.1-3
- Switch to automatic dependency generator (also fixes #1556164)
- Recommend python37

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Matthias Runge <mrunge@redhat.com> - 2.9.1-1
- update to 2.9.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Matthias Runge <mrunge@redhat.com> - 2.7.0-1
- upgrade to 2.7.0

* Sun Apr 09 2017 Miro Hron??ok <mhroncok@redhat.com> - 2.3.1-8
- Recommend the devel subpackages of Pythons (so tox works with extension modules)

* Tue Feb 14 2017 Miro Hron??ok <mhroncok@redhat.com> - 2.3.1-7
- Recommend python36

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 2.3.1-5
- Rebuild for Python 3.6

* Mon Oct 10 2016 Miro Hron??ok <mhroncok@redhat.com> - 2.3.1-4
- Recommend "all the Pythons"

* Thu Aug 11 2016 Miro Hron??ok <mhroncok@redhat.com> - 2.3.1-3
- /usr/bin/tox is Python3
- Python 2 subpackage is python2-tox
- Run the tests also on Python 3
- Update Source URL and URL
- Use modern macros
- Get rid of Fedora 17 checks

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 29 2016 Matthias Runge <mrunge@redhat.com> - 2.3.1-1
- update to 2.3.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Aug 25 2015 Matthias Runge <mrunge@redhat.com> - 2.1.1-2
- add requirement: python-pluggy

* Tue Aug 18 2015 Matthias Runge <mrunge@redhat.com> - 2.1.1-1
- update to 2.1.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 16 2014 Matthias Runge <mrunge@redhat.com> - 1.8.1-1
- update to 1.8.1

* Wed Aug 13 2014 Matthias Runge <mrunge@redhat.com> - 1.7.1-3
- Fix ConfigError: ConfigError: substitution key 'posargs' not found
  (rhbz#1127961, rhbz#1128562)

* Wed Jul 30 2014 Matthias Runge <mrunge@redhat.com> - 1.7.1-2
- require virtualenv >= 1.11.2 (rhbz#1122603)

* Tue Jul 08 2014 Matthias Runge <mrunge@redhat.com> - 1.7.1-1
- update to 1.7.1 (rhbz#111797)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 24 2013 Matthias Runge <mrunge@redhat.com> - 1.6.1-1
- update to 1.6.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 14 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-7
- add requires python-py, python-virtualenv (rhbz#876246)

* Thu Oct 18 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-6
- change license to GPLv2+ and MIT

* Tue Oct 16 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-5
- totally disable python3 support for now

* Fri Oct 12 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-4
- conditionalize checks, as internet connection required, not available on koji

* Thu Oct 11 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-3
- buildrequirement: virtualenv
- disable python3-tests because of missing build-requirement python3-virtualenv

* Wed Oct 10 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-2
- include tests

* Tue Oct 09 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-1
- initial packaging
