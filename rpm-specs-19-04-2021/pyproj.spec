# note: PROJ_MIN_VERSION is defined in the setup.py file of pyproj
# a compatibility matrix is also provided in docs/installation.rst
%global minimal_needed_proj_version 7.2.0

Name:           pyproj
Version:        3.0.1
Release:        2%{?dist}
Summary:        Cython wrapper to provide python interfaces to Proj
License:        MIT
URL:            https://github.com/jswhit/%{name}
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
# the old source url still works, but if need be it can be replaced
# with: https://files.pythonhosted.org/packages/source/p/%%{name}/%%{name}-%%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  proj-devel >= %{minimal_needed_proj_version}
BuildRequires:  proj >= %{minimal_needed_proj_version}

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-Cython
BuildRequires:  python3-certifi

# needed to run the tests
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-pandas
BuildRequires:  python3-shapely
BuildRequires:  python3-xarray

# needed to remove the hardcoded path '/usr/lib' from the _proj.so file
BuildRequires:  chrpath

# needed to build the documentation
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-argparse
BuildRequires:  python3-sphinx_rtd_theme

%global _description \
Cython wrapper to provide python interfaces to Proj. \
Performs cartographic transformations between geographic (Lat/Lon) \
and map projection (x/y) coordinates. Can also transform directly \
from one map projection coordinate system to another. \
Coordinates can be given as numpy arrays, python arrays, lists or scalars. \
Optimized for numpy arrays.

%description %_description


%package -n python3-%{name}

Summary: %summary

Requires:  proj >= %{minimal_needed_proj_version}

# ensure python provides are provided when python3 becomes the default runtime
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name} %_description

%package -n python3-%{name}-doc

Summary:    Documentation and example code
BuildArch:  noarch

%description -n python3-%{name}-doc
This package contains the html documentation for the pyproj module.

%prep
%autosetup -p1

# no longer needed: Delete Cython generated files
# rm -v $(grep -rl '/\* Generated by Cython')

# remove use of /usr/bin/env in docs/conf.py
sed -i -e 's/^#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/g' docs/conf.py

%build
export PROJ_DIR="%{_usr}/"

%py3_build

# generate documentation
cd docs

# Need to point to the build dir so sphinx can import the module
# before it is installed.
# Note that %%{_arch} does not work for all architectures
# so some if/then's are needed here, since I could not find any
# standard macro that solves this.
%ifarch x86_64 aarch64 ppc64le s390x
  %global py_build_libdir lib.linux-%{_arch}-%{python3_version}
%endif
%ifarch i686
  # %%{_arch} seems to expand to i386 here which does not work
  # so make explicit what we need
  %global py_build_libdir lib.linux-i686-%{python3_version}
%endif
%ifarch armv7hl
  # %%{_arch} seems to expand to arm here which does not work
  # so make explicit what we need
  %global py_build_libdir lib.linux-armv7l-%{python3_version}
%endif

PYTHONPATH=%{_builddir}/%{name}-%{version}/build/%{py_build_libdir}/ make html
PYTHONPATH=%{_builddir}/%{name}-%{version}/build/%{py_build_libdir}/ make man

# rpmlint complains many times with the rather cryptic warning:
#     "a special character is not allowed in a name"
# Actually for this man page this indicates a syntax error, since
# it does not have a space after ".B" in many places.
# (it is not clear to me where this originates, from the sphinx tool
#  or the input sources.)
# This sed command corrects for this problem.
sed -i -e 's/^\.B\\-/\.B \\-/g' %{_builddir}/%{name}-%{version}/docs/_build/man/pyproj.1
 
%install
export PROJ_DIR="%{_usr}/"

%py3_install

# ensure the autogenerated hidden .buildinfo file is not included
# since rpmlint does not like hidden files in the documentation
%{__rm} %{_builddir}/%{name}-%{version}/docs/_build/html/.buildinfo

# copy documentation
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -r %{_builddir}/%{name}-%{version}/docs/_build/html \
      %{buildroot}%{_datadir}/doc/%{name}/html

# copy pyproj man page
mkdir -p %{buildroot}/%{_mandir}/man1
cp %{_builddir}/%{name}-%{version}/docs/_build/man/pyproj.1 \
   %{buildroot}/%{_mandir}/man1/

