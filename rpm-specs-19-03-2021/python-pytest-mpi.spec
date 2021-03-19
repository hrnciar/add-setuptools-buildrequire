%?python_enable_dependency_generator
%global srcname pytest-mpi

Name:           python-%{srcname}
Version:        0.4
Release:        4%{?dist}
Summary:        Pytest plugin for running tests under MPI

License:        BSD
URL:            https://github.com/aragilar/pytest-mpi
Source0:        https://github.com/aragilar/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Fix build with newer pytest
Patch0:         https://patch-diff.githubusercontent.com/raw/aragilar/pytest-mpi/pull/12.patch

BuildArch:      noarch

%description
pytest_mpi is a plugin for pytest providing some useful tools when running
tests under MPI, and testing MPI-related code.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Pytest plugin for running tests under MPI
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-sybil
BuildRequires:  mpich-devel
BuildRequires:  python%{python3_pkgversion}-mpi4py-mpich
BuildRequires:  openmpi-devel
BuildRequires:  python%{python3_pkgversion}-mpi4py-openmpi

%description -n python%{python3_pkgversion}-%{srcname}
pytest_mpi is a plugin for pytest providing some useful tools when running
tests under MPI, and testing MPI-related code.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
module load mpi/mpich-%{_host_cpu}
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$MPI_PYTHON3_SITEARCH
py.test-%{python3_version} -p pytester --runpytest=subprocess -vv
module unload mpi/mpich-%{_host_cpu}
module load mpi/openmpi-%{_host_cpu}
export OMPI_MCA_rmaps_base_oversubscribe=1
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$MPI_PYTHON3_SITEARCH
py.test-%{python3_version} -p pytester --runpytest=subprocess -vv
module unload mpi/openmpi-%{_host_cpu}


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/pytest_mpi/
%{python3_sitelib}/pytest_mpi-*.egg-info/


%changelog
* Sat Jan 30 2021 Orion Poplawski <orion@nwra.com> - 0.4-4
- Set OMPI_MCA_rmaps_base_oversubscribe=1 for openmpi tests (bz#1900524)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov  1 2020 Orion Poplawski <orion@nwra.com> - 0.4-2
- Change URL
- Fix permissions

* Sun Oct 11 2020 Orion Poplawski <orion@nwra.com> - 0.4-1
- Initial package
