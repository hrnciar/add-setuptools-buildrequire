%global pypi_name interrogate

%global _description %{expand:
interrogate checks your code base for missing docstrings.
Documentation should be as important as code itself. And it should 
live within code. Python standardized docstrings, allowing for developers 
to navigate libraries as simply as calling help() on objects, and with 
powerful tools like Sphinx, pydoc, and Docutils to automatically generate 
HTML, LaTeX, PDFs, etc.}

Name:           python-%{pypi_name}
Version:        1.3.2
Release:        1%{?dist}
Summary:        Interrogate a codebase for docstring coverage

License:        MIT
URL:            https://github.com/econchick/interrogate
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(tabulate)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-cov)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:  %{summary}

%description -n python-%{pypi_name}-doc
Documentation for interrogate

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest tests/

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/interrogate
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Apr 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.2-1
- Initial package
