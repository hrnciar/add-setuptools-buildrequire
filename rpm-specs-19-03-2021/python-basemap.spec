%global debug_package %{nil}

Name:           python-basemap
Version:        1.2.2
Release:        3%{?dist}
Summary:        Plots data on map projections (with continental and political boundaries) 
License:        LGPLv2+
URL:            https://matplotlib.org/basemap/
Source0:        https://github.com/matplotlib/basemap/archive/v%{version}rel/basemap-%{version}.tar.gz

BuildRequires:  gcc

%global _description\
Basemap is a matplotlib toolkit that allows you to plot data on map\
projections (with continental and political boundaries).

%description %_description

%package -n     python-basemap-examples
Summary:        Example programs and data for python3-basemap
License:        Copyright only
Requires:       python3-basemap

%description -n python-basemap-examples
%{summary}.

%package -n python3-basemap
Summary:        Plots data on map projections (with continental and political boundaries)
License:        LGPLv2+
BuildRequires:  python3-devel, proj-devel, shapelib-devel, python3-numpy-f2py, geos-devel
BuildRequires:  python3-setuptools
# Needed to regenerate Cython generated files.
BuildRequires:  python3-Cython
BuildRequires:  python3-httplib2
BuildRequires:  python3-matplotlib >= 0.98
BuildRequires:  python3-pyproj
Requires:       python3-matplotlib >= 0.98
Provides: python3-basemap-data = %{version}-%{release}
Obsoletes: python3-basemap-data < %{version}-%{release}

%description -n python3-basemap
Basemap is a matplotlib toolkit that allows you to plot data on map
projections (with continental and political boundaries).

%prep
%autosetup -n basemap-%{version}rel -p1
# Remove the bundled libraries
rm -rf goes-3.3.3/

