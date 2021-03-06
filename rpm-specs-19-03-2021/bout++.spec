Name:           bout++
Version:        4.3.2
Release:        6%{?dist}
Summary:        Library for the BOUndary Turbulence simulation framework

# BOUT++ itself is LGPL, but we are linking with GPLed code, so the distributed library is GPL
License:        GPLv3+
URL:            https://boutproject.github.io/
Source0:        https://github.com/boutproject/BOUT-dev/releases/download/v%{version}/BOUT++-v%{version}.tar.gz

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%else
%bcond_with flexiblas
%endif

# Disable tests and manual on epel < 8
%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_with manual
%bcond_with test
%bcond_with sundials
%bcond_with petsc
%else
%bcond_without manual
%bcond_without test
%bcond_without sundials
%bcond_without petsc
%endif

# Enable both mpi every where
%bcond_without mpich
%bcond_without openmpi

# Enable weak dependencies
%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} > 7 )
%bcond_without recommend
%else
%bcond_with recommend
%endif

%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} > 7 )
# Use system mpark
%bcond_without system_mpark
%else
%bcond_with system_mpark
%endif

#
#           DEPENDENCIES
#

BuildRequires:  m4
BuildRequires:  zlib-devel
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  gettext-devel
BuildRequires:  automake
BuildRequires:  environment-modules
BuildRequires:  netcdf-devel
BuildRequires:  netcdf-cxx%{?fedora:4}-devel
BuildRequires:  hdf5-devel
BuildRequires:  fftw-devel
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-netcdf4
BuildRequires:  python%{python3_pkgversion}-scipy
%if %{with flexiblas}
BuildRequires:  flexiblas-devel
%else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
%endif
BuildRequires:  gcc-c++
%if %{with system_mpark}
BuildRequires:  mpark-variant-devel
%endif
# cxx generation
BuildRequires:  python%{python3_pkgversion}-jinja2
# Documentation
%if %{with manual}
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
%endif
%if %{with petsc} && %{with mpich}
BuildRequires: petsc-mpich-devel
BuildRequires: hdf5-mpich-devel
%endif
%if %{with petsc} && %{with openmpi}
BuildRequires: petsc-openmpi-devel
BuildRequires: hdf5-openmpi-devel
%endif
%if %{with sundials} && %{with mpich}
BuildRequires: sundials-mpich-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1839131
BuildRequires: sundials-devel
%endif
%if %{with sundials} && %{with openmpi}
BuildRequires: sundials-openmpi-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1839131
BuildRequires: sundials-devel
%endif

#
#           DESCRIPTIONS
#


%if %{with mpich}
BuildRequires:  mpich-devel
%global mpi_list mpich
%endif
%if %{with openmpi}
BuildRequires:  openmpi-devel
%global mpi_list %{?mpi_list} openmpi
%endif

%description
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.



%if %{with mpich}
%package mpich
Summary: BOUT++ mpich libraries
Requires: %{name}-common = %{version}-%{release}
# Use bundled version, to reproduce upstream results
Provides: bundled(libpvode)
%if %{with recommend}
Recommends: environment-modules
%endif

%package mpich-devel
Summary: BOUT++ mpich libraries
Requires:  %{name}-mpich = %{version}-%{release}
Recommends:  gcc-c++
Recommends:  make
Recommends:  mpich-devel
Recommends:  zlib-devel
Recommends:  gettext-devel
Recommends:  netcdf-devel
Recommends:  netcdf-cxx%{?fedora:4}-devel
Recommends:  hdf5-devel
Recommends:  fftw-devel
%if %{with flexiblas}
Recommends:  flexiblas-devel
%else
Recommends:  blas-devel
Recommends:  lapack-devel
%endif
%if %{with system_mpark}
Recommends:  mpark-variant-devel
%endif
%if %{with petsc}
Recommends:  petsc-mpich-devel
Recommends:  hdf5-mpich-devel
%endif
%if %{with sundials}
Recommends:  sundials-mpich-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1839131
Recommends:  sundials-devel
%endif


%description mpich-devel
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This BOUT++ library is build for mpich.

%description mpich
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This BOUT++ library is build for mpich.

%package -n python%{python3_pkgversion}-%{name}-mpich
Summary:  BOUT++ mpich library for python%{python3_pkgversion}
Requires: %{name}-mpich
Requires: python%{python3_pkgversion}-%{name}
BuildRequires: python%{python3_pkgversion}-devel
Requires: mpich
Requires: python%{python3_pkgversion}-mpich
Requires: python%{python3_pkgversion}-numpy
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}-mpich}
%description  -n python%{python3_pkgversion}-%{name}-mpich
This is the BOUT++ library python%{python3_pkgversion} with mpich.

