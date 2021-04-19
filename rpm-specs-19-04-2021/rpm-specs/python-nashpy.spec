%global pypi_name nashpy
%global pretty_name Nashpy

%global _description %{expand:
This library implements the following algorithms for Nash equilibria
on 2 player games: Support enumeration, Best response polytope vertex
enumeration, Lemke Howson algorithm.}

Name:           python-%{pypi_name}
Version:        0.0.21
Release:        1%{?dist}
Summary:        A library to compute equilibria of 2 player normal form games

License:        MIT
URL:            https://github.com/drvinceknight/%{pretty_name}
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)

# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version}
# Remove bundled egg-info
rm -rf %{pretty_name}.egg-info

%build
%py3_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
pytest src/nashpy --cov=nashpy --cov-fail-under=5 --flake8

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGES.md CITATION.md paper.md paper.bib
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE
%doc html/
%changelog
* Mon Apr 5 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.21-1
- Add subpackage for docs

* Sun Apr 4 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.21-1
- Initial package
