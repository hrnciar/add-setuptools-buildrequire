%bcond_without mpich
%bcond_without openmpi

# Tests
# https://github.com/NeuralEnsemble/PyNN/blob/master/ci/test_script.sh
# Use nose, so disabled by default, but tested locally with --with-tests
# Issue filed upstream: https://github.com/NeuralEnsemble/PyNN/issues/705
%bcond_with tests

# Issue filed about warnings while compiling NEURON mod files:
# https://github.com/NeuralEnsemble/PyNN/issues/707


# Exclude privately used libnrnmech from provides
%global __provides_exclude ^libnrnmech\\.so.*$

%global pypi_name PyNN
%global mod_name pyNN
%global lower_name pynn

%global _description %{expand:
PyNN (pronounced 'pine') is a simulator-independent language for building
neuronal network models.

In other words, you can write the code for a model once, using the PyNN API and
the Python programming language, and then run it without modification on any
simulator that PyNN supports (currently NEURON, NEST and Brian) and on a number
of neuromorphic hardware systems.

The PyNN API aims to support modelling at a high-level of abstraction
(populations of neurons, layers, columns and the connections between them)
while still allowing access to the details of individual neurons and synapses
when required. PyNN provides a library of standard neuron, synapse and synaptic
plasticity models, which have been verified to work the same on the different
supported simulators. PyNN also provides a set of commonly-used connectivity
algorithms (e.g. all-to-all, random, distance-dependent, small-world) but makes
it easy to provide your own connectivity in a simulator-independent way.

Even if you don’t wish to run simulations on multiple simulators, you may
benefit from writing your simulation code using PyNN’s powerful, high-level
interface. In this case, you can use any neuron or synapse model supported by
your simulator, and are not restricted to the standard models.

Documentation: http://neuralensemble.org/docs/PyNN/
Mailing list: https://groups.google.com/forum/?fromgroups#!forum/neuralensemble

This package supports the NEURON, NEST, and Brian simulators.}

Name:           python-%{lower_name}
Version:        0.9.6
Release:        1%{?dist}
Summary:        A package for simulator-independent specification of neuronal network models

License:        CeCILL
URL:            http://neuralensemble.org/%{pypi_name}/
Source0:        %pypi_source %{pypi_name}

# Random123 does not build on these, so neither can NEURON, so nothing that
# depends on NEURON supports them either
# https://github.com/neuronsimulator/nrn/issues/114
ExcludeArch:    mips64r2 mips32r2

# Disable pynn's way of building extensions
# We do it ourselves
Patch0:         0001-Disable-nest-extension-build-by-setup.patch
# outdated: does not work any more
Patch1:         0002-Remove-nest-ext-doc-generation.patch
# Use correct operator
# Sent upstream: https://github.com/NeuralEnsemble/PyNN/pull/706
Patch2:        0003-Use-correct-comparison-operator.patch

# For NEST extensions
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gsl-devel
BuildRequires:  libneurosim-devel
BuildRequires:  ncurses-devel
BuildRequires:  nest
BuildRequires:  nest-headers
BuildRequires:  neuron-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  readline-devel

%if %{with tests}
BuildRequires:  python3-brian2
BuildRequires:  python3-cheetah
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist lazyarray}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist neo}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist nose-testconfig}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  python3-nest
BuildRequires:  python3-neuron
BuildRequires:  %{py3_dist quantities}

%if %{with mpich}
BuildRequires:  python3-mpi4py-mpich
BuildRequires:  python3-nest-mpich
BuildRequires:  python3-neuron-mpich
BuildRequires:  rpm-mpi-hooks
BuildRequires:  mpich
BuildRequires:  mpich-devel
%endif

%if %{with openmpi}
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  python3-nest-openmpi
BuildRequires:  python3-neuron-openmpi
BuildRequires:  rpm-mpi-hooks
BuildRequires:  openmpi
BuildRequires:  openmpi-devel
%endif
%endif

%{?python_enable_dependency_generator}

%description %_description

%package devel
Summary:        %{summary}
Requires:       python3-%{lower_name}%{?_isa} = %{version}-%{release}

%description devel %_description

%package -n python3-%{lower_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{lower_name} %_description

%package doc
Summary:        %{summary}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version} -S git
rm -rfv %{pypi_name}-%{version}/%{mod_name}.egg-info

%build
%py3_build

# Build NEURON modules
pushd ./build/lib/pyNN/neuron/nmodl/ || exit 1
    nrnivmodl .
popd
# The tests however, look for these here, so we also build them
pushd pyNN/neuron/nmodl || exit 1
    nrnivmodl .
popd

# NEST extensions: we build and install them ourselves
mkdir ./build/lib/pyNN/nest/extensions/_build/ || exit 1
pushd ./build/lib/pyNN/nest/extensions/_build/ || exit 1
    %cmake -Dwith-nest=%{_bindir}/nest-config ..
    %cmake_build
popd

%install
%py3_install

# NEST extensions
pushd ./build/lib/pyNN/nest/extensions/_build/ || exit 1
    %cmake_install
popd

# Includes compiled arch specific files but installs in /lib
# Manually move to arch specific folder
%if "%{python3_sitelib}" != "%{python3_sitearch}"
mkdir -p 0644 $RPM_BUILD_ROOT/%{python3_sitearch}/
mv $RPM_BUILD_ROOT/%{python3_sitelib}/pyNN $RPM_BUILD_ROOT/%{python3_sitearch}/
mv $RPM_BUILD_ROOT/%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info $RPM_BUILD_ROOT/%{python3_sitearch}/
%endif

# Delete temporary files that do not need to be installed
rm -rf $RPM_BUILD_ROOT/%{python3_sitearch}/pyNN/nest/extensions

%check
%if %{with tests}
%if %{with mpich}
%{_mpich_load}
%{__python3} setup.py nosetests -e backends -v --tests=test/unittests
%{_mpich_unload}
%endif

%if %{with openmpi}
%{_openmpi_load}
%{__python3} setup.py nosetests -e backends -v --tests=test/unittests
%{_openmpi_unload}
%endif
%endif

# These files are NEURON files that are required by PyNN to run bits using the NEURON backend
# The libnrnmech.so file, along with the .libs/libnrnmech.so symlink are both required
# So is the "special" script that loads these libraries
# We can remove some temporary compilation files, though:
find $RPM_BUILD_ROOT/%{python3_sitearch}/pyNN/neuron/nmodl/*/ -name "*.c" -o -name "*.c" -o -name "*.mod" -delete


%files -n python3-%{lower_name}
%license LICENSE
%doc README.rst AUTHORS changelog
%{_libdir}/nest/
%{_datadir}/nest/sli/pynn_extensions-init.sli
%{python3_sitearch}/%{mod_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files devel
%{_includedir}/%{lower_name}_extensions.h

%files doc
%license LICENSE
%doc examples


%changelog
* Tue Feb 09 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.6-1
- Remove duplicate neuron-devel BR
- Add patch to correct python operator usage
- Use arch dependent and version specific requirement on base package
- Add comment about NEURON files
- Filter out private libnrnmech from provides

* Fri Jan 08 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.6-1
- Initial build
