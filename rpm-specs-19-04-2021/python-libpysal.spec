%global srcname libpysal

Name:           python-%{srcname}
Version:        4.4.0
Release:        1%{?dist}
Summary:        Python Spatial Analysis Library core components

License:        BSD
URL:            https://pysal.org
# PyPI source doesn't include test data or docs.
Source0:        https://github.com/pysal/libpysal/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Test example datasets.
Source1:        https://geodacenter.github.io/data-and-lab//data/ncovr.zip
Source2:        https://github.com/sjsrey/newHaven/archive/master/newHaven.zip
Source3:        https://github.com/sjsrey/rio_grande_do_sul/archive/master/rio_grande_do_sul.zip
# Hard-code the list of datasets to not use the network.
Patch0001:      0001-Hard-code-list-of-example-datasets.patch
# https://github.com/pysal/libpysal/issues/391
Patch0002:      0002-Workaround-test-changes-for-GEOS-3.9.0.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(numpy) >= 1.3
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(scipy) >= 0.11
BuildRequires:  python3dist(setuptools)

BuildRequires:  python3dist(geomet)
BuildRequires:  python3dist(geopandas) >= 0.2
BuildRequires:  python3dist(matplotlib) >= 1.5.1
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
#BuildRequires:  python3dist(numba)
BuildRequires:  python3dist(rtree) >= 0.8
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(xarray)

%description
Core components of PySAL - A library of spatial analysis functions. Modules
include computational geometry, input and output, spatial weights, and built-in
example datasets.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Core components of PySAL - A library of spatial analysis functions. Modules
include computational geometry, input and output, spatial weights, and built-in
example datasets.


%package -n     python-%{srcname}-doc
Summary:        Documentation for python-libpysal

BuildRequires:  pandoc
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx) >= 1.4.3
BuildRequires:  python3dist(sphinx-bootstrap-theme) >= 0.7
BuildRequires:  python3dist(sphinx-gallery)
BuildRequires:  python3dist(sphinxcontrib-bibtex)

%description -n python-%{srcname}-doc
Documentation files for python-libpysal


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Remove pre-built docs
rm -rf docs
echo "bibtex_bibfiles = ['_static/references.bib']" >> docsrc/conf.py

mkdir pysal_data
unzip %SOURCE1 -d pysal_data/NCOVR
unzip %SOURCE2 -d pysal_data/newHaven
unzip %SOURCE3 -d pysal_data/Rio_Grande_do_Sul


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD}/build/lib sphinx-build-3 docsrc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
export PYSALDATA=$PWD/pysal_data
%{python3} setup.py test


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{srcname}-doc
%doc html libpysal/examples
%license LICENSE.txt


%changelog
* Sat Feb 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.4.0-1
- Update to latest version (#1909569)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-1
- Update to latest version

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 4.2.2-2
- Rebuilt for Python 3.9

* Sun Feb 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.2.2-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.0-1
- Update to latest version

* Sat Mar 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.1-2
- Cleanup rpmlint warnings

* Fri Mar 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.1-1
- Initial package.
