%global srcname xarray
%global data_commit 5fdb22b5613ba8176b9f6fa67be783d7810643eb

%bcond_with docs

Name:           python-%{srcname}
Version:        0.17.0
Release:        1%{?dist}
Summary:        N-D labeled arrays and datasets in Python

License:        ASL 2.0
URL:            https://github.com/pydata/xarray
Source0:        %pypi_source
# Data for examples only.
Source1:        https://github.com/pydata/xarray-data/archive/%{data_commit}/xarray-data-%{data_commit}.tar.gz
Source2:        https://github.com/mapbox/rasterio/raw/1.0.21/tests/data/RGB.byte.tif
# All Fedora specific.
Patch0001:      0001-DOC-Don-t-download-RGB.byte.tif-during-build.patch
Patch0002:      0002-DOC-Skip-examples-using-unpackaged-dependencies.patch
Patch0003:      0003-DOC-Don-t-print-out-conda-pip-environment.patch
# Fix tests with Matplotlib 3.4.
Patch0004:      https://github.com/pydata/xarray/pull/4256.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cftime) >= 1
BuildRequires:  python3-dask+array >= 2.11
BuildRequires:  python3-dask+dataframe >= 2.11
BuildRequires:  python3dist(netcdf4) >= 1.5
BuildRequires:  python3dist(numpy) >= 1.17
BuildRequires:  python3dist(pandas) >= 1
BuildRequires:  python3dist(pint)
BuildRequires:  python3dist(pytest) >= 2.7.1
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(rasterio) >= 1.1
BuildRequires:  python3dist(seaborn) >= 0.10
BuildRequires:  python3dist(setuptools) >= 41.2
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(zarr) >= 2.4

%global _description %{expand: \
Xarray (formerly xray) is an open source project and Python package that
makes working with labelled multi-dimensional arrays simple, efficient,
and fun!

Xarray introduces labels in the form of dimensions, coordinates and
attributes on top of raw NumPy-like arrays, which allows for a more
intuitive, more concise, and less error-prone developer experience. The
package includes a large and growing library of domain-agnostic functions
for advanced analytics and visualization with these data structures.

Xarray was inspired by and borrows heavily from pandas, the popular data
analysis package focused on labelled tabular data. It is particularly
tailored to working with netCDF files, which were the source of xarray's
data model, and integrates tightly with dask for parallel computing.}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}


%if %{with docs}
%package -n python-%{srcname}-doc
Summary:        xarray documentation

BuildRequires:  python3dist(cartopy)
BuildRequires:  natural-earth-map-data-110m
BuildRequires:  natural-earth-map-data-10m
BuildRequires:  python3-ipython-sphinx
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-gallery)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python-%{srcname}-doc
Documentation for xarray
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1

%if %{with docs}
# Provide example datasets for building docs.
tar xf %SOURCE1 --transform='s~^\(%{srcname}-data-%{data_commit}/\)~\1.xarray_tutorial_data/~'
cp -p %SOURCE2 ./doc/gallery/
%endif


%build
%py3_build

%if %{with docs}
# generate html docs
pushd doc
PYTHONPATH=${PWD}/.. HOME=${PWD}/../%{srcname}-data-%{data_commit} make html
# remove the sphinx-build leftovers
rm -rf _build/html/.{doctrees,buildinfo}
popd
%endif


%install
%py3_install


%check
rm -rf xarray
%{pytest} -ra -n auto -m "not network" --pyargs xarray


%files -n python3-%{srcname}
%license LICENSE licenses/DASK_LICENSE licenses/NUMPY_LICENSE licenses/PANDAS_LICENSE licenses/PYTHON_LICENSE licenses/SEABORN_LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%if %{with docs}
%files -n python-%{srcname}-doc
%doc doc/_build/html
%license LICENSE licenses/DASK_LICENSE licenses/NUMPY_LICENSE licenses/PANDAS_LICENSE licenses/PYTHON_LICENSE licenses/SEABORN_LICENSE
%endif


%changelog
* Sat Mar 13 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-1
- Update to latest version (#1933230)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.2-1
- Update to latest version (#1902888)

* Sat Sep 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.1-1
- Update to latest version (#1880864)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-1
- Update to latest version

* Tue Jun 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15.1-3
- Backport patch to fix tests catching too many warnings

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.15.1-3
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15.1-2
- Fix broken install with missing files
- Test against installed version to catch above issue
- Add more test dependencies

* Wed Mar 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15.1-1
- Update to latest version

* Fri Mar 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15.0-2
- Backport fix for seaborn 0.10.0

* Sat Feb 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15.0-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.12.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12.3-1
- Update to latest version

* Sat Mar 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12.0-1
- Initial package.
