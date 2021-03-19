Summary:        Generic Programming for Computer Vision
Name:           vigra
Version:        1.11.1
Release:        27%{?dist}
License:        MIT
# The "Lenna" files are non-free, we need to remove them from the source tarball.
# wget https://github.com/ukoethe/vigra/releases/download/Version-1-11-1/vigra-1.11.1-src.tar.gz
# tar xf vigra-1.11.1-src.tar.gz
# find vigra-1.11.1/ -name "lenna*" -delete
# tar zcf vigra-1.11.1-src-clean.tar.gz vigra-1.11.1/
Source0:        %{name}-%{version}-src-clean.tar.gz
Source1:        vigra-config.sh
# Backported from upstream master, fixes a build failure:
# https://github.com/ukoethe/vigra/issues/414
Patch0:         https://github.com/ukoethe/vigra/commit/81958d302494e137f98a8b1d7869841532f90388.patch
# Avoid attempt to install non-free 'lenna' files
Patch1:         vigra-1.10.0-no-lenna.patch
Patch2:         vigra-1.11.1.docdir.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1597394
Patch3:         vigra-1.11.1.py37.patch
URL:            http://ukoethe.github.io/vigra/
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  fftw-devel >= 3
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  doxygen
%if ! 0%{?rhel}
Requires: python3
BuildRequires:  hdf5-devel
BuildRequires:  python3-sphinx
BuildRequires:  OpenEXR-devel
BuildRequires:  python3-numpy-f2py
BuildRequires:  boost-python3
BuildRequires:  boost-python3-devel
%else
Requires: python
%endif

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel computer vision
library that puts its main emphasis on customizable algorithms and data
structures. By using template techniques similar to those in the C++ Standard
Template Library, you can easily adapt any VIGRA component to the needs of your
application without thereby giving up execution speed.

#'

%package devel
Summary: Development tools for programs which will use the vigra library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libjpeg-devel libtiff-devel libpng-devel zlib-devel fftw-devel >= 3
Requires: boost-devel
%if ! 0%{?rhel}
Requires: hdf5-devel
Requires: OpenEXR-devel
Requires: python3-numpy-f2py boost-python3 boost-python3-devel
%endif

%description devel
The vigra-devel package includes the header files necessary for developing
programs that use the vigra library.

%if ! 0%{?rhel}
%package -n python3-vigra
%{?python_provide:%python_provide python3-vigra}
Summary: Python 3 interface for the vigra computer vision library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-numpy python3-numpy-f2py

%description -n python3-vigra
The python3-vigra package provides python 3 bindings for vigra
%endif

%prep
%autosetup -p1

%build
# Will need to set LEMON_DIR to /usr/share/coin-or-lemon/cmake to compile WITH_LEMON
# once the coin-or-lemon package's installed cmake is fixed for x86_64 arch.
%if ! 0%{?rhel}
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' \
       config/vigra-config.in
sed -i 's=SET(BOOST_PYTHON_NAMES=& boost_python%{python3_version_nodots}=' \
      config/FindVIGRANUMPY_DEPENDENCIES.cmake

%cmake -DWITH_OPENEXR=1 -DWITH_HDF5=1 -DWITH_VALGRIND=0 -DWITH_LEMON=0 \
          -DWITH_VIGRANUMPY=1 -DPYTHON_VERSION=%{python3_version}
%cmake_build
%else
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python}=' \
      config/vigra-config.in

%cmake . -DWITH_OPENEXR=0 -DWITH_HDF5=0 -DWITH_VIGRANUMPY=0 -DWITH_VALGRIND=0 -DWITH_LEMON=0
make VERBOSE=1 %{?_smp_mflags}
%endif

# cleanup
rm -f doc/vigranumpy/.buildinfo
rm -f doc/vigra/lenna*
rm -f doc/vigranumpy/vigra/lenna*
find ./doc/ -type f | xargs chmod -x

%install
rm -rf %{buildroot}

%if ! 0%{?rhel}
%cmake_install
mv %{buildroot}/%{_libdir}/vigranumpy/VigranumpyConfig.cmake \
   %{buildroot}/%{_libdir}/vigranumpy/Vigranumpy3Config.cmake

%else
make install DESTDIR=%{buildroot}
%endif

rm -rf %{buildroot}/usr/doc
(
 cd $RPM_BUILD_ROOT%{_bindir}
 mv vigra-config vigra-config-%{__isa_bits}
)
install -p -m755 -D %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/vigra-config

#fixme: this fails,
#%check
#make VERBOSE=1 check

%ldconfig_scriptlets

%files
%doc LICENSE.txt
%{_libdir}/libvigraimpex.so.*

%files devel
%{_includedir}/vigra
%{_bindir}/vigra-config*
%{_libdir}/libvigraimpex.so
%{_libdir}/vigra
%doc doc/vigra doc/vigranumpy

%if ! 0%{?rhel}
%files -n python3-vigra
%{python3_sitearch}/vigra
%{_libdir}/vigranumpy
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.11.1-26
- Rebuilt for Boost 1.75

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 1.11.1-25
- Rebuild for OpenEXR 2.5.3.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Bruno Postle <bruno@postle.net> - 1.11.1-23
- Rebuild for changed cmake macros

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 1.11.1-22
- Rebuild for hdf5 1.10.6

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.11.1-21
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-20
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-17
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 1.11.1-15
- Rebuild for OpenEXR 2.3.0.

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.11.1-14
- Rebuild for hdf5 1.10.5

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.11.1-12
- Rebuilt for Boost 1.69

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-11
- Subpackage python2-vigra has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Aug 22 2018 Bruno Postle <bruno@postle.net> - 1.11.1-10
- Patched for python 3.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-8
- Rebuilt for Python 3.7

