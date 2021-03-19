# Created by pyp2rpm-3.3.4
%global pypi_name ipywidgets
# Documentation is disabled because it requires jupyter-sphinx
%bcond_with doc

Name:           python-%{pypi_name}
Version:        7.6.3
Release:        1%{?dist}
Summary:        IPython HTML widgets for Jupyter

License:        BSD
URL:            http://ipython.org
Source0:        %{pypi_source}
Patch0:         py3_10.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(ipykernel)
# Docs
%if %{with doc}
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(recommonmark)
BuildRequires:  python3dist(sphinx)
%endif
# Tests
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pytest)

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%if %{with doc}
%package -n python-%{pypi_name}-doc
Summary:        ipywidgets documentation
%description -n python-%{pypi_name}-doc
Documentation for ipywidgets
%endif

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i "s/from distutils.core /from setuptools /" setup.py
# Jupyterlab_widgets is a new dependency in ipywidgets 7.6
# and it contains code which enables widgets in Jupyter lab
# not requiring any manual steps. But we don't have Jupyter lab
# in Fedora yet so we do not need this package at all.
sed -i "/jupyterlab_widgets/d" setup.py


%build
%py3_build
%if %{with doc}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
# The skipped test is not compatible with Py 3.10 and was already
# removed upstream together with the related functionality.
# https://github.com/jupyter-widgets/ipywidgets/commit/372457b8cb1523ecd5120b508e2d9c3a5f43c2e8
%pytest -k "not test_priority"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with doc}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Thu Feb 11 2021 Lumír Balhar <lbalhar@redhat.com> - 7.6.3-1
- Update to 7.6.3
Resolves: rhbz#1927539

* Mon Feb 08 2021 Lumír Balhar <lbalhar@redhat.com> - 7.5.1-4
- Fix tests for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Lumír Balhar <lbalhar@redhat.com> - 7.5.1-1
- Initial package.
