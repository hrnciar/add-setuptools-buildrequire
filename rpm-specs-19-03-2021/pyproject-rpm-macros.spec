Name:           pyproject-rpm-macros
Summary:        RPM macros for PEP 517 Python packages
License:        MIT

%bcond_without tests

# Keep the version at zero and increment only release
Version:        0
Release:        38%{?dist}

# Macro files
Source001:      macros.pyproject

# Implementation files
Source101:      pyproject_buildrequires.py
Source102:      pyproject_save_files.py
Source103:      pyproject_convert.py
Source104:      pyproject_preprocess_record.py
Source105:      pyproject_construct_toxenv.py

# Tests
Source201:      test_pyproject_buildrequires.py
Source202:      test_pyproject_save_files.py

# Test data
Source301:      pyproject_buildrequires_testcases.yaml
Source302:      pyproject_save_files_test_data.yaml
Source303:      test_RECORD

# Metadata
Source901:      README.md
Source902:      LICENSE

URL:            https://src.fedoraproject.org/rpms/pyproject-rpm-macros

BuildArch:      noarch

%if %{with tests}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pyyaml)
BuildRequires: python3dist(packaging)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(toml)
BuildRequires: python3dist(tox-current-env) >= 0.0.3
BuildRequires: python3dist(wheel)
%endif


%description
These macros allow projects that follow the Python packaging specifications
to be packaged as RPMs.

They are still provisional: we can make non-backwards-compatible changes to
the API.
Please subscribe to Fedora's python-devel list if you use the macros.

They work for:

* traditional Setuptools-based projects that use the setup.py file,
* newer Setuptools-based projects that have a setup.cfg file,
* general Python projects that use the PEP 517 pyproject.toml file
  (which allows using any build system, such as setuptools, flit or poetry).

These macros replace %%py3_build and %%py3_install,
which only work with setup.py.


%prep
# Not strictly necessary but allows working on file names instead
# of source numbers in install section
%setup -c -T
cp -p %{sources} .

%build
# nothing to do, sources are not buildable

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}/redhat
install -m 644 macros.pyproject %{buildroot}%{_rpmmacrodir}/
install -m 644 pyproject_buildrequires.py %{buildroot}%{_rpmconfigdir}/redhat/
install -m 644 pyproject_convert.py %{buildroot}%{_rpmconfigdir}/redhat/
install -m 644 pyproject_save_files.py  %{buildroot}%{_rpmconfigdir}/redhat/
install -m 644 pyproject_preprocess_record.py %{buildroot}%{_rpmconfigdir}/redhat/
install -m 644 pyproject_construct_toxenv.py %{buildroot}%{_rpmconfigdir}/redhat/

%if %{with tests}
%check
export HOSTNAME="rpmbuild"  # to speedup tox in network-less mock, see rhbz#1856356
%{python3} -m pytest -vv --doctest-modules
%endif


%files
%{_rpmmacrodir}/macros.pyproject
%{_rpmconfigdir}/redhat/pyproject_buildrequires.py
%{_rpmconfigdir}/redhat/pyproject_convert.py
%{_rpmconfigdir}/redhat/pyproject_save_files.py
%{_rpmconfigdir}/redhat/pyproject_preprocess_record.py
%{_rpmconfigdir}/redhat/pyproject_construct_toxenv.py

%doc README.md
%license LICENSE

%changelog
* Sun Feb 07 2021 Miro Hron??ok <mhroncok@redhat.com> - 0-38
- Include nested __pycache__ directories in %%pyproject_save_files
- Fixes: rhbz#1925963

* Tue Feb 02 2021 Miro Hron??ok <mhroncok@redhat.com> - 0-37
- Remove support for Python 3.7 from %%pyproject_buildrequires
- Generate python3dist(toml) BR with pyproject.toml earlier to avoid extra install round
- Generate python3dist(setutpools/wheel) BR without pyproject.toml earlier as well

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Miro Hron??ok <mhroncok@redhat.com> - 0-35
- Update the description of the package to match the new README content

* Fri Dec 04 2020 Miro Hron??ok <miro@hroncok.cz> - 0-34
- List all files in %%pyproject_files explicitly to avoid duplicate %%lang entries
- If you amend the installed files after %%pyproject_install, %%pyproject_files might break

* Fri Nov 27 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-33
- Pass PYTHONDONTWRITEBYTECODE=1 to %%tox to avoid packaged PYTEST bytecode

* Tue Nov 03 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-32
- Allow multiple -e in %%pyproject_buildrequires
- Fixes: rhbz#1886509

