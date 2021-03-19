# No tests, they run examples for tests.
# https://github.com/Neurosim-lab/netpyne/blob/development/.travis.yml
# Require optional pyneuroml, which cannot be packaged in Fedora.
# Refer to https://docs.fedoraproject.org/en-US/neurofedora/copr/ for more information.

# So tests are disabled
# We add + enable the NeuroFedora COPR for pyneuroml in mock and run tests
# manually
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enablerepo=neurofedora-copr --with=tests

%bcond_with tests

# Missing a dep, currently disabled
%bcond_with docs

%global pypi_name netpyne

%global _description %{expand:
NetPyNE is a Python package to facilitate the development, simulation,
parallelization, analysis, and optimization of biological neuronal networks
using the NEURON simulator.

For more details, installation instructions, documentation, tutorials, forums,
videos and more, please visit: www.netpyne.org

This package is developed and maintained by the Neurosim lab
(www.neurosimlab.org) }

Name:           python-%{pypi_name}
Version:        0.9.9.1
Release:        1%{?dist}
Summary:        Develop, simulate and analyse biological neuronal networks in NEURON

# netpyne/support/stackedBarGraph.py is GPLv3+
# everything else is MIT
License:        MIT and GPLv3+
URL:            https://github.com/Neurosim-lab/%{pypi_name}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Docs
%if %{with docs}
BuildRequires:  %{py3_dist sphinx}
# Not yet packaged
# BuildRequires:  %%{py3_dist autodocsum}
%endif

%if %{with tests}
BuildRequires:  gcc-g++
BuildRequires:  %{py3_dist bokeh}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist future}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist matplotlib-scalebar}
BuildRequires:  neuron-devel
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist pyneuroml}
%endif

Requires:  %{py3_dist neuron}
# Optional dep in COPR, users will have to install it manually if they want to use its features
# Requires:  %%{py3_dist pyneuroml}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# None executable script
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%if %{with docs}
pushd doc/
    %{python3} build.py
popd
%endif

%install
%py3_install

%check
%if %{with tests}
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
pushd doc/source/code
nrnivmodl mod
%{python3} tut2.py --nogui
%{python3} tut3.py --nogui
%{python3} tut4.py --nogui
%{python3} tut5.py --nogui
%{python3} tut6.py --nogui
%{python3} tut7.py --nogui
popd

pushd examples/HHTut
%{python3} HHTut_run.py -nogui
%{python3} HHTut_export.py -nogui
popd

pushd examples/HybridTut
nrnivmodl .
%{python3} HybridTut_run.py -nogui
%{python3} HybridTut_export.py -nogui
popd

pushd examples/M1
nrnivmodl .
%{python3} M1_run.py -nogui
%{python3} M1_export.py -nogui
popd

pushd examples/PTcell
nrnivmodl mod
%{python3} init.py -nogui
popd

pushd examples/LFPrecording
nrnivmodl mod
%{python3} cell_lfp.py -nogui
popd

pushd examples/saving
%{python3} init.py -nogui
popd

pushd examples/rxd_buffering
%{python3} buffering.py -nogui
popd

pushd examples/rxd_net
nrnivmodl mod
%{python3} init.py -nogui
popd

pushd examples/NeuroMLImport/
nrnivmodl .
%{python3} SimpleNet_import.py -nogui
popd
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGES.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%if %{with docs}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
* Thu Mar 04 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.9.1-1
- Update to latest upstream release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.8-1
- Update to latest release

* Tue Oct 13 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.7-2.20201009git548ffc6
- Update license to include GPLv3+
- Add comment to explain why pyneuroml cannot be included in Fedora
- use python3 instead of __python3

* Fri Oct 09 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.7-2.20201009git548ffc6
- Update to latest snapshot
- Remove unneeded BRs
- Document how to run with tests enabled in mock

* Thu Oct 08 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.7-1
- Initial build