%endif




%if %{with openmpi}
%package openmpi
Summary: BOUT++ openmpi libraries
# Use bundled version, to reproduce upstream results
Provides: bundled(libpvode)
Requires: %{name}-common = %{version}-%{release}
%if %{with recommend}
Recommends: environment-modules
%endif

%package openmpi-devel
Summary: BOUT++ openmpi libraries
Requires: %{name}-openmpi = %{version}-%{release}
Recommends:  gcc-c++
Recommends:  make
Recommends:  openmpi-devel
Recommends:  zlib-devel
Recommends:  gettext-devel
Recommends:  netcdf-devel
Recommends:  netcdf-cxx%{?fedora:4}-devel
Recommends:  hdf5-devel
Recommends:  fftw-devel
%if %{with flexiblas}
Recommends:  flexiblas-devel
%else
Recommends:  blas-devel
Recommends:  lapack-devel
%endif
%if %{with system_mpark}
Recommends:  mpark-variant-devel
%endif
%if %{with petsc}
Recommends:  petsc-openmpi-devel
Recommends:  hdf5-openmpi-devel
%endif
%if %{with sundials}
Recommends:  sundials-openmpi-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1839131
Recommends:  sundials-devel
%endif



%description openmpi-devel
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This BOUT++ library is build for openmpi and provides the required
header files.

%description openmpi
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This BOUT++ library is build for openmpi.

%package -n python%{python3_pkgversion}-%{name}-openmpi
Summary:  BOUT++ openmpi library for python%{python3_pkgversion}
Requires: %{name}-openmpi
Requires: python%{python3_pkgversion}-%{name}
BuildRequires: python%{python3_pkgversion}-devel
Requires: openmpi
Requires: python%{python3_pkgversion}-openmpi
Requires: python%{python3_pkgversion}-numpy
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}-openmpi}

%description  -n python%{python3_pkgversion}-%{name}-openmpi
This is the BOUT++ library python%{python3_pkgversion} with openmpi.

%endif


%package common
Summary: Common files for BOUT++
%description common
MPI-independent files for BOUT++, namely localisation files.

%package -n python%{python3_pkgversion}-%{name}
Summary: BOUT++ python library
Requires: netcdf4-python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-numpy
%if %{with recommend}
Recommends: python%{python3_pkgversion}-scipy
Recommends: python%{python3_pkgversion}-matplotlib
%endif
BuildArch: noarch
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Provides:  python%{python3_pkgversion}-boututils
Provides:  python%{python3_pkgversion}-boutdata
Provides:  python%{python3_pkgversion}-bout_runners
Provides:  python%{python3_pkgversion}-zoidberg
%{?python_provide:%python_provide python%{python3_pkgversion}-bout_runners}
%{?python_provide:%python_provide python%{python3_pkgversion}-boututils}
%{?python_provide:%python_provide python%{python3_pkgversion}-boutdata}
%{?python_provide:%python_provide python%{python3_pkgversion}-zoidberg}

%description -n python%{python3_pkgversion}-%{name}
Python%{python3_pkgversion} library for pre and post processing of BOUT++ data




%if %{with manual}
%package -n %{name}-doc
Summary: BOUT++ Documentation
BuildArch: noarch

%description -n %{name}-doc
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This package contains the documentation.
%endif

#
#           PREP
#

%prep
%setup -q -n BOUT++-v%{version}

%if %{with system_mpark}
# use mpark provided by fedora
rm -rf externalpackages/mpark.variant/
mkdir -p externalpackages/mpark.variant/include/
%endif

# Remove shebang
for f in $(find -L tools/pylib/ -type f | grep -v _boutcore_build )
do
    sed -i '/^#!\//d' $f
done

autoreconf


#
#           BUILD
#

%build

# MPI builds
export CC=mpicc
export CXX=mpicxx

for mpi in %{mpi_list}
do
  mkdir build_$mpi
  cp -al [^b]* build-aux bin build_$mpi
done
for mpi in %{mpi_list}
do
  pushd build_$mpi
  if [ $mpi = mpich ] ; then
      %_mpich_load
  elif [ $mpi = openmpi ] ; then
      %_openmpi_load
  else
      echo "unknown mpi" &> /dev/stderr
      exit 1
  fi

  %configure \
	     --with-netcdf \
             --with-hdf5 \
             --enable-shared \
	     --with-system-mpark \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_datadir} \
%if %{with petsc}
           --with-petsc \
%endif
%if %{with sundials}
           --with-sundials \
