%global pypi_name sphinx-tabs
%global python_module_name sphinx_tabs

Name:           python-sphinx-tabs
Version:        2.0.0
Release:        2%{?dist}
Summary:        Tabbed views for Sphinx
License:        MIT
URL:            https://github.com/executablebooks/sphinx-tabs
Source0:        https://github.com/executablebooks/%{pypi_name}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Create tabbed content in Sphinx documentation when building HTML.}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Needed for testing
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
# Not yet packaged
#BuildRequires:  python3dist(pytest-regressions)

%generate_buildrequires
%pyproject_buildrequires


%description %{_description}


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%package -n python3-%{pypi_name}-doc
Summary:        HTML documentation for %{pypi_name}
Requires:       python3-%{pypi_name}

%description -n python3-%{pypi_name}-doc
%{summary}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%pyproject_wheel

PYTHONPATH=$(pwd) sphinx-build -b html docs html_docs


%install
%pyproject_install
%pyproject_save_files %{python_module_name}


%check
# TODO: Missing BR


%files -n  python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.md
# https://bugzilla.redhat.com/show_bug.cgi?id=1925963
%dir %{python3_sitelib}/%{python_module_name}/__pycache__

%files -n python3-%{pypi_name}-doc
%doc html_docs/*


%changelog
* Sun Feb 07 2021 Richard Shaw <hobbes1069@gmail.com> - 2.0.0-2
- Make sure doc subpackage requires main package.
- Add __pycache__ dir to %%files temporarily, see:
  https://bugzilla.redhat.com/show_bug.cgi?id=1925963

* Fri Feb 05 2021 Richard Shaw <hobbes1069@gmail.com> - 2.0.0-1
- Update to latest release and correct spec per reviewer comments.

* Wed Dec  9 2020 Richard Shaw <hobbes1069@gmail.com> 1.3.0-1
- Initial Packaging
