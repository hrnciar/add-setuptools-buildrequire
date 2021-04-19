# uses nose, which is deprecated so we only run these locally
# All tests pass
# Issue filed upstream:
# https://github.com/BlueBrain/NeuroM/issues/887
%bcond_with tests

# Requires sphinxcontrib napoleon which isn't in Fedora yet.
%bcond_with docs

%global pypi_name neurom
%global pretty_name NeuroM

%global _description %{expand:
NeuroM is a Python-based toolkit for the analysis and processing of neuron
morphologies.

Documentation is available at https://neurom.readthedocs.io/
}

Name:           python-%{pypi_name}
Version:        1.8.0
Release:        1%{?dist}
Summary:        Neuronal Morphology Analysis Tool

License:        BSD
URL:            https://github.com/BlueBrain/NeuroM
Source0:        %pypi_source

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist tox}
%endif

%if %{with docs}
BuildRequires:  %{py3_dist sphinx}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation for %{name}

%description doc %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Fix shebangs
find . -type f -exec sed -i 's|^#![  ]*/usr/bin/env.*$|#!/usr/bin/python3|' {} ';'
sed -i '/^#![  ]*\/usr\/bin\/python3.*$/ d' neurom/check/runner.py

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%if %{with docs}
make -C doc SPHINXBUILD=sphinx-build-3 html
rm -rf doc/_build/html/{.doctrees,.buildinfo} -vf
%endif

%install
%pyproject_install
%pyproject_save_files neurom

# Remove spurious installed files
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/apps

%check
%if %{with tests}
%tox
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md AUTHORS.md
%{_bindir}/morph_check
%{_bindir}/morph_stats
%{_bindir}/neurom
%{_bindir}/raw_data_check

%files doc
%license LICENSE.txt
%if %{with docs}
%doc doc/_build/html
%endif
%doc examples ipynb tutorial

%changelog
* Wed Apr 14 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.8.0-1
- Initial build

