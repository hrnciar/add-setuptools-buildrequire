%global srcname dask

# Requires distributed, which is a loop.
# Also, some tests require packages that require dask itself.
# Force bootstrap for package review.
%bcond_without bootstrap

Name:           python-%{srcname}
Version:        2021.4.0
Release:        1%{?dist}
Summary:        Parallel PyData with Task Scheduling

License:        BSD
URL:            https://github.com/dask/dask/
Source0:        %pypi_source
# https://github.com/dask/dask/issues/6725
Patch0001:      0001-Skip-test_encoding_gh601-on-big-endian-machines.patch

BuildArch:      noarch

%description
Dask is a flexible parallel computing library for analytics.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
%global cloudpickle_version 0.2.2
BuildRequires:  python3dist(cloudpickle) >= %{cloudpickle_version}
%global fsspec_version 0.6
BuildRequires:  python3dist(fsspec) >= %{fsspec_version}
BuildRequires:  python3dist(graphviz)
BuildRequires:  python3dist(ipython)
%global numpy_version 1.15.1
BuildRequires:  python3dist(numpy) >= %{numpy_version}
%global pandas_version 0.25
BuildRequires:  python3dist(pandas) >= %{pandas_version}
%global partd_version 0.3.10
BuildRequires:  python3dist(partd) >= %{partd_version}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
%global toolz_version 0.8.2
BuildRequires:  python3dist(toolz) >= %{toolz_version}
%if %{without bootstrap}
%global distributed_version 2021.3
BuildRequires:  python3dist(distributed) >= %{distributed_version}
BuildRequires:  python3dist(scikit-image)
BuildRequires:  python3dist(xarray)
%endif
# Optional test requirements.
BuildRequires:  python3dist(fastavro)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(zarr)

Recommends:     python3-%{srcname}+array = %{version}-%{release}
Recommends:     python3-%{srcname}+bag = %{version}-%{release}
Recommends:     python3-%{srcname}+dataframe = %{version}-%{release}
Recommends:     python3-%{srcname}+delayed = %{version}-%{release}
%if %{without bootstrap}
Recommends:     python3-%{srcname}+distributed = %{version}-%{release}
%endif

%description -n python3-%{srcname}
Dask is a flexible parallel computing library for analytics.


%package -n     python3-%{srcname}+array
Summary:        Meta-package for python3-%{srcname} with array feature
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{srcname}+array}

Requires:       python3-%{srcname} = %{version}-%{release}
Requires:       python3dist(numpy) >= %{numpy_version}
Requires:       python3dist(toolz) >= %{toolz_version}

%description -n python3-%{srcname}+array
This package installs dask with dependencies required for its array feature.
Dask is a flexible parallel computing library for analytics.


%package -n     python3-%{srcname}+bag
Summary:        Meta-package for python3-%{srcname} with bag feature
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{srcname}+bag}

Requires:       python3-%{srcname} = %{version}-%{release}
Requires:       python3dist(cloudpickle) >= %{cloudpickle_version}
Requires:       python3dist(fsspec) >= %{fsspec_version}
Requires:       python3dist(partd) >= %{partd_version}
Requires:       python3dist(toolz) >= %{toolz_version}

%description -n python3-%{srcname}+bag
This package installs dask with dependencies required for its bag feature.
Dask is a flexible parallel computing library for analytics.


%package -n     python3-%{srcname}+dataframe
Summary:        Meta-package for python3-%{srcname} with dataframe feature
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{srcname}+dataframe}

Requires:       python3-%{srcname} = %{version}-%{release}
Requires:       python3dist(fsspec) >= %{fsspec_version}
Requires:       python3dist(numpy) >= %{numpy_version}
Requires:       python3dist(pandas) >= %{pandas_version}
Requires:       python3dist(partd) >= %{partd_version}
Requires:       python3dist(toolz) >= %{toolz_version}

%description -n python3-%{srcname}+dataframe
This package installs dask with dependencies required for its dataframe
feature.
Dask is a flexible parallel computing library for analytics.


%package -n     python3-%{srcname}+delayed
Summary:        Meta-package for python3-%{srcname} with delayed feature
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{srcname}+delayed}

Requires:       python3-%{srcname} = %{version}-%{release}
Requires:       python3dist(cloudpickle) >= %{cloudpickle_version}
Requires:       python3dist(toolz) >= %{toolz_version}