%endif

  sed -e "s| -L%{_libdir} | |g" \
      -e "s| -Wl,--as-needed | |g" \
      -i make.config

  # Debug linking issues:
  # -e 's|@$(LD)|$(LD)|'  \

  %if %{with flexiblas}
  sed -e 's|-lblas|-lflexiblas|g' \
      -e 's|-llapack|-lflexiblas|g' \
      -i make.config
  %endif
  cat make.config

  make %{?_smp_mflags} shared python
  export LD_LIBRARY_PATH=$(pwd)/lib
  %if %{with manual}
  make %{?_smp_mflags} -C manual html
  %endif
  if [ $mpi = mpich ] ; then
      %_mpich_unload
  elif [ $mpi = openmpi ] ; then
      %_openmpi_unload
  fi
  popd
done

#
#           INSTALL
#

%install

for mpi in %{mpi_list}
do
  pushd build_$mpi
  if [ $mpi = mpich ] ; then
      %_mpich_load
  else
      %_openmpi_load
  fi
  make install DESTDIR=${RPM_BUILD_ROOT}

  # mark this as a released version, to disable compiling the library
  sed -i '27 i RELEASED                 = %{version}-%{release}' ${RPM_BUILD_ROOT}/%{_includedir}/${mpi}-%{_arch}/bout++/make.config

  rm -rf  ${RPM_BUILD_ROOT}/usr/share/bout++
  rm -f ${RPM_BUILD_ROOT}/%{_libdir}/${mpi}/lib/*.a

  install lib/*.so.* ${RPM_BUILD_ROOT}/%{_libdir}/${mpi}/lib/
  pushd ${RPM_BUILD_ROOT}/%{_libdir}/${mpi}/lib/
  for f in *.so.*
  do
      ln -s $f ${f%%.so*}.so
  done
  popd
  popd
  mkdir -p ${RPM_BUILD_ROOT}/usr/share/modulefiles/bout++
  cat > ${RPM_BUILD_ROOT}/usr/share/modulefiles/bout++/$MPI_COMPILER <<EOF
#%Module 1.0
#
#  BOUT++ module for use with 'environment-modules' package
#  Created by bout-add-mod-path v0.9
# Only allow one bout++ module to be loaded at a time
conflict bout++
# Require mpi
prereq mpi/$MPI_COMPILER

setenv    BOUT_TOP   $MPI_INCLUDE/bout++/
EOF

  if [ $mpi = mpich ] ; then
      %_mpich_unload
  else
      %_openmpi_unload
  fi
done

# install python libraries
pushd tools/pylib
for d in boutdata bout_runners boututils zoidberg
do
    mkdir -p ${RPM_BUILD_ROOT}/%{python3_sitelib}/$d
    cp $d/*py ${RPM_BUILD_ROOT}/%{python3_sitelib}/$d/
done
popd

# install manual
%if %{with manual}
mandir=$(ls build_*/manual -d|head -n1)
mkdir -p ${RPM_BUILD_ROOT}/%{_defaultdocdir}/bout++/
rm -rf $mandir/html/.buildinfo
rm -rf $mandir/html/.doctrees
rm -rf $mandir/html/_sources
cp -r $mandir/html ${RPM_BUILD_ROOT}/%{_defaultdocdir}/bout++/
%endif

# install boutcore library
for mpi in %{mpi_list}
do
    mkdir -p ${RPM_BUILD_ROOT}/%{python3_sitearch}/${mpi}/
    install build_$mpi/tools/pylib/boutcore.*.so ${RPM_BUILD_ROOT}/%{python3_sitearch}/${mpi}/
done

%find_lang libbout

#
#           CHECK
#

%check

%if %{with test}
for mpi in %{mpi_list}
do
    if [ $mpi = mpich ] ; then
        %_mpich_load
    else
        %_openmpi_load
    fi
    export OMPI_MCA_rmaps_base_oversubscribe=yes
    # Increase timeout for copr / s390x
    export BOUT_TEST_TIMEOUT=15m
    sed 's/ 3s / 30s /' tests/integrated/test-coordinates-initialization/runtest

    pushd build_$mpi
    make %{?_smp_mflags} build-check
    SEGFAULT_SIGNALS="segv" LD_PRELOAD=%{_libdir}/libSegFault.so make check
    popd
    if [ $mpi = mpich ] ; then
        %_mpich_unload
    else
        %_openmpi_unload
    fi
done
%endif

#
#           FILES SECTION
#

