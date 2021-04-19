Name:		python-ipyparallel
Version:	6.3.0
Release:	5%{?dist}
Summary:	Interactive Parallel Computing with IPython

License:	BSD
URL:		https://github.com/ipython/ipyparallel
Source0:	https://github.com/ipython/ipyparallel/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-ipython_genutils
BuildRequires:	python3-decorator
BuildRequires:	python3-zmq >= 13
BuildRequires:	python3-traitlets >= 4.3
BuildRequires:	python3-ipython >= 4
BuildRequires:	python3-jupyter-client
BuildRequires:	python3-ipykernel >= 4.4
BuildRequires:	python3-tornado >= 4
BuildRequires:	python3-dateutil >= 2.1
#		For testing:
BuildRequires:	python3-pytest
BuildRequires:	python3-zmq-tests
#		IPython.testing.decorators uses numpy's decorators
BuildRequires:	python3-numpy
#		Dependency of numpy.testing.noseclasses
BuildRequires:	python3-nose
#		For documentation
BuildRequires:	python3-sphinx
BuildRequires:	python3-ipython-sphinx

%description
ipyparallel is the new home of IPython.parallel. ipyparallel is a
Python package and collection of CLI scripts for controlling clusters
for Jupyter.

%package -n python3-ipyparallel
Summary:	Interactive Parallel Computing with IPython
%{?python_provide:%python_provide python3-ipyparallel}
Requires:	python3-ipython_genutils
Requires:	python3-decorator
Requires:	python3-zmq >= 13
Requires:	python3-traitlets >= 4.3
Requires:	python3-ipython >= 4
Requires:	python3-jupyter-client
Requires:	python3-ipykernel >= 4.4
Requires:	python3-tornado >= 4
Requires:	python3-dateutil >= 2.1
Requires:	python-jupyter-filesystem

%description -n python3-ipyparallel
ipyparallel is the new home of IPython.parallel. ipyparallel is a
Python package and collection of CLI scripts for controlling clusters
for Jupyter.

%package -n python3-ipyparallel-tests
Summary:	Tests for python3-ipyparallel
%{?python_provide:%python_provide python3-ipyparallel-tests}
Requires:	python3-ipyparallel = %{version}-%{release}
Requires:	python3-pytest
Requires:	python3-zmq-tests
Requires:	python3-numpy
Requires:	python3-nose

%description -n python3-ipyparallel-tests
This package contains the tests of python3-ipyparallel.

%package doc
Summary:	Documentation for python-ipyparallel

%description doc
This package contains the documentation of python-ipyparallel.

%prep
%setup -q -n ipyparallel-%{version}

%build
%py3_build

pushd docs
PYTHONPATH=.. make html SPHINXBUILD=sphinx-build-3
rm -f build/html/.buildinfo
popd

%install
%py3_install

for f in apps/ipclusterapp.py apps/ipcontrollerapp.py apps/ipengineapp.py \
	 apps/iploggerapp.py controller/heartmonitor.py; do
  sed '/\/usr\/bin\/env/d' -i %{buildroot}%{python3_sitelib}/ipyparallel/${f}
done

# Fix wrong install directory for configuraton files
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%check
# The test_abort test fails - reported upstream:
# https://github.com/ipython/ipyparallel/issues/375

# The test_px_blocking and test_px_nonblocking tests fail on Fedora 35
# But only on koji, not in a local mock build...

pytest-3 -vs ipyparallel/tests \
%if %{fedora} >= 35
    -k 'not test_abort and not test_px_blocking and not test_px_nonblocking'
%else
    -k 'not test_abort'
%endif

%files -n python3-ipyparallel
%license COPYING.md
%doc README.md
%{python3_sitelib}/ipyparallel-*.egg-info
%dir %{python3_sitelib}/ipyparallel
%{python3_sitelib}/ipyparallel/*.py
%{python3_sitelib}/ipyparallel/__pycache__
%{python3_sitelib}/ipyparallel/apps
%{python3_sitelib}/ipyparallel/client
%{python3_sitelib}/ipyparallel/controller
%{python3_sitelib}/ipyparallel/engine
%{python3_sitelib}/ipyparallel/nbextension
%{python3_sitelib}/ipyparallel/serialize
%{_bindir}/ipcluster
%{_bindir}/ipcontroller
%{_bindir}/ipengine
%{_datadir}/jupyter/nbextensions/ipyparallel
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_notebook_config.d/ipyparallel-serverextension.json
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/tree.d/ipyparallel-nbextension.json

%files -n python3-ipyparallel-tests
%{python3_sitelib}/ipyparallel/tests

%files doc
%license COPYING.md
%doc docs/build/html

%changelog
* Tue Apr 13 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.0-5
- Disable the test_px_blocking and test_px_nonblocking tests on Fedora 35+
- Remove obsolete scriptlet for removing old style config

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.3.0-2
- Rebuilt for Python 3.9

* Wed May 06 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.0-1
- Update to 6.3.0
- Drop patches (accepted upstream, or previously backported)

* Mon Apr 20 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.5-1
- Update to 6.2.5
- Remove Python 2 parts from the spec file (Fedora 29 is EOL)
- Drop patches (accepted upstream, or previously backported)
- Prevent KeyError when handling heart failures of already shut down engines
- Print more helpful errors from pytest.warns(None)
- Fix client test for python 3.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.4-4
- Compatibility with ipykernel 5.1.2 (backport from upstream)

* Mon Aug 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.4-3
- Compatibility fixes for Python 3.7, 3.8 (backport from upstream)
- Use unittest.mock if available
- Adapt to Python 3.8 with PEP 570
- Disable the test_abort test (occasional random failures)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.4-1
- Update to 6.2.4
- Avoid python3-mock dependency

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.3-2
- Don't build Python 2 packages for Fedora >= 30

* Mon Oct 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.3-1
- Update to 6.2.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.2-1
- Update to 6.2.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.2.1-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.1-1
- Update to 6.2.1
- This version uses the possibility to split the configuration files into
  smaller files in .d directories introduced in Jupyter notebook 5.3.0
- Drop scriptlets for handling the old configuration
- Add scriptlet to remove old configuration when updating from earlier versions
- Enable the test_wait_for_send test again (the test suite now tries it three
  times before failing)

* Mon Jun 11 2018 Miro Hrončok <mhroncok@redhat.com> - 6.1.1-2
- Don't own /usr/share/jupyter/nbextensions,
  require python-jupyter-filesystem instead (#1589420)

* Wed Feb 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1.1-1
- Update to 6.1.1

* Tue Feb 06 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1.0-1
- Update to 6.1.0
- Drop patch python-ipyparallel-pr254.patch (previously backported)
- Only provide one documentation package
- Disable the test_wait_for_send test (occasional random failures)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.2-2
- Put tests in a separate subpackage

* Sun Apr 30 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.2-1
- Initial packaging
