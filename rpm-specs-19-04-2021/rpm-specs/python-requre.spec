%global srcname requre

Name:           python-%{srcname}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Python library what allows re/store output of various objects for testing

License:        MIT
URL:            https://github.com/packit/requre
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
BuildRequires:  python3dist(sphinx)

%description
REQUest REcordingRequre [rekure] - Is Library for storing output of various
function and methods to persistent storage and be able to replay the stored
output to functions.

%package -n     python3-%{srcname}
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides
%if 0%{?fedora} < 33
%{?python_provide:%python_provide python3-%{srcname}}
%endif

%description -n python3-%{srcname}
REQUest REcordingRequre [rekure] - Is Library for storing output of various
function and methods to persistent storage and be able to replay the stored
output to functions.

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{_bindir}/requre-patch
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 12 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.7.0-1
- New version of requre 0.7.0 (Jan Ščotka)
- Workflow for uploading release to PyPI (Jiri Popelka)
- fix the name of storage file for unittest, use just class.method.yaml (Jan Ščotka)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])

* Mon Mar 01 2021 Jan Ščotka <jscotka@redhat.com> - 0.6.1-1
- version increased (Jan Ščotka)
- test Tuple type (Jan Ščotka)
- add tuple as base simple type (Jan Ščotka)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])

* Tue Feb 16 2021 Jan Ščotka <jscotka@redhat.com> - 0.6.0-1
- release new version 0.6.0 (Jan Ščotka)
- Cleanup import system (#152) (jscotka)
- improve failing test (Jan Ščotka)
- prepare code before next cleanup (Jan Ščotka)
- remove unused type of decoration and it was outtaded (Jan Ščotka)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- Don't recommend to use 'pip' with 'sudo' (Hunor Csomortáni)
- Change 'master' to 'main' (Hunor Csomortáni)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- small issue with setting up storage mode debug (Jan Ščotka)
- Bump Version in fedora/python-requre.spec (Jiri Popelka)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- add backward compatibility to files (Jan Ščotka)
- improve file operations with guess if not given (Jan Ščotka)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.5.0-1
- apply PR suggestion (Jan Ščotka)
- add default decorator and test (Jan Ščotka)
- guess proper return object type based on  return value (Jan Ščotka)
- Link our common contribution guidelines (Matej Focko)
- Fix mypy remark (Matej Focko)
- Move rebase check from pre-commit to pre-push hook (Matej Focko)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- update documentation (Jan Ščotka)
- fix examples (Jan Ščotka)
- fix ip addr and DNS issue inside tests (Jan Ščotka)
- Do not skip bug and security issues by stalebot (Frantisek Lachman)
- Do not run tests for zuul gating (Frantisek Lachman)
- Add more specific type for __replace_module_match_with_multiple_decorators (Frantisek Lachman)
- fix mistake (Jan Ščotka)
- Update requre/modules_decorate_all_methods.py (jscotka)
- apply PR suggestions (Jan Ščotka)
- Allow to use list as parameter for decoratos and add common aliases for decorators. (Jan Ščotka)
- Update pre-commit configuration for prettier (Hunor Csomortáni)
- Copy modules when listing to avoid changes during execution (Frantisek Lachman)
- adapt PR review issues (Jan Ščotka)
- optimise files handling, avoid duplication of stored files in test_data files (Jan Ščotka)
- Document installation instructions in README (Frantisek Lachman)
- Enable all fedora targets for master/release copr builds (Frantisek Lachman)
- Use default packit COPR projects (Frantisek Lachman)

* Tue Sep 22 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.4.0-1
- new upstream release: 0.4.0

* Mon Sep 21 2020 Jan Ščotka <jscotka@redhat.com> - 0.3.0-1
- new upstream release: 0.3.0

* Wed Jan 15 2020 Jan Ščotka <jscotka@redhat.com> - 0.2.0-1
- Initial package.
