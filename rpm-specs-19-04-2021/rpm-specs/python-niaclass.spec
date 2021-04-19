%bcond_without tests

%global pypi_name niaclass
%global pretty_name NiaClass

%global _description %{expand:
NiaClass is a framework for solving classification tasks using nature-inspired
algorithms. The framework is written fully in Python. Its goal is to find the
best possible set of classification rules for the input data using the NiaPy
framework, which is a popular Python collection of nature-inspired algorithms.
The NiaClass classifier support numerical and categorical features.}

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Python framework for building classifiers using nature-inspired algorithms

License:        MIT
URL:            https://github.com/lukapecnik/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

#use Fedora versions of dependencies
Patch0:         0001-Niaclass-use-fedora-dep-versions.patch

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires: %{py3_dist lockfile}
BuildRequires: %{py3_dist packaging}
BuildRequires: %{py3_dist pep517}
BuildRequires: %{py3_dist poetry}

#main packages
BuildRequires: %{py3_dist niapy}
BuildRequires: %{py3_dist numpy}
BuildRequires: %{py3_dist pandas}
BuildRequires: %{py3_dist scikit-learn}

#For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

#tests
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version} -S git
rm -rf %{pretty_name}.egg-info
rm -fv poetry.lock

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo} -vf

%install
%pyproject_install
%pyproject_save_files niaclass

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/LICENSE
rm -rf %{buildroot}/%{python3_sitelib}/CHANGELOG.md

%check	
%if %{with tests}
%{python3} -m pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files doc
%license LICENSE
%doc docs/_build/html
%doc examples/

%changelog
* Thu Apr 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.0-1
- Initial package
