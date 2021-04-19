%global srcname junit-xml
%global modname %(echo '%{srcname}' | tr - _)

Name:           python-%{modname}
Summary:        Python module for creating JUnit XML test result documents
%global forgeurl https://github.com/kyrus/python-%{srcname}/
# Upstream does not tag releases on GitHub (and did not upload a source archive
# to PyPI for version 1.9).
%global commit ba89b41638df8ad2011c2818672f208a91a5a4a0
Version:        1.9
%forgemeta
Release:        6%{?dist}

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
# Version requirement for RHBZ#1925963
BuildRequires:  pyproject-rpm-macros > 0-37

# Fix errors like:
#   import file mismatch:
#   imported module 'tests.test_test_case' has this __file__ attribute:
#     /builddir/.../.pyproject-builddir/pip-req-build-sm4hmtok/tests/test_test_case.py
#   which is not the same as the test file we want to collect:
#     /builddir/.../tests/test_test_case.py
#   HINT: remove __pycache__ / .pyc files and/or use a unique basename for your
#   test file modules
# which seem to be a peculiarity of using pyproject-rpm-macros, rather than a
# bug that should be reported and fixed upstream.
Patch0:         %{name}-1.9-tests-with-pyproject.patch

%global common_description %{expand:
A Python module for creating JUnit XML test result documents that can be read
by tools such as Jenkins or Bamboo. If you are ever working with test tool or
test suite written in Python and want to take advantage of Jenkins’ or Bamboo’s
pretty graphs and test reporting capabilities, this module will let you
generate the XML test reports.}

%description %{common_description}


%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %{common_description}


%generate_buildrequires
%pyproject_buildrequires -t


%prep
%autosetup -n python-%{srcname}-%{commit} -p1


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%tox


%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.9-6
- Drop python3dist(setuptools) BR, redundant with %%pyproject_buildrequires

* Mon Mar 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.9-5
- Replace ' with ’ in description

* Thu Feb 11 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.9-4
- Rebuilt for pyproject-rpm-macros-0-38 to fix unowned nested __pycache__
  directories (RHBZ#1925963)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.9-2
- Drop conditionals for Fedora 32

* Thu Jan 14 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.9-1
- Update to 1.9 (RHBZ#1486729)

* Thu Jan 14 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.8-13
- Drop EPEL compatibility and unnecessary macros; EPEL7/8 will be supported by
  a forked spec file instead of conditional macros
- Use pyproject-rpm-macros, including generated BR’s
- Fix banned %%{python3_sitelib}/* in %%files
- Use %%pytest, %%pypi_source macros
- Update summary and description from upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Adrian Reber <adrian@lisas.de> - 1.8-9
- Apply adapted upstream fix for test failures

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8-5
- Subpackage python2-junit_xml has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 James Hogarth <james.hogarth@gmail.com> - 1.8-1
- update to 1.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 James Hogarth <james.hogarth@gmail.com> - 1.7-1
- Initial package