* Mon Oct 05 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-31
- Support PEP 517 list based backend-path

* Tue Sep 29 2020 Lum??r Balhar <lbalhar@redhat.com> - 0-30
- Process RECORD files in %%pyproject_install and remove them
- Support the extras configuration option of tox in %%pyproject_buildrequires -t
- Support multiple -x options for %%pyproject_buildrequires
- Fixes: rhbz#1877977
- Fixes: rhbz#1877978

* Wed Sep 23 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-29
- Check the requirements after installing "requires_for_build_wheel"
- If not checked, installing runtime requirements might fail

* Tue Sep 08 2020 Gordon Messmer <gordon.messmer@gmail.com> - 0-28
- Support more Python version specifiers in generated BuildRequires
- This adds support for the '~=' operator and wildcards

* Fri Sep 04 2020 Miro Hron??ok <miro@hroncok.cz> - 0-27
- Make code in $PWD importable from %%pyproject_buildrequires
- Only require toml for projects with pyproject.toml
- Remove a no longer useful warning for unrecognized files in %%pyproject_save_files

* Mon Aug 24 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0-26
- Implement automatic detection of %%lang files in %%pyproject_save_files
  and mark them with %%lang in filelist

* Fri Aug 14 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-25
- Handle Python Extras in %%pyproject_buildrequires on Fedora 33+

* Tue Aug 11 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-24
- Allow multiple, comma-separated extras in %%pyproject_buildrequires -x

* Mon Aug 10 2020 Lum??r Balhar <lbalhar@redhat.com> - 0-23
- Make macros more universal for alternative Python stacks

* Thu Aug 06 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0-22
- Change %%pyproject_save_files +bindir argument to +auto
  to list all unclassified files in filelist

* Tue Aug 04 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-21
- Actually implement %%pyproject_extras_subpkg

* Wed Jul 29 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-20
- Implement %%pyproject_extras_subpkg

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-18
- %%pyproject_buildrequires -x (extras requires for tests) now implies -r
  (runtime requires) instead of erroring without it for better UX.

* Wed Jul 15 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-17
- Set HOSTNAME to prevent tox 3.17+ from a DNS query
- Fixes rhbz#1856356

* Fri Jun 19 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-16
- Switch from upstream deprecated pytoml to toml

* Thu May 07 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0-15
- Adapt %%pyproject_install not to create a PEP 610 direct_url.json file

* Wed Apr 15 2020 Patrik Kopkan <pkopkan@redhat.com> - 0-14
- Add %%pyproject_save_file macro for generating file section
- Handle extracting debuginfo from extension modules (#1806625)

* Mon Mar 02 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-13
- Tox dependency generator: Handle deps read in from a text file (#1808601)

* Wed Feb 05 2020 Miro Hron??ok <mhroncok@redhat.com> - 0-12
- Fallback to setuptools.build_meta:__legacy__ backend instead of setuptools.build_meta
- Properly handle backends with colon
- Preserve existing flags in shebangs of Python files in /usr/bin

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Patrik Kopkan <pkopkan@redhat.com> - 0-10
- Install wheel in '$PWD/pyproject-macros-wheeldir' to have more explicit path from which we install.
- The path can be changed by redefining %%_pyproject_wheeldir.

* Wed Nov 13 2019 Anna Khaitovich <akhaitov@redhat.com> - 0-9
- Remove stray __pycache__ directory from /usr/bin when running %%pyproject_install

* Fri Oct 25 2019 Miro Hron??ok <mhroncok@redhat.com> - 0-8
- When tox fails, print tox output before failing

* Tue Oct 08 2019 Miro Hron??ok <mhroncok@redhat.com> - 0-7
- Move a verbose line of %%pyproject_buildrequires from stdout to stderr

* Fri Jul 26 2019 Petr Viktorin <pviktori@redhat.com> - 0-6
- Use importlib_metadata rather than pip freeze

* Fri Jul 26 2019 Miro Hron??ok <mhroncok@redhat.com> - 0-5
- Allow to fetch test dependencies from tox
- Add %%tox macro to invoke tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Miro Hron??ok <mhroncok@redhat.com> - 0-3
- Add %%pyproject_buildrequires

* Tue Jul 02 2019 Miro Hron??ok <mhroncok@redhat.com> - 0-2
- Fix shell syntax errors in %%pyproject_install
- Drop PATH warning in %%pyproject_install

* Fri Jun 28 2019 Patrik Kopkan <pkopkan@redhat.com> - 0-1
- created package