%description -n python3-%{srcname}+delayed
This package installs dask with dependencies required for its delayed feature.
Dask is a flexible parallel computing library for analytics.


%if %{without bootstrap}
%package -n     python3-%{srcname}+distributed
Summary:        Meta-package for python3-%{srcname} with distributed feature
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{srcname}+distributed}

Requires:       python3-%{srcname} = %{version}-%{release}
Requires:       python3dist(distributed) >= %{distributed_version}

%description -n python3-%{srcname}+distributed
This package installs dask with dependencies required for its distributed
feature.
Dask is a flexible parallel computing library for analytics.
%endif


%if %{without bootstrap}
%package -n python-%{srcname}-doc
Summary:        dask documentation

BuildRequires:  python3dist(dask_sphinx_theme) >= 1.3.5
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx)

%description -n python-%{srcname}-doc
Documentation for dask
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build

%if %{without bootstrap}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%py3_install


%check
%ifarch armv7hl
    %{pytest} -m 'not network' -n 2
%else
    %{pytest} -m 'not network' -n auto
%endif


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files -n python3-%{srcname}+array
%{?python_extras_subpkg:%ghost %{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info}

%files -n python3-%{srcname}+bag
%{?python_extras_subpkg:%ghost %{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info}

%files -n python3-%{srcname}+dataframe
%{?python_extras_subpkg:%ghost %{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info}

%files -n python3-%{srcname}+delayed
%{?python_extras_subpkg:%ghost %{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info}

%if %{without bootstrap}
%files -n python3-%{srcname}+distributed
%{?python_extras_subpkg:%ghost %{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info}
%endif

%if %{without bootstrap}
%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt
%endif


%changelog
* Fri Apr 02 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2021.4.0-1
- Update to latest version (#1943694)

* Sun Mar 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2021.3.0-1
- Update to latest version (#1936017)

* Fri Feb 05 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2021.2.0-1
- Update to latest version (#1925645)

* Wed Jan 27 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2021.1.1-1
- Update to latest version (#1919397)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2021.1.0-1
- Update to latest version (#1906637)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.30.0-1
- Update to latest version (#1884852)

* Mon Oct 05 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.29.0-1
- Update to latest version (#1884852)

* Sat Sep 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.28.0-1
- Update to latest version (#1882873)

* Fri Sep 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.27.0-1
- Update to latest version (#1880693)

* Sat Sep 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.26.0-1
- Update to latest version (#1878309)

* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.25.0-1
- Update to latest version (#1873659)

* Sun Aug 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.24.0-1
- Update to latest version (#1871358)

* Sat Aug 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.23.0-1
- Update to latest version (#1868951)

* Sun Aug 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.22.0-1
- Update to latest version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.21.0-1
- Update to latest version

* Fri Jul 10 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.20.0-2
- Add metadata for Python extras subpackages

* Sun Jul 05 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.20.0-1
- Update to latest version

* Sat Jun 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-1
- Update to latest version

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.17.2-1
- Update to latest version

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.16.0-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.16.0-1
- Update to latest version

* Wed Apr 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.14.0-1
- Update to latest version

* Thu Mar 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.13.0-1
- Update to latest version

* Sat Mar 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.12.0-1
- Update to latest version

* Fri Feb 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.11.0-3
- Fix typo in dependency
- Fix flaky test

* Wed Feb 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.11.0-2
- Fix minimum dependency versions
- Make keeping minimum dependency versions in sync a bit easier

* Wed Feb 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.11.0-1
- Update to latest version

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.10.1-1
- Update to latest version

* Tue Jan 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.10.0-1
- Update to latest version

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.9.1-1
- Update to latest version

* Fri Nov 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.1-1
- Update to latest version

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.0-1
- Update to latest version

* Tue Nov 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.0-1
- Update to latest version
- Disabled distributed subpackage until it's available

* Thu Oct 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.6.0-1
- Update to latest version

* Sat Oct 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.2-1
- Update to latest version

* Sat Sep 28 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.0-1
- Update to latest version

* Fri Sep 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.0-1
- Update to latest version

* Thu Sep 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.0-1
- Update to latest version

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to latest version

* Sat Apr 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Mon Apr 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.5-1
- Update to latest version

* Sat Mar 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-1
- Update to latest version
- Remove now unnecessary patches

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.3-3
- Mark partitioning test as expected failure on 32-bit systems as well

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.3-2
- Add meta-subpackages for individual features

* Sat Mar 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.3-1
- Initial package.
