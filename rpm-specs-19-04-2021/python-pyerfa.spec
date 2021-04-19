%global module_name erfa
%global pypi_name pyerfa

Name:           python-pyerfa
Version:        1.7.1.1
Release:        2%{?dist}
Summary:        Python wrapper for the ERFA library
License:        BSD
URL:            https://github.com/liberfa/pyerfa
Source0:        %{pypi_source}

# Python BuildRequires
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist jinja2}
BuildRequires:  %{py3_dist pytest_astropy}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist setuptools_scm}
# Non-Python BuildRequires
BuildRequires:  erfa-devel
BuildRequires:  gcc


%description
PyERFA is the Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU). All C routines are wrapped as Numpy universal functions, so that
they can be called with scalar or array inputs.


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
PyERFA is the Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU). All C routines are wrapped as Numpy universal functions, so that
they can be called with scalar or array inputs.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
# Build using system liberfa, not bundled one
PYERFA_USE_SYSTEM_LIBERFA=1 %py3_build


%install
%py3_install


%check
pushd %{buildroot}%{python3_sitearch}/%{module_name}
%{__python3} -m pytest
rm -rf .pytest_cache
rm tests/__pycache__/test_erfa*pytest*.pyc
popd


%files -n  python3-%{pypi_name}
%license LICENSE.rst
%doc AUTHORS.rst CHANGES.rst README.rst
%{python3_sitearch}/%{module_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 11:37:40 CET 2020 Christian Dersch <lupinix@fedoraproject.org> - 1.7.1.1-1
- initial package (Review: RHBZ #1898135)
