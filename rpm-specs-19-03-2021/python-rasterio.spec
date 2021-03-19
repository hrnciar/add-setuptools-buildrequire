%global srcname rasterio

Name:           python-%{srcname}
Version:        1.2.1
Release:        1%{?dist}
Summary:        Fast and direct raster I/O for use with Numpy and SciPy

License:        BSD
URL:            https://github.com/mapbox/rasterio
# PyPI tarball doesn't include test data.
Source0:        https://github.com/mapbox/rasterio/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gdal >= 1.11
BuildRequires:  gdal-devel >= 1.11

%global _description \
Rasterio reads and writes geospatial raster data. Geographic information \
systems use GeoTIFF and other formats to organize and store gridded, or raster, \
datasets. Rasterio reads and writes these formats and provides a Python API \
based on ND arrays.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3dist(affine)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(click) >= 4
BuildRequires:  python3dist(click-plugins)
BuildRequires:  python3dist(cligj) >= 0.5
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(snuggs) >= 1.4.1

BuildRequires:  python3dist(boto3) >= 1.2.4
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(ipython) >= 2
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pytest) >= 2.8.2
BuildRequires:  python3dist(shapely)

%description -n python3-%{srcname} %{_description}


%{?python_extras_subpkg:%{python_extras_subpkg -n python3-rasterio -i %{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/ ipython plot s3}}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
rm -r %{srcname}  # Don't try unbuilt copy.

# Skip tests on s390x, GEOS is broken on that arch and results in test failures
%ifnarch s390x
# test_outer_boundless_pixel_fidelity is very flaky, so skip it.
# Skip debian tests since we are not on debian
%{pytest} -v -m 'not network and not wheel' \
        -k 'not test_outer_boundless_pixel_fidelity and not debian'
%endif


%files -n python3-%{srcname}
%doc README.rst AUTHORS.txt CHANGES.txt CITATION.txt
%license LICENSE.txt
%{_bindir}/rio
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Sat Mar 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- Update to latest version (#1934831)

* Sat Feb 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version
- Add extras subpackages

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 13:07:29 CET 2020 Sandro Mani <manisandro@gmail.com> - 1.1.8-2
- Rebuild (proj, gdal)

* Wed Oct 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.8-1
- Update to latest version (#1879133)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-3
- Rebuilt for Python 3.9

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 1.1.4-2
- Rebuild (gdal)

* Sun May 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-1
- Update to latest version

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.1.3-2
- Rebuild (gdal)

* Wed Feb 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.3-1
- Update to latest version

* Tue Jan 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.2-1
- Update to latest version

* Mon Oct 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-2
- rebuilt

* Mon Oct 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Mon Sep 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.28-1
- Update to latest version

* Sun Sep 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.27-1
- Update to latest version

* Fri Aug 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.26-1
- Update to latest version

* Fri Aug 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.25-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.24-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.24-1
- Update to latest version

* Thu May 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.23-1
- Update to latest version

* Thu Mar 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.22-1
- Update to latest version

* Sun Mar 03 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.21-1
- Update to latest version

* Thu Feb 28 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.20-1
- Update to latest version

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.18-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.13-1
- Update to latest version

* Wed Dec 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.12-1
- Update to latest version

* Mon Nov 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.9-1
- Update to latest version

* Fri Sep 21 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Drop Python 2 subpackage

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.0.2-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version

* Tue Jul 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Fri Jul 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0b1-2
- Rebuilt for Python 3.7

* Sun May 27 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0b1-1
- Update to latest version.

* Sat Jan 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0a12-1
- Initial package.