* Tue May 01 2018 Jonathan Wakely <jwakely@redhat.com> - 1.11.1-7
- Require boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.11.1-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")
- Clean tarball of non-free image files (bump to 1.11.1 omitted this)
- Backport patch from upstream to fix build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Troy Curtis, Jr <troycurtisjr@gmail.com> - 1.11.1-4
- Add python3 subpackage
- Disable compiling with LEMON
- Move python shebang fix into spec file.

* Wed Dec 13 2017 Bruno Postle <bruno@postle.net> - 1.11.1-3
- fix -devel dependency on boost-python2

* Mon Dec 11 2017 Bruno Postle <bruno@postle.net> - 1.11.1-2
- Remove 'lenna' images

* Sun Dec 10 2017 Bruno Postle <bruno@postle.net> - 1.11.1-1
- Upstream stable release

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.11.0-11
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.11.0-10
- Python 2 binary package renamed to python2-vigra
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.11.0-7
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 1.11.0-6
- Rebuilt for Boost 1.64

* Fri Feb 17 2017 Jonathan Wakely <jwakely@redhat.com> - 1.11.0-5
- Fix build failure with GCC 7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 1.11.0-4
- Rebuild for hdf5 1.8.18

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 1.11.0-2
- Rebuild for hdf5 1.8.17

* Wed Apr 13 2016 Bruno Postle <bruno@postle.net> - 1.11.0-1
- Upstream stable release

* Tue Feb  2 2016 Tom Callaway <spot@fedoraproject.org> - 1.10.0-18
- remove lenna files (non-free)

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.10.0-17
- Rebuild for hdf5 1.8.16

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-16
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-15
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.10.0-13
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.10.0-11
- Rebuild for hdf5 1.8.15

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.10.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 1.10.0-9
- Bump for rebuild.

* Mon Feb 02 2015 Bruno Postle <bruno@postle.net> - 1.10.0-8
- Fix for transparent alpha bug in 16bit and EXR output

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.10.0-7
- Rebuild for boost 1.57.0

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.10.0-6
- Rebuild for hdf5 1.8.14

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1.10.0-5
- rebuild (openexr), tighten subpkg deps (via %%{?_isa})

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.10.0-2
- Rebuild for boost 1.55.0

* Fri Dec 13 2013 Bruno Postle <bruno@postle.net> - 1.10.0-1
- upstream release

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.9.0-14
- rebuild (openexr)

* Sat Sep 21 2013 David Tardon <dtardon@redhat.com> - 1.9.0-13
- rebuild for atlas 3.10

* Thu Sep 12 2013 Caolán McNamara <caolanm@redhat.com> - 1.9.0-12
- bump n-v-r

* Thu Aug 29 2013 Caolán McNamara <caolanm@redhat.com> - 1.9.0-11
- Resolves: rhbz#884207 multi-lib vigra-config

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.9.0-9
- Rebuild for boost 1.54.0

* Wed Jul 24 2013 Caolán McNamara <caolanm@redhat.com> - 1.9.0-8
- Resolves: rhbz#987048 explicit python path in shebang

* Tue Jun 04 2013 Caolán McNamara <caolanm@redhat.com> - 1.9.0-7
- Resolves: rhbz#970561 no hdf5-devel in RHEL-7

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-6
- Rebuild for hdf5 1.8.11

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.9.0-5
- rebuild (OpenEXR)

* Thu Feb 14 2013 Caolán McNamara <caolanm@redhat.com> - 1.9.0-4
- no hdf5-devel in RHEL-7

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.9.0-3
- Rebuild for Boost-1.53.0

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.9.0-2
- rebuild due to "jpeg8-ABI" feature drop

* Tue Nov 06 2012 Bruno Postle <bruno@postle.net> 1.9.0-1
- upstream release, support impex OpenEXR

* Tue Nov 06 2012 Caolán McNamara <caolanm@redhat.com> - 1.8.0-7
- document that there is a test suite, but it fails

* Wed Oct 31 2012 Tom Callaway <spot@fedoraproject.org> - 1.8.0-6
- rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Bruno Postle <bruno@postle.net> 1.8.0-4
- patch to build with gcc-4.7.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.8.0-2
- Rebuild for new libpng

* Sat Sep 24 2011 Bruno Postle <bruno@postle.net> 1.8.0-1
- upstream release

* Fri Aug 26 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.1-4
- rebuild against boost

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 1.7.1-3
- Rebuild for hdf5 1.8.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Bruno Postle <bruno@postle.net> 1.7.1-1
- upstream release

* Fri Jul 30 2010 Toshio Kuratomi <toshio@fedoraproject.org> 1.7.0-2
- Rebuild for new python release

* Tue Apr 20 2010 Bruno Postle <bruno@postle.net> 1.7.0-1
- new upstream with cmake replacing autotools.
- patch for x86_64 systems.
- add vigra-python sub-package.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Bruno Postle - 1.6.0-1
- Update to latest release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Bruno Postle <bruno@postle.net> 1.5.0-3
  - Bumping for Jesse

* Mon Feb 19 2007 Bruno Postle <bruno@postle.net> 1.5.0-2
  - update to 1.5.0 release
  - fix bug 228926: vigra: $RPM_OPT_FLAGS not used

* Sun Nov 23 2003 Bruno Postle <bruno@postle.net>
  - initial package


