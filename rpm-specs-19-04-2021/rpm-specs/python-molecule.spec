%global srcname molecule
%global pkgname python-molecule
%global setup_flags SKIP_PIP_INSTALL=1 PBR_VERSION=%{version}

Name:    %{pkgname}
Version: 3.2.4
Release: 1%{?dist}
Summary: Molecule is designed to aid in the development and testing of Ansible roles

# Most of the package is MIT licensed.
#
# There are two files in the archive that are licensed with ASL 2.0:
# - molecule-2.7/molecule/interpolation.py
# - molecule-2.7/test/unit/test_interpolation.py
License: MIT and ASL 2.0

URL:     https://github.com/ansible/molecule
Source0: %{pypi_source}
Patch1: 0002-explicit-shebang-python-version.patch

BuildArch: noarch

BuildRequires: yamllint
BuildRequires: python-devel

BuildRequires: python3dist(sh)
BuildRequires: python3dist(toml)
BuildRequires: python3dist(jinja2) >= 2.10.1
BuildRequires: python3dist(pytest) >= 6.0.2
BuildRequires: python3dist(pyyaml)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(tabulate)
BuildRequires: python3dist(colorama)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(marshmallow)
BuildRequires: python3dist(tree-format)
BuildRequires: python3dist(setuptools-scm)
BuildRequires: python3dist(molecule-docker)
BuildRequires: python3dist(molecule-podman)
BuildRequires: python3dist(sphinx-ansible-theme) >= 0.2.2


%description
Molecule is designed to aid in the development and testing of Ansible roles.
Molecule provides support for testing with multiple instances, operating
systems and distributions, virtualization providers, test frameworks and
testing scenarios. Molecule is opinionated in order to encourage an approach
that results in consistently developed roles that are well-written, easily
understood and maintained. Molecule uses Ansible playbooks to exercise the role
and its associated tests. Molecule supports any provider that Ansible supports.

%package -n python-molecule-doc
Summary: %summary
%description -n python-molecule-doc
Documentation for python-molecule a tool designed to aid in the development and testing
of Ansible roles

%package -n python3-molecule
Summary: %summary

Recommends: python-molecule-doc
Recommends: python3dist(docker)

Requires: yamllint
Requires: pre-commit

Requires: python3dist(sh)
Requires: python3dist(rich) >= 9.5.1
Requires: python3dist(poyo)
Requires: python3dist(toml)
Requires: python3dist(click) >= 7.0
Requires: python3dist(click) < 8.0
Requires: python3dist(enrich) >= 1.2.5
Requires: python3dist(flake8)
Requires: python3dist(jinja2) >= 2.10.1
Requires: python3dist(future)
Requires: python3dist(pyyaml) >= 5.1
Requires: python3dist(pyyaml) < 6
Requires: python3dist(pluggy) >= 0.7.1
Requires: python3dist(pluggy) < 1.0
Requires: python3dist(ansible)
Requires: python3dist(selinux)
Requires: python3dist(cerberus) >= 1.3.1
Requires: python3dist(requests)
Requires: python3dist(colorama)
Requires: python3dist(tabulate)
Requires: python3dist(paramiko) >= 2.5.0
Requires: python3dist(paramiko) < 3
Requires: python3dist(python-gilt)
Requires: python3dist(tree-format)
Requires: python3dist(marshmallow)
Requires: python3dist(ansible-lint)
Requires: python3dist(cookiecutter) >= 1.6.0
Requires: python3dist(git-url-parse)
Requires: python3dist(subprocess-tee)
Requires: python3dist(molecule-docker)
Requires: python3dist(molecule-podman)
Requires: python3dist(pytest-testinfra)
Requires: python3dist(click-completion) >= 0.5.1
Requires: python3dist(click-help-colors) >= 0.6
Requires: python3dist(sphinx-ansible-theme) >= 0.2.2


%{?python_disable_dependency_generator}
%py_provides python3-%{srcname}
%description -n python3-molecule
Molecule is designed to aid in the development and testing of Ansible roles.
Molecule provides support for testing with multiple instances, operating
systems and distributions, virtualization providers, test frameworks and
testing scenarios. Molecule is opinionated in order to encourage an approach
that results in consistently developed roles that are well-written, easily
understood and maintained. Molecule uses Ansible playbooks to exercise the role
and its associated tests. Molecule supports any provider that Ansible supports.