%if %{with mpich}
%files mpich
%{_libdir}/mpich/lib/libbout++.so.4.3.1
%{_libdir}/mpich/lib/*.so.1.0.0
%{_libdir}/mpich/bin/*
%doc README.md
%doc CITATION.bib
%doc CITATION.cff
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%license LICENSE.GPL
/usr/share/modulefiles/bout++/mpich-*

%files mpich-devel
%{_includedir}/mpich-%{_arch}/bout++
%{_libdir}/mpich/lib/*.so

%files -n python%{python3_pkgversion}-%{name}-mpich
%{python3_sitearch}/mpich/*
%endif


%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/lib/libbout++.so.4.3.1
%{_libdir}/openmpi/lib/*.so.1.0.0
%{_libdir}/openmpi/bin/*
%doc README.md
%doc CITATION.bib
%doc CITATION.cff
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%license LICENSE.GPL
/usr/share/modulefiles/bout++/openmpi-*

%files openmpi-devel
%{_includedir}/openmpi-%{_arch}/bout++
%{_libdir}/openmpi/lib/*.so

%files -n python%{python3_pkgversion}-%{name}-openmpi
%{python3_sitearch}/openmpi/*
%endif

%files common -f libbout.lang
%dir /usr/share/modulefiles/bout++/

%files -n python%{python3_pkgversion}-%{name}
%{python3_sitelib}/*bout*
%{python3_sitelib}/zoidberg
%doc README.md
%doc CITATION.bib
%doc CITATION.cff
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%license LICENSE.GPL


%if %{with manual}
%files -n %{name}-doc
%doc  %{_defaultdocdir}/bout++/
%endif

#
#           CHANGELOG
#

%changelog
* Sat Feb 06 2021 David Schw??rer <davidsch@fedoraproject.org> 4.3.2-6
- Increase timeout for test coordinates-initialization

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 David Schw??rer <davidsch@fedoraproject.org> 4.3.2-4
- Increase timeout for tests RHBZ#1914777

* Wed Jan 06 2021 Orion Poplawski <orion@nwra.com> - 4.3.2-3
- Rebuild for sundials 5.6.1

* Sun Nov 22 2020 David Schw??rer <davidsch@fedoraproject.org> 4.3.2-2
- Rebuild for sundials 5.5.0 and petsc 3.14.1

* Wed Oct 21 2020 David Schw??rer <davidsch@fedoraproject.org> 4.3.2-1
- Update to 4.3.2
- add python provides
- add recomands for devel packages
- add module files

* Wed Oct  7 2020 Orion Poplawski <orion@nwra.com> - 4.3.1-8
- Rebuild for sundials 5.4.0

* Thu Aug 20 2020 I??aki ??car <iucar@fedoraproject.org> - 4.3.1-7
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 15 2020 David Schw??rer <davidsch@fedoraproject.org> 4.3.1-6
- Enable sundials and petsc
- Rebuild with flexiblas

* Sat Aug 08 2020 David Schw??rer <schword2mail.dcu.ie> - 4.3.1-5
- Disable lto for s390x

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 David Schw??rer <schword2mail.dcu.ie> - 4.3.1-1
- Update to 4.3.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 David Schw??rer <schword2mail.dcu.ie> - 4.3.0-2
- update make.config during install

* Thu Dec 05 2019 David Schw??rer <schword2mail.dcu.ie> - 4.3.0-1
- update to 4.3.0
- add common subpackage for lang files

* Fri Aug 23 2019 David Schw??rer <schword2mail.dcu.ie> - 4.2.2-1
- Remove ldconfig scriptlets
- Use mpi scriplets
- Ensure sitelib packages do not match arched mpi packages
- Move commons package to the base packages
- Specify so version
- Drop man page for library

* Fri Mar 01 2019 David Schw??rer <schword2mail.dcu.ie> - 4.2.2-0
- Update to version 4.2.2

* Thu Feb 07 2019 David Schw??rer <schword2mail.dcu.ie> - 4.2.1-0
- Fix license
- Bump to 4.2.1
- Use new release
- Release contains gtest, so we can run make check

* Tue Dec 04 2018 David Schw??rer <schword2mail.dcu.ie> - 4.2.0-3
- Fix recommend

* Thu Oct 18 2018 David Schw??rer <schword2mail.dcu.ie> - 4.2.0-2
- Update to 4.2.0
- Remove python2 support
- Add boutcore support
- Fix mangling of shebangs

* Tue Dec 12 2017 David Schw??rer <schword2mail.dcu.ie> - 4.1.2-2
- Add missing python_provide macro

* Fri Dec 01 2017 David Schw??rer <schword2mail.dcu.ie> - 4.1.2-1
- Update to new release, remove patch

* Tue May 02 2017 David Schw??rer <schword2mail.dcu.ie> - 4.1.1-1
- Initial RPM release.
