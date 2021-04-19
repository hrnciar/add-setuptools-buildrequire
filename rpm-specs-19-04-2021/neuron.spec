# This is a serial build of NEURON
%global _description %{expand:
NEURON is a simulation environment for modeling individual neurons and networks
of neurons. It provides tools for conveniently building, managing, and using
models in a way that is numerically sound and computationally efficient. It is
particularly well-suited to problems that are closely linked to experimental
data, especially those that involve cells with complex anatomical and
biophysical properties.

This package does not include MPI support.

Please install the %{name}-devel package to compile nmodl files and so on.
}

%global tarname nrn

# fails somehow, disabled by default
%bcond_with metis

# Music support
%bcond_with music

%bcond_without mpich
%bcond_without openmpi

Name:       neuron
Version:    7.8.1
Release:    10%{?dist}
Summary:    A flexible and powerful simulator of neurons and networks

License:    GPLv3+
URL:        http://www.neuron.yale.edu/neuron/
Source0:    https://github.com/neuronsimulator/%{tarname}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:     0001-Unbundle-Random123.patch
# libstdc++ bundled is from 1988: seems heavily modified. Headers from there
# are not present in the current version
# https://github.com/neuronsimulator/nrn/issues/145

# Use system copy of Catch
Patch1:     0002-Unbundle-catch.patch
# We install the python bits ourselves
Patch2:     0003-Disable-python-build-and-install.patch
# Set soversions for all shared objects
Patch3:     0004-Set-soversions-for-libs.patch
# Set the right path for libdir
# Upstreamable
Patch4:     0005-Correct-librxdmath-path-for-64bit.patch
# stop build scripts from generating version during build
Patch5:     0006-Do-not-generate-version-info-at-buildtime.patch
# Remove rpaths
Patch6:     0007-Remove-rpaths.patch

# Quite a lot of files have been dropped in 7.8.1
# https://github.com/neuronsimulator/nrn/issues/719

# Random123 does not build on these, so neither can NEURON
# https://github.com/neuronsimulator/nrn/issues/114
ExcludeArch:    mips64r2 mips32r2

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bison-devel
BuildRequires:  cmake
BuildRequires:  catch-devel
# Needs to be packaged separately
# BuildRequires:  coreneuron-devel
BuildRequires:  flex
BuildRequires:  (flex-devel or libfl-devel)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
# the cmake build requires iv with cmake too
BuildRequires:  iv-devel >= 0.1
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libtool
%if %{with metis}
BuildRequires:  metis-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  Random123-devel

# Bundles sundials. WIP
# https://github.com/neuronsimulator/nrn/issues/113
# BuildRequires:  sundials-devel
Provides: bundled(sundials) = 2.0.1

%description %_description

%package devel
Summary:    Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires:  ncurses-devel
Requires:  readline-devel
Requires:  gcc-c++
Requires:  libtool
Requires:  libX11-devel
Requires:  libXext-devel

%description devel
Headers and development shared libraries for the %{name} package

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch

%description doc
Documentation for %{name}

%package -n python3-%{name}
Summary:   Python3 interface to %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest

%description -n python3-%{name} %_description

%if %{with mpich}
%package mpich
Summary:   %{name} built with MPICH support
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-mpich

Requires:       mpich
Requires:       python3-mpi4py-mpich


%description mpich %_description

%package mpich-devel
Summary:    Development files for %{name}
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
Headers and development shared libraries for the %{name} package

%package -n python3-%{name}-mpich
Summary:    Python3 interface to %{name}-mpich
Requires:  %{name}-mpich%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-mpich
%endif

%if %{with openmpi}
%package openmpi
Summary:   %{name} built with OpenMPI support
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-openmpi

Requires:       openmpi
Requires:       python3-mpi4py-openmpi


%description openmpi %_description

%package openmpi-devel
Summary:    Development files for %{name}
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
Headers and development shared libraries for the %{name} package

%package -n python3-%{name}-openmpi
Summary:    Python3 interface to %{name}-openmpi
Requires:  %{name}-openmpi%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-openmpi
%endif

%prep
%autosetup -n %{tarname}-%{version} -S git

