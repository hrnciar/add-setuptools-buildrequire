%bcond_without docs

# Created by pyp2rpm-3.3.5
%global pypi_name libcst

%global common_description %{expand:
LibCST parses Python source code as a CST tree that keeps all formatting
details (comments, whitespaces, parentheses, etc). It's useful for building
automated refactoring (codemod) applications and linters.

LibCST creates a compromise between an Abstract Syntax Tree (AST) and a
traditional Concrete Syntax Tree (CST). By carefully reorganizing and naming
node types and fields, it creates a lossless CST that looks and feels like an
AST.}

Name:           python-%{pypi_name}
Version:        0.3.17
Release:        4%{?dist}
Summary:        A concrete syntax tree with AST-like properties for Python 3

# see LICENSE in the upstream sources for the breakdown
License:        MIT and (MIT and Python) and ASL 2.0
URL:            https://github.com/Instagram/LibCST
Source0:        %{url}/archive/v%{version}.tar.gz#/LibCST-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml) >= 5.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-inspect) >= 0.4
%if %{with docs}
BuildRequires:  graphviz
BuildRequires:  sed
BuildRequires:  python3-docs
BuildRequires:  python3-metakernel-python
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(nbsphinx) >= 0.4.2
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.4.3
%endif

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} == 32
%py_provides    python3-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
%{common_description}

%if %{with docs}
%package        doc
Summary:        %{name} documentation
Requires:       python3-docs

%description    doc
Documentation for %{name}
%endif

%prep
%autosetup -n LibCST-%{version}
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/source/conf.py
%endif

%build
%py3_build
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
# test_codegen_clean is tracked in https://github.com/Instagram/LibCST/issues/304
# test_codemod_cli is tracked in https://github.com/Instagram/LibCST/issues/331
# test_fuzz depends on hypothesmith (not packaged yet)
# test_pyre_integration depends on pyre (not packaged yet)
# test_type_enforce is tracked in https://github.com/Instagram/LibCST/issues/305
%pytest \
  --ignore=libcst/codegen/tests/test_codegen_clean.py \
  --ignore=libcst/codemod/tests/test_codemod_cli.py \
  --ignore=libcst/tests/test_fuzz.py \
  --ignore=libcst/tests/test_pyre_integration.py \
  --ignore=libcst/tests/test_type_enforce.py \

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif

%changelog
* Wed Mar 03 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.3.17-4
- Fix intersphinx inventory path
- Fix %%py_provides gating

* Wed Mar 03 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.3.17-3
- Fix docs build and enable it by default

* Tue Mar 02 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.3.17-2
- Fix license
- Switch to GitHub tarball
- Add docs build (disabled by default)
- Switch to pytest and document ignored tests

* Tue Mar 02 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.3.17-1
- Initial package.
