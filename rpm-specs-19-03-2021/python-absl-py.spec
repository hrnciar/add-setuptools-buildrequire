%global modname absl
%global srcname %{modname}-py
%global reponame abseil-py
%global egginfo_name %(echo %{srcname} | tr - _)

Name:           python-%{srcname}
Version:        0.12.0
Release:        3%{?dist}
Summary:        Abseil Python Common Libraries

# Overall license is ASL 2.0. Contents of absl/third_party/unittest3_backport/
# are under the Python license (derived from the Python 3 standard library).
License:        ASL 2.0 and Python
URL:            https://github.com/abseil/%{reponame}/
Source0:        %{url}/archive/pypi-v%{version}/%{reponame}-pypi-v%{version}.tar.gz

BuildRequires:  python3-devel >= 3.4
BuildRequires:  pyproject-rpm-macros

BuildArch:      noarch

%global common_description %{expand:
This repository is a collection of Python library code for building Python
applications. The code is collected from Google’s own Python code base, and has
been extensively tested and used in production.

Features:

  • Simple application startup
  • Distributed commandline flags system
  • Custom logging module with additional features
  • Testing utilities}

%description %{common_description}


%generate_buildrequires
%pyproject_buildrequires -r


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{reponame}-pypi-v%{version} -p1
cp -p absl/third_party/unittest3_backport/LICENSE LICENSE-PYTHON

# Despite the third_party/ prefix, absl/third_party/unittest3_backport/ is not
# exactly a bundled library. On Python 3, it is merely a shim around the
# unittest module from the Python standard library. On Python 2, it is a
# backport of much of the added functionality from the Python 3 version of the
# unittest module; while derived from some version of the Python 3 standard
# library, this backport is specific to absl-py, is maintained in the same
# source code repository, and appears not to be separately distributed or used
# by any other software.


%build
%py3_build


%install
%py3_install


%check
# We cannot use smoke_tests/smoke_test.sh because it downloads things from the
# Internet. We can, however, run the sample Python scripts manually, which is
# better than nothing.
PYTHONPATH=%{buildroot}/%{python3_sitelib}; export PYTHONPATH
%{__python3} smoke_tests/sample_app.py --echo smoke 
%{__python3} smoke_tests/sample_test.py

# Running the actual test suite requires bazel, which will almost certainly
# never be packaged for Fedora due to its Byzantine mass of bundled
# dependencies. It is possible to invoke the tests with another runner, such as
# pytest, but there are many spurious failures due to the incorrect
# environment, so it is useless to do so.


%files -n python3-%{srcname}
%license LICENSE
%license LICENSE-PYTHON
%doc AUTHORS
%doc absl/CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%doc smoke_tests

%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{egginfo_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.12.0-3
- Drop python3dist(setuptools) BR, redundant with %%pyproject_buildrequires

* Wed Mar 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.12.0-2
- Add CHANGELOG.md, from absl/, to documentation

* Wed Mar 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.12.0-1
- Update to 0.12.0
- Drop python-absl-py-0.11.0-python-3.10.patch, now upstreamed

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-4
- Fix Python 3.10 incompatibility due to incorrect string-based version
  detection (RHBZ#1906811, https://github.com/abseil/abseil-py/issues/161)

* Tue Dec  1 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-3
- Remove conditionals for Fedora 32 and older

* Wed Nov 25 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-2
- Remove EPEL conditionals from Fedora spec file

* Wed Nov 25 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-1
- Initial package
