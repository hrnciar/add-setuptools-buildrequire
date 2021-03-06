%global pname MDAnalysis
%bcond_without check

Name: python-%{pname}
Version: 0.20.1
Release: 6%{?dist}
Summary: Analyze and manipulate molecular dynamics trajectories
License: GPLv2+ and BSD and MIT and CC-BY-ND
# BSD:
# MDAnalysis/lib/formats/*/xdrfile*
# MDAnalysis/lib/qcprot.pyx
# MDAnalysis/lib/src/transformations/transformations.c
# MDAnalysis/lib/transformations.py
# MIT:
# MDAnalysisTests-0.16.0/MDAnalysisTests/tempdir.py
# CC-BY-ND:
# doc/sphinx/source/_static/logos
# GPLv2+:
# everything else
URL: http://www.mdanalysis.org
Source0: https://files.pythonhosted.org/packages/source/M/%{pname}/%{pname}-%{version}.tar.gz
Source1: https://files.pythonhosted.org/packages/source/M/%{pname}Tests/%{pname}Tests-%{version}.tar.gz
Source2: https://github.com/%{pname}/mdanalysis/files/1935925/pypidoc.zip
# force rebuild of cythonized intermediate sources
Patch1: %{name}-cython.patch
Patch2: %{name}-flags.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1853117
Patch3: 2763.patch
# 32-bit archs: https://github.com/MDAnalysis/mdanalysis/issues/2342
# ppc64le, aarch64: https://github.com/MDAnalysis/mdanalysis/issues/2343
ExcludeArch: i686 armv7hl s390x ppc64le aarch64
# we don't want to provide private python extension libs in python3 dirs
# there are actually called lib...so, so this is needed
%global __provides_exclude_from ^%{python3_sitearch}/.*\\.so$

%global desc \
MDAnalysis is a python framework to analyze molecular dynamics trajectories\
generated by CHARMM, NAMD, LAMMPS, or Gromacs. It is mainly useful for geometric\
analyses, as there is no implemented potential model. \
\
It is inspired by the Schulten Group's MDtools for python, and the source for\
the DCD reading code is derived from VMD. MDAnalysis isGPL licensed, except for\
the dcd reading code (UIUC Open Source Licence) which comes from VMD (and is\
GPL-compatible). Gromacs trajectories are utilizing the Gromacs libxdrfile\
library (GPL). MDAnalysis exposes trajectory data transparently as NumPy arrays\
and as such it is easily extensible.

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
Requires: python3-biopython
Requires: python3-GridDataFormats >= 0.4.0
Requires: python3-gsd
Requires: python3-joblib
Requires: python3-matplotlib
Requires: python3-mmtf
Requires: python3-networkx
Requires: python3-numpy
Requires: python3-scipy
# optional deps
# this should also include matplotlib and scipy,
# but their lack is not handled gracefully
# https://github.com/MDAnalysis/mdanalysis/issues/1361
Recommends: python3-netcdf4
Recommends: python3-scikit-learn
Recommends: python3-seaborn
BuildRequires: python3-Cython
BuildRequires: python3-devel
BuildRequires: python3-gsd
BuildRequires: python3-numpy
BuildRequires: python3-setuptools
%if %{with check}
BuildRequires: python3-biopython
BuildRequires: python3-GridDataFormats >= 0.4.0
BuildRequires: python3-hypothesis
BuildRequires: python3-joblib
BuildRequires: python3-matplotlib
BuildRequires: python3-mmtf
BuildRequires: python3-mock
BuildRequires: python3-netcdf4
BuildRequires: python3-networkx
BuildRequires: python3-psutil
BuildRequires: python3-pytest-xdist
BuildRequires: python3-scikit-learn
BuildRequires: python3-tempdir
%endif
BuildRequires: gcc-c++
# MDAnalysis/coordinates/xdrfile/src
Provides: bundled(xdrfile) = 0.7.7
%{?python_provide:%python_provide python3-%{pname}}

%description -n python3-%{pname}
%{desc}

%package doc
Summary: Documentation for MDAnalysis
BuildArch: noarch
License: CC-BY-ND and GPLv2+

%description doc
MDAnalysis is a python framework to analyze molecular dynamics trajectories
generated by CHARMM, NAMD, LAMMPS, or Gromacs. It is mainly useful for geometric
analyses, as there is no implemented potential model.

This package contains the documentation

%prep
%setup -q -n %{pname}-%{version} -a 1
%patch1 -p1 -b .cython
%patch2 -p1 -b .flags
%patch3 -p1
# force rebuild of Egg Metadata
rm -r %{pname}.egg-info
rm -r %{pname}Tests-%{version}/%{pname}Tests.egg-info
chmod -x %{pname}Tests-%{version}/%{pname}Tests/data/dlpoly/CONFIG*

%build
%{py3_build}

pushd %{pname}Tests-%{version}
%{py3_build}
popd

mkdir -p doc/html
unzip -qq -o %{SOURCE2} -d doc/html
find doc/html -type d |xargs chmod 755

%install
%{py3_install}
find %{buildroot}%{python3_sitearch}/%{pname} -type f -name "*.so" | xargs chmod 755

pushd %{pname}Tests-%{version}
%{py3_install}
popd

