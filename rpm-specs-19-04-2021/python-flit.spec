# circular build dependency on requests-download and testpath
%bcond_without tests

%global srcname flit

Name:		python-%{srcname}
Version:	3.2.0
Release:	1%{?dist}
Summary:	Simplified packaging of Python modules

# ./flit/log.py under ASL 2.0 license
# ./flit/upload.py under PSF license
License:	BSD and ASL 2.0 and Python

URL:		https://flit.readthedocs.io/en/latest/
Source0:	https://github.com/takluyver/flit/archive/%{version}/%{srcname}-%{version}.tar.gz

# For the tests
Source1:	https://pypi.org/pypi?%3Aaction=list_classifiers#/classifiers.lst

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	pyproject-rpm-macros
BuildRequires:	python3-pip

# Runtime deps needed to build self
BuildRequires:	python3-toml

%if %{with tests}
# Runtime deps, others
BuildRequires:	python3-requests
BuildRequires:	python3-docutils
BuildRequires:	python3-pygments

# Test deps
BuildRequires:	/usr/bin/python
BuildRequires:	python3-pytest
BuildRequires:	python3-responses

# Test deps that require flit to build:
BuildRequires:	python3-testpath
BuildRequires:	python3-requests-download
%endif

%global _description %{expand:
Flit is a simple way to put Python packages and modules on PyPI.

Flit only creates packages in the new 'wheel' format. People using older
versions of pip (<1.5) or easy_install will not be able to install them.

Flit packages a single importable module or package at a time, using the import
name as the name on PyPI. All sub-packages and data files within a package are
included automatically.

Flit requires Python 3, but you can use it to distribute modules for Python 2,
so long as they can be imported on Python 3.}

%description %_description


%package -n python3-%{srcname}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:	python3-%{srcname}-core = %{version}-%{release}

# https://pypi.python.org/pypi/tornado
# ./flit/log.py unknown version
Provides:	bundled(python3dist(tornado))

# soft dependency: (WARNING) Cannot analyze code. Pygments package not found.
Recommends:	python3-pygments

%description -n python3-%{srcname} %_description


%package -n python3-%{srcname}-core
Summary:	PEP 517 build backend for packages using Flit
%{?python_provide:%python_provide python3-%{srcname}-core}
Conflicts:	python3-%{srcname} < 2.1.0-2

%description -n python3-%{srcname}-core
This provides a PEP 517 build backend for packages using Flit.
The only public interface is the API specified by PEP 517,
at flit_core.buildapi.


%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
export FLIT_NO_NETWORK=1

# first, build flit_core with self
cd flit_core
%pyproject_wheel
# Move %%{_pyproject_wheeldir}/flit_core wheel to the main dir
mv %{_pyproject_wheeldir} ..
cd -

# build of the main flit (needs flit_core)
PYTHONPATH=$PWD:$PWD/flit_core %pyproject_wheel

%install
%pyproject_install

# don't ship tests in flit_core package
# if upstream decides to change the installation, it can be removed:
# https://github.com/takluyver/flit/issues/403
rm -r %{buildroot}%{python3_sitelib}/flit_core/tests/

%if %{with tests}
%check
# flit attempts to download list of classifiers from PyPI, but not if it's cached
# test_invalid_classifier fails without the list
mkdir -p fake_cache/flit
cp %{SOURCE1} fake_cache/flit
export XDG_CACHE_HOME=$PWD/fake_cache

%pytest
%endif


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/flit-*.dist-info/
%{python3_sitelib}/flit/
%{_bindir}/flit


%files -n python3-%{srcname}-core
%license LICENSE
%doc flit_core/README.rst
%{python3_sitelib}/flit_core-*.dist-info/
%{python3_sitelib}/flit_core/


%changelog
* Tue Mar 30 2021 Karolina Surma <ksurma@redhat.com> - 3.2.0-1
- Update to 3.2.0
Resolves: rhbz#1940399
- Remove tests from the flip_core package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.0.0-2
- Replace deprecated pytoml with toml

* Mon Sep 21 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.9

* Sun May 24 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.3.0-2
- Bootstrap for Python 3.9

* Mon May 11 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Sat Dec 14 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.1.0-2
- Properly package flit-core and restore /usr/bin/flit (#1783610)

* Tue Dec 03 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3-1
- Update to 1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-1
- Update to 1.1

* Sat Aug 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0-4
- Drop pypandoc as requires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.0-2
- Rebuilt for Python 3.7

* Sun Apr 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0-1
- Update to 1.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.13-2
- Recommend Pygments

* Sat Dec 23 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> -  0.13-1
- Update to 0.13

* Thu Nov 16 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Wed Nov 08 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Mon Nov 06 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12-2
- Add pytoml as dependency

* Sun Nov 05 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12-1
- Update to 0.12
- Add pytoml as buildrequires

* Mon Aug 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.4-1
- Update to 0.11.4
- Drop file-encoding patch (fixed upstream)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Michal Cyprian <mcyprian@redhat.com> - 0.9-5
- Use python install wheel macro

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 0.9-4
- Rebuild for Python 3.6

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9-3
- Updated spec file with license comments and provides

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9-2
- spec file cleanup

* Sat Jul 2 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.9-1
- Initial RPM release
