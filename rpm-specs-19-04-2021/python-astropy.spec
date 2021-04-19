%bcond_without check

%global srcname astropy

Name: python-%{srcname}
Version: 4.2
Release: 3%{?dist}
Summary: A Community Python Library for Astronomy
License: BSD

URL: http://astropy.org
Source0: %{pypi_source}
Source1: astropy-README.dist
Patch0: python-astropy-system-configobj.patch
Patch1: python-astropy-system-ply.patch

%global _description %{expand:
The Astropy project is a common effort to develop a single core package
for Astronomy. Major packages such as PyFITS, PyWCS, vo, and asciitable
already merged in, and many more components being worked on. In
particular, we are developing imaging, photometric, and spectroscopic
functionality, as well as frameworks for cosmology, unit handling, and
coordinate transformations.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: expat-devel 
BuildRequires: cfitsio-devel >= 3.490
BuildRequires: wcslib-devel
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist setuptools_scm}
BuildRequires: %{py3_dist Cython}
BuildRequires: %{py3_dist jinja2}
BuildRequires: %{py3_dist numpy}
BuildRequires: %{py3_dist extension-helpers}
BuildRequires: %{py3_dist configobj}
BuildRequires: %{py3_dist ply}
%if %{with check}
BuildRequires: %{py3_dist pytest}
BuildRequires: %{py3_dist hypothesis}
BuildRequires: %{py3_dist pyerfa}
BuildRequires: %{py3_dist pytest-remotedata}
BuildRequires: %{py3_dist pytest-astropy}
#
BuildRequires: %{py3_dist scipy}
BuildRequires: %{py3_dist matplotlib}
BuildRequires: %{py3_dist pandas}
BuildRequires: %{py3_dist h5py}
BuildRequires: %{py3_dist scikit-image}
# Not if Fedora
##BuildRequires: %%{py3_dist asdf}
%endif

Requires: %{py3_dist configobj}
Requires: %{py3_dist ply}
Provides: bundled(jquery) = 3.11

%description -n python3-%{srcname} %_description

%package -n python3-%{srcname}-doc
Summary: Documentation for %{name}, includes full API docs

%description -n python3-%{srcname}-doc
This package contains the full API documentation for %{name}.

%package -n %{srcname}-tools
Summary: Astropy utility tools
BuildArch: noarch
Requires: python3-%{srcname} = %{version}-%{release}

%description -n %{srcname}-tools
Utilities provided by Astropy.

%prep
%autosetup -n %{srcname}-%{version} -p1
# To be sure
rm -rf astropy/extern/configobj
rm -rf astropy/extern/ply
rm -rf cextern/cfitsio
rm -rf cextern/expat
rm -rf cextern/wcslib

%build
export ASTROPY_USE_SYSTEM_ALL=1
# Search for headers in subdirs
export CPATH="/usr/include/cfitsio:/usr/include/wcslib"
%{py3_build}

%install
export ASTROPY_USE_SYSTEM_ALL=1
# Search for headers in subdirs
export CPATH="/usr/include/cfitsio:/usr/include/wcslib"
%{py3_install}

%if %{with check}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
# wcs tests fail due to the different
# version of wcslib
pushd %{buildroot}/%{python3_sitearch}
  pytest \
         --deselect "astropy/coordinates/tests/accuracy/test_altaz_icrs.py::test_against_pyephem" \
         --deselect "astropy/wcs/tests/test_wcsprm.py::test_fix" \
         --deselect "astropy/wcs/tests/test_wcs.py::test_fixes" \
         --deselect "astropy/wcs/tests/test_wcs.py::test_pix2world" \
         --deselect "astropy/wcs/tests/test_wcs.py::test_warning_about_defunct_keywords" \
         --deselect "astropy/wcs/tests/test_wcs.py::test_validate" \
%ifarch armv7hl
         --deselect "astropy/table/tests/test_showtable.py::test_stats" \
%endif
  astropy 
  # remove hypothesis dir
  rm -rf .hypothesis
popd
%endif

