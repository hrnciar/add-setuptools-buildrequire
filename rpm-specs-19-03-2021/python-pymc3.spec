
%bcond_with check

%global srcname pymc3

Name: python-%{srcname}
Version: 3.9.3
Release: 4%{?dist}
Summary: Exploratory analysis of Bayesian models

License: ASL 2.0 and MIT and BSD
# pymc3/variational/updates.py is MIT
# the following files are generated from sphinx templates
# the license of the template is BSD
# these files are not currently installed
# pymc3/source/semantic_sphinx/static/searchtools.js
# pymc3/source/semantic_sphinx/static/highlight.min.js
# pymc3/source/semantic_sphinx/search.html
URL: https://docs.pymc.io/
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
PyMC3 is a Python package for Bayesian statistical modeling 
and Probabilistic Machine Learning focusing on advanced 
Markov chain Monte Carlo (MCMC) and 
variational inference (VI) algorithms. 
Its flexibility and extensibility make it applicable 
to a large suite of problems.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with check}
# Testing is extremely slow
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-theano
BuildRequires:  python3-pandas
BuildRequires:  python3-arviz
BuildRequires:  python3-h5py
BuildRequires:  python3-tqdm
# required to test with theano
BuildRequires:  python3-parameterized
BuildRequires:  python3-nose
%endif
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{pypi_name}.egg-info
# require theano-pymc instead of theano
sed -i 's/theano/theano-pymc/g' requirements.txt
# Remove shebang
sed -i -e "1d" pymc3/distributions/multivariate.py

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}%{python3_sitelib}
  py.test-%{python3_version} -v pymc3 || :
popd
%endif

%files -n python3-%{srcname}
#%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 3.9.3-3
- Require theano-pymc

* Sun Sep 20 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.9.3-2
- Remove egg info

* Wed Jul 08 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.9.3-1
- New upstream source (3.9.3)

* Tue Jun 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8-3
- Add additional licenses

* Wed May 27 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8-2
- Add a conditional for tests

* Tue May 26 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8-1
- Initial spec file