# Remove executable perms from source files
find src -type f -executable ! -name '*.sh' -exec chmod -x {} +

# Remove bundled Random123
rm -rf src/Random123
rm -rf src/readline

# Create version file ourselves
# To create this, we run the git2version.sh script in a checked out copy of neuron
export TIMESTAMP=$(date +%Y-%m-%d)
cat > src/nrnoc/nrnversion.h << EOF
#define GIT_DATE "$TIMESTAMP"
#define GIT_BRANCH "master"
#define GIT_CHANGESET "da13bb7c"
#define GIT_DESCRIBE "7.8.1-1-gda13bb7c (Fedora %{fedora})"
EOF

# Use system libtool instead of a local copy that neuron tries to install
for f in bin/*_makefile.in; do
    sed -r -i 's|(LIBTOOL.*=.*)\$\(pkgdatadir\)(.*)|\1$(bindir)\2|' $f
done

# Stop system from using hard coded flags
sed -i '/CompilerFlagsHelpers/ d' cmake/ReleaseDebugAutoFlags.cmake

%build
# Not yet to be used
# export SUNDIALS_SYSTEM_INSTALL="yes"
%global do_build %{expand:
echo
echo "*** BUILDING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
%set_build_flags
    cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE \\\
        -DCMAKE_INSTALL_LIBDIR:PATH=$MPI_LIB \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
        -DNRN_ENABLE_SHARED=ON \\\
        -DNRN_ENABLE_INTERVIEWS=ON \\\
        -DNRN_ENABLE_PYTHON=ON \\\
        -DNRN_ENABLE_PYTHON_DYNAMIC=OFF \\\
        -DNRN_ENABLE_THREADS=ON \\\
        -DNRN_ENABLE_MEMACS=ON \\\
        -DNRN_ENABLE_RX3D=ON \\\
        -DNRN_ENABLE_CORENEURON=OFF \\\
        -DNRN_ENABLE_TESTS=ON \\\
        -DNRN_ENABLE_REL_RPATH=OFF \\\
        -DNRN_ENABLE_MODULE_INSTALL=ON \\\
        -DNRN_ENABLE_INTERNAL_READLINE=OFF \\\
        -DNRN_ENABLE_MPI=$MPI_YES \\\
        -DMPI_INCLUDE_PATH=$MPI_INCLUDE \\\
        -DMPI_LIBRARY=$MPI_LIBFILE \\\
%if "%{_lib}" == "lib64" \
        -DLIB_SUFFIX=64 -B $MY_CMAKE_BUILDDIR && \
%else                      \
        -DLIB_SUFFIX="" -B $MY_CMAKE_BUILDDIR && \
%endif
%make_build -C $MY_CMAKE_BUILDDIR \

%if %{with music}
pushd $MY_CMAKE_BUILDDIR/src/neuronmusic
%make_build
%{py3_build}
popd
%endif
}


# Serial version
export MPI_COMPILER=serial
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_INCLUDE=%{_includedir}
export MPI_LIB="%{_libdir}"
export MPI_LIBFILE=""
export MPI_YES=OFF
# Python 3
export MPI_COMPILE_TYPE=""
export MPI_SITEARCH="%{python3_sitearch}"
export MY_CMAKE_BUILDDIR="%_vpath_builddir"
%{do_build}

# MPICH
%if %{with mpich}
%{_mpich_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
# Python 3
export MPI_COMPILE_TYPE="-mpich"
export MY_CMAKE_BUILDDIR="%_vpath_builddir""-mpich"
export MPI_LIBFILE="$MPI_LIB/libmpi.so"
%{do_build}
%{_mpich_unload}
%endif

# OpenMPI
%if %{with openmpi}
%{_openmpi_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
# Python 3
export MPI_COMPILE_TYPE="-openmpi"
export MY_CMAKE_BUILDDIR="%_vpath_builddir""-openmpi"
export MPI_LIBFILE="$MPI_LIB/libmpi.so"
%{do_build}
%{_openmpi_unload}
%endif

%install
# Install everything

%global do_install %{expand:
echo
echo "*** INSTALLING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
%make_install -C $MY_CMAKE_BUILDDIR

%if %{with music}
pushd $MY_CMAKE_BUILDDIR/src/neuronmusic
%{py3_install}
popd
%endif

# Python bits from the post install hook
# It requires the libraries before to be installed, not just built, so it must
# be done here. The only alternative is a different package that requires this,
# but this is simpler
RPM_LD_FLAGS="%{?__global_ldflags} -L$RPM_BUILD_ROOT/$MPI_LIB"
pushd $MY_CMAKE_BUILDDIR/src/nrnpython/
%{py3_build}
%{py3_install "--install-lib" "$MPI_PYTHON3_SITEARCH"}
popd

# set up second symlink for shared objects
pushd $RPM_BUILD_ROOT/$MPI_LIB/
    ln -sv ./libnrniv.so.0.0.0 libnrniv.so.0
    ln -sv ./librxdmath.so.0.0.0 librxdmath.so.0
popd
}

%global do_post_install_tweaks %{expand:
# Remove installed libfiles
rm -rfv $RPM_BUILD_ROOT/$MPI_HOME/lib/python/neuron/
# Post install clean up: remove stray object files
# Must be done at end, otherwise it deletes object files required for other builds
find . $RPM_BUILD_ROOT/$MPI_LIB/ -name "*.o" -exec rm -f '{}' \\;
# Remove libtool archives
find . $RPM_BUILD_ROOT/$MPI_LIB/ -name "*.la" -exec rm -f '{}' \\;
# Remove installed copy of libtool
# Remove iv header provided by iv package
rm -rf $RPM_BUILD_ROOT/$MPI_HOME/include/ivstream.h
# Delete installed libtool
rm -fv $RPM_BUILD_ROOT/$MPI_HOME/share/%{tarname}/libtool

# Only needed for MPI builds
if [ x"$MPI_SUFFIX" != "x" ]
then
# Do not install demo files for MPI packages
rm -rf $RPM_BUILD_ROOT/$MPI_HOME/share/%{tarname}/demo
# Renaming MPI bits
pushd $RPM_BUILD_ROOT/$MPI_BIN/
# Rename file references to use MPI_SUFFIX before renaming them
sed -i "s/nrniv\"/nrniv$MPI_SUFFIX\"/g" nrngui
sed -i -e "s/nrniv\"/nrniv$MPI_SUFFIX\"/g" -e "s/nrnmech_makefile/nrnmech_makefile$MPI_SUFFIX/g" -e "s/nocmodl/nocmodl$MPI_SUFFIX/g" nrnivmodl
sed -i -e "s/nocmodl/nocmodl$MPI_SUFFIX/g" nrnmech_makefile
sed -i -e "s/nocmodl/nocmodl$MPI_SUFFIX/g" mkthreadsafe

# Rename files to include $MPI_SUFFIX
for f in modlunit neurondemo nrngui nrniv sortspike mkthreadsafe nocmodl nrnivmodl nrnmech_makefile
do
    mv -v "$f"{,$MPI_SUFFIX}
done
mv -v nrnpyenv{,$MPI_SUFFIX}.sh
mv -v set_nrnpyenv{,$MPI_SUFFIX}.sh
popd
fi
}

# Serial
export MPI_LIB="%{_libdir}"
export MPI_COMPILE_TYPE=""
export MPI_PYTHON3_SITEARCH=%{python3_sitearch}
export MY_CMAKE_BUILDDIR="%_vpath_builddir"
export MPI_HOME="%{_prefix}"
export MPI_BIN="%{_bindir}"
export MPI_SUFFIX=""
%do_install
%do_post_install_tweaks
# Remove duplicate files. These are installed in the correct python locations already
# rm -rf $RPM_BUILD_ROOT/%%{_datadir}/%%{tarname}/lib/python/%%{name}



# mpich
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
export MY_CMAKE_BUILDDIR="%_vpath_builddir""-mpich"
%do_install
%do_post_install_tweaks
%{_mpich_unload}
%endif

# OpenMPI
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
export MY_CMAKE_BUILDDIR="%_vpath_builddir""-openmpi"
%do_install
%do_post_install_tweaks
%{_openmpi_unload}
%endif

# The makefiles do not have shebangs
%files
%license Copyright
%{_bindir}/modlunit
%{_bindir}/neurondemo
%{_bindir}/nrngui
%{_bindir}/nrniv
%{_bindir}/sortspike
# Not needed but I'll include them for completeness anyway
%{_bindir}/nrnpyenv.sh
%{_bindir}/set_nrnpyenv.sh
# Libs
%{_libdir}/libnrniv.so.0.0.0
%{_libdir}/libnrniv.so.0
%{_libdir}/librxdmath.so.0.0.0
%{_libdir}/librxdmath.so.0
# other hoc files and data
%dir %{_datadir}/%{tarname}
%{_datadir}/%{tarname}/lib

# Python bits
%files -n python3-%{name}
# A data file resides here
%{python3_sitelib}/%{name}
# The libraries are here
%{python3_sitearch}/%{name}
# Egg info
%{python3_sitearch}/NEURON-7.8-py%{python3_version}.egg-info

%files devel
%license Copyright
%doc README.md
%{_bindir}/mkthreadsafe
%{_bindir}/nocmodl
%{_bindir}/nrnivmodl
%{_bindir}/nrnmech_makefile
# Headers
%{_includedir}/*.h
%{_includedir}/nrncvode/
# Shared objects
%{_libdir}/libnrniv.so
%{_libdir}/librxdmath.so
# required by neuron
# https://github.com/neuronsimulator/nrn/issues/719#issuecomment-677501890
%{_datadir}/%{tarname}/nrnmain.cpp

%files doc
%license Copyright
%{_datadir}/%{tarname}/demo

%if %{with mpich}
%files mpich
%license Copyright
%{_libdir}/mpich/bin/modlunit_mpich
%{_libdir}/mpich/bin/neurondemo_mpich
%{_libdir}/mpich/bin/nrngui_mpich
%{_libdir}/mpich/bin/nrniv_mpich
%{_libdir}/mpich/bin/sortspike_mpich
# Not needed but I'll include them for completeness anyway
%{_libdir}/mpich/bin/nrnpyenv_mpich.sh
%{_libdir}/mpich/bin/set_nrnpyenv_mpich.sh
# Libs
%{_libdir}/mpich/lib/libnrniv.so.0.0.0
%{_libdir}/mpich/lib/libnrniv.so.0
%{_libdir}/mpich/lib/librxdmath.so.0.0.0
%{_libdir}/mpich/lib/librxdmath.so.0
# 
%dir %{_libdir}/mpich/share/%{tarname}
%{_libdir}/mpich/share/%{tarname}/lib

# Python bits
%files -n python3-%{name}-mpich
# The libraries are here
%{python3_sitearch}/mpich/%{name}
# Egg info
%{python3_sitearch}/mpich/NEURON-7.8-py%{python3_version}.egg-info

%files mpich-devel
%license Copyright
%doc README.md
%{_libdir}/mpich/bin/mkthreadsafe_mpich
%{_libdir}/mpich/bin/nocmodl_mpich
%{_libdir}/mpich/bin/nrnivmodl_mpich
%{_libdir}/mpich/bin/nrnmech_makefile_mpich
# Headers
%{_libdir}/mpich/include/*.h
%{_libdir}/mpich/include/nrncvode/
# Shared objects
%{_libdir}/mpich/lib/libnrniv.so
%{_libdir}/mpich/lib/librxdmath.so
# required by neuron
# https://github.com/neuronsimulator/nrn/issues/719#issuecomment-677501890
%{_libdir}/mpich/share/%{tarname}/nrnmain.cpp
%endif

%if %{with openmpi}
%files openmpi
%license Copyright
%{_libdir}/openmpi/bin/modlunit_openmpi
%{_libdir}/openmpi/bin/neurondemo_openmpi
%{_libdir}/openmpi/bin/nrngui_openmpi
%{_libdir}/openmpi/bin/nrniv_openmpi
%{_libdir}/openmpi/bin/sortspike_openmpi
# Not needed but I'll include them for completeness anyway
%{_libdir}/openmpi/bin/nrnpyenv_openmpi.sh
%{_libdir}/openmpi/bin/set_nrnpyenv_openmpi.sh
# Libs
%{_libdir}/openmpi/lib/libnrniv.so.0.0.0
%{_libdir}/openmpi/lib/libnrniv.so.0
%{_libdir}/openmpi/lib/librxdmath.so.0.0.0
%{_libdir}/openmpi/lib/librxdmath.so.0
# 
%dir %{_libdir}/openmpi/share/%{tarname}
%{_libdir}/openmpi/share/%{tarname}/lib

# Python bits
%files -n python3-%{name}-openmpi
# The libraries are here
%{python3_sitearch}/openmpi/%{name}
# Egg info
%{python3_sitearch}/openmpi/NEURON-7.8-py%{python3_version}.egg-info

%files openmpi-devel
%license Copyright
%doc README.md
%{_libdir}/openmpi/bin/mkthreadsafe_openmpi
%{_libdir}/openmpi/bin/nocmodl_openmpi
%{_libdir}/openmpi/bin/nrnivmodl_openmpi
%{_libdir}/openmpi/bin/nrnmech_makefile_openmpi
# Headers
%{_libdir}/openmpi/include/*.h
%{_libdir}/openmpi/include/nrncvode/
# Shared objects
%{_libdir}/openmpi/lib/libnrniv.so
%{_libdir}/openmpi/lib/librxdmath.so
# required by neuron
# https://github.com/neuronsimulator/nrn/issues/719#issuecomment-677501890
%{_libdir}/openmpi/share/%{tarname}/nrnmain.cpp
%endif

%changelog
* Wed Feb 10 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-10
- Also build on s390x now that Random123 supports it

* Tue Feb 09 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-9
- Remove rpaths

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-7
- Fix version info

* Mon Nov 23 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-6
- Bumpspec

* Mon Nov 23 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-5
- Enable mpi builds

* Thu Oct 08 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-4
- Add missing g++ and X dependencies
- Patch to let it correctly find librxdmath

* Thu Oct 08 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-3
- Remove iv header
- disable dynamic build, not needed for Fedora: we support the default python version
- disble hard coded compiler flags

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-2
- Correct flex dependency
- #1871091

* Tue Aug 18 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-1
- Update to new release
- Move to cmake build system
- use new cmake out of source build

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-7
- Bump to build in py3.9 side tag

* Thu May 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-6
- Include libtool as Requires for the makefiles
- Reshuffle files for better subpackages

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.7.2-5
- Rebuilt for Python 3.9

* Thu May 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-4
- Update supported architectures

* Thu May 14 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-3
- Add missing BR for neuron-devel
- Move makefiles to -devel sub package

* Wed May 13 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-2
- Update description: this is built with iv support.
- Remove unneeded scriptlet
- Fix sed command to modify neuron's make files

* Sun Mar 22 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.7.2-1
- Update to latest version (seems to be just bugfixes)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-12
- Build with iv support

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.7.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7.7.1-10
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-8
- Enable Python build also

* Sat Jul 13 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-7
- Test a fixed python setup
- https://github.com/neuronsimulator/nrn/issues/238#issuecomment-505191230

* Sun Jun 23 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-6
- Add another patch

* Sun Jun 23 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-5
- Improve patch to install all headers

* Sun Jun 23 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-4
- Install all header files

* Wed Jun 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-3
- Replace patch to inclde required headers

* Wed Jun 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-2
- Remove iv header from nrnconfig file

* Wed Jun 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-1
- Revert to using release tar
- Use bundled sundials

* Fri May 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-7.20181214git
- Fix file list

* Fri May 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-6.20181214git
- Rename oc to hoc to prevent conflict with origin-client binary
- rhbz 1696118

* Sat Mar 02 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-5.20181214git5687519
- Bump and rebuild

* Thu Jan 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-4.20181214git5687519
- Remove libtool archives
- Remove stray comment
- Improve previous changelog

* Sun Jan 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-3.20181214git5687519
- Unbundle readline
- Remove readme: only speaks about installation
- Move header to includedir
- Update license
- Remove exec permissions from source files

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-2.20181214git5687519
- Put each BR on different line
- Remove unneeded comment
- Re-do random123 patch to only modify autotools files
- Remove random123 in prep

* Fri Dec 28 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-1.20181214git5687519
- Update to latest git snapshot that uses current sundials
- Build without MPI