%files -n %{srcname}-tools
%{_bindir}/*

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.rst
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info

%files -n python3-%{srcname}-doc
%doc README.rst 
%license LICENSE.rst

%changelog
* Tue Feb 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 4.2-3
- Exclude test failling in armv7hl

* Tue Feb 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 4.2-2
- New upstream source 4.2
- Cleanup specfile

* Tue Feb 02 2021 Christian Dersch <lupinix@mailbox.org> - 4.0.1.post1-6
- Rebuilt for libcfitsio.so.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.post1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.post1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1.post1-3
- Rebuilt for Python 3.9

* Sat May 23 2020 Orion Poplawski <orion@nwra.com> - 4.0.1.post1-2
- Drop old pyfits-tools obsoletes/provides
- Build with system wcslib on EL8

* Thu May 07 2020 Orion Poplawski <orion@nwra.com> - 4.0.1.post1-1
- Update to 4.0.1.post1

* Fri Mar 20 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 4.0-3
- Rebuildt for wcslib 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 4.0-1
- New upstream version (4.0)

* Thu Nov 07 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.2.3-1
- New upstream version (3.2.3), fixes problem with IERS data download

* Wed Oct 09 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.2.2-1
- New upstream version (3.2.2)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.2.1-1
- New upstream version (3.2.1)
- Remove patches included upsteam

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 3.1.2-2
- Imported upstream fix for PyYAML 5.x

* Mon Mar 04 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.1.2-1
- New version (3.1.2)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 21 2018 Christian Dersch <lupinix@mailbox.org> - 3.0.5-1
- new version

* Mon Aug 13 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-2
- Enable s390x (#1610996)

* Fri Aug 03 2018 Christian Dersch <lupinix.fedora@gmail.com> - 3.0.4-1
- new version (3.0.4)
- reenable tests
- ExcludeArch s390x until #1610996 is fixed

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 3.0.3-5
- BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Christian Dersch <lupinix@fedoraproject.org> - 3.0.3-3
- Disable tests until we have the pyyaml fix
  https://github.com/yaml/pyyaml/pull/181

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.3-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 3.0.3-1
- New release (3.0.3)

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 3.0.2-1
- new version

* Sat Mar 17 2018 Christian Dersch <lupinix@mailbox.org> - 3.0.1-1
- new version
- cleaned up excluded tests, adapted patch from Debian for known failures
- removed Python 2 bits (in new package python2-astropy), astropy moved to
  Python 3 only

* Wed Mar 14 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.5-1
- new version
- enabled fixed tests

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.4-3
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.4-2
- Provide and Obsolete python-wcsaxes, which has been merged into astropy

* Tue Feb 13 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.4-1
- update to bugfix release 2.0.4
- fixes FTBFS on rawhide (due to fixes for newer numpy etc.)
- disabled tests on s390x as they hang sometimes (same as with scipy)
- removed python-astropy-fix-hdf5-test.patch (applied upstream)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0.2-2
- Use system erfa

* Sun Oct 08 2017 Christian Dersch <lupinix@mailbox.org> - 2.0.2-1
- new version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Christian Dersch <lupinix@mailbox.org> - 1.3.3-1
- new version

* Sun Apr 02 2017 Christian Dersch <lupinix@mailbox.org> - 1.3.2-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 5 2017 Orion Poplawski <orion@cora.nwra.com> - 1.3-1
- Update to 1.3

* Wed Dec 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3-0.1.rc1
- Update to 1.3rc1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-6
- Rebuild for Python 3.6

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-5
- Use bundled erfa and wcslib where necessary (bug #1396601)
- Specify scipy version requirements
- Use cairo matplotlib backend due to ppc64 segfault
- Add BR on pandas for tests

* Sun Nov 06 2016 Björn Esser <fedora@besser82.io> - 1.2.1-4
- Rebuilt for ppc64

* Fri Sep 30 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.1-3
- Fix wrong provides of python3-astropy in python2-astropy (bz #1380135)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.1-1
- New upstream (1.2.1)

* Thu Apr 14 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.2-1
- New upstream (1.1.2)
- Uses wcslib 5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-2
- Modernize spec
- Prepare for python3 in EPEL

* Sun Jan 10 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.1-1
- New upstream (1.1.1)

* Wed Jan 06 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-1.post2
- New upstream (1.1.post2)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.6-2
- Enabled again tests that failed with numpy 1.10

* Wed Oct 28 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.6-1
- New upstream (1.0.6), with better support of numpy 1.10

* Fri Oct 09 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.5-2
- Fixes test problem https://github.com/astropy/astropy/issues/4226

* Tue Oct 06 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.5-1
- New upstream (1.0.5)

* Mon Sep 14 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.4-2
- Disable some tests that fail with numpy 1.10

* Thu Sep 03 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.4-1
- New upstream (1.0.4)

* Tue Jun 30 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.3-4
- Reenable tests
- Handle changes regarding python3 and pyfits-tools in fedora >= 22

* Mon Jun 29 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.3-3
- Obsolete pyfits-tools (fixes bz #1236562)
- astropy-tools requires python3

* Tue Jun 16 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.3-1
- New upstream (1.0.3), with 2015-06-30 leap second

* Tue Apr 21 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-1
- New upstream (1.0.2)

* Thu Feb 19 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0-1
- New upstream (1.0)

* Thu Jan 22 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.4-1
- New upstream (0.4.4)

* Fri Jan 16 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.3-1
- New upstream (0.4.3)

* Tue Dec 09 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-5
- Disable tests for the moment

* Tue Dec 09 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-4
- Update patch for bug 2516

* Mon Dec 08 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-3
- Mark problematic tests as xfail via patch

* Fri Dec 05 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-2
- Fix to use configobj 5
- Patches reorganized

* Thu Sep 25 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-1
- New upstream (0.4.2)

* Mon Sep 01 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.1-1
- New upstream (0.4.1)
- Unbundling patches modified
- No checks for the moment

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 0.3.2-5
- Rebuild for Python 3.4

* Thu May 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-4
- Build with wcslib 4.23
- Skip test, bug 2171

* Thu May 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-3
- Astropy bundles jquery
- Unbundle plpy

* Thu May 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-2
- Add missing patches

* Mon May 19 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-1
- New upstream (0.3.2)
- Enable checks
- Patch to fix upstream bug 2171
- Disable problematic test (upstream 2516)

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Mar 25 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.1-2
- Disable checks until https://github.com/astropy/astropy/issues/2171 is fixed
- Patch to fix https://github.com/astropy/astropy/pull/2223

* Wed Mar 05 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.1-1
- New upstream version (0.3.1)
- Remove require python(3)-matplotlib-qt4 (bug #1030396 fixed)
- Run the tests on the installed files
- Add patch to run with six 1.5.x

* Mon Jan 27 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-7
- Add missing requires python3-six

* Sat Jan 18 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-6
- Do not exclude hidden file, it breaks tests

* Thu Jan 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-5
- Remove split -devel subpackage, it does not make much sense

* Fri Jan 10 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-4
- Disable noarch for doc subpackages to avoid name colision

* Fri Jan 10 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-3
- Enable HDF5 version check (fixed in h5py)
- Patch for failing test with wcslib 4.20
- Require python(3)-matplotlib-qt4 due to bug #1030396

* Sun Jan 05 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-2
- Disable HDF5 version check

* Mon Nov 25 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-1
- New upstream (0.3)

* Tue Nov 19 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-0.3.rc1
- New upstream, first release candidate Testing 0.3rc1

* Wed Nov 06 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-0.2.b1
- Split utility scripts in subpackage

* Tue Nov 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-0.1.b1
- Testing 0.3 (0.3b1)

* Mon Oct 28 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.5-1
- New upstream version (0.2.5)

* Tue Oct 22 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.4-4
- Split header files into devel subpackages

* Mon Oct 21 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.4-3
- Disable tests in Rawhide

* Thu Oct 10 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.4-3
- Add a patch to build with cfitsio 3.35

* Wed Oct 02 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.4-1
- Initial spec