%if %{with check}
%check
# https://github.com/MDAnalysis/mdanalysis/wiki/UnitTests#recommended
# skip some tests for now
# https://github.com/MDAnalysis/mdanalysis/issues/1969
# https://github.com/MDAnalysis/mdanalysis/issues/1970
# GSD test needs a native-endian sample, so skip on big-endian for now
# https://github.com/MDAnalysis/mdanalysis/issues/1829
cd %{pname}Tests-%{version}/%{pname}Tests
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} \
 pytest-%{python3_version} \
 -v \
 --disable-pytest-warnings \
 --numprocesses=auto \
 -k 'not test_hes \
 and not test_clustering_KMeans_direct \
 and not test_clustering_method_w_no_distance_matrix \
%ifarch s390x
 and not test_clustering_three_ensembles_two_identical \
 and not test_rmsd \
 and not (test_rms and test_custom_weighted) \
 and not (test_rms and test_mass_weighted) \
 and not (test_chainreader and test_time) \
 and not test_dcd \
 and not (test_lammps and test_Timestep_time) \
 and not (test_lammps and test_dt) \
 and not test_rename_aux \
 and not test_iter_as_aux_lowf \
 and not test_iter_as_aux_highf \
%endif
%ifarch ppc64 s390x
 and not test_gsd \
%endif
 and not test_clustering_two_methods_one_w_no_distance_matrix' \

%endif

%files -n python3-%{pname}
%license LICENSE
%doc AUTHORS CHANGELOG README SUMMARY.txt
%{python3_sitearch}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pname}
%exclude %{python3_sitelib}/%{pname}Tests-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/%{pname}Tests

%files doc
%license LICENSE
%doc doc/html/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Christoph Junghans <junghans@votca.org> - 0.20.1-4
- Fix build with matplotlib 3.3.0rc1 (bug #1853117)

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.20.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Christoph Junghans <junghans@votca.org> - 0.20.1-1
- Version bump to 0.20.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.18.0-2
- Switch to Python 3

* Mon Jul 02 2018 Dominik Mierzejewski <rpm@greysector.net> - 0.18.0-1
- update to 0.18.0
- drop obsolete patches
- fix analysis tests on 32bit
- new dependency: python-gsd
- upstream switched from nose to pytest for testing
- use standard bcond to enable/disable tests
- use pytest options to skip some tests instead of patching them out

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Dominik Mierzejewski <rpm@greysector.net> - 0.16.2-1
- update to 0.16.2
- update doc tarball URL and handling
- drop obsolete patch

* Thu Jun 22 2017 Dominik Mierzejewski <rpm@greysector.net> - 0.16.1-3
- fix endianness issues on BE arches (ppc64, s390x)
- increase test process timeout (was timing out on aarch64)

* Sat Jun 17 2017 Dominik Mierzejewski <rpm@greysector.net> - 0.16.1-2
- backport more fixes from git

* Thu Jun 08 2017 Dominik Mierzejewski <rpm@greysector.net> - 0.16.1-1
- update to 0.16.1
- fix test failures on 32bit

* Thu May 18 2017 Dominik Mierzejewski <rpm@greysector.net> - 0.16.0-1
- update to 0.16.0
- drop obsolete patches
- add new dependencies (joblib, mmtf, mock, psutil)
- fix netcdf4-python dependencies (need python2-netcdf4, actually)
- switch to nosetests while strange test failures are investigated
  (https://github.com/MDAnalysis/mdanalysis/issues/1360)
- add a link to upstream-recommended way of running tests
- modernize python module dependencies

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.14.0-4
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 15 2016 Dominik Mierzejewski <rpm@greysector.net> 0.14.0-2
- fix non-standard-dir-perm in doc subpackage
- move python2 build to python2-MDAnalysis subpackage
- exclude private libmdaxdr.so from Provides:

* Fri Mar 11 2016 Dominik Mierzejewski <rpm@greysector.net> 0.14.0-1
- update to 0.14.0
- don't build docs for now, upstream published them in a zip file
- drop obsolete patch
- fix tests with numpy 1.11
- fix license field for docs subpackage
- install LICENSE with the doc subpackage as well
- move building of docs to the build section
- use some python-related convenience macros

* Tue Feb 09 2016 Dominik Mierzejewski <rpm@greysector.net> 0.13.0-2
- build docs
- new dependency: seaborn
- omit failing tests on f24 for now

* Mon Feb 08 2016 Dominik Mierzejewski <rpm@greysector.net> 0.13.0-1
- update to 0.13.0
- fix running tests
- add Provides for bundled xdrfile
- docs not included and failing to build, so disable for now

* Wed Oct 14 2015 Dominik Mierzejewski <rpm@greysector.net> 0.12.1-1
- update to 0.12.1
- drop obsolete patch
- use the new mda_nosetests script for running tests

* Mon May 18 2015 Dominik Mierzejewski <rpm@greysector.net> 0.9.2-4
- relax Improper Torsion topology test check on i686

* Mon May 11 2015 Dominik Mierzejewski <rpm@greysector.net> 0.9.2-3
- document licensing breakdown
- package docs

* Fri May 08 2015 Dominik Mierzejewski <rpm@greysector.net> 0.9.2-2
- call the testsuite per upstream docs

* Wed May 06 2015 Dominik Mierzejewski <rpm@greysector.net> 0.9.2-1
- update to 0.9.2
- update upstream URL
- drop obsolete patch
- fix testsuite invocation

* Wed Feb 04 2015 Dominik Mierzejewski <rpm@greysector.net> 0.8.1-1
- initial build
