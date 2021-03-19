%global srcname cartopy
%global Srcname Cartopy

# Some tests use the network.
%bcond_with network

Name:           python-%{srcname}
Version:        0.19.0~rc1
%global Version 0.19.0rc1
Release:        1%{?dist}
Summary:        Cartographic Python library with Matplotlib visualisations

License:        LGPLv3
URL:            http://scitools.org.uk/cartopy/docs/latest/
Source0:        %pypi_source %{Srcname} %{Version}
# Set location of Fedora-provided pre-existing data.
Source1:        siteconfig.py
# Might not go upstream in current form.
Patch0004:      0001-Increase-tolerance-for-new-FreeType.patch

BuildRequires:  gcc-c++
BuildRequires:  geos-devel >= 3.3.3
BuildRequires:  proj-devel >= 4.9.0

%global _description %{expand:
Cartopy is a Python package designed to make drawing maps for data analysis
and visualisation easy. It features:
* object oriented projection definitions
* point, line, polygon and image transformations between projections
* integration to expose advanced mapping in matplotlib with a simple and
  intuitive interface
* powerful vector data handling by integrating shapefile reading with Shapely
  capabilities
}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(cython) >= 0.29.2
BuildRequires:  python3dist(numpy) >= 1.13.3
BuildRequires:  python3dist(shapely) >= 1.5.6
BuildRequires:  python3dist(pyshp) >= 2
# OWS requirements
BuildRequires:  python3dist(owslib) >= 0.8.11
BuildRequires:  python3dist(pillow) >= 1.7.8
# Plotting requirements
BuildRequires:  python3dist(matplotlib) >= 1.5.1
BuildRequires:  python3dist(gdal) >= 1.10
BuildRequires:  python3dist(pillow) >= 1.7.8
BuildRequires:  python3dist(pykdtree) >= 1.2.2
BuildRequires:  python3dist(scipy) >= 0.10
# Testing requirements
BuildRequires:  python3dist(flufl.lock)
BuildRequires:  python3dist(pytest) >= 3

Requires:       python-%{srcname}-common = %{version}-%{release}
# OWS requirements
Recommends:     python3dist(owslib) >= 0.8.11
Recommends:     python3dist(pillow) >= 1.7.8
# Plotting requirements
Recommends:     python3dist(matplotlib) >= 1.5.1
Recommends:     python3dist(gdal) >= 1.10
Recommends:     python3dist(pillow) >= 1.7.8
Recommends:     python3dist(pykdtree) >= 1.2.2
Recommends:     python3dist(scipy) >= 0.10

%description -n python3-%{srcname} %{_description}


%package -n     python-%{srcname}-common
Summary:        Data files for %{srcname}
BuildArch:      noarch

BuildRequires:  natural-earth-map-data-110m
BuildRequires:  natural-earth-map-data-50m

Recommends:     natural-earth-map-data-110m
Suggests:       natural-earth-map-data-50m
Suggests:       natural-earth-map-data-10m

%description -n python-%{srcname}-common
Data files for %{srcname}.


%prep
%autosetup -n %{Srcname}-%{Version} -p1
cp -a %SOURCE1 lib/cartopy/

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
FORCE_CYTHON=1 %py3_build


%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/cartopy/shapefiles/natural_earth/
for theme in physical cultural; do
    ln -s %{_datadir}/natural-earth-map-data/${theme} \
        %{buildroot}%{_datadir}/cartopy/shapefiles/natural_earth/${theme}
done


%check
%if %{with network}
MPLBACKEND=Agg \
    %{pytest} --doctest-modules --pyargs cartopy
%else
MPLBACKEND=Agg \
    %{pytest} --doctest-modules --pyargs cartopy -m "not network"
%endif


%files -n python-%{srcname}-common
%doc README.md
%license COPYING COPYING.LESSER lib/cartopy/data/LICENSE
%{_datadir}/cartopy/

%files -n python3-%{srcname}
%{python3_sitearch}/cartopy/
%{python3_sitearch}/%{Srcname}-%{Version}-py*.egg-info/


%changelog
* Sat Mar 13 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.19.0~rc1-1
- Update to latest version (#1938248)

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 0.18.0-7
- Rebuild (proj)

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 0.18.0-6
- Rebuild (geos)

* Sat Jan 30 2021 Jos de Kloe <josdekloe@gmail.com> 0.18.0-5
- Add a patch to fix build failures caused by np.float deprecation
- Modify patch to add more tolerance to image comparisons
- skip test_grid_labels, since it seems to suffer from a bug that is
  not yet solved upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 13:06:18 CET 2020 Sandro Mani <manisandro@gmail.com> - 0.18.0-4
- Rebuild (proj, gdal)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-2
- Rebuilt for Python 3.9

* Mon May 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0-1
- Update to latest version

* Fri May 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0~rc1-1
- Update to latest release candidate

* Mon Apr 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0~b2-1
- Update to latest beta

* Mon Feb 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0~b1-1
- Update to latest beta

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-5
- Fix build against FreeType 2.10.0

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-4
- Rebuilt for updated Proj

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-2
- Remove pytest bytecode

* Sat Nov 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-1
- Update to latest version
- Remove workaround for unpackaged Natural Earth data
- Drop Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-5
- Add explicit gcc-c++ BR

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-4
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-3
- Drop patch for old versions of Matplotlib.
- Use python2- prefix for dependencies.

* Sun Feb 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-2
- Enable testing with now-packaged Natural Earth data.

* Fri Feb 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-1
- Initial package.