%build
# regenerate Cython generated files
%{__python3} -m cython src/*.pyx
export GEOS_LIB="/usr/"
%{__python3} setup.py config
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    %{__python3} -c 'from mpl_toolkits.basemap import Basemap'

%files -n python-basemap-examples
%doc examples/*

%files -n python3-basemap
%license LICENSE_data LICENSE_epsg
%doc Changelog README.md
%{python3_sitearch}/mpl_toolkits/basemap
%{python3_sitearch}/*.egg-info
%{python3_sitearch}/basemap-1.2.1-py%{python3_version}-nspkg.pth
%{python3_sitearch}/_geoslib.cpython-3*.so


%changelog
* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 1.2.2-3
- Rebuild (geos)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.2.2-1
- 1.2.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.2.1-4
- BR python3-setuptools

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.2.1-1
- 1.2.1, move -data to this SRPM.

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Fri Feb 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.0.7-29
- Drop python2 support.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Marcel Plch <mplch@redhat.com> - 1.0.7-27
- Make build regenerate Cython files

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.0.7-25
- Rebuilt for Python 3.7

* Sat May 05 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.0.7-24
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build)

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-23
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.7-21
- Fix python2 package name

* Sat Aug 19 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.7-20
- Python 2 binary package renamed to python2-basemap
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 1.0.7-16
- geos rebuild.

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 1.0.7-15
- Rebuild for Python 3.6

* Fri Dec 09 2016 Jon Ciesla <limburgher@gmail.com> - 1.0.7-14
- Patch for numpy change, BZ 1403159.

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.0.7-13
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Jon Ciesla <limburgher@gmail.com> - 1.0.7-10
- Fix Python 3 build.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 14 2015 Jon Ciesla <limburgher@gmail.com> - 1.0.7-8
- geos rebuild.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.0.7-6
- Add a patch fixing the location of basemap_datadir
- Replace the sed command that did not work by a patch that does work, fixes
  RHBZ#1177052

* Wed Jan 14 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.0.7-5
- Fix the location of the datadir. Fixes RHBZ#1177052

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 13 2014 Jon Ciesla <limburgher@gmail.com> - 1.0.7-1
- Latest upstream, Python3 support, BZ 1076037.
- Dropped datadir patch, no longer needed.

* Fri Oct 04 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.6-5
- geos rebuild.

* Thu Sep 12 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.6-4
- geos rebuild.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Devrim G??ND??Z <devrim@gunduz.org> - 1.0.6-2
- Rebuild with new geos.

* Mon Feb 04 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.6-1
- Latest upstream, 870640.

* Sun Jan 27 2013 Jon Ciesla <limburgher@gmail.com> - 0.99.4-17
- Rebuild for geos soname bump.

* Mon Nov 19 2012 Devrim G??ND??Z <devrim@gunduz.org> - 0.99.4-16
- Rebuild with newer geos.

* Wed Nov 14 2012 Jon Ciesla <limburgher@gmail.com> - 0.99.4-15
- Rebuild for geos soname bump.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Jon Ciesla <limburgher@gmail.com> - 0.99.4-13
- Rebuild for geos soname bump.

* Wed Oct 05 2011 Jon Ciesla <limb@jcomserv.net> - 0.99.4-12
- Rebuild for geos soname bump.

* Fri Jun 03 2011 Jon Ciesla <limb@jcomserv.net> - 0.99.4-11
- Rebuild for geos soname bump.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.99.4-9
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 03 2010 Jef Spaleta <jspaleta@fedoraproject.org> - 0.99.4-8
- update the homepage url 

* Fri May 28 2010 Jef Spaleta <jspaleta@fedoraproject.org> - 0.99.4-7
- Examples is now a subpackage of python-basemap instead of python-basemap-data 

* Mon Apr 12 2010 Jef Spaleta <jspaleta@fedoraproject.org> - 0.99.4-6
- Fix the data directory patch. 

* Mon Apr 12 2010 Jef Spaleta <jspaleta@fedoraproject.org> - 0.99.4-5
- Rebuild to for geos soname bump and numpy 1.3 reversion. 

* Thu Apr 01 2010 Jef Spaleta <jspaleta@fedoraproject.org> - 0.99.4-4
- Added back the data directory patch. It is needed to correctly set the 
  default location of system data files provided by the python-basemap-data 
  package.  Setting the environment variable at build time is not sufficient 
  to set the correct system-wide location for distribution packaging.  

* Thu Apr 01 2010 Jef Spaleta <jspaleta@fedoraproject.org> - 0.99.4-3
- Rebuild to fix numpy ABI change.

* Fri Jan 08 2010 Jon Ciesla <limb@jcomserv.net> - 0.99.4-2
- Rebuild for broken dep.

* Fri Dec 11 2009 Jon Ciesla <limb@jcomserv.net> - 0.99.4-1
- Update to latest upstream.
- Dropped datadir patch, now handled with environment variable.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Caol??n McNamara <caolanm@redhat.com> - 0.99.2-4
- Resolves: rhbz#511576 FTBFS showimg numpy -> numpy-f2py

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.99.2-2
- Update data directory patch

* Thu Dec 11 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.99.2-1
- Update to latest release

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.99-6
- Rebuild for Python 2.6

* Thu Oct 23 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.99-5
- Also patch runtime GEOS version check (as discussed on the fedora-devel-list)

* Sun Oct 19 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.99-4
- Update -setup.py patch for geos 3.0.1

* Sun Oct 19 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.99-3
- Rebuild for new geos, fixes broken deps

* Fri Jul 11 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.99-2
- File conflict fix for Bug 455005

* Wed Jul 02 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.99-1
- Update to match latest matplotlib 

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.5-5
- Autorebuild for GCC 4.3

* Fri Jan 04 2008 Jef Spaleta <jspaleta@fedoraproject.org> 0.9.5-4
- Fix for egg-info file creation

* Thu Aug 23 2007 Orion Poplawski <orion@cora.nwra.com> 0.9.5-3
- Explicitly remove included libraries in prep
- Update license tag to LGPLv2+
- Rebuild for BuildID

* Wed Jun 06 2007 Orion Poplawski <orion@cora.nwra.com> 0.9.5-2
- Rebuild

* Fri Mar 23 2007 Orion Poplawski <orion@cora.nwra.com> 0.9.5-1
- Update to 0.9.5
- Ship the examples in a separate rpm

* Mon Dec 11 2006 Orion Poplawski <orion@cora.nwra.com> 0.9.4-2
- Remove unnecessary (and damaging) line ending change

* Mon Nov 20 2006 Orion Poplawski <orion@cora.nwra.com> 0.9.4-1
- Update to upstream 0.9.4

* Wed Oct 18 2006 Orion Poplawski <orion@cora.nwra.com> 0.9.3-1
- Update to upstream 0.9.3

* Thu Sep  7 2006 Orion Poplawski <orion@cora.nwra.com> 0.9.2-1
- Update to upstream 0.9.2

* Fri Jul 28 2006 Orion Poplawski <orion@cora.nwra.com> 0.9.1-1
- Update to upstream 0.9.1

* Mon Jul  3 2006 Orion Poplawski <orion@cora.nwra.com> 0.9-1
- Update to upstream 0.9

* Mon Mar  6 2006 Orion Poplawski <orion@cora.nwra.com> 0.8.2-3
- Rebuild for updated shapelib

* Tue Feb 28 2006 Orion Poplawski <orion@cora.nwra.com> 0.8.2-2
- python-matplotlib now owns toolkits directoery

* Mon Feb 27 2006 Orion Poplawski <orion@cora.nwra.com> 0.8.2-1
- Update to upstream 0.8.2

* Fri Feb 24 2006 Orion Poplawski <orion@cora.nwra.com> 0.8.1-1
- Update to upstream 0.8.1

* Sun Nov 20 2005 Orion Poplawski <orion@cora.nwra.com> 0.7.2.1-1
- Update to upstream 0.7.2.1
- Split into python-basemap and python-basemap-data
- No longer requires python-numarray
- Use system shapelib for pyshapelib components

* Tue Sep 13 2005 Orion Poplawski <orion@cora.nwra.com> 0.6.2-1
- Update to upstream 0.6.2

* Tue Aug 02 2005 Orion Poplawski <orion@cora.nwra.com> 0.5.2-1
- Initial package for Fedora Extras
