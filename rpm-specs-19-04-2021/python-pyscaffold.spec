# Enabled by default
# If the package needs to download data for the test which cannot be done in
# koji, these can be disabled in koji by using `bcond_with` instead, but the
# tests must be validated in mock with network enabled like so:
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enable-network --rpmbuild-opts="--with tests"
%bcond_without tests

%global pretty_name PyScaffold
%global pypi_name pyscaffold

%global desc %{expand: \
PyScaffold helps you setup a new Python project.

PyScaffold comes with a lot of elaborated features and configuration defaults
to make the most common tasks in developing, maintaining and distributing your
own Python package as easy as possible.
}

Name:           python-%{pypi_name}
Version:        3.2.1
Release:        8%{?dist}
Summary:        Template tool for putting up the scaffold of a Python project

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source %{pretty_name}

# Make pyscaffold work with setuptools_scm 6+
# A more complex fix is in upstream since 4.0.1
# https://github.com/pyscaffold/pyscaffold/issues/428
Patch1:         setuptools_scm-6.patch

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
# For tests
BuildRequires:  git
BuildRequires:  %{py3_dist coverage}
BuildRequires:  %{py3_dist cookiecutter}
BuildRequires:  %{py3_dist django}
BuildRequires:  %{py3_dist flake8}
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist pytest-runner}
BuildRequires:  %{py3_dist pytest-virtualenv}
BuildRequires:  %{py3_dist pytest-xdist}
BuildRequires:  %{py3_dist wheel}
# For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%{?python_provide:%python_provide python3-%{pypi_name}}

# Dep generator didn't pick them up
Requires:  python3-setuptools
Requires:  python3-setuptools_scm
Requires:  %{py3_dist pytest-runner}

%description -n python3-%{pypi_name}
%{desc}

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -p1 -n %{pretty_name}-%{version}
# Remove egg info
rm -rf src/%{pretty_name}*.egg-info

# Remove bundled bits but leave configupdater
# configupdater itself requires pyscaffold: cyclic dependency, so one of them
# needs to bundle the other to begin with
rm -rf src/pyscaffold/contrib/{__pycache__,setuptools_scm,ptr.py}

# Remove mention of non configupdater bundled bits
sed -i 's/from pyscaffold.contrib.setuptools_scm/from setuptools_scm/' setup.py
sed -i 's/from .contrib.setuptools_scm/from setuptools_scm/' src/pyscaffold/{utils,integration}.py
sed -i 's/from .contrib import ptr/import ptr/' src/pyscaffold/{utils,integration}.py
sed -i 's/from pyscaffold.contrib.setuptools_scm/from setuptools_scm/' tests/test_integration.py
sed -i '/setuptools/ d' setup.cfg

# In tests, change invocations from python to python3
find tests -name "*.py" -exec sed -i "s/'python'/'python3'/g" '{}' \;
# Correct all shebangs in tests
find tests -name "*.py" -exec sed -i 's|#!/usr/bin/env.*python|#!/usr/bin/python3|' '{}' \;

# In templates. replace /usr/bin/env python with /usr/bin/python3
pushd src/pyscaffold/templates || exit -1
for i in *.template; do
    sed -i 's|#!/usr/bin/env.*python|#!/usr/bin/python3|' $i
done
popd

%build
# It doesn't like the --executable option that's in %%py3_build
%set_build_flags
%{__python3} setup.py build

# Generate docs
PYTHONPATH=src/ sphinx-build-3 docs html
# Remove hidden files
rm -f html/.buildinfo
rm -rf html/.doctrees

%install
%py3_install
# setup.py does not install the template files
install -p -m 0644 src/pyscaffold/templates/*.template -t %{buildroot}/%{python3_sitelib}/%{pypi_name}/templates/

%check
%if %{with tests}
# Required for a test
git config --global user.email "jane@doe.com"
git config --global user.name "jane doe"
# remove tests that use network to do things with pip and git
rm tests/test_install.py
rm tests/system/test_common.py
PYTHONPATH=%{buildroot}/%{python3_sitelib} pytest-3 . -k "not test_update_version_3_0_to_3_1 and not test_pipenv_works_with_pyscaffold and not test_create_project_with_cookiecutter and not test_cli_with_cookiecutter"
%endif

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}
%{_bindir}/putup

%files doc
%license LICENSE.txt
%doc html

%changelog
* Fri Mar 19 2021 Miro Hron??ok <mhroncok@redhat.com> - 3.2.1-8
- Make pyscaffold work with setuptools_scm 6+

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.2.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.2.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.2.1-2
- Rebuilt for Python 3.8

* Mon Aug 05 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-1
- Update to 3.2.1
- Add rtd-theme

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1-1
- Initial build
