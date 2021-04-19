# Issue filed upstream asking them to not use nose
# https://github.com/NeuralEnsemble/elephant/issues/408

# Disabled by default
%bcond_with docs

# Try to download data, so a few are disabled.
# We test these in mock using --with=net_tests --enable-network
%bcond_with net_tests

%global pypi_name elephant

Name:       python-%{pypi_name}
Version:    0.10.0
Release:    2%{?dist}
Summary:    Elephant is a package for analysis of electrophysiology data in Python
License:    BSD
URL:        http://neuralensemble.org/elephant
Source0:    %{pypi_source}
BuildArch:  noarch

# Remove bits from setup.py that try to download fim.
# we use the packaged version
# Patch0:     0001-Do-not-download-fim-so.patch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(neo)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(quantities)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(statsmodels)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(fim)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(tqdm)

%if %{with docs}
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3dist(sphinx-gallery)
BuildRequires:  python3dist(sphinxcontrib-bibtex)
%endif

%description
Elephant - Electrophysiology Analysis Toolkit Elephant is a package for the
analysis of neurophysiology data, based on Neo.

%{?python_enable_dependency_generator}

%package -n     python3-%{pypi_name}
Summary:        %{summary}


# For F32
%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name}
Elephant - Electrophysiology Analysis Toolkit Elephant is a package for the
analysis of neurophysiology data, based on Neo.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        elephant documentation

%description -n python-%{pypi_name}-doc
Documentation for elephant

%endif

%prep
%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

rm -frv doc/_build

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# Use fim from python-pyfim which is faster
sed -i 's|from elephant.spade_src import fim|import fim|' elephant/spade.py

%build
%py3_build

%if %{with docs}
pushd doc
    make SPHINXBUILD=sphinx-build-3 html
    rm -rf build/.doctrees
    rm -rf build/.buildinfo
popd
%endif

%install
%py3_install

%check
# One test fails generally: reported upstream
# https://github.com/NeuralEnsemble/elephant/issues/409
# Another fails on 32 bit builders: reported upstream
# https://github.com/NeuralEnsemble/elephant/issues/410
%if %{with net_tests}
pytest-%{python3_version} -k "not test_repr and not test__UE_surrogate"
%else
# Disable tests that download bits
pytest-%{python3_version} -k "not test_repr and not test__UE_surrogate and not test_spike_contrast_with_Izhikevich_network_auto and not test_Riehle_et_al_97_UE"
%endif


%files -n python3-%{pypi_name}
%license LICENSE.txt elephant/spade_src/LICENSE
%doc README.md elephant/current_source_density_src/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc doc/_build/html
%license LICENSE.txt elephant/spade_src/LICENSE
%endif

%changelog
* Fri Mar 12 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.0-2
- Add py_provides macro for F32

* Thu Mar 11 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.0-1
- Update to new release
- Enable all non-network dependent tests
- File bug for failing tests
- Update fim tweak: no longer required in the test file
- include statsmodels dependency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.4-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.2-3
- Use pyfim which is 10 times faster than the python fast_fca according to docs
- Patch out bits that try to download fim
- Version neo requirements

* Fri Jun 14 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.2-2
- Report issues upstream and add links to spec file

* Tue Jun 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.2-2
- Fix comment #11 BZ#1651824

* Fri Jun 07 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.2-1
- Initial package.