%prep
%setup -q -n %{srcname}-%{version}
%patch1 -p1

cat <<EOF >> setup.cfg

[files]
data_files =
    %{python3_sitelib}/%{srcname}/cookiecutter = molecule/cookiecutter/*
EOF

%build
%{setup_flags} %{py3_build}

# generate html docs
PYTHONPATH=. sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{setup_flags} %{py3_install}
# Fix for some files execute permission
chmod a+x %{buildroot}%{python3_sitelib}/molecule/data/validate-dockerfile.yml
chmod a+x %{buildroot}%{python3_sitelib}/molecule/test/scenarios/verifier/molecule/testinfra-pre-commit/tests/test_default.py

%check
# FIXME: library pathing issues causing tests to fail
# X{setup_flags} X{__python3} setup.py test

%files -n python3-molecule
%license LICENSE
%{python3_sitelib}/*
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}
%{_bindir}/mol

%files -n python-molecule-doc
%license LICENSE
%doc *.rst

%changelog
* Sun Mar 21 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.2.4-1
- Update to version 3.2.4 (#1939754)

* Wed Feb 17 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.2.3-1
- update to version 3.2.1 (#1922542)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.2.2-1
- update to version 3.2.2 (#1914355)

* Mon Jan 04 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.2.1-1
- update to version 3.2.1 (#1892112)

* Mon Nov 23 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.1.5-2
- update dependency (python-testinfra)

* Tue Oct 27 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.1.5-1
- update to 3.1.5 (#1876819)

* Tue Oct 06 2020 Stefano Figura <stefano@figura.im> - 3.0.8-2
- add python3-libselinux dependency to ensure molecule works in Fedora toolbox

* Thu Aug 20 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.0.8-1
- update to 3.0.8

* Tue Aug 18 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.0.7-1
- update to 3.0.7

* Sat Jul 18 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.0.6-1
- update to 3.0.6

* Wed Jul 08 2020 Ken Dreyer <kdreyer@redhat.com> - 3.0.4-1
- update to 3.0.4 (rhbz#1822314)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-7
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.0.2-6
- adding new dependencies

* Mon Feb 24 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.0.2
- update to 3.0.2

* Fri Feb 21 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.0.1
- update to 3.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Chedi Toueiti <chedi.toueiti@gmail.com> - 2.22-1
- update to 2.22

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.20.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Juerg Ritter <juerg_ritter@bluewin.ch> - 2.20.1-1
- update to 2.20.1 and disabled dependency generator

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Brett Lentz <brett.lentz@gmail.com> - 2.19-1
- update to 2.19

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 2.16-2
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 17 2018 Brett Lentz <brett.lentz@gmail.com> - 2.16-1
- update to 2.16

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.13.1-3
- Rebuilt for Python 3.7

* Fri May 11 2018 Brett Lentz <brett.lentz@gmail.com> - 2.13.1-2
- add Recommends for default use case

* Wed May 9 2018 Brett Lentz <brett.lentz@gmail.com> - 2.13.1-1
- update to 2.13.1
- ensure all needed files are installed

* Mon Apr 30 2018 Brett Lentz <brett.lentz@gmail.com> - 2.13-1
- update to 2.13

* Mon Apr 2 2018 Brett Lentz <brett.lentz@gmail.com> - 2.12.1-2
- update to 2.12.1

* Thu Mar 29 2018 Brett Lentz <brett.lentz@gmail.com> - 2.11-1
- update to 2.11

* Wed Mar 14 2018 Brett Lentz <brett.lentz@gmail.com> - 2.10.1-3
- fix package deps

* Mon Mar 12 2018 Brett Lentz <brett.lentz@gmail.com> - 2.10.1-1
- update to 2.10.1

* Mon Mar 5 2018 Brett Lentz <brett.lentz@gmail.com> - 2.9-1
- update to 2.9

* Tue Jan 23 2018 Brett Lentz <brett.lentz@gmail.com> - 2.7-1
- initial package
