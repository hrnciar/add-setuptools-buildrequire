# TESTING NOTE: The tests are disabled by default.  The koji builders may or
# may not have a GPU, and the CPU-only POCL implementation does not provide
# a device that libgpuarray is able to use.  The tests should be run manually
# on a machine with a supported GPU prior to committing changes.
%bcond_with tests

%{?python_enable_dependency_generator}

%global srcname pygpu

Name:           libgpuarray
Version:        0.7.6
Release:        11%{?dist}
Summary:        Library to manipulate tensors on a GPU

# All files are ISC except src/util/xxhash.{c,h}, which are BSD
License:        ISC and BSD
URL:            http://deeplearning.net/software/libgpuarray/
Source0:        https://github.com/Theano/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

%if %{with tests}
BuildRequires:  pkgconfig(check)
%endif

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(clblast)
BuildRequires:  pkgconfig(OpenCL)

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist breathe}
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist mako}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

%description
The goal of this project is to make a common GPU ndarray (n dimensional
array) that can be reused by all projects, that is as future proof as
possible, while keeping it easy to use for simple needs and quick tests.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%description    doc
Documentation for %{name}.

%package -n     python3-%{srcname}
Summary:        Python 3 interface to manipulate tensors on a GPU
# All files are ISC except pygpu/dtypes.py, which is MIT
License:        ISC and MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{py3_dist numpy}

%description -n python3-%{srcname}
The goal of this project is to make a common GPU ndarray (n dimensional
array) that can be reused by all projects, that is as future proof as
possible, while keeping it easy to use for simple needs and quick tests.

%package -n     python3-%{srcname}-devel
Summary:        Development files for python3-%{srcname}
Requires:       python3-%{srcname}%{?_isa} = %{version}-%{release}

%description -n python3-%{srcname}-devel
The python3-%{srcname}-devel package contains libraries and header files
for developing applications that use python3-%{srcname}.

%prep
%autosetup

# Do not use /usr/bin/env, and specify the python version
sed -i.orig "s,%{_bindir}/env python,%{python3}," bin/gpuarray-cache
touch -r bin/gpuarray-cache.orig bin/gpuarray-cache
rm bin/gpuarray-cache.orig

# Fix the library install directory on 64-bit platforms
if [ "%{_lib}" != "lib" ]; then
  sed -i "s/\(DESTINATION \)lib/\1%{_lib}/" src/CMakeLists.txt
fi

# Fix finding the headers and library when building the python interface
sed -e "s|^\(include_dirs = \[\)|\1\"$PWD/src\",|" \
    -e "s|^\(library_dirs = \[\)|\1\"$PWD/lib\"|" \
    -i setup.py

%build
# Build the library
%cmake
%cmake_build

# Build pygpu for python 3
%py3_build

# Build the documentation
export LD_LIBRARY_PATH=$PWD/lib
cp -p build/lib.linux-*-%{python3_version}/pygpu/*.so pygpu
make -C doc html

%install
# Install the library
%cmake_install

# We do not want the static library
rm -f %{buildroot}%{_libdir}/%{name}-static.a

# Install pygpu for python 3
%py3_install

%if %{with tests}
%check
export GPUARRAY_TEST_DEVICE=opencl1
make test
%endif

%files
%license LICENSE
%doc README.txt
%{_libdir}/%{name}.so.3
%{_libdir}/%{name}.so.3.*

%files devel
%{_includedir}/gpuarray/
%{_libdir}/%{name}.so

%files doc
%doc doc/_build/html/*

%files -n python3-%{srcname}
%{python3_sitearch}/%{srcname}*.egg-info/
%{python3_sitearch}/%{srcname}/
%exclude %{python3_sitearch}/%{srcname}/*.c
%exclude %{python3_sitearch}/%{srcname}/*.h

%files -n python3-%{srcname}-devel
%{python3_sitearch}/%{srcname}/*.c
%{python3_sitearch}/%{srcname}/*.h

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Jerry James <loganjerry@gmail.com> - 0.7.6-10
- Drop font unbundling now that sphinx_rtd_theme handles it

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-8
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Jerry James <loganjerry@gmail.com> - 0.7.6-2
- Rebuild for clblast 1.5.0

* Tue Aug 28 2018 Jerry James <loganjerry@gmail.com> - 0.7.6-1
- Initial RPM