# correct wrong write permission for group
%{__chmod} 755 %{buildroot}/%{python3_sitearch}/%{name}/*.so

# remove the rpath setting from _proj.so
chrpath -d %{buildroot}/%{python3_sitearch}/%{name}/*.so


%check

# follow the hint given in pyproj github issue
# https://github.com/pyproj4/pyproj/issues/647
# i.e. take the test folder outside the build folder
# to prevent the
#    cannot import name '_datadir' from partially initialized module
#    'pyproj' (most likely due to a circular import) 
# error.
cd ..
mkdir pyproj-test-folder
cd pyproj-test-folder
cp -r ../pyproj-%{version}/test .
cp -r ../pyproj-%{version}/pytest.ini .

PATH="%{buildroot}%{_bindir}:$PATH" PYTHONPATH="%{buildroot}%{python3_sitearch}" \
py.test-3 -m "not network"

%files -n python3-%{name}
%doc docs README.md
%{_bindir}/%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-*-py*.egg-info/
%{_mandir}/man1/pyproj*

%files -n python3-%{name}-doc
%doc %{_datadir}/doc/%{name}/


%changelog
* Wed Mar 10 2021 Sandro Mani <manisandro@gmail.com> - 3.0.1-2
- Rebuild (proj)

* Tue Mar 09 2021 Jos de Kloe <josdekloe@gmail.com> 3.0.1-1
- Update to 3.0.1
- Add man page for standalone pyproj tool

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 3.0.0.post1-3
- Rebuild (proj)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.post1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 3.0.0.post1-1
- Update to 3.0.0 for proj-7.2.0 compatibility

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1.post1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.1.post1-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Jos de Kloe <josdekloe@gmail.com> 2.6.1.post1-1
- Update to 2.6.1.post1

* Thu Mar 19 2020 Jos de Kloe <josdekloe@gmail.com> 2.6.0-1
- Update to 2.6.0

* Sat Feb 29 2020 Jos de Kloe <josdekloe@gmail.com> 2.5.0-1
- Update to 2.5.0

* Sun Dec 01 2019 Jos de Kloe <josdekloe@gmail.com> 2.4.2.post1-1
- Update to 2.4.2.post1 and remove patch (fix was included upstream)

* Sat Nov 23 2019 Jos de Kloe <josdekloe@gmail.com> 2.4.1-2
- Patch bug that caused 6 failing tests on i686 architecture
  and clean up some no longer needed fixes

* Sat Nov 9 2019 Jos de Kloe <josdekloe@gmail.com> 2.4.1-1
- Update to 2.4.1

* Sun Sep 08 2019 Jos de Kloe <josdekloe@gmail.com> 2.3.1-2
- add documentation generation, fix python usage in it and add a doc subpackage

* Wed Sep 4 2019 Devrim Gündüz <devrim@gunduz.org> - 2.3.1-1
- Update to 2.3.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.6-2
- Subpackage python2-pyproj has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Feb 17 2019 Jos de Kloe <josdekloe@gmail.com> 1.9.6-1
- update to version 1.9.6, remove python2 sub-package for Fedora 30+
- remove use of py3dir macro when building python3 sub-package

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.9.5.1-18
- Rebuilt for updated Proj

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 17 2018 Jos de Kloe <josdekloe@gmail.com> 1.9.5.1-16
- merge with cython patch by Miro Hrončok <pagure@pkgs.fedoraproject.org>
  (there is no more cython3 command; Cython behaves the same on both Pythons)
- remove the no_inv_hammer_test patch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.5.1-14
- Rebuilt for Python 3.7

* Sat Feb 24 2018 Jos de Kloe <josdekloe@gmail.com> 1.9.5.1-13
- Add explicit BuildRequires for gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.9.5.1-9
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu Jul 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.9.5.1-8
- move package specific (Build)Requires in the correspondig sub-packages

* Thu Jul 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.9.5.1-7
- setup filtering for private libs correctly

* Fri Jun 30 2017 Jos de Kloe <josdekloe@gmail.com> 1.9.5.1-6
- rename pyproj to python2-pyproj following the new package naming scheme

* Wed Feb 01 2017 Jos de Kloe <josdekloe@gmail.com> 1.9.5.1-5
- force rebuild after libproj soname jump

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.5.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jos de Kloe <josdekloe@gmail.com> 1.9.5.1-1
- update to new upstream version
- remove the inverse hammer test

* Thu Nov 12 2015 Jos de Kloe <josdekloe@gmail.com> 1.9.4-4
- apply patch to fix a bug in _proj.pyx that surfaced in cython 0.23
- apply chrpath to fix binary-or-shlib-defines-rpath error reported by rpmlint

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Jos de Kloe <josdekloe@gmail.com> 1.9.4-1
- update to version 1.9.4
- replace python_sitearch macro with python2_sitearch
- replace the deprecated macro __python by __python3
- activate the check section

* Sat Jan 11 2014 Jos de Kloe <josdekloe@gmail.com> 1.9.2-8.20120712svn300
- replace the deprecated macro __python by __python2
- require proj-epsg to solve bug #1022238

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-7.20120712svn300
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-6.20120712svn300
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 12 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.2-5.20120712svn300
- adapted version number format to comply to the Snapshot packages 
  guidelines, and move to svn revision 300.

* Wed Jun 20 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.2-4.r298
- Added proj-nad as explicit Requirement since it contains data files needed
  to run the module, and bumped the version number to the one mentioned in 
  the setup-proj.py script

* Fri Jun 15 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.0-3.r298
- Adapted to build with python3

* Thu May 31 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.0-2.r298
- Adapted to svn revision r298 which has some modifications
  to allow building without using the included proj sources

* Mon Apr 23 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.0-1
- Initial package for Fedora